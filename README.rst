########################################
Li and Ma, 1983, Estimating Significance
########################################
|TestStatus| |PyPiStatus| |BlackStyle| |PackStyleBlack|


A python implementation of the equations 9, and 17 proposed by Li and Ma in 1983.

.. code-block:: bib

    @article{lima1983analysis,
        title={Analysis methods for results in gamma-ray astronomy},
        author={Li, Ti-Pei and Ma, Yu-Qian},
        journal={The Astrophysical Journal},
        volume={272},
        pages={317--324},
        year={1983}
    }

The names of the variables are adopted from Li and Ma.

*******
Install
*******

.. code-block:: bash

    pip install lima1983analysis_sebastian-achim-mueller


**************
Significance S
**************

Estimate the significance ``S`` of a detection.

.. code-block:: python

    estimate_S_eq9(N_on, N_off, alpha)
    estimate_S_eq17(N_on, N_off, alpha)


*****************
Signal-Counts N_s
*****************

Estimate how much signal-counts ``N_s`` are required to claim a detection.

.. code-block:: python

    estimate_N_s_eq9(N_off, alpha, S)
    estimate_N_s_eq17(N_off, alpha, S, margin=1e-6, max_num_iterations=1000, N_s_start=None)


.. |TestStatus| image:: https://github.com/cherenkov-plenoscope/lima1983analysis/actions/workflows/test.yml/badge.svg?branch=main
    :target: https://github.com/cherenkov-plenoscope/lima1983analysis/actions/workflows/test.yml

.. |PyPiStatus| image:: https://img.shields.io/pypi/v/lima1983analysis_sebastian-achim-mueller
    :target: https://pypi.org/project/lima1983analysis_sebastian-achim-mueller

.. |BlackStyle| image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/psf/black

.. |PackStyleBlack| image:: https://img.shields.io/badge/pack%20style-black-000000.svg
    :target: https://github.com/cherenkov-plenoscope/black_pack
