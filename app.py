from flask import Flask, request, render_template
import numpy as np
import pickle
from tensorflow.keras.models import load_model

model = load_model('model.h5')
with open('scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html',data={})

@app.route('/predict', methods=['POST'])
def predict():
    features = [float(x) for x in request.form.values()]
    features_array = np.array(features).reshape(1, -1)

    scaled_features = scaler.transform(features_array)
    prediction = model.predict(scaled_features)

    output = 'Positive for Liver Disease' if prediction[0][0] > 0.5 else 'Negative for Liver Disease'

    data = request.form.to_dict()

    statement = f'{prediction[0][0] * 100:.2f}%'
    return render_template('index.html', prediction_text=f'{output}', statement=statement, data=data)


if __name__ == "__main__":
    app.run(debug=True)
