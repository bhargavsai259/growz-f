import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import warnings

# Suppress warnings
warnings.filterwarnings("ignore", message="X does not have valid feature names")

app = Flask(__name__)
soilmodel = pickle.load(open('soilmodel.pkl', 'rb'))

fertilizermodel = pickle.load(open('fertilizermodel.pkl', 'rb'))
yieldmodel = pickle.load(open('crop_pred_model.pkl', 'rb'))


#soil analysis
@app.route('/')
def home1():
    return render_template('soil.html')

#soil analysis telugu
@app.route('/soilpredicttelugu')
def home1telugu():
    return render_template('soiltelugu.html')



#soil analysis hindi
@app.route('/soilpredicthindi')
def home1hindi():
    return render_template('soilhindi.html')




#fertilizer
@app.route('/fertilizer')
def home2():
    return render_template('fertilizer.html')


#fertilizer telugu
@app.route('/fertilizertelugu')
def home2telugu():
    return render_template('fertilizertelugu.html')



#fertilizer hindi
@app.route('/fertilizerhindi')
def home2hindi():
    return render_template('fertilizerhindi.html')




#crop yield
@app.route('/yield')
def home():
    return render_template('yield.html')

#crop yield
@app.route('/yieldtelugu')
def hometelugu():
    return render_template('yieldtelugu.html')



#crop yield
@app.route('/yieldhindi')
def homehindi():
    return render_template('yieldhindi.html')







#soil analysis
@app.route('/soilpredict',methods=['POST'])
def soilpredict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = soilmodel.predict(final_features)
    output = prediction
    return render_template('soil.html', prediction_text='Suggested crop for given soil health condition is: "{}".'.format(output[0]))


@app.route('/soilpredicttelugu', methods=['POST'])
def soilpredicttelugu():
    '''
    For rendering results on HTML GUI
    '''
    telugu_translations = {
        "rice": "బియ్యం",
        "maize": "మొక్కజొన్న",
        "chickpea": "సెనగలు",
        "kidneybeans": "రాజ్మా",
        "pigeonpeas": "రేగుట",
        "mothbeans": "అడవిలుల్లు",
        "mungbean": "పెసర్లు",
        "blackgram": "మినుములు",
        "lentil": "మసూరి",
        "pomegranate": "దానిమ్మ",
        "banana": "అరటి",
        "mango": "మామిడి",
        "grapes": "ద్రాక్ష",
        "watermelon": "పుచ్చకాయ",
        "muskmelon": "కిర్ణాటినిమ్మ",
        "apple": "ఆపిల్",
        "orange": "నారింజ",
        "papaya": "బొప్పాయి",
        "coconut": "కొబ్బరి",
        "cotton": "బట్టాణి",
        "jute": "జూట్",
        "coffee": "కాఫీ"
    }

    int_features = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = soilmodel.predict(final_features)
    predicted_crop = prediction[0]
    
    # Get the Telugu translation of the predicted crop if available, otherwise use the original name
    telugu_crop = telugu_translations.get(predicted_crop, predicted_crop)
    
    return render_template('soiltelugu.html', prediction_text='నేల ఆరోగ్య పరిస్థితికి సూచించబడిన పంట: "{}".'.format(telugu_crop))





@app.route('/soilpredicthindi', methods=['POST'])
def soilpredicthindi():
    '''
    For rendering results on HTML GUI
    '''
    hindi_translations = {
        "rice": "चावल",
        "maize": "मक्का",
        "chickpea": "चना",
        "kidneybeans": "राजमा",
        "pigeonpeas": "अरहर",
        "mothbeans": "मोथ",
        "mungbean": "मूंग",
        "blackgram": "उड़द",
        "lentil": "मसूर",
        "pomegranate": "अनार",
        "banana": "केला",
        "mango": "आम",
        "grapes": "अंगूर",
        "watermelon": "तरबूज",
        "muskmelon": "खरबूजा",
        "apple": "सेब",
        "orange": "संतरा",
        "papaya": "पपीता",
        "coconut": "नारियल",
        "cotton": "कपास",
        "jute": "जूट",
        "coffee": "कॉफी"
    }

    int_features = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = soilmodel.predict(final_features)
    predicted_crop = prediction[0]
    
    # Get the Hindi translation of the predicted crop if available, otherwise use the original name
    hindi_crop = hindi_translations.get(predicted_crop, predicted_crop)
    
    return render_template('soilhindi.html', prediction_text='मिट्टी स्वास्थ्य विश्लेषण के आधार पर सिफारिशित फसल: "{}"'.format(hindi_crop))




