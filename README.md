## Introduction
LivCheck is a web-based Liver Health Analysis Tool, designed to assist users in analyzing liver function based on the LFT results as input. Utilizing a trained artificial neural network (ANN) model, the tool provides insights into liver health and diseases.

## Features
User-Friendly Interface: An intuitive web interface for easy data input and analysis.
Real-Time Analysis: Instant results based on user inputs.
Detailed Insights: Information on liver function based on standard medical tests.
Model Integration: Uses a trained ANN model for accurate predictions.
#### Technologies Used
Frontend: HTML, CSS, JavaScript (for user interface)
Backend: Python, Flask
Machine Learning: TensorFlow (for the ANN model)
Data Handling: Pandas, NumPy

## Installation
To run the Liver Health Analysis Tool locally, follow these steps:

#### Clone the repository:
git clone https://github.com/anantmahambrey/Liver-Health-Analysis-Tool.git
cd Liver-Health-Analysis-Tool

#### Install the required packages: 
Make sure you have Python 3.12.0 installed. Create a virtual environment (optional) and install the dependencies:
pip install -r requirements.txt

#### Run the application: 
Start the Flask server:
python app.py

#### Access the tool: 
Open your web browser and navigate to http://127.0.0.1:5000/.

## Usage
Input the required values based on your liver function test.
Click the Analyze button to get results.
View the categorized outputs displayed on the screen.

## Model Details
The model is trained on the ILPD liver disease dataset, using various features from liver function tests to predict the liver health status.
The dataset is preprocessed using python libraries Numpy and Pandas, followed by training the model.
The ANN architecture is designed to achieve high accuracy in classification tasks, providing reliable results.
