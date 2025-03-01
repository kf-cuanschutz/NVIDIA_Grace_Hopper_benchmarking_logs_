import sklearn
import matplotlib.pyplot as plt
from pathlib import Path
import time

start_time = time.time()

# Train and Fine-tune Decision Tree on Moon Dataset
from sklearn.model_selection import ShuffleSplit
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.base import clone
from scipy.stats import mode
from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV

X_moons, y_moons = make_moons(n_samples=10000, noise=0.4, random_state=42)

X_train, X_test, y_train, y_test = train_test_split(X_moons, y_moons,
                                                    test_size=0.2,
                                                    random_state=42)
params = {
    'max_leaf_nodes': list(range(2, 100)),
    'max_depth': list(range(1, 7)),
    'min_samples_split': [2, 3, 4]
}
grid_search_cv = GridSearchCV(DecisionTreeClassifier(random_state=42),
                              params,
                              cv=3)
grid_search_cv.fit(X_train, y_train)
grid_search_cv.best_estimator_
y_pred = grid_search_cv.predict(X_test)
print("Decision Tree with Moons Accuracy Score: ", accuracy_score(y_test, y_pred))
# Train/Grow a Forest:

n_trees = 1000
n_instances = 100

mini_sets = []

rs = ShuffleSplit(n_splits=n_trees, test_size=len(X_train) - n_instances,
                  random_state=42)

for mini_train_index, mini_test_index in rs.split(X_train):
    X_mini_train = X_train[mini_train_index]
    y_mini_train = y_train[mini_train_index]
    mini_sets.append((X_mini_train, y_mini_train))
forest = [clone(grid_search_cv.best_estimator_) for _ in range(n_trees)]
accuracy_scores = []

for tree, (X_mini_train, y_mini_train) in zip(forest, mini_sets):
    tree.fit(X_mini_train, y_mini_train)
    
    y_pred = tree.predict(X_test)
    accuracy_scores.append(accuracy_score(y_test, y_pred))
  
np.mean(accuracy_scores)

# "Majority Vote" Prediction:

Y_pred = np.empty([n_trees, len(X_test)], dtype=np.uint8)

for tree_index, tree in enumerate(forest):
    Y_pred[tree_index] = tree.predict(X_test)
y_pred_majority_votes, n_votes = mode(Y_pred, axis=0)
print ("Forest Accuracy Score: ", accuracy_score(y_test, y_pred_majority_votes.reshape([-
1])))

end_time = time.time()

execution_time= end_time - start_time
print("Funciton execution time: ", execution_time, " seconds")
