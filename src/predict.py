import joblib

model = joblib.load('model/fire_model.pkl')

def predict_fire(temp, RH, wind, rain):
    features = [[temp, RH, wind, rain]]
    prediction = model.predict(features)
    return "🔥 Forest Fire Risk!" if prediction[0] == 1 else "✅ No Forest Fire Risk"
