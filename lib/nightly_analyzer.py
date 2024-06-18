
class NightlyAnalyzer:
    def __init__(self, ci_obj, rp, fa, sa):
        self.ci_obj = ci_obj
        self.rp = rp
        self.fa = fa
        self.sa = sa
        self.result_file = ""

    def analyze_and_report(self, nightly_pipeline):
        report_result = self.ci_obj.analyze_report(nightly_pipeline)

        print(f"Starting Downstream Analysis for {nightly_pipeline} nightly jobs")
        nightly_df = self.rp.parse_output(report_result)

        print("Starting Failure Analysis and Comparison for Downstream jobs")
        failures_df = self.fa.parse_output(report_result)

        result = {"Nightly": nightly_df, "Failures": failures_df}
        self.sa.write_to_excel(nightly_pipeline, result)
