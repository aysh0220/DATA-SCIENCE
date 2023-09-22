import numpy as np
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

# Provided data
data = {
    'y_actual': [1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0],
    'y_predicted': [1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0]
}

# Extract actual and predicted labels
y_actual = data['y_actual']
y_predicted = data['y_predicted']

# Create a confusion matrix
conf_matrix = confusion_matrix(y_actual, y_predicted)

# Plot the confusion matrix as a heatmap
plt.figure(figsize=(6, 6))
sns.heatmap(conf_matrix, annot=True, fmt="d", cmap="Blues", cbar=False,
            xticklabels=['Predicted 0', 'Predicted 1'],
            yticklabels=['Actual 0', 'Actual 1'])
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Confusion Matrix')
plt.show()

