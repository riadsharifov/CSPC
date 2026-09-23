# CSPC Computer Science for Physics and Chemistry
My coursework repository. each practical is under PW<n>/Lab <X>/.

## Setup
Create the environment for a given lab:
```bash
conda env create -f PW1/Lab\ A/environment.yml
conda activate cspc 

PW1
Lab A: Reproducible foundations
What I built:
set up the repo structure, created conda env, added pytest tests, and compared pure Python loop speed with numpy.
Speed comparison (loop vs numppy):
loop: 0.0458s
numpy: 0.0139s
speed-up: 3.29x faster
Tests: all passing
conclusion:
everything worked as expected, created the virtual environment and configured git with gitHub without problems. numpy turned out to be around 3x faster than the usual python loop, and all tests passed.

## Pw1 lab B

1 observed decay data shows exponential decay over time
2 the scatter points line up nicely with the theoretical curve so the decay law holds up
3 snakemake automates figure creation and only rebuilds figure.png if plot.py or decay_observed.csv gets updated
