from flask import Flask, render_template, request, redirect, url_for
import os
import inference  # This imports the model prediction logic

app = Flask(__name__)

# Route for the home page
@app.route('/', methods=['GET', 'POST']) # app.route() is a decorator that tells Flask what URL should trigger the function, it maps the URL to the function
def index():
    if request.method == 'POST': # request.method is a string that specifies the HTTP method used
        uploaded_file = request.files['file']  # request.files is a dictionary object that contains all the uploaded files, it accesses the file using the key 'file' from the form (index.html)
        if uploaded_file.filename != '':
            # Save the uploaded file to the 'static' folder
            image_path = os.path.join('static', uploaded_file.filename)
            uploaded_file.save(image_path)

            # Get the prediction from the model
            predicted_class = inference.get_prediction(image_path)
            
            # Map the predicted class to a human-readable label (Fashion MNIST labels)
            class_labels = {
                0: 'T-shirt/top', 1: 'Trouser', 2: 'Pullover', 3: 'Dress', 4: 'Coat',
                5: 'Sandal', 6: 'Shirt', 7: 'Sneaker', 8: 'Bag', 9: 'Ankle boot'
            }
            
            result = class_labels[predicted_class]
            
            # Render the result on the 'show.html' page
            return render_template('show.html', result=result, image_path=image_path)
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=False)