#Fertilizer
@app.route('/fertilizerpredict',methods=['POST'])
def fertilizerpredict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = fertilizermodel.predict(final_features)
    output = prediction
    return render_template('fertilizer.html', prediction_text='Suggested Fertilizer for given soil health condition is: "{}".'.format(output[0]))


@app.route('/fertilizerpredicthindi', methods=['POST'])
def fertilizerpredicthindi():
    '''
    For rendering results on HTML GUI
    '''
    hindi_translations = {
        "Urea": "यूरिया",
        "DAP": "डीएपी",
        "14-35-14": "14-35-14",
        "28-28": "28-28",
        "17-17-17": "17-17-17",
        "20-20": "20-20",
        "10-26-26": "10-26-26"
    }

    int_features = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = fertilizermodel.predict(final_features)
    predicted_fertilizer = prediction[0]

    # Get the Hindi translation of the predicted fertilizer if available, otherwise use the original name
    hindi_fertilizer = hindi_translations.get(predicted_fertilizer, predicted_fertilizer)

    return render_template('fertilizerhindi.html', prediction_text='मिट्टी स्वास्थ्य विश्लेषण के आधार पर सिफारिशित उर्वरक: "{}"'.format(hindi_fertilizer))


@app.route('/fertilizerpredicttelugu', methods=['POST'])
def fertilizerpredicttelugu():
    '''
    For rendering results on HTML GUI
    '''
    telugu_translations = {
        "Urea": "యూరియా",
        "DAP": "డిఎపి",
        "14-35-14": "14-35-14",
        "28-28": "28-28",
        "17-17-17": "17-17-17",
        "20-20": "20-20",
        "10-26-26": "10-26-26"
    }

    int_features = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = fertilizermodel.predict(final_features)
    predicted_fertilizer = prediction[0]

    # Get the Telugu translation of the predicted fertilizer if available, otherwise use the original name
    telugu_fertilizer = telugu_translations.get(predicted_fertilizer, predicted_fertilizer)

    return render_template('fertilizertelugu.html', prediction_text='భూమి ఆరోగ్య విశ్లేషణ ఆధారంగా సిఫార్శ్ చేసిన ఎరువు: "{}"'.format(telugu_fertilizer))




#crop yield
@app.route('/yieldpredict',methods=['POST'])
def yieldpredict():
    '''
    For rendering results on HTML GUI
    '''
    
    int_features = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = yieldmodel.predict(final_features)
    
    output = prediction

    return render_template('yield.html', prediction_text='Crop Yield Acquired  is: "{}".'.format(output[0]))



#crop yield telugu
@app.route('/yieldpredicttelugu',methods=['POST'])
def yieldpredicttelugu():
    '''
    For rendering results on HTML GUI
    '''
    
    int_features = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = yieldmodel.predict(final_features)
    
    output = prediction

    return render_template('yieldtelugu.html', prediction_text='పొందిన పంట దిగుబడి : "{}".'.format(output[0]))






@app.route('/yieldpredicthindi', methods=['POST'])
def yieldpredicthindi():
    '''
    '''

    int_features = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = yieldmodel.predict(final_features)

    output = prediction

    return render_template('yieldhindi.html', prediction_text='प्राप्त किया गया फसल उत्पादन: "{}".'.format(output[0]))





#soil analysis
@app.route('/soilpredict_api',methods=['POST'])
def soilpredict_api():
    '''
    For direct API calls trought request
    '''
    data = request.get_json(force=True)
    prediction = soilmodel.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)

#Fertilizer
@app.route('/fertilizerpredict_api',methods=['POST'])
def fertilizerpredict_api():
    '''
    For direct API calls trought request
    '''
    data = request.get_json(force=True)
    prediction = fertilizermodel.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)

#Yield
@app.route('/yieldpredict_api',methods=['POST'])
def yieldpredict_api():
    '''
    For direct API calls trought request
    '''
    data = request.get_json(force=True)
    prediction = yieldmodel.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8080)