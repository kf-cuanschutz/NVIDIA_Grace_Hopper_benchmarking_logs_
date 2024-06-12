
# Pytorch Benchmarking on Grace Hopper Compared to A100: Single GPU Test

The Goal with this experiment is to test a single Hopper GPU against a single A100 GPU on CU Boulder's Alpine system as it trains on various machine learning and neural network models. This will be done using tensorflow and keras, including the datasets that come with those packages.

All software will be installed with anaconda (conda/mamba) on both systems, with matching versions in each anaconda environment for consistency in the experiment. The time it takes a single GPU to train each algorithm/neural net will be the primary metric reported in this experiment. (ADDITIONAL METRICS HERE OR ELSEWHERE?) A python script included below will be executed on each system, and any inconsistencies between the two systems will be noted in the comments below.

## Set Up
In order for this experiment to work, we need an identical environment for both the Grace Hopper GPU and the A100 GPU. While we have no control over the underlying architecture, we can control the software versions on each to make an identical testing environment. We do so using Anaconda (conda/mamba).

Alpine A100 Environment:
- sklearn-pandas: 2.2.0
- tensorflow: 2.12.1
- python: 3.11.5
- 

- tensorflow (covers keras?) cover this first
- Versions for GH: 2.5.0, 2.8.2, 2.9.1, 2.10-12.0
- Versions for Alpine:
- sklearn=2.2.0, python=3.11.5, tensorflow=2.12.1, numpy=1.26.4, keras=2.12.0


- Versions for GH: 2.4.3, 2.6.0, 2.8.0, 2.9.0, 2.10.0, 2.11.0, 2.12.0, 3.0.5
- Versions for Alpine: 2.0.8; 2.1.2-6; 2.2.0,2,4; 2.3.1; 2.4.3; 2.6.0; 2.8,9,10,11,12.0; 3.0.5

#### Environment Set Up: Grace Hopper Commands

(After setting up Anaconda on Grace Hopper using [these instructions](https://github.com/kf-cuanschutz/NVIDIA_Grace_Hopper_benchmarking_logs_/blob/main/README.md))

```
conda create -n test_env
conda activate test_env  # this command needs to be run every new session, the rest do not
conda install sklearn-pandas=2.2.0 matplotlib pathlib numpy
conda install tensorflow  # !!!!!!!!! Downgrades numpy to 1.23.5 and python to 3.11.5 !!!!!!!!!!
# !!!!!!!!! INSTALLS tensorflow version 2.12.0
```

##### Environment Set Up: Alpine Commands

(Given you have an Alpine account and Anaconda set up)
```
acompile  # Get onto a compute node
module load anaconda
ml mambaforge
mamba create -n test_env
mamba activate test_env
mamba install tensorflow=2.12.1 sklearn-pandas=2.2.0

```

### Dataset
