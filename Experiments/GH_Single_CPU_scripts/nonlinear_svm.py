import sklearn
import matplotlib.pyplot as plt
from pathlib import Path
import time

start_time = time.time()

# Nonlinear SVM:

from sklearn.datasets import make_moons
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import LinearSVC

X, y = make_moons(n_samples=100, noise=0.15, random_state=42)

polynomial_svm_clf = make_pipeline(
    PolynomialFeatures(degree=3),
    StandardScaler(),
    LinearSVC(C=10, max_iter=10_000, dual=True, random_state=42)
)

polynomial_svm_clf.fit(X, y)

# Prediction:

X_new = [[5.5, 1.7], [5.0, 1.5]]
print("Sample prediction: ", polynomial_svm_clf.predict(X_new))

polynomial_svm_clf.decision_function(X_new)

end_time = time.time()

execution_time= end_time - start_time
print("Funciton execution time: ", execution_time, " seconds")
