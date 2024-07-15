from flask import Flask, request, render_template # type: ignore
import pickle
import numpy as np # type: ignore

app = Flask(__name__)

# Load the model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    age = float(request.form['Age'])
    systolic_bp = float(request.form['SystolicBP'])
    diastolic_bp = float(request.form['DiastolicBP'])
    bs = float(request.form['BS'])
    body_temp = float(request.form['BodyTemp'])
    heart_rate = float(request.form['HeartRate'])
    
    # Create input array
    input_data = np.array([[age, systolic_bp, diastolic_bp, bs, body_temp, heart_rate]])
    
    # Predict
    prediction = model.predict(input_data)
    
    if prediction[0] == 1:
        result = "High Risk"
    else:
        result = "Low Risk"
    
    return render_template('result.html', result=result)

if __name__ == '_main_':
    app.run(debug=True)