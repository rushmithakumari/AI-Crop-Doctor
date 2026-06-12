import gradio as gr
import random
from datetime import datetime
def get_weather(location):
    conditions = ["Sunny", "Cloudy", "Rainy", "Humid", "Windy"]
    temp = random.randint(20, 38)
    rain_chance = random.randint(0, 100)

    return f"""
📍 Location: {location}
🌡 Temperature: {temp}°C
☁ Condition: {random.choice(conditions)}
🌧 Rain Chance: {rain_chance}%
"""
def detect_disease(image):
    diseases = [
        "Leaf Blight 🍂",
        "Rust Disease 🍁",
        "Healthy Crop 🌿",
        "Powdery Mildew ⚪",
        "Bacterial Spot 🔴"
    ]
    return f"Prediction: {random.choice(diseases)}"
def irrigation(temp, soil_moisture):
    temp = int(temp)
    soil_moisture = int(soil_moisture)

    if soil_moisture < 30 or temp > 32:
        return "💧 Irrigate immediately (High water need)"
    elif soil_moisture < 60:
        return "🚿 Light irrigation recommended"
    else:
        return "✅ No irrigation needed"
def yield_prediction(area, crop):
    base = random.randint(20, 40)
    yield_estimate = base * float(area)
    return f"🌾 Estimated {crop} yield: {yield_estimate:.2f} quintals"
def fertilizer_recommendation(crop):
    data = {
        "rice": "Use Nitrogen-rich fertilizer (Urea)",
        "wheat": "Use Potash + Phosphorus mix",
        "cotton": "Use balanced NPK fertilizer",
        "maize": "High Nitrogen fertilizer recommended"
    }

    return data.get(crop.lower(), "Use NPK balanced fertilizer")
def voice_assistant(query):
    responses = {
        "weather": "Today is mostly sunny with moderate humidity.",
        "irrigation": "Check soil moisture before watering crops.",
        "fertilizer": "Use NPK based fertilizer for best growth.",
        "disease": "Inspect leaves for spots or discoloration."
    }

    for key in responses:
        if key in query.lower():
            return responses[key]

    return "Sorry, I didn't understand. Try asking about weather, irrigation, fertilizer, or disease."
def ai_advisor(question):
    tips = [
        "Use drip irrigation to save water 💧",
        "Rotate crops to maintain soil fertility 🌱",
        "Use organic manure for better yield 🌿",
        "Monitor pests weekly for healthy crops 🐛",
        "Avoid overwatering during rainy season 🌧"
    ]
    return random.choice(tips)
def dashboard():
    return f"""
📊 FARM DASHBOARD
----------------------
📅 Date: {datetime.now().strftime('%Y-%m-%d')}
🌾 Crop Health: Good
💧 Water Level: Medium
🌱 Soil Quality: Fertile
📈 Growth Status: Stable
"""
def gps_tips(location):
    return f"📍 Farming Tip for {location}: Use local seasonal crops for higher yield and less water usage."
with gr.Blocks(title="AI Crop Doctor") as app:

    gr.Markdown("# 🌱 AI CROP DOCTOR (Smart Farming Assistant)")

    with gr.Tab("🌦 Weather"):
        loc = gr.Textbox(label="Enter Location")
        weather_out = gr.Textbox()
        gr.Button("Get Weather").click(get_weather, loc, weather_out)

    with gr.Tab("🌿 Disease Detection"):
        img = gr.Image(type="pil")
        disease_out = gr.Textbox()
        gr.Button("Detect Disease").click(detect_disease, img, disease_out)

    with gr.Tab("💧 Irrigation"):
        temp = gr.Textbox(label="Temperature")
        soil = gr.Textbox(label="Soil Moisture %")
        irr_out = gr.Textbox()
        gr.Button("Check Irrigation").click(irrigation, [temp, soil], irr_out)

    with gr.Tab("🌾 Yield Prediction"):
        area = gr.Textbox(label="Farm Area (acres)")
        crop = gr.Textbox(label="Crop Name")
        yield_out = gr.Textbox()
        gr.Button("Predict Yield").click(yield_prediction, [area, crop], yield_out)

    with gr.Tab("🌿 Fertilizer"):
        crop2 = gr.Textbox(label="Crop Name")
        fert_out = gr.Textbox()
        gr.Button("Get Fertilizer").click(fertilizer_recommendation, crop2, fert_out)

    with gr.Tab("🎙 Voice Assistant"):
        voice_in = gr.Textbox(label="Ask Question")
        voice_out = gr.Textbox()
        gr.Button("Ask").click(voice_assistant, voice_in, voice_out)

    with gr.Tab("🤖 AI Advisor"):
        q = gr.Textbox(label="Ask AI Farming Question")
        ai_out = gr.Textbox()
        gr.Button("Get Advice").click(ai_advisor, q, ai_out)

    with gr.Tab("📊 Dashboard"):
        dash_out = gr.Textbox()
        gr.Button("Show Dashboard").click(lambda: dashboard(), None, dash_out)

    with gr.Tab("📍 GPS Tips"):
        gps_in = gr.Textbox(label="Location")
        gps_out = gr.Textbox()
        gr.Button("Get Tips").click(gps_tips, gps_in, gps_out)
app.queue()
app.launch(share=True)