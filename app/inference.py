import requests
import json
import numpy as np
from tensorflow.keras.preprocessing import image

# URL for the TensorFlow Serving API (yes, you can call it MODEL_URI)
MODEL_URI = 'http://tensorflow-serving:8501/v1/models/clothing_model:predict'

# Function to preprocess the input image
def preprocess_image(image_path):
    # 1. Load the image and resize it to 28x28 (same as your model input)
    img = image.load_img(image_path, target_size=(28, 28), color_mode='grayscale')
    
    # 2. Convert the image to a NumPy array
    img_array = image.img_to_array(img)
    
    # 3. Expand the dimensions to add a batch dimension
    img_array = np.expand_dims(img_array, axis=0)
    
    # 4. Normalize the image (scale pixel values to [0, 1])
    img_array = img_array / 255.0
    
    return img_array

# Function to make predictions by calling TensorFlow Serving
def get_prediction(image_path):
    # Preprocess the image
    img_array = preprocess_image(image_path)
    
    # Convert the image to JSON format that TensorFlow Serving can accept
    data = json.dumps({
        "instances": img_array.tolist()  # Convert the NumPy array to a list
    })
    
    # Send the POST request to TensorFlow Serving
    response = requests.post(MODEL_URI, data=data)
    
    # Parse the response from TensorFlow Serving
    result = json.loads(response.text)
    
    # Extract the predicted class from the 'predictions' field
    predicted_class = np.argmax(result['predictions'], axis=1)[0]
    
    return predicted_class