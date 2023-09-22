import numpy as np
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt

# Provided data
data = {
    'y_actual': ['yes', 'No', 'No', 'yes', 'No', 'yes', 'No', 'No', 'yes', 'No', 'yes', 'No'],
    'y_predicted': ['yes', 'yes', 'No', 'yes', 'No', 'yes', 'yes', 'No', 'yes', 'No', 'No', 'No']
}

# Define a mapping for 'yes' and 'No' to binary values (1 and 0)
label_mapping = {'yes': 1, 'No': 0}

# Convert the labels in the data dictionary to binary values
y_actual = [label_mapping[label] for label in data['y_actual']]
y_predicted = [label_mapping[label] for label in data['y_predicted']]

# Compute the confusion matrix
conf_matrix = confusion_matrix(y_actual, y_predicted)

# Create a heatmap of the confusion matrix
plt.figure(figsize=(6, 6))
plt.imshow(conf_matrix, cmap='Blues', interpolation='nearest')
plt.colorbar()
plt.xticks([0, 1], ['Predicted No', 'Predicted Yes'])
plt.yticks([0, 1], ['Actual No', 'Actual Yes'])
plt.xlabel('Predicted Label')
plt.ylabel('True Label')
plt.title('Confusion Matrix')
plt.show()
