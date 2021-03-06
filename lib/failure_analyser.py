from lib.result_analyser import ResultAnalyser
import pandas as pd
import itertools
import os


class FailureAnalyser(ResultAnalyser):
    def __init__(self, output):
        self.rg = ResultAnalyser(output)
        self.fdata = {}
        self.f_list = {}
        self.failures_list = os.path.join(os.path.dirname(__file__), "../data/failures_list.csv")

    def get_suites_list(self, test_list):
        comb_list = []
        for key, value in self.rg.rdata.items():
            if "gsc" not in key:
                self.fdata[key] = value.get('failures', {})
                self.fdata[key]["build_details"] = value['build_details']

        for test in test_list:
            if test == "build_details":
                comb_list.extend(list(itertools.product([test], ['node', "sgx", "result"])))
            else:
                max_value = max([len(fvalue.get(test, [])) for fkey, fvalue in self.fdata.items()])
                max_value = max_value+1 if (max_value == 0) else max_value
                comb_list.extend(list(itertools.product([test], list(range(max_value)))))

        return comb_list

    def parse_output(self):
        orig_headers = list(self.rg.rdata.keys())
        headers = orig_headers.copy()
        [headers.remove(job) for job in orig_headers if "gsc" in job]
        test_suites = self.rg.get_test_suites()
        test_list = test_suites.copy()
        suites_list = self.get_suites_list(test_list)
        self.fetch_known_failures()
        row_list = pd.MultiIndex.from_tuples(suites_list)
        df = pd.DataFrame('', row_list, columns=headers)
        try:
            for tc in test_list:
                for suite, data in self.fdata.items():
                    res = data.get(tc, {})
                    if tc == "build_details":
                        df.loc[(tc, 'node'), suite] = res['node']
                        df.loc[(tc, 'sgx'), suite] = res['sgx']
                        df.loc[(tc, 'result'), suite] = res['result']
                    else:
                        for index, val in enumerate(res):
                            df.loc[(tc, index), suite] = val

        except Exception as e:
            print("Exception Occured during failure analysis:", e)

        f_df = df.copy()
        sample = f_df.style.apply(self.color_format)

        return sample

    def fetch_known_failures(self):
        self.f_list = pd.read_csv(self.failures_list)

    def get_node_failures(self, node, sgx_mode):
        return list(self.f_list.loc[(self.f_list['Node'] == node) & (self.f_list['SGX'] == sgx_mode)]['Test'])

    def color_format(self, f_df):
        node_name = f_df['build_details']['node']
        sgx_mode = f_df['build_details']['sgx']
        job_result = f_df['build_details']['result']
        self.node_failures = self.get_node_failures(node_name, sgx_mode)
        df_1 = f_df.copy()
        for index in range(len(f_df)):
            if (f_df.iloc[index] in self.node_failures) or (f_df.iloc[index] in [node_name, '', sgx_mode, job_result]):
                if f_df.iloc[index] == "ABORTED":
                    df_1.iloc[index] = 'background-color: #FFC000;'
                else:
                    df_1.iloc[index] = '' #background-color: #FFC000;
            else:
                df_1.iloc[index] = 'background-color: red;'
        return df_1
