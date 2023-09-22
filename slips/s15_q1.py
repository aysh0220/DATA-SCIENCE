import numpy as np

# Create a dataset
data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Alter rows and columns
data = np.delete(data, 1, axis=0)  # Delete the second row
data = np.delete(data, 1, axis=1)  # Delete the second column

# Print the altered dataset
print(data)

                                                            # Output:
                                                            # [[1 3]
                                                            # [7 9]]