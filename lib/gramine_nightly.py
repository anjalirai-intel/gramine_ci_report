
class GramineNightly:
    def __init__(self, ci_obj, rp, fa, sa):
        self.ci_obj = ci_obj
        self.rp = rp
        self.fa = fa
        self.sa = sa
        self.result_file = ""

    def analyze_and_report(self, nightly_pipeline):
        self.result_file = f"{nightly_pipeline}_results"
        report_result = self.ci_obj.analyze_report(nightly_pipeline)
        print(report_result)

        # report_result = {'local_ci_graphene_native_18.04_5.18': {'test_pal': {'Pass': 32, 'Fail': 0, 'Skip': 3, 'Total': 35}, 'test_libos': {'Pass': 219, 'Fail': 0, 'Skip': 57, 'Total': 276}, 'test_entrypoint': {'Pass': 8, 'Fail': 0, 'Skip': 0, 'Total': 8}, 'test_fs': {'Pass': 17, 'Fail': 0, 'Skip': 2, 'Total': 19}, 'test_tmpfs': {'Pass': 11, 'Fail': 0, 'Skip': 5, 'Total': 16}, 'test_enc': {'Pass': 0, 'Fail': 0, 'Skip': 20, 'Total': 20}, 'ltp': {'Pass': 462, 'Fail': 4, 'Skip': 854, 'Total': 1320}, 'test_workloads': {'bash': 'PASSED', 'python': 'PASSED', 'memcached': 'PASSED', 'lightppd': 'PASSED', 'nginx': 'PASSED', 'blender': 'PASSED', 'redis': 'PASSED', 'sqlite': 'PASSED', 'busybox': 'PASSED', 'go_helloworld': 'SKIPPED', 'rust': 'PASSED', 'openjdk': 'PASSED', 'tensorflow': 'PASSED', 'curl': 'PASSED', 'nodejs': 'PASSED', 'pytorch': 'PASSED', 'r': 'PASSED', 'gcc': 'PASSED', 'openvino': 'PASSED', 'ra_tls_mbedtls': 'SKIPPED', 'ra_tls_secret_prov': 'SKIPPED'}, 'failures': {'test_pal': [], 'test_libos': [], 'test_entrypoint': [], 'test_fs': [], 'test_tmpfs': [], 'test_enc': [], 'ltp': ['test_ltp[clock_gettime01]', 'test_ltp[fork08]', 'test_ltp[select01]', 'test_ltp[select03]'], 'test_workloads': []}, 'build_details': {'node': 'graphene_18.04_5.18', 'IP': '10.66.234.110', 'Kernel Version': '5.18.2-051802-generic', 'Mode': 'Gramine Native', 'OS': 'Ubuntu 18.04', 'result': 'UNSTABLE', 'build_no': 312}}, 'local_ci_graphene_native_20.04_6.0': {'test_pal': {'Pass': 32, 'Fail': 0, 'Skip': 3, 'Total': 35}, 'test_libos': {'Pass': 221, 'Fail': 0, 'Skip': 57, 'Total': 278}, 'test_entrypoint': {'Pass': 8, 'Fail': 0, 'Skip': 0, 'Total': 8}, 'test_fs': {'Pass': 17, 'Fail': 0, 'Skip': 2, 'Total': 19}, 'test_tmpfs': {'Pass': 11, 'Fail': 0, 'Skip': 5, 'Total': 16}, 'test_enc': {'Pass': 0, 'Fail': 0, 'Skip': 20, 'Total': 20}, 'ltp': {'Pass': 462, 'Fail': 4, 'Skip': 854, 'Total': 1320}, 'test_workloads': {'bash': 'PASSED', 'python': 'PASSED', 'memcached': 'PASSED', 'lightppd': 'PASSED', 'nginx': 'PASSED', 'blender': 'PASSED', 'redis': 'PASSED', 'sqlite': 'PASSED', 'busybox': 'PASSED', 'go_helloworld': 'PASSED', 'rust': 'PASSED', 'openjdk': 'PASSED', 'tensorflow': 'PASSED', 'curl': 'PASSED', 'nodejs': 'PASSED', 'pytorch': 'PASSED', 'r': 'PASSED', 'gcc': 'PASSED', 'openvino': 'PASSED', 'ra_tls_mbedtls': 'SKIPPED', 'ra_tls_secret_prov': 'SKIPPED'}, 'failures': {'test_pal': [], 'test_libos': [], 'test_entrypoint': [], 'test_fs': [], 'test_tmpfs': [], 'test_enc': [], 'ltp': ['test_ltp[clock_gettime01]', 'test_ltp[fork08]', 'test_ltp[select01]', 'test_ltp[select03]'], 'test_workloads': []}, 'build_details': {'node': 'graphene_20.04_6.0_WilsonCity', 'IP': '10.66.234.199', 'Kernel Version': '6.0.0-060000-generic', 'Mode': 'Gramine Native', 'OS': 'Ubuntu 20.04', 'result': 'FAILURE', 'build_no': 488}}, 'local_ci_graphene_native_20.04_5.17': {'test_pal': {'Pass': 32, 'Fail': 0, 'Skip': 3, 'Total': 35}, 'test_libos': {'Pass': 219, 'Fail': 0, 'Skip': 57, 'Total': 276}, 'test_entrypoint': {'Pass': 8, 'Fail': 0, 'Skip': 0, 'Total': 8}, 'test_fs': {'Pass': 17, 'Fail': 0, 'Skip': 2, 'Total': 19}, 'test_tmpfs': {'Pass': 11, 'Fail': 0, 'Skip': 5, 'Total': 16}, 'test_enc': {'Pass': 0, 'Fail': 0, 'Skip': 20, 'Total': 20}, 'ltp': {'Pass': 462, 'Fail': 4, 'Skip': 854, 'Total': 1320}, 'test_workloads': {'bash': 'PASSED', 'python': 'PASSED', 'memcached': 'PASSED', 'lightppd': 'PASSED', 'nginx': 'PASSED', 'blender': 'PASSED', 'redis': 'PASSED', 'sqlite': 'PASSED', 'busybox': 'PASSED', 'go_helloworld': 'SKIPPED', 'rust': 'PASSED', 'openjdk': 'PASSED', 'tensorflow': 'PASSED', 'curl': 'PASSED', 'nodejs': 'PASSED', 'pytorch': 'PASSED', 'r': 'PASSED', 'gcc': 'PASSED', 'openvino': 'PASSED', 'ra_tls_mbedtls': 'SKIPPED', 'ra_tls_secret_prov': 'SKIPPED'}, 'failures': {'test_pal': [], 'test_libos': [], 'test_entrypoint': [], 'test_fs': [], 'test_tmpfs': [], 'test_enc': [], 'ltp': ['test_ltp[clock_gettime01]', 'test_ltp[fork08]', 'test_ltp[select01]', 'test_ltp[select03]'], 'test_workloads': []}, 'build_details': {'node': 'graphene_20.04_5.17', 'IP': '10.66.234.189', 'Kernel Version': '5.17.14-051714-generic', 'Mode': 'Gramine Native', 'OS': 'Ubuntu 20.04', 'result': 'UNSTABLE', 'build_no': 651}}, 'local_ci_graphene_native_22.04_6.0': {'test_pal': {'Pass': 32, 'Fail': 0, 'Skip': 3, 'Total': 35}, 'test_libos': {'Pass': 219, 'Fail': 0, 'Skip': 57, 'Total': 276}, 'test_entrypoint': {'Pass': 8, 'Fail': 0, 'Skip': 0, 'Total': 8}, 'test_fs': {'Pass': 17, 'Fail': 0, 'Skip': 2, 'Total': 19}, 'test_tmpfs': {'Pass': 11, 'Fail': 0, 'Skip': 5, 'Total': 16}, 'test_enc': {'Pass': 0, 'Fail': 0, 'Skip': 20, 'Total': 20}, 'ltp': {'Pass': 462, 'Fail': 4, 'Skip': 854, 'Total': 1320}, 'test_workloads': {'bash': 'PASSED', 'python': 'PASSED', 'memcached': 'SKIPPED', 'lightppd': 'PASSED', 'nginx': 'PASSED', 'blender': 'PASSED', 'redis': 'PASSED', 'sqlite': 'PASSED', 'busybox': 'PASSED', 'go_helloworld': 'SKIPPED', 'rust': 'PASSED', 'openjdk': 'PASSED', 'tensorflow': 'SKIPPED', 'curl': 'PASSED', 'nodejs': 'PASSED', 'pytorch': 'PASSED', 'r': 'PASSED', 'gcc': 'PASSED', 'openvino': 'SKIPPED', 'ra_tls_mbedtls': 'SKIPPED', 'ra_tls_secret_prov': 'SKIPPED'}, 'failures': {'test_pal': [], 'test_libos': [], 'test_entrypoint': [], 'test_fs': [], 'test_tmpfs': [], 'test_enc': [], 'ltp': ['test_ltp[clock_gettime01]', 'test_ltp[fork08]', 'test_ltp[select01]', 'test_ltp[select03]'], 'test_workloads': []}, 'build_details': {'node': 'graphene_22.04_6.0', 'IP': '10.66.247.82', 'Kernel Version': '6.0.0-060000-generic', 'Mode': 'Gramine Native', 'OS': 'Ubuntu 22.04', 'result': 'UNSTABLE', 'build_no': 51}}, 'local_ci_graphene_native_22.04_5.18': {'build_details': {'node': 'graphene_22.04_5.18', 'IP': '10.66.253.149', 'Kernel Version': '5.18.0-051800-generic', 'Mode': 'Gramine Native', 'OS': 'Ubuntu 22.04', 'result': 'FAILURE', 'build_no': 37}}, 'local_ci_graphene_gsc_18.04': {'test_workloads': {'python': 'PASSED', 'bash': 'PASSED', 'helloworld': 'PASSED'}, 'failures': {'test_workloads': {}}, 'build_details': {'node': 'graphene_18.04_5.18', 'IP': '10.66.234.110', 'Kernel Version': '5.18.2-051802-generic', 'Mode': 'Gramine SGX', 'OS': 'Ubuntu 18.04', 'result': 'SUCCESS', 'build_no': 863}}, 'local_ci_graphene_gsc_20.04': {'test_workloads': {'python': 'PASSED', 'bash': 'PASSED', 'helloworld': 'PASSED'}, 'failures': {'test_workloads': {}}, 'build_details': {'node': 'graphene_20.04_5.17', 'IP': '10.66.234.189', 'Kernel Version': '5.17.14-051714-generic', 'Mode': 'Gramine SGX', 'OS': 'Ubuntu 20.04', 'result': 'SUCCESS', 'build_no': 200}}, 'local_ci_graphene_gsc_centos': {'test_workloads': {'python': 'PASSED', 'bash': 'PASSED', 'helloworld': 'PASSED'}, 'failures': {'test_workloads': {}}, 'build_details': {'node': 'graphene_icl_centos8_5.18', 'IP': '10.66.244.41', 'Kernel Version': '5.18.0', 'Mode': 'Gramine SGX', 'OS': 'Centos 8', 'result': 'SUCCESS', 'build_no': 204}}, 'local_ci_graphene_sgx_22.04_6.0': {'test_pal': {'Pass': 34, 'Fail': 0, 'Skip': 1, 'Total': 35}, 'test_libos': {'Pass': 253, 'Fail': 0, 'Skip': 23, 'Total': 276}, 'test_entrypoint': {'Pass': 8, 'Fail': 0, 'Skip': 0, 'Total': 8}, 'test_fs': {'Pass': 14, 'Fail': 0, 'Skip': 5, 'Total': 19}, 'test_tmpfs': {'Pass': 11, 'Fail': 0, 'Skip': 5, 'Total': 16}, 'test_enc': {'Pass': 21, 'Fail': 0, 'Skip': 0, 'Total': 21}, 'ltp': {'Pass': 444, 'Fail': 4, 'Skip': 872, 'Total': 1320}, 'test_workloads': {'bash': 'PASSED', 'python': 'PASSED', 'memcached': 'SKIPPED', 'lightppd': 'PASSED', 'nginx': 'PASSED', 'blender': 'PASSED', 'redis': 'PASSED', 'sqlite': 'PASSED', 'busybox': 'PASSED', 'go_helloworld': 'SKIPPED', 'rust': 'PASSED', 'openjdk': 'SKIPPED', 'tensorflow': 'SKIPPED', 'curl': 'PASSED', 'nodejs': 'PASSED', 'pytorch': 'PASSED', 'r': 'PASSED', 'gcc': 'PASSED', 'openvino': 'SKIPPED', 'ra_tls_mbedtls': 'SKIPPED', 'ra_tls_secret_prov': 'SKIPPED', 'sandstone': 'SKIPPED'}, 'failures': {'test_pal': [], 'test_libos': [], 'test_entrypoint': [], 'test_fs': [], 'test_tmpfs': [], 'test_enc': [], 'ltp': ['test_ltp[bind01]', 'test_ltp[clock_gettime01]', 'test_ltp[fork08]', 'test_ltp[select01]'], 'test_workloads': []}, 'build_details': {'node': 'graphene_22.04_6.0', 'IP': '10.66.247.82', 'Kernel Version': '6.0.0-060000-generic', 'Mode': 'Gramine SGX', 'OS': 'Ubuntu 22.04', 'result': 'UNSTABLE', 'build_no': 55}}, 'local_ci_graphene_sgx_22.04_5.18': {'build_details': {'node': 'graphene_22.04_5.18', 'IP': '10.66.253.149', 'Kernel Version': '5.18.0-051800-generic', 'Mode': 'Gramine SGX', 'OS': 'Ubuntu 22.04', 'result': 'FAILURE', 'build_no': 49}}, 'local_ci_graphene_native_oot': {'test_pal': {'Pass': 32, 'Fail': 0, 'Skip': 3, 'Total': 35}, 'test_libos': {'Pass': 219, 'Fail': 0, 'Skip': 57, 'Total': 276}, 'test_entrypoint': {'Pass': 8, 'Fail': 0, 'Skip': 0, 'Total': 8}, 'test_fs': {'Pass': 17, 'Fail': 0, 'Skip': 2, 'Total': 19}, 'test_tmpfs': {'Pass': 11, 'Fail': 0, 'Skip': 5, 'Total': 16}, 'test_enc': {'Pass': 0, 'Fail': 0, 'Skip': 20, 'Total': 20}, 'ltp': {'Pass': 462, 'Fail': 4, 'Skip': 854, 'Total': 1320}, 'test_workloads': {'bash': 'PASSED', 'python': 'PASSED', 'memcached': 'PASSED', 'lightppd': 'PASSED', 'nginx': 'PASSED', 'blender': 'PASSED', 'redis': 'PASSED', 'sqlite': 'PASSED', 'busybox': 'PASSED', 'go_helloworld': 'SKIPPED', 'rust': 'PASSED', 'openjdk': 'PASSED', 'tensorflow': 'PASSED', 'curl': 'PASSED', 'nodejs': 'PASSED', 'pytorch': 'PASSED', 'r': 'PASSED', 'gcc': 'PASSED', 'openvino': 'PASSED', 'ra_tls_mbedtls': 'SKIPPED', 'ra_tls_secret_prov': 'SKIPPED'}, 'failures': {'test_pal': [], 'test_libos': [], 'test_entrypoint': [], 'test_fs': [], 'test_tmpfs': [], 'test_enc': [], 'ltp': ['test_ltp[clock_gettime01]', 'test_ltp[fork08]', 'test_ltp[select01]', 'test_ltp[select03]'], 'test_workloads': []}, 'build_details': {'node': 'graphene_anjali_dev', 'IP': '10.66.241.140', 'Kernel Version': '5.15.0-56-generic', 'Mode': 'Gramine Native', 'OS': 'Ubuntu 18.04', 'result': 'UNSTABLE', 'build_no': 549}}, 'local_ci_graphene_native_centos_5.18': {'test_pal': {'Pass': 32, 'Fail': 0, 'Skip': 3, 'Total': 35}, 'test_libos': {'Pass': 221, 'Fail': 0, 'Skip': 57, 'Total': 278}, 'test_entrypoint': {'Pass': 8, 'Fail': 0, 'Skip': 0, 'Total': 8}, 'test_fs': {'Pass': 17, 'Fail': 0, 'Skip': 2, 'Total': 19}, 'test_tmpfs': {'Pass': 11, 'Fail': 0, 'Skip': 5, 'Total': 16}, 'test_enc': {'Pass': 0, 'Fail': 0, 'Skip': 20, 'Total': 20}, 'ltp': {'Pass': 462, 'Fail': 4, 'Skip': 854, 'Total': 1320}, 'test_workloads': {'bash': 'PASSED', 'python': 'PASSED', 'memcached': 'SKIPPED', 'lightppd': 'PASSED', 'nginx': 'PASSED', 'blender': 'PASSED', 'redis': 'PASSED', 'sqlite': 'PASSED', 'busybox': 'PASSED', 'go_helloworld': 'PASSED', 'rust': 'PASSED', 'openjdk': 'PASSED', 'tensorflow': 'PASSED', 'curl': 'PASSED', 'nodejs': 'PASSED', 'pytorch': 'PASSED', 'r': 'PASSED', 'gcc': 'SKIPPED', 'openvino': 'SKIPPED', 'ra_tls_mbedtls': 'SKIPPED', 'ra_tls_secret_prov': 'SKIPPED'}, 'failures': {'test_pal': [], 'test_libos': [], 'test_entrypoint': [], 'test_fs': [], 'test_tmpfs': [], 'test_enc': [], 'ltp': ['test_ltp[clock_gettime01]', 'test_ltp[fork08]', 'test_ltp[select01]', 'test_ltp[select03]'], 'test_workloads': []}, 'build_details': {'node': 'graphene_icl_centos8_5.18', 'IP': '10.66.244.41', 'Kernel Version': '5.18.0', 'Mode': 'Gramine Native', 'OS': 'Centos 8', 'result': 'FAILURE', 'build_no': 661}}, 'local_ci_graphene_native_centos_6.0': {'test_pal': {'Pass': 32, 'Fail': 0, 'Skip': 3, 'Total': 35}, 'test_libos': {'Pass': 219, 'Fail': 0, 'Skip': 57, 'Total': 276}, 'test_entrypoint': {'Pass': 8, 'Fail': 0, 'Skip': 0, 'Total': 8}, 'test_fs': {'Pass': 17, 'Fail': 0, 'Skip': 2, 'Total': 19}, 'test_tmpfs': {'Pass': 11, 'Fail': 0, 'Skip': 5, 'Total': 16}, 'test_enc': {'Pass': 0, 'Fail': 0, 'Skip': 20, 'Total': 20}, 'ltp': {'Pass': 462, 'Fail': 4, 'Skip': 854, 'Total': 1320}, 'test_workloads': {'bash': 'PASSED', 'python': 'PASSED', 'memcached': 'SKIPPED', 'lightppd': 'PASSED', 'nginx': 'PASSED', 'blender': 'PASSED', 'redis': 'PASSED', 'sqlite': 'PASSED', 'busybox': 'PASSED', 'go_helloworld': 'SKIPPED', 'rust': 'PASSED', 'openjdk': 'PASSED', 'tensorflow': 'PASSED', 'curl': 'PASSED', 'nodejs': 'PASSED', 'pytorch': 'PASSED', 'r': 'PASSED', 'gcc': 'SKIPPED', 'openvino': 'SKIPPED', 'ra_tls_mbedtls': 'SKIPPED', 'ra_tls_secret_prov': 'SKIPPED'}, 'failures': {'test_pal': [], 'test_libos': [], 'test_entrypoint': [], 'test_fs': [], 'test_tmpfs': [], 'test_enc': [], 'ltp': ['test_ltp[clock_gettime01]', 'test_ltp[fork08]', 'test_ltp[select01]', 'test_ltp[select03]'], 'test_workloads': []}, 'build_details': {'node': 'graphene_centos_8_6.0', 'IP': '10.66.234.93', 'Kernel Version': '6.0.0', 'Mode': 'Gramine Native', 'OS': 'Centos 8', 'result': 'UNSTABLE', 'build_no': 419}}, 'local_ci_graphene_native_rhel_server': {'test_pal': {'Pass': 32, 'Fail': 0, 'Skip': 3, 'Total': 35}, 'test_libos': {'Pass': 221, 'Fail': 0, 'Skip': 57, 'Total': 278}, 'test_entrypoint': {'Pass': 8, 'Fail': 0, 'Skip': 0, 'Total': 8}, 'test_fs': {'Pass': 17, 'Fail': 0, 'Skip': 2, 'Total': 19}, 'test_tmpfs': {'Pass': 11, 'Fail': 0, 'Skip': 5, 'Total': 16}, 'test_enc': {'Pass': 0, 'Fail': 0, 'Skip': 20, 'Total': 20}, 'ltp': {'Pass': 462, 'Fail': 4, 'Skip': 854, 'Total': 1320}, 'test_workloads': {'bash': 'PASSED', 'python': 'PASSED', 'memcached': 'SKIPPED', 'lightppd': 'PASSED', 'nginx': 'PASSED', 'blender': 'PASSED', 'redis': 'PASSED', 'sqlite': 'PASSED', 'busybox': 'PASSED', 'go_helloworld': 'PASSED', 'rust': 'PASSED', 'openjdk': 'PASSED', 'tensorflow': 'PASSED', 'curl': 'PASSED', 'nodejs': 'PASSED', 'pytorch': 'PASSED', 'r': 'PASSED', 'gcc': 'SKIPPED', 'openvino': 'PASSED', 'ra_tls_mbedtls': 'SKIPPED', 'ra_tls_secret_prov': 'SKIPPED'}, 'failures': {'test_pal': [], 'test_libos': [], 'test_entrypoint': [], 'test_fs': [], 'test_tmpfs': [], 'test_enc': [], 'ltp': ['test_ltp[clock_gettime01]', 'test_ltp[fork08]', 'test_ltp[select01]', 'test_ltp[select03]'], 'test_workloads': []}, 'build_details': {'node': 'graphene_icl_rhel8', 'IP': '10.66.253.188', 'Kernel Version': '6.0.0', 'Mode': 'Gramine Native', 'OS': 'Rhel 8.4', 'result': 'FAILURE', 'build_no': 774}}, 'local_ci_graphene_native_rhel_client': {'test_pal': {'Pass': 32, 'Fail': 0, 'Skip': 3, 'Total': 35}, 'test_libos': {'Pass': 219, 'Fail': 0, 'Skip': 57, 'Total': 276}, 'test_entrypoint': {'Pass': 8, 'Fail': 0, 'Skip': 0, 'Total': 8}, 'test_fs': {'Pass': 17, 'Fail': 0, 'Skip': 2, 'Total': 19}, 'test_tmpfs': {'Pass': 11, 'Fail': 0, 'Skip': 5, 'Total': 16}, 'test_enc': {'Pass': 0, 'Fail': 0, 'Skip': 20, 'Total': 20}, 'ltp': {'Pass': 462, 'Fail': 4, 'Skip': 854, 'Total': 1320}, 'test_workloads': {'bash': 'PASSED', 'python': 'PASSED', 'memcached': 'SKIPPED', 'lightppd': 'PASSED', 'nginx': 'PASSED', 'blender': 'PASSED', 'redis': 'PASSED', 'sqlite': 'PASSED', 'busybox': 'PASSED', 'go_helloworld': 'SKIPPED', 'rust': 'PASSED', 'openjdk': 'PASSED', 'tensorflow': 'PASSED', 'curl': 'PASSED', 'nodejs': 'PASSED', 'pytorch': 'PASSED', 'r': 'PASSED', 'gcc': 'SKIPPED', 'openvino': 'PASSED', 'ra_tls_mbedtls': 'SKIPPED', 'ra_tls_secret_prov': 'SKIPPED'}, 'failures': {'test_pal': [], 'test_libos': [], 'test_entrypoint': [], 'test_fs': [], 'test_tmpfs': [], 'test_enc': [], 'ltp': ['test_ltp[clock_gettime01]', 'test_ltp[fork08]', 'test_ltp[select01]', 'test_ltp[select03]'], 'test_workloads': []}, 'build_details': {'node': 'graphene_icl_rhel_client', 'IP': '10.66.234.125', 'Kernel Version': '5.19.0', 'Mode': 'Gramine Native', 'OS': 'Rhel 8.1', 'result': 'UNSTABLE', 'build_no': 193}}, 'local_ci_graphene_native_dcap': {'test_pal': {'Pass': 32, 'Fail': 0, 'Skip': 2, 'Total': 34}, 'test_libos': {'Pass': 219, 'Fail': 0, 'Skip': 57, 'Total': 276}, 'test_entrypoint': {'Pass': 8, 'Fail': 0, 'Skip': 0, 'Total': 8}, 'test_fs': {'Pass': 17, 'Fail': 0, 'Skip': 2, 'Total': 19}, 'test_tmpfs': {'Pass': 11, 'Fail': 0, 'Skip': 5, 'Total': 16}, 'test_enc': {'Pass': 0, 'Fail': 0, 'Skip': 20, 'Total': 20}, 'ltp': {'Pass': 462, 'Fail': 4, 'Skip': 854, 'Total': 1320}, 'test_workloads': {'bash': 'PASSED', 'python': 'PASSED', 'memcached': 'PASSED', 'lightppd': 'PASSED', 'nginx': 'PASSED', 'blender': 'PASSED', 'redis': 'PASSED', 'sqlite': 'PASSED', 'busybox': 'PASSED', 'go_helloworld': 'SKIPPED', 'rust': 'PASSED', 'openjdk': 'PASSED', 'tensorflow': 'PASSED', 'curl': 'PASSED', 'nodejs': 'PASSED', 'pytorch': 'PASSED', 'r': 'PASSED', 'gcc': 'PASSED', 'openvino': 'PASSED', 'ra_tls_mbedtls': 'SKIPPED', 'ra_tls_secret_prov': 'SKIPPED'}, 'failures': {'test_pal': [], 'test_libos': [], 'test_entrypoint': [], 'test_fs': [], 'test_tmpfs': [], 'test_enc': [], 'ltp': ['test_ltp[clock_gettime01]', 'test_ltp[fork08]', 'test_ltp[select01]', 'test_ltp[select03]'], 'test_workloads': []}, 'build_details': {'node': 'graphene_icl_dcap', 'IP': '10.66.234.64', 'Kernel Version': '5.19.0-051900-generic', 'Mode': 'Gramine Native', 'OS': 'Ubuntu 18.04', 'result': 'UNSTABLE', 'build_no': 449}}, 'local_ci_graphene_sgx_18.04_5.18': {'test_pal': {'Pass': 34, 'Fail': 0, 'Skip': 1, 'Total': 35}, 'test_libos': {'Pass': 253, 'Fail': 0, 'Skip': 23, 'Total': 276}, 'test_entrypoint': {'Pass': 8, 'Fail': 0, 'Skip': 0, 'Total': 8}, 'test_fs': {'Pass': 14, 'Fail': 0, 'Skip': 5, 'Total': 19}, 'test_tmpfs': {'Pass': 11, 'Fail': 0, 'Skip': 5, 'Total': 16}, 'test_enc': {'Pass': 21, 'Fail': 0, 'Skip': 0, 'Total': 21}, 'ltp': {'Pass': 443, 'Fail': 5, 'Skip': 872, 'Total': 1320}, 'test_workloads': {'bash': 'PASSED', 'python': 'PASSED', 'memcached': 'PASSED', 'lightppd': 'PASSED', 'nginx': 'PASSED', 'blender': 'PASSED', 'redis': 'PASSED', 'sqlite': 'PASSED', 'busybox': 'PASSED', 'go_helloworld': 'SKIPPED', 'rust': 'PASSED', 'openjdk': 'SKIPPED', 'tensorflow': 'PASSED', 'curl': 'PASSED', 'nodejs': 'PASSED', 'pytorch': 'PASSED', 'r': 'PASSED', 'gcc': 'PASSED', 'openvino': 'SKIPPED', 'ra_tls_mbedtls': 'SKIPPED', 'ra_tls_secret_prov': 'SKIPPED', 'sandstone': 'SKIPPED'}, 'failures': {'test_pal': [], 'test_libos': [], 'test_entrypoint': [], 'test_fs': [], 'test_tmpfs': [], 'test_enc': [], 'ltp': ['test_ltp[bind01]', 'test_ltp[clock_gettime01]', 'test_ltp[fork08]', 'test_ltp[gettimeofday02]', 'test_ltp[select01]'], 'test_workloads': []}, 'build_details': {'node': 'graphene_18.04_5.18', 'IP': '10.66.234.110', 'Kernel Version': '5.18.2-051802-generic', 'Mode': 'Gramine SGX', 'OS': 'Ubuntu 18.04', 'result': 'UNSTABLE', 'build_no': 313}}, 'local_ci_graphene_sgx_centos_5.18': {'test_pal': {'Pass': 34, 'Fail': 0, 'Skip': 1, 'Total': 35}, 'test_libos': {'Pass': 255, 'Fail': 0, 'Skip': 23, 'Total': 278}, 'test_entrypoint': {'Pass': 8, 'Fail': 0, 'Skip': 0, 'Total': 8}, 'test_fs': {'Pass': 14, 'Fail': 0, 'Skip': 5, 'Total': 19}, 'test_tmpfs': {'Pass': 11, 'Fail': 0, 'Skip': 5, 'Total': 16}, 'test_enc': {'Pass': 21, 'Fail': 0, 'Skip': 0, 'Total': 21}, 'ltp': {'Pass': 444, 'Fail': 4, 'Skip': 872, 'Total': 1320}, 'test_workloads': {'bash': 'PASSED', 'python': 'PASSED', 'memcached': 'SKIPPED', 'lightppd': 'PASSED', 'nginx': 'PASSED', 'blender': 'PASSED', 'redis': 'PASSED', 'sqlite': 'PASSED', 'busybox': 'PASSED', 'go_helloworld': 'PASSED', 'rust': 'PASSED', 'openjdk': 'PASSED', 'tensorflow': 'PASSED', 'curl': 'PASSED', 'nodejs': 'PASSED', 'pytorch': 'PASSED', 'r': 'PASSED', 'gcc': 'SKIPPED', 'openvino': 'SKIPPED', 'ra_tls_mbedtls': 'SKIPPED', 'ra_tls_secret_prov': 'SKIPPED', 'sandstone': 'PASSED'}, 'failures': {'test_pal': [], 'test_libos': [], 'test_entrypoint': [], 'test_fs': [], 'test_tmpfs': [], 'test_enc': [], 'ltp': ['test_ltp[bind01]', 'test_ltp[clock_gettime01]', 'test_ltp[fork08]', 'test_ltp[select01]'], 'test_workloads': []}, 'build_details': {'node': 'graphene_icl_centos8_5.18', 'IP': '10.66.244.41', 'Kernel Version': '5.18.0', 'Mode': 'Gramine SGX', 'OS': 'Centos 8', 'result': 'FAILURE', 'build_no': 641}}, 'local_ci_graphene_sgx_centos_6.0': {'test_pal': {'Pass': 34, 'Fail': 0, 'Skip': 1, 'Total': 35}, 'test_libos': {'Pass': 253, 'Fail': 0, 'Skip': 23, 'Total': 276}, 'test_entrypoint': {'Pass': 8, 'Fail': 0, 'Skip': 0, 'Total': 8}, 'test_fs': {'Pass': 14, 'Fail': 0, 'Skip': 5, 'Total': 19}, 'test_tmpfs': {'Pass': 11, 'Fail': 0, 'Skip': 5, 'Total': 16}, 'test_enc': {'Pass': 21, 'Fail': 0, 'Skip': 0, 'Total': 21}, 'ltp': {'Pass': 444, 'Fail': 4, 'Skip': 872, 'Total': 1320}, 'test_workloads': {'bash': 'PASSED', 'python': 'PASSED', 'memcached': 'SKIPPED', 'lightppd': 'PASSED', 'nginx': 'PASSED', 'blender': 'PASSED', 'redis': 'PASSED', 'sqlite': 'PASSED', 'busybox': 'PASSED', 'go_helloworld': 'SKIPPED', 'rust': 'PASSED', 'openjdk': 'SKIPPED', 'tensorflow': 'PASSED', 'curl': 'PASSED', 'nodejs': 'PASSED', 'pytorch': 'PASSED', 'r': 'PASSED', 'gcc': 'SKIPPED', 'openvino': 'SKIPPED', 'ra_tls_mbedtls': 'SKIPPED', 'ra_tls_secret_prov': 'SKIPPED', 'sandstone': 'SKIPPED'}, 'failures': {'test_pal': [], 'test_libos': [], 'test_entrypoint': [], 'test_fs': [], 'test_tmpfs': [], 'test_enc': [], 'ltp': ['test_ltp[bind01]', 'test_ltp[clock_gettime01]', 'test_ltp[fork08]', 'test_ltp[select01]'], 'test_workloads': []}, 'build_details': {'node': 'graphene_centos_8_6.0', 'IP': '10.66.234.93', 'Kernel Version': '6.0.0', 'Mode': 'Gramine SGX', 'OS': 'Centos 8', 'result': 'UNSTABLE', 'build_no': 417}}, 'local_ci_graphene_sgx_rhel_server': {'test_pal': {'Pass': 34, 'Fail': 0, 'Skip': 1, 'Total': 35}, 'test_libos': {'Pass': 255, 'Fail': 0, 'Skip': 23, 'Total': 278}, 'test_entrypoint': {'Pass': 8, 'Fail': 0, 'Skip': 0, 'Total': 8}, 'test_fs': {'Pass': 14, 'Fail': 0, 'Skip': 5, 'Total': 19}, 'test_tmpfs': {'Pass': 11, 'Fail': 0, 'Skip': 5, 'Total': 16}, 'test_enc': {'Pass': 21, 'Fail': 0, 'Skip': 0, 'Total': 21}, 'ltp': {'Pass': 444, 'Fail': 4, 'Skip': 872, 'Total': 1320}, 'test_workloads': {'bash': 'PASSED', 'python': 'PASSED', 'memcached': 'SKIPPED', 'lightppd': 'PASSED', 'nginx': 'PASSED', 'blender': 'PASSED', 'redis': 'PASSED', 'sqlite': 'PASSED', 'busybox': 'PASSED', 'go_helloworld': 'PASSED', 'rust': 'PASSED', 'openjdk': 'PASSED', 'tensorflow': 'PASSED', 'curl': 'PASSED', 'nodejs': 'PASSED', 'pytorch': 'PASSED', 'r': 'PASSED', 'gcc': 'SKIPPED', 'openvino': 'PASSED', 'ra_tls_mbedtls': 'SKIPPED', 'ra_tls_secret_prov': 'SKIPPED', 'sandstone': 'PASSED'}, 'failures': {'test_pal': [], 'test_libos': [], 'test_entrypoint': [], 'test_fs': [], 'test_tmpfs': [], 'test_enc': [], 'ltp': ['test_ltp[bind01]', 'test_ltp[clock_gettime01]', 'test_ltp[fork08]', 'test_ltp[select01]'], 'test_workloads': []}, 'build_details': {'node': 'graphene_icl_rhel8', 'IP': '10.66.253.188', 'Kernel Version': '6.0.0', 'Mode': 'Gramine SGX', 'OS': 'Rhel 8.4', 'result': 'FAILURE', 'build_no': 819}}, 'local_ci_graphene_sgx_rhel_client': {'test_pal': {'Pass': 34, 'Fail': 0, 'Skip': 1, 'Total': 35}, 'test_libos': {'Pass': 253, 'Fail': 0, 'Skip': 23, 'Total': 276}, 'test_entrypoint': {'Pass': 8, 'Fail': 0, 'Skip': 0, 'Total': 8}, 'test_fs': {'Pass': 14, 'Fail': 0, 'Skip': 5, 'Total': 19}, 'test_tmpfs': {'Pass': 11, 'Fail': 0, 'Skip': 5, 'Total': 16}, 'test_enc': {'Pass': 21, 'Fail': 0, 'Skip': 0, 'Total': 21}, 'ltp': {'Pass': 443, 'Fail': 5, 'Skip': 872, 'Total': 1320}, 'test_workloads': {'bash': 'PASSED', 'python': 'PASSED', 'memcached': 'SKIPPED', 'lightppd': 'PASSED', 'nginx': 'PASSED', 'blender': 'PASSED', 'redis': 'PASSED', 'sqlite': 'PASSED', 'busybox': 'PASSED', 'go_helloworld': 'SKIPPED', 'rust': 'PASSED', 'openjdk': 'SKIPPED', 'tensorflow': 'PASSED', 'curl': 'PASSED', 'nodejs': 'PASSED', 'pytorch': 'PASSED', 'r': 'PASSED', 'gcc': 'SKIPPED', 'openvino': 'SKIPPED', 'ra_tls_mbedtls': 'SKIPPED', 'ra_tls_secret_prov': 'SKIPPED', 'sandstone': 'SKIPPED'}, 'failures': {'test_pal': [], 'test_libos': [], 'test_entrypoint': [], 'test_fs': [], 'test_tmpfs': [], 'test_enc': [], 'ltp': ['test_ltp[bind01]', 'test_ltp[clock_gettime01]', 'test_ltp[fork08]', 'test_ltp[gettimeofday02]', 'test_ltp[select01]'], 'test_workloads': []}, 'build_details': {'node': 'graphene_icl_rhel_client', 'IP': '10.66.234.125', 'Kernel Version': '5.19.0', 'Mode': 'Gramine SGX', 'OS': 'Rhel 8.1', 'result': 'UNSTABLE', 'build_no': 218}}, 'local_ci_graphene_sgx_20.04_6.0': {'test_pal': {'Pass': 34, 'Fail': 0, 'Skip': 1, 'Total': 35}, 'test_libos': {'Pass': 255, 'Fail': 0, 'Skip': 23, 'Total': 278}, 'test_entrypoint': {'Pass': 8, 'Fail': 0, 'Skip': 0, 'Total': 8}, 'test_fs': {'Pass': 14, 'Fail': 0, 'Skip': 5, 'Total': 19}, 'test_tmpfs': {'Pass': 11, 'Fail': 0, 'Skip': 5, 'Total': 16}, 'test_enc': {'Pass': 21, 'Fail': 0, 'Skip': 0, 'Total': 21}, 'ltp': {'Pass': 444, 'Fail': 4, 'Skip': 872, 'Total': 1320}, 'test_workloads': {'bash': 'PASSED', 'python': 'PASSED', 'memcached': 'PASSED', 'lightppd': 'PASSED', 'nginx': 'PASSED', 'blender': 'PASSED', 'redis': 'PASSED', 'sqlite': 'PASSED', 'busybox': 'PASSED', 'go_helloworld': 'PASSED', 'rust': 'PASSED', 'openjdk': 'PASSED', 'tensorflow': 'PASSED', 'curl': 'PASSED', 'nodejs': 'PASSED', 'pytorch': 'PASSED', 'r': 'PASSED', 'gcc': 'PASSED', 'openvino': 'PASSED', 'ra_tls_mbedtls': 'SKIPPED', 'ra_tls_secret_prov': 'SKIPPED', 'sandstone': 'PASSED'}, 'failures': {'test_pal': [], 'test_libos': [], 'test_entrypoint': [], 'test_fs': [], 'test_tmpfs': [], 'test_enc': [], 'ltp': ['test_ltp[bind01]', 'test_ltp[clock_gettime01]', 'test_ltp[fork08]', 'test_ltp[select01]'], 'test_workloads': []}, 'build_details': {'node': 'graphene_20.04_6.0_WilsonCity', 'IP': '10.66.234.199', 'Kernel Version': '6.0.0-060000-generic', 'Mode': 'Gramine SGX', 'OS': 'Ubuntu 20.04', 'result': 'FAILURE', 'build_no': 530}}, 'local_ci_graphene_sgx_20.04_5.17': {'test_pal': {'Pass': 34, 'Fail': 0, 'Skip': 1, 'Total': 35}, 'test_libos': {'Pass': 253, 'Fail': 0, 'Skip': 23, 'Total': 276}, 'test_entrypoint': {'Pass': 8, 'Fail': 0, 'Skip': 0, 'Total': 8}, 'test_fs': {'Pass': 14, 'Fail': 0, 'Skip': 5, 'Total': 19}, 'test_tmpfs': {'Pass': 11, 'Fail': 0, 'Skip': 5, 'Total': 16}, 'test_enc': {'Pass': 21, 'Fail': 0, 'Skip': 0, 'Total': 21}, 'ltp': {'Pass': 444, 'Fail': 4, 'Skip': 872, 'Total': 1320}, 'test_workloads': {'bash': 'PASSED', 'python': 'PASSED', 'memcached': 'PASSED', 'lightppd': 'PASSED', 'nginx': 'PASSED', 'blender': 'PASSED', 'redis': 'PASSED', 'sqlite': 'PASSED', 'busybox': 'PASSED', 'go_helloworld': 'SKIPPED', 'rust': 'PASSED', 'openjdk': 'SKIPPED', 'tensorflow': 'PASSED', 'curl': 'PASSED', 'nodejs': 'PASSED', 'pytorch': 'PASSED', 'r': 'PASSED', 'gcc': 'PASSED', 'openvino': 'SKIPPED', 'ra_tls_mbedtls': 'SKIPPED', 'ra_tls_secret_prov': 'SKIPPED', 'sandstone': 'SKIPPED'}, 'failures': {'test_pal': [], 'test_libos': [], 'test_entrypoint': [], 'test_fs': [], 'test_tmpfs': [], 'test_enc': [], 'ltp': ['test_ltp[bind01]', 'test_ltp[clock_gettime01]', 'test_ltp[fork08]', 'test_ltp[select01]'], 'test_workloads': []}, 'build_details': {'node': 'graphene_20.04_5.17', 'IP': '10.66.234.189', 'Kernel Version': '5.17.14-051714-generic', 'Mode': 'Gramine SGX', 'OS': 'Ubuntu 20.04', 'result': 'UNSTABLE', 'build_no': 570}}, 'local_ci_graphene_sgx_dcap': {'test_pal': {'Pass': 33, 'Fail': 0, 'Skip': 1, 'Total': 34}, 'test_libos': {'Pass': 253, 'Fail': 0, 'Skip': 23, 'Total': 276}, 'test_entrypoint': {'Pass': 8, 'Fail': 0, 'Skip': 0, 'Total': 8}, 'test_fs': {'Pass': 14, 'Fail': 0, 'Skip': 5, 'Total': 19}, 'test_tmpfs': {'Pass': 11, 'Fail': 0, 'Skip': 5, 'Total': 16}, 'test_enc': {'Pass': 21, 'Fail': 0, 'Skip': 0, 'Total': 21}, 'ltp': {'Pass': 444, 'Fail': 4, 'Skip': 872, 'Total': 1320}, 'test_workloads': {'bash': 'PASSED', 'python': 'PASSED', 'memcached': 'PASSED', 'lightppd': 'PASSED', 'nginx': 'PASSED', 'blender': 'PASSED', 'redis': 'PASSED', 'sqlite': 'PASSED', 'busybox': 'PASSED', 'go_helloworld': 'SKIPPED', 'rust': 'PASSED', 'openjdk': 'SKIPPED', 'tensorflow': 'SKIPPED', 'curl': 'PASSED', 'nodejs': 'PASSED', 'pytorch': 'PASSED', 'r': 'PASSED', 'gcc': 'PASSED', 'openvino': 'SKIPPED', 'ra_tls_mbedtls': 'PASSED', 'ra_tls_secret_prov': 'PASSED', 'sandstone': 'SKIPPED'}, 'failures': {'test_pal': [], 'test_libos': [], 'test_entrypoint': [], 'test_fs': [], 'test_tmpfs': [], 'test_enc': [], 'ltp': ['test_ltp[bind01]', 'test_ltp[clock_gettime01]', 'test_ltp[fork08]', 'test_ltp[select01]'], 'test_workloads': []}, 'build_details': {'node': 'graphene_icl_dcap', 'IP': '10.66.234.64', 'Kernel Version': '5.19.0-051900-generic', 'Mode': 'Gramine SGX', 'OS': 'Ubuntu 18.04', 'result': 'UNSTABLE', 'build_no': 541}}, 'local_ci_graphene_sgx_oot': {'test_pal': {'Pass': 34, 'Fail': 0, 'Skip': 1, 'Total': 35}, 'test_libos': {'Pass': 253, 'Fail': 0, 'Skip': 23, 'Total': 276}, 'test_entrypoint': {'Pass': 8, 'Fail': 0, 'Skip': 0, 'Total': 8}, 'test_fs': {'Pass': 14, 'Fail': 0, 'Skip': 5, 'Total': 19}, 'test_tmpfs': {'Pass': 11, 'Fail': 0, 'Skip': 5, 'Total': 16}, 'test_enc': {'Pass': 21, 'Fail': 0, 'Skip': 0, 'Total': 21}, 'ltp': {'Pass': 444, 'Fail': 4, 'Skip': 872, 'Total': 1320}, 'test_workloads': {'bash': 'PASSED', 'python': 'PASSED', 'memcached': 'PASSED', 'lightppd': 'PASSED', 'nginx': 'PASSED', 'blender': 'PASSED', 'redis': 'PASSED', 'sqlite': 'PASSED', 'busybox': 'PASSED', 'go_helloworld': 'SKIPPED', 'rust': 'PASSED', 'openjdk': 'SKIPPED', 'tensorflow': 'PASSED', 'curl': 'PASSED', 'nodejs': 'PASSED', 'pytorch': 'PASSED', 'r': 'PASSED', 'gcc': 'PASSED', 'openvino': 'SKIPPED', 'ra_tls_mbedtls': 'SKIPPED', 'ra_tls_secret_prov': 'SKIPPED', 'sandstone': 'SKIPPED'}, 'failures': {'test_pal': [], 'test_libos': [], 'test_entrypoint': [], 'test_fs': [], 'test_tmpfs': [], 'test_enc': [], 'ltp': ['test_ltp[bind01]', 'test_ltp[clock_gettime01]', 'test_ltp[fork08]', 'test_ltp[select01]'], 'test_workloads': []}, 'build_details': {'node': 'graphene_anjali_dev', 'IP': '10.66.241.140', 'Kernel Version': '5.15.0-56-generic', 'Mode': 'Gramine SGX', 'OS': 'Ubuntu 18.04', 'result': 'UNSTABLE', 'build_no': 653}}}
        print(f"Starting Downstream Analysis for {nightly_pipeline} nightly jobs")
        nightly_df = self.rp.parse_output(report_result)
        summary_df = self.rp.parse_output(report_result, True)

        print("Starting Failure Analysis and Comparison for Downstream jobs")
        failures_df = self.fa.parse_output(report_result)

        result = {"Nightly": summary_df, "Jenkins": nightly_df, "Failures": failures_df}

        self.sa.write_to_excel(self.result_file, result)