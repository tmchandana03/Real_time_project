# Real_time_project
Project Description
# Project Structure

dog-cat/
├── cat_dog_classifier.h5        # Trained CNN model
├── dog_cat.py                   # Main script for training and prediction
├── dataset/
│   ├── train/                   # Training images
│   └── validation/              # Validation images
├── readme.txt                   # Original documentation or notes
# Dataset
The dataset is split into two folders:
train/ — Used for training the model
validation/ — Used for validating the model performance
Each folder contains images of cats and dogs.

# Model
The model architecture is a CNN built using TensorFlow/Keras. After training, the model is saved as cat_dog_classifier.h5.
# How to Run
Clone the repository

git clone https://github.com/your-username/dog-cat.git
cd dog-cat
Install dependencies

pip install tensorflow numpy matplotlib
Train the model (optional if using the provided .h5 file)

python dog_cat.py
Use the model to predict new images
Modify the dog_cat.py to load your image and run the prediction using the saved model.

# Output
A trained model file: cat_dog_classifier.h5
Model performance evaluated using validation data
Prediction results printed in the terminal or saved as output

# Technologies Used
Python
TensorFlow / Keras
NumPy
Matplotlib
PIL or OpenCV for image handling

