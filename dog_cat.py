import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array, load_img
import tkinter as tk
from tkinter import filedialog, Label, Button
import matplotlib.pyplot as plt
import numpy as np

# Load the saved model
model = load_model('cat_dog_classifier.h5')  # Update with your model path

# Function to predict image label
def predict_image(img_path):
    img = load_img(img_path, target_size=(150, 150))
    img_array = img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0

    prediction = model.predict(img_array)
    if prediction[0] > 0.5:
        return "It's a dog!"
    else:
        return "It's a cat!"

# Function to handle image upload and prediction
def upload_and_predict():
    file_path = filedialog.askopenfilename()
    if file_path:
        result_text.set(predict_image(file_path))
        img = load_img(file_path)
        img = img.resize((250, 250))
        img = img_to_array(img) / 255.0
        img = np.clip(img, 0, 1)
        plt.imshow(img)
        plt.axis('off')
        plt.show()

# Create GUI window
root = tk.Tk()
root.title('Cat or Dog Classifier')

# Configure window size and position
window_width = 800
window_height = 600
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width / 2) - (window_width / 2)
y = (screen_height / 2) - (window_height / 2)
root.geometry(f'{window_width}x{window_height}+{int(x)}+{int(y)}')

# Create widgets
upload_btn = Button(root, text='Upload Image', command=upload_and_predict, font=('Helvetica', 16))
upload_btn.pack(pady=20)

result_text = tk.StringVar()
result_label = Label(root, textvariable=result_text, font=('Helvetica', 24, 'bold'), fg='blue')
result_label.pack(pady=20)

# Center window on screen
root.eval('tk::PlaceWindow . center')

# Start GUI main loop
root.mainloop()
