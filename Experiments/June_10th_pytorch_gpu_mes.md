
# Pytorch Benchmarking on Grace Hopper Compared to A100: Single GPU Test

The Goal with this experiment is to test a single Hopper GPU against an A100 GPU on CU Boulder's Alpine system. **ADD MORE HERE**

## Set Up
In order for this experiment to work, we need an identical environment for both the Grace Hopper GPU and the A100 GPU. While we have no control over the underlying architecture, we can control the software versions on each to make an identical testing environment. We do so using Anaconda (conda/mamba).

Versions for our matching environments:
- sklearn-pandas=2.2.0
- matplotlib=3.8.4
- pathlib=1.0.1
- numpy=1.26.4
- python=3.11.9

- tensorflow (covers keras?) cover this first
- keras=2.0.8; 2.1.2-6; 2.2.0,2,4; 2.3.1; 2.4.3; 2.6.0; 2.8,9,10,11,12.0; 3.0.5

#### Environment Set Up: Grace Hopper Commands

(After setting up Anaconda on Grace Hopper using [these instructions](https://github.com/kf-cuanschutz/NVIDIA_Grace_Hopper_benchmarking_logs_/blob/main/README.md))

```
conda create -n test_env
conda activate test_env  # this command needs to be run every new session, the rest do not
conda install sklearn-pandas=2.2.0 matplotlib pathlib numpy
```

##### Environment Set Up: Alpine Commands

(Given you have an Alpine account and Anaconda set up)
```
acompile  # Get onto a compute node
module load anaconda
conda create -n test_env
conda activate test_env
conda install sklearn-pandas=2.2.0 python=3.11.9
```

### Dataset
