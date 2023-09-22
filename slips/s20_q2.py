import pandas as pd
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

# Create a DataFrame from the provided data
data = {
    'actual': [1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0],
    'predicted': [1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0]
}

df = pd.DataFrame(data)

# Calculate the confusion matrix
confusion = confusion_matrix(df['actual'], df['predicted'])

# Create a heatmap for the confusion matrix
plt.figure(figsize=(6, 6))
sns.heatmap(confusion, annot=True, fmt='d', cmap='Blues', cbar=False)
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Confusion Matrix')
plt.show()

