[![Project generated with PyScaffold](https://img.shields.io/badge/-PyScaffold-005CA0?logo=pyscaffold)](https://pyscaffold.org/)
<!-- These are examples of badges you might also want to add to your README. Update the URLs accordingly.
[![Built Status](https://api.cirrus-ci.com/github/<USER>/optimization-benchmark.svg?branch=main)](https://cirrus-ci.com/github/<USER>/optimization-benchmark)
[![ReadTheDocs](https://readthedocs.org/projects/optimization-benchmark/badge/?version=latest)](https://optimization-benchmark.readthedocs.io/en/stable/)
[![Coveralls](https://img.shields.io/coveralls/github/<USER>/optimization-benchmark/main.svg)](https://coveralls.io/r/<USER>/optimization-benchmark)
[![PyPI-Server](https://img.shields.io/pypi/v/optimization-benchmark.svg)](https://pypi.org/project/optimization-benchmark/)
[![Conda-Forge](https://img.shields.io/conda/vn/conda-forge/optimization-benchmark.svg)](https://anaconda.org/conda-forge/optimization-benchmark)
[![Monthly Downloads](https://pepy.tech/badge/optimization-benchmark/month)](https://pepy.tech/project/optimization-benchmark)
[![Twitter](https://img.shields.io/twitter/url/http/shields.io.svg?style=social&label=Twitter)](https://twitter.com/optimization-benchmark)
-->

# optimization-benchmark (WIP)

> A high-dimensional property predictor framed as a pseudo-materials discovery benchmark with fake compositional (linear) and "no-more-than-X-components" (non-linear) constraints.

Industry-relevant materials discovery tasks are
often _hierarchical_, _noisy_, _multi-fidelity_, _multi-objective_, _high-dimensional_, _non-linearly correlated_, and
exhibit _mixed numerical and categorical variables_ subject to _linear and non-linear
constraints_. To boot, experimental iterations are usually prohibitively expensive.

Examples of such materials discovery tasks include formulation optimization, compositional design of high
entropy alloys, and multi-step synthesis. Choosing an algorithm that can expertly
navigate such complex design spaces is a non-trivial task, and [no single algorithm is
supreme](https://dx.doi.org/10.1016/j.mtcomm.2022.103440).

<p align="center"> <i> So, how do you pair an algorithm with a design task? </i> </p>

Here, we introduce
`PseudoCrab`: a high-dimensional property predictor framed as a pseudo-materials discovery
benchmark with fake compositional (linear) and "no-more-than-X-components" (non-linear)
constraints. We apply a state-of-the-art high-dimensional Bayesian optimization
algorithm (SAASBO) in conjunction with a multi-objective parallel Noisy Expected
Hypervolume Improvement (qNEHVI) acquisition function and compare it against other
high-performing models. Because PseudoCrab is customizable, researchers can adjust the
PseudoCrab benchmark to more closely match their applications of interest during the
algorithm downselection process prior to expensive materials discovery campaigns.

Additional WIP: https://colab.research.google.com/drive/1-tSKAfYbBhYESqfi0n04NSZRJj4h9Drj?usp=sharing

## Installation

In order to set up the necessary environment:

1. review and uncomment what you need in `environment.yml` and create an environment `optimization-benchmark` with the help of [conda]:
   ```
   conda env create -f environment.yml
   ```
2. activate the new environment with:
   ```
   conda activate optimization-benchmark
   ```

> **_NOTE:_**  The conda environment will have optimization-benchmark installed in editable mode.
> Some changes, e.g. in `setup.cfg`, might require you to run `pip install -e .` again.


Optional and needed only once after `git clone`:

3. install several [pre-commit] git hooks with:
   ```bash
   pre-commit install
   # You might also want to run `pre-commit autoupdate`
   ```
   and checkout the configuration under `.pre-commit-config.yaml`.
   The `-n, --no-verify` flag of `git commit` can be used to deactivate pre-commit hooks temporarily.

4. install [nbstripout] git hooks to remove the output cells of committed notebooks with:
   ```bash
   nbstripout --install --attributes notebooks/.gitattributes
   ```
   This is useful to avoid large diffs due to plots in your notebooks.
   A simple `nbstripout --uninstall` will revert these changes.


Then take a look into the `scripts` and `notebooks` folders.

## Dependency Management & Reproducibility

1. Always keep your abstract (unpinned) dependencies updated in `environment.yml` and eventually
   in `setup.cfg` if you want to ship and install your package via `pip` later on.
2. Create concrete dependencies as `environment.lock.yml` for the exact reproduction of your
   environment with:
   ```bash
   conda env export -n optimization-benchmark -f environment.lock.yml
   ```
   For multi-OS development, consider using `--no-builds` during the export.
3. Update your current environment with respect to a new `environment.lock.yml` using:
   ```bash
   conda env update -f environment.lock.yml --prune
   ```
## Project Organization

```
├── AUTHORS.md              <- List of developers and maintainers.
├── CHANGELOG.md            <- Changelog to keep track of new features and fixes.
├── CONTRIBUTING.md         <- Guidelines for contributing to this project.
├── Dockerfile              <- Build a docker container with `docker build .`.
├── LICENSE.txt             <- License as chosen on the command-line.
├── README.md               <- The top-level README for developers.
├── configs                 <- Directory for configurations of model & application.
├── data
│   ├── external            <- Data from third party sources.
│   ├── interim             <- Intermediate data that has been transformed.
│   ├── processed           <- The final, canonical data sets for modeling.
│   └── raw                 <- The original, immutable data dump.
├── docs                    <- Directory for Sphinx documentation in rst or md.
├── environment.yml         <- The conda environment file for reproducibility.
├── models                  <- Trained and serialized models, model predictions,
│                              or model summaries.
├── notebooks               <- Jupyter notebooks. Naming convention is a number (for
│                              ordering), the creator's initials and a description,
│                              e.g. `1.0-fw-initial-data-exploration`.
├── pyproject.toml          <- Build configuration. Don't change! Use `pip install -e .`
│                              to install for development or to build `tox -e build`.
├── references              <- Data dictionaries, manuals, and all other materials.
├── reports                 <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures             <- Generated plots and figures for reports.
├── scripts                 <- Analysis and production scripts which import the
│                              actual PYTHON_PKG, e.g. train_model.
├── setup.cfg               <- Declarative configuration of your project.
├── setup.py                <- [DEPRECATED] Use `python setup.py develop` to install for
│                              development or `python setup.py bdist_wheel` to build.
├── src
│   └── optimization_benchmark <- Actual Python package where the main functionality goes.
├── tests                   <- Unit tests which can be run with `pytest`.
├── .coveragerc             <- Configuration for coverage reports of unit tests.
├── .isort.cfg              <- Configuration for git hook that sorts imports.
└── .pre-commit-config.yaml <- Configuration of pre-commit git hooks.
```

<!-- pyscaffold-notes -->

## Note

This project has been set up using [PyScaffold] 4.2.3.post1.dev12+g22876ea6 and the [dsproject extension] 0.7.2.post1.dev4+g5267ba3.

[conda]: https://docs.conda.io/
[pre-commit]: https://pre-commit.com/
[Jupyter]: https://jupyter.org/
[nbstripout]: https://github.com/kynan/nbstripout
[Google style]: http://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings
[PyScaffold]: https://pyscaffold.org/
[dsproject extension]: https://github.com/pyscaffold/pyscaffoldext-dsproject
