import os
import pickle
import pandas as pd
from sklearn.ensemble import IsolationForest

# Model save path
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, "detection", "model.pkl")


def train_model(data_file):
    global model

    try:
        df = pd.read_csv(data_file)
       
        if len(df) < 5:
            print("⚠️ Not enough data to train AI")
            return False

        features = df[["port", "packet_size"]]
    

        model = IsolationForest(contamination=0.05, random_state=42)
        model.fit(features)

        # 💾 Save model
        with open(MODEL_PATH, "wb") as f:
            pickle.dump(model, f)

        print("🤖 AI Model Trained & Saved Successfully")
        return True

    except Exception as e:
        print("AI Training Error:", e)
        return False


def load_model():
    global model

    if os.path.exists(MODEL_PATH):
        with open(MODEL_PATH, "rb") as f:
            model = pickle.load(f)
        print("🤖 AI Model Loaded Successfully")
        return True

    return False
5
def detect_anomaly(port, packet_size):
    global model

    if model is None:
        return False

    # Create DataFrame with correct feature names
    input_data = pd.DataFrame(
        [[port, packet_size]],
        columns=["port", "packet_size"]
    )

    prediction = model.predict(input_data)

    return prediction[0] == -1