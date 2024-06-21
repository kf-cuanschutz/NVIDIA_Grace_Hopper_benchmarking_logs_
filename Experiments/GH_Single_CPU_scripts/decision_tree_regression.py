import sklearn
import matplotlib.pyplot as plt
from pathlib import Path
import time
start_time = time.time()
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeRegressor
# Training Regression Decision Tree:
np.random.seed(42)
X_quad = np.random.rand(200, 1) - 0.5  # a single random input feature
y_quad = X_quad ** 2 + 0.025 * np.random.randn(200, 1)
tree_reg = DecisionTreeRegressor(max_depth=2, random_state=42)
tree_reg.fit(X_quad, y_quad)
# Predict (?)

end_time = time.time()
execution_time= end_time - start_time
print("Funciton execution time: ", execution_time, " seconds")
