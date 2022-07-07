import flask
from flask import request
app = flask.Flask(__name__)
app.config["DEBUG"] = True

from flask_cors import CORS
CORS(app)


@app.route('/',methods=['GET'])
def default():
    return ''' <h1> hello april 24th   </h1>'''


@app.route('/corona',methods=['GET'])
def corona():
    return ''' <h1> Corona is no more </h1>'''




@app.route('/predict',methods=['GET'])
def predict():
    import joblib
    model = joblib.load('hp_trained_model.pkl')
    price = model.predict([[int(request.args['sqft']),
                            int(request.args['place']),
                            int(request.args['yo']),
                            int(request.args['tf']),
                            int(request.args['bhk']),
                           ]])
    return str(round(price[0]))


app.run()
