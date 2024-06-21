import sklearn
import matplotlib.pyplot as plt
from pathlib import Path
import time

start_time = time.time()

from sklearn.datasets import load_iris
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import LinearSVC

# Training of Linear SVM:

iris = load_iris(as_frame=True)
X = iris.data[["petal length (cm)", "petal width (cm)"]].values
y = (iris.target == 2)  # Iris virginica
svm_clf = make_pipeline(StandardScaler(),
                        LinearSVC(C=1, dual=True, random_state=42))
svm_clf.fit(X, y)

# Prediction:

X_new = [[5.5, 1.7], [5.0, 1.5]]
print("Sample prediction: ", svm_clf.predict(X_new))

svm_clf.decision_function(X_new)

end_time = time.time()

execution_time= end_time - start_time
print("Funciton execution time: ", execution_time, " seconds")
