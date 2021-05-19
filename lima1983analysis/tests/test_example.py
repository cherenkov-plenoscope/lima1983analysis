import lima1983analysis as lima


def test_ratio():
    assert lima._relative_ratio(a=1, b=1) == 0.0


def test_example():
    alpha = 0.2

    example_signal_rate_in_onregion = 2.207
    example_background_rate_in_onregion = 590

    requested_significance_S = 5.0
    obsetvation_time = 60
    N_s = example_signal_rate_in_onregion * obsetvation_time
    N_B = example_background_rate_in_onregion * obsetvation_time
    N_off = N_B / alpha
    N_on = N_B + N_s

    N_s_eq9 = lima.estimate_N_s_eq9(
        N_off=N_off, alpha=alpha, S=requested_significance_S
    )

    N_s_eq17 = lima.estimate_N_s_eq17(
        N_off=N_off, alpha=alpha, S=requested_significance_S
    )

    S_eq9 = lima.estimate_S_eq9(N_on=N_on, N_off=N_off, alpha=alpha)
    S_eq17 = lima.estimate_S_eq17(N_on=N_on, N_off=N_off, alpha=alpha)

    N_on_eq9 = N_s_eq9 + N_B
    N_on_eq17 = N_s_eq17 + N_B

    check_S_eq9 = lima.estimate_S_eq9(N_on=N_on_eq9, N_off=N_off, alpha=alpha)
    check_S_eq17 = lima.estimate_S_eq17(
        N_on=N_on_eq17, N_off=N_off, alpha=alpha
    )

    assert lima._relative_ratio(check_S_eq9, requested_significance_S) < 1e-2
    assert lima._relative_ratio(check_S_eq17, requested_significance_S) < 1e-5
