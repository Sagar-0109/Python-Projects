# import joblib
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.model_selection import train_test_split
# from sklearn.datasets import load_iris

# # Load dataset (Replace with your dataset)
# data = load_iris()
# X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, test_size=0.2, random_state=42)

# # Train model (Use your actual model)
# model = RandomForestClassifier()
# model.fit(X_train, y_train)

# # Save the model
# joblib.dump(model, "facerecogination_model.pkl")

# print("Model saved as 'facerecogination_model.pkl' ✅")
# import cv2
# import joblib
# import numpy as np
# from skimage.feature import hog
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.model_selection import train_test_split
# from sklearn.datasets import load_digits  # Example dataset with images

# # Load image dataset (Replace with your own dataset)
# digits = load_digits()
# X, y = digits.images, digits.target

# # Extract HOG features
# X_hog = np.array([hog(cv2.resize(img, (64, 64)), pixels_per_cell=(8, 8), cells_per_block=(2, 2)) for img in X])

# # Split dataset
# X_train, X_test, y_train, y_test = train_test_split(X_hog, y, test_size=0.2, random_state=42)

# # Train the model
# clf = RandomForestClassifier()
# clf.fit(X_train, y_train)

# # Save the trained model
# joblib.dump(clf, "facerecogination_model.pkl")
# print("Model trained and saved ✅")


# import cv2
# import numpy as np
# import joblib
# from skimage.feature import hog
# from sklearn.svm import SVC
# from sklearn.model_selection import train_test_split
# from keras.datasets import mnist  # Example dataset (Replace with FER2013)

# # Load dataset (Replace this with your actual dataset of facial expressions)
# (X_train, y_train), (X_test, y_test) = mnist.load_data()  # Example, replace with facial expression dataset

# # Resize images to match HOG requirements (48x48)
# X_train_resized = np.array([cv2.resize(img, (48, 48)) for img in X_train])
# X_test_resized = np.array([cv2.resize(img, (48, 48)) for img in X_test])

# # Extract HOG features (Ensure consistency with testing)
# X_train_hog = np.array([hog(img, pixels_per_cell=(4, 4), cells_per_block=(2, 2)) for img in X_train_resized])
# X_test_hog = np.array([hog(img, pixels_per_cell=(4, 4), cells_per_block=(2, 2)) for img in X_test_resized])

# # Train the SVM classifier
# clf = SVC(kernel='linear', probability=True)
# clf.fit(X_train_hog, y_train)

# # Save the trained model
# joblib.dump(clf, "facerecognition_model.pkl")
# print("✅ Model trained and saved successfully!")

