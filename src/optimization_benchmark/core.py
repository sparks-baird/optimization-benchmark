"""
This is a skeleton file that can serve as a starting point for a Python
console script. To run this script uncomment the following lines in the
``[options.entry_points]`` section in ``setup.cfg``::

    console_scripts =
         fibonacci = optimization_benchmark.skeleton:run

Then run ``pip install .`` (or ``pip install -e .`` for editable mode)
which will install the command ``fibonacci`` inside your current environment.

Besides console scripts, the header (i.e. until ``_logger``...) of this file can
also be used as template for Python modules.

Note:
    This file can be renamed depending on your needs or safely removed if not needed.

References:
    - https://setuptools.pypa.io/en/latest/userguide/entry_point.html
    - https://pip.pypa.io/en/stable/reference/pip_install
"""

import argparse
import logging
import sys

from optimization_benchmark import __version__

__author__ = "sgbaird"
__copyright__ = "sgbaird"
__license__ = "MIT"

_logger = logging.getLogger(__name__)


# ---- Python API ----
# The functions defined in this section can be imported by users in their
# Python scripts/interactive interpreter, e.g. via
# `from optimization_benchmark.skeleton import fib`,
# when using this Python module as a library.


def fib(n):
    """Fibonacci example function

    Args:
      n (int): integer

    Returns:
      int: n-th Fibonacci number
    """
    assert n > 0
    a, b = 1, 1
    for _i in range(n - 1):
        a, b = b, a + b
    return a


class PseudoCrab:
    def __init__(
        self,
        batch_size_pseudo,
        fudge_pseudo,
        d_model_pseudo,
        N_pseudo,
        heads_pseudo,
        out_hidden4_pseudo,
        emb_scaler_pseudo,
        pos_scaler_pseudo,
        bias_pseudo,
        dim_feedforward_pseudo,
        dropout_pseudo,
        elem_prop_pseudo,
        epoch_step_pseudo,
        pe_resolution_pseudo,
        ple_resolution_pseudo,
        criterion_pseudo,
        lr_pseudo,
        betas1_pseudo,
        betas2_pseudo,
        eps_pseudo,
        weight_decay_pseudo,
        alpha_pseudo,
        k_pseudo,
    ):
        pass


[
    {"name": "batch_size", "type": "range", "bounds": [32, 256]},
    {"name": "fudge", "type": "range", "bounds": [0.0, 0.1]},
    {"name": "d_model", "type": "range", "bounds": [100, 1024]},
    {"name": "N", "type": "range", "bounds": [1, 10]},
    {"name": "heads", "type": "range", "bounds": [1, 10]},
    {"name": "out_hidden4", "type": "range", "bounds": [32, 512]},
    {"name": "emb_scaler", "type": "range", "bounds": [0.0, 1.0]},
    {"name": "pos_scaler", "type": "range", "bounds": [0.0, 1.0]},
    {"name": "bias", "type": "choice", "values": [False, True]},
    {
        "name": "dim_feedforward",
        "type": "range",
        "bounds": [1024, 4096],
    },
    {"name": "dropout", "type": "range", "bounds": [0.0, 1.0]},
    # jarvis and oliynyk don't have enough elements
    # ptable contains str, which isn't a handled case
    {
        "name": "elem_prop",
        "type": "choice",
        "values": [
            "mat2vec",
            "magpie",
            "onehot",
        ],  # "jarvis", "oliynyk", "ptable"
    },
    {"name": "epochs_step", "type": "range", "bounds": [5, 20]},
    {"name": "pe_resolution", "type": "range", "bounds": [2500, 10000]},
    {
        "name": "ple_resolution",
        "type": "range",
        "bounds": [2500, 10000],
    },
    {
        "name": "criterion",
        "type": "choice",
        "values": ["RobustL1", "RobustL2"],
    },
    {"name": "lr", "type": "range", "bounds": [0.0001, 0.006]},
    {"name": "betas1", "type": "range", "bounds": [0.5, 0.9999]},
    {"name": "betas2", "type": "range", "bounds": [0.5, 0.9999]},
    {"name": "eps", "type": "range", "bounds": [0.0000001, 0.0001]},
    {"name": "weight_decay", "type": "range", "bounds": [0.0, 1.0]},
    {"name": "alpha", "type": "range", "bounds": [0.0, 1.0]},
    {"name": "k", "type": "range", "bounds": [2, 10]},
]


# ---- CLI ----
# The functions defined in this section are wrappers around the main Python
# API allowing them to be called directly from the terminal as a CLI
# executable/script.


def parse_args(args):
    """Parse command line parameters

    Args:
      args (List[str]): command line parameters as list of strings
          (for example  ``["--help"]``).

    Returns:
      :obj:`argparse.Namespace`: command line parameters namespace
    """
    parser = argparse.ArgumentParser(description="Just a Fibonacci demonstration")
    parser.add_argument(
        "--version",
        action="version",
        version=f"optimization_benchmark {__version__}",
    )
    parser.add_argument(dest="n", help="n-th Fibonacci number", type=int, metavar="INT")
    parser.add_argument(
        "-v",
        "--verbose",
        dest="loglevel",
        help="set loglevel to INFO",
        action="store_const",
        const=logging.INFO,
    )
    parser.add_argument(
        "-vv",
        "--very-verbose",
        dest="loglevel",
        help="set loglevel to DEBUG",
        action="store_const",
        const=logging.DEBUG,
    )
    return parser.parse_args(args)


def setup_logging(loglevel):
    """Setup basic logging

    Args:
      loglevel (int): minimum loglevel for emitting messages
    """
    logformat = "[%(asctime)s] %(levelname)s:%(name)s:%(message)s"
    logging.basicConfig(
        level=loglevel, stream=sys.stdout, format=logformat, datefmt="%Y-%m-%d %H:%M:%S"
    )


def main(args):
    """Wrapper allowing :func:`fib` to be called with string arguments in a CLI fashion

    Instead of returning the value from :func:`fib`, it prints the result to the
    ``stdout`` in a nicely formatted message.

    Args:
      args (List[str]): command line parameters as list of strings
          (for example  ``["--verbose", "42"]``).
    """
    args = parse_args(args)
    setup_logging(args.loglevel)
    _logger.debug("Starting crazy calculations...")
    print("The {}-th Fibonacci number is {}".format(args.n, fib(args.n)))
    _logger.info("Script ends here")


def run():
    """Calls :func:`main` passing the CLI arguments extracted from :obj:`sys.argv`

    This function can be used as entry point to create console scripts with setuptools.
    """
    main(sys.argv[1:])


if __name__ == "__main__":
    # ^  This is a guard statement that will prevent the following code from
    #    being executed in the case someone imports this file instead of
    #    executing it as a script.
    #    https://docs.python.org/3/library/__main__.html

    # After installing your project with pip, users can also run your Python
    # modules as scripts via the ``-m`` flag, as defined in PEP 338::
    #
    #     python -m optimization_benchmark.skeleton 42
    #
    run()
