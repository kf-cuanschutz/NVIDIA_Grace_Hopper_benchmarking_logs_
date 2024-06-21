import sklearn
import matplotlib.pyplot as plt
from pathlib import Path
import time

start_time = time.time()

from sklearn.svm import SVC
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import make_moons

# Poly Kernel SVM:

X, y = make_moons(n_samples=100, noise=0.15, random_state=42)

poly_kernel_svm_clf = make_pipeline(StandardScaler(),
                                    SVC(kernel="poly", degree=3, coef0=1, C=5))
poly_kernel_svm_clf.fit(X, y)

# Predict:

X_new = [[5.5, 1.7], [5.0, 1.5]]
print("Sample prediction: ", poly_kernel_svm_clf.predict(X_new))

end_time = time.time()

execution_time= end_time - start_time
print("Funciton execution time: ", execution_time, " seconds")
