#What is Machine Learning? Overview of ML TypesCode: Write a program to classify data into supervised, unsupervised, or reinforcement learning types

from sklearn.datasets import load_iris
from sklearn.utils import Bunch

def classify_ml_type(dataset: Bunch, environment_interaction=False):
    """
    Classify a dataset into supervised, unsupervised, or reinforcement learning types.

    Parameters:
        dataset (Bunch): Dataset object from sklearn or similar, containing data and optionally labels.
        environment_interaction (bool): True if learning involves interacting with an environment.

    Returns:
        str: Type of machine learning (Supervised, Unsupervised, Reinforcement).
    """
    if environment_interaction:
        return "Reinforcement Learning"
    elif hasattr(dataset, 'target'):  # Check if the dataset has labels
        return "Supervised Learning"
    else:
        return "Unsupervised Learning"


# Load a dataset (Iris dataset)
iris_dataset = load_iris()

# Case 1: Classify the Iris dataset (has labels)
ml_type_iris = classify_ml_type(iris_dataset)
print(f"Iris dataset is suitable for: {ml_type_iris}")

# Case 2: Remove labels to simulate unsupervised learning
iris_unsupervised = Bunch(data=iris_dataset.data)  # Only features, no target
ml_type_unsupervised = classify_ml_type(iris_unsupervised)
print(f"Iris dataset without labels is suitable for: {ml_type_unsupervised}")

# Case 3: Simulate reinforcement learning (interactive environment)
ml_type_reinforcement = classify_ml_type(iris_dataset, environment_interaction=True)
print(f"Interactive case is suitable for: {ml_type_reinforcement}")
