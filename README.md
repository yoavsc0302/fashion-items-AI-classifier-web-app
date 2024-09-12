# Fashion Items AI Classifier Web App

## Project Overview

This project is an AI-powered image classification web application that can classify fashion items into categories such as T-shirts, trousers, dresses, etc. It leverages a pre-trained neural network model, hosted with TensorFlow Serving, to predict categories of fashion items from the Fashion MNIST dataset. The app is built using Flask for the web framework, and the machine learning model is integrated via an API.

## Features

- Upload images of fashion items from your local device.
- Classify images into predefined categories: T-shirt/Top, Trouser, Pullover, Dress, Coat, Sandal, Shirt, Sneaker, Bag, and Ankle Boot.
- The model is served using TensorFlow Serving and queried by the Flask web application.
- A visually appealing web interface, built using HTML and CSS.
- Dockerized environment for both the Flask app and TensorFlow Serving for seamless deployment.

## Project Structure

IMAGE_CLASSIFICATION_APP/
│
├── app/
│   ├── static/
│   ├── templates/
│   ├── __pycache__/
│   ├── app.py             # Main Flask application code
│   ├── inference.py        # Model inference logic
│   ├── show.html           # Results page template
│   └── index.html          # Upload page template
│
├── models/
│   ├── clothing_model/     # TensorFlow Serving model folder
│   │   ├── 1/
│   │   │   ├── saved_model.pb  # Model binary file
│   │   │   ├── assets/
│   │   │   ├── variables/
│
├── .elasticbeanstalk/       # AWS Elastic Beanstalk configuration
├── .gitignore
├── Dockerfile               # Dockerfile to build the Flask app
├── docker-compose.yml       # Docker Compose file for multi-container setup
├── requirements.txt         # Python dependencies
└── README.md                # Documentation (this file)


## Tech Stack

- **Flask**: A lightweight web framework for Python.
- **TensorFlow Serving**: Used to serve the trained model.
- **Docker**: Containerization of both the Flask app and TensorFlow Serving.
- **AWS Elastic Beanstalk**: Deployment platform for hosting the application.
- **HTML/CSS**: For building the front-end user interface.

## Installation and Usage Instructions

### Prerequisites

- Docker installed on your local machine.
- An AWS account for deployment.

### Local Setup

1. Clone the repository:
    ```
    git clone https://github.com/your-repo/fashion-items-AI-classifier-web-app.git
    cd fashion-items-AI-classifier-web-app
    ```

2. Build and run the Docker containers:
    ```
    docker-compose up --build
    ```

3. Visit `http://localhost:80` to access the app locally.

### Deployment to AWS

1. Set up Elastic Beanstalk using the AWS CLI:
    ```
    eb init
    eb create
    ```

2. Deploy updates to AWS:
    ```
    eb deploy
    ```

## How It Works

1. Users upload an image of a fashion item via the web interface.
2. The image is saved to the `/static` directory on the server.
3. The uploaded image is passed to the `inference.py` module, where it is preprocessed.
4. A request is made to the TensorFlow Serving API to get the predicted category.
5. The prediction is displayed on the results page (`show.html`) along with the uploaded image.

## Key Skills Demonstrated

- **MLOps**: The project demonstrates a basic understanding of managing AI/ML models, including preprocessing, serving, and deploying them.
- **Docker**: Shows familiarity with containerization using Docker and Docker Compose.
- **AI/ML Frameworks**: Experience with TensorFlow for serving machine learning models.
- **Flask Development**: Development of web applications with Python and Flask.
- **AWS**: Using AWS Elastic Beanstalk for deploying and managing applications.
- **HTML/CSS**: Building user-friendly front-end interfaces.

## Future Improvements

- Add CI/CD pipelines for automated testing and deployment.
- Enhance model accuracy through advanced preprocessing and algorithmic techniques.
- Add user authentication to save and track user classifications.
- Implement a more complex UI/UX using frameworks like React or Vue.js.

