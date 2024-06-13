
# Pytorch Benchmarking on Grace Hopper Compared to A100: Single GPU Test

The Goal with this experiment is to test a single Hopper GPU against a single A100 GPU on CU Boulder's Alpine system as it trains on various machine learning and neural network models. This will be done using tensorflow and keras, including the datasets that come with those packages.

All software will be installed with anaconda (conda/mamba) on both systems, with matching versions in each anaconda environment for consistency in the experiment. The time it takes a single GPU to train each algorithm/neural net will be the primary metric reported in this experiment. (ADDITIONAL METRICS HERE OR ELSEWHERE?) A python script included below will be executed on each system, and any inconsistencies between the two systems will be noted in the comments below.

## Set Up
In order for this experiment to work, we need an identical environment for both the Grace Hopper GPU and the A100 GPU. While we have no control over the underlying architecture, we can control the software versions on each to make an identical testing environment. We do so using Anaconda (conda/mamba).


Versions for Alpine:
- sklearn=2.2.0, python=3.11.5, tensorflow=2.12.1, numpy=1.26.4, keras=2.12.0, matplotlib=!!!, pathlib=!!!, tensorflow-gpu=!!!

Versions for Grace Hopper:
- sklearn=2.2.0, python=3.11.5, tensorflow=2.12.0, numpy=!!!, keras=!!!, matplotlib=!!!, pathlib=!!!, tensorflow-gpu=!!!

#### Environment Set Up: Grace Hopper Commands

(After setting up Anaconda on Grace Hopper using [these instructions](https://github.com/kf-cuanschutz/NVIDIA_Grace_Hopper_benchmarking_logs_/blob/main/README.md))

```
conda create -n test_env
conda activate test_env  # this command needs to be run every new session, the rest do not
conda install sklearn-pandas=2.2.0 matplotlib pathlib numpy
conda install tensorflow  # !!!!!!!!! Downgrades numpy to 1.23.5 and python to 3.11.5 !!!!!!!!!!
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

### Test Scripts

The first experiment will be done training an SVM using 1 GPU. Here is the set up:

```
import sklearn
import matplotlib.pyplot as plt
import tensorflow as tf
from pathlib import Path


# Make tensorflow run script on a GPU
with tf.device('/gpu:0')

# Parameters/Bounds on GPU (for potential future tests):
# gpu_devices = tf.config.experimental.list_physical_devices('GPU')
# if gpu_devices:
#   for gpu in gpu_devices:
#     tf.config.experimental.set_virtual_device_configuration(
#            gpu,
#            [tf.config.experimental.VirtualDeviceConfiguration(memory_limit=2048)])

# FUTURE TESTING: nvidia-smi (NOT READY). Need to install (and import?) nvidia-smi first. Below is just an example/outline!
# import subprocess
# def get_gpu_usage():
#     try:
#         result = subprocess.run(['nvidia-smi', '--query-gpu=utilization.gpu', '--format=csv,noheader,nounits'], stdout=subprocess.PIPE)
#         gpu_usage = result.stdout.decode('utf-8').strip().split('\n')
#         return [int(utilization) for utilization in gpu_usage]
#     except Exception as e:
#         print("Error getting GPU usage:", e)
#         return None


plt.rc('font', size=14)
plt.rc('axes', labelsize=14, titlesize=14)
plt.rc('legend', fontsize=14)
plt.rc('xtick', labelsize=10)
plt.rc('ytick', labelsize=10)

# Create the images/SVM folder first and define the save_fig() function which is used in this code to save figures in high-res:

# Changes here are necessary to change future outputs (!!!)

IMAGES_PATH = Path() / "images" / "svm"
IMAGES_PATH.mkdir(parents=True, exist_ok=True)

def save_fig(fig_id, tight_layout=True, fig_extension="png", resolution=300):
    path = IMAGES_PATH / f"{fig_id}.{fig_extension}"
    if tight_layout:
        plt.tight_layout()
    plt.savefig(path, format=fig_extension, dpi=resolution)
```

#### Linear SVM Classification:

Creating the SVM

```
import numpy as np
from sklearn.datasets import load_iris
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import LinearSVC

iris = load_iris(as_frame=True)
X = iris.data[["petal length (cm)", "petal width (cm)"]].values
y = (iris.target == 2)  # Iris virginica

svm_clf = make_pipeline(StandardScaler(),
                        LinearSVC(C=1, dual=True, random_state=42))
svm_clf.fit(X, y)
```

Predicting Values

```
X_new = [[5.5, 1.7], [5.0, 1.5]]
svm_clf.predict(X_new)

svm_clf.decision_function(X_new)
```

Nonlinear SVM? Polynomial SVM? Should I print outputs as well? Predictions? Or just time it?

This experiment should be replilcated adjusting GPU parameters and also for testing Neural Networks (next major experiment, see Neural Network Script found [here](https://github.com/ageron/handson-ml3/blob/main/10_neural_nets_with_keras.ipynb)
