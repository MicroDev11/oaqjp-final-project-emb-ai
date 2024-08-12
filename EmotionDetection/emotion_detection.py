import requests
import json

def emotion_detector(text_to_analyze):
    # URL of emotion detector service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # Set the headers required for the API request
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    # Payload for the POST request
    input_json = { 
        "raw_document": { 
            "text": text_to_analyze 
        } 
    }

    # Send POST request to API
    response = requests.post(url, headers=headers, json=input_json)

    # Convert response text into a dictionary using the json library
    formatted_response = json.loads(response.text)

    # Extract emotion predictions from the response
    emotion_predictions = formatted_response['emotionPredictions'][0]['emotion']

    # Find the dominant emotion based on the highest score
    dominant_emotion = max(emotion_predictions.items(), key=lambda x: x[1])[0]

    # Return the emotion predictions and the dominant emotion
    return {
        "anger": emotion_predictions["anger"],
        "disgust": emotion_predictions["disgust"],
        "fear": emotion_predictions["fear"],
        "joy": emotion_predictions["joy"],
        "sadness": emotion_predictions["sadness"],
        "dominant_emotion": dominant_emotion
    }
