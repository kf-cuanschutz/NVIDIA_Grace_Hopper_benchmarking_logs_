import sklearn
import matplotlib.pyplot as plt
from pathlib import Path
import time

start_time = time.time()

import numpy as np
from sklearn.svm import LinearSVR
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

# Poly Kernel SVM:

np.random.seed(42)
X = 2 * np.random.rand(50, 1)
y = 4 + 3 * X[:, 0] + np.random.randn(50)
svm_reg = make_pipeline(StandardScaler(),
                        LinearSVR(epsilon=0.5, dual=True, random_state=42))
svm_reg.fit(X, y)

# Predict:

X_new = [[5.5], [5.0]]
print("Sample prediction: ", svm_reg.predict(X_new))

end_time = time.time()

execution_time= end_time - start_time
print("Funciton execution time: ", execution_time, " seconds")
