# Importing essential libraries
from flask import Flask, render_template, request
import pickle
import numpy as np

# Load the Random Forest CLassifier model
filename = 'model.pkl'
classifier = pickle.load(open(filename, 'rb'))

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        oxy = int(request.form['oxygen'])
        temp = int(request.form['temperature'])
        humid = int(request.form['humidity'])

        
        data = np.array([[oxy,temp,humid]])
        my_prediction = classifier.predict_proba(data)
        my_predictions='{0:-{1}f}'.format(my_prediction[0][1],2)
        if my_predictions>str(0.5):
            return render_template('index.html', prediction='Your forest is in Danger')
        else:
            return render_template('index.html', prediction='Your forest is safe')            

if __name__ == '__main__':
	app.run(debug=True)