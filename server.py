from flask import Flask, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector', methods=['POST'])
def emotion_detector_route():
    # Get the input text from the request
    data = request.get_json()
    text_to_analyze = data.get('text')

    if not text_to_analyze:
        return jsonify({"error": "No text provided"}), 400

    # Use the emotion_detector function to analyze the text
    result = emotion_detector(text_to_analyze)

    # Format the response as required
    response_text = (
        f"For the given statement, the system response is 'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, 'fear': {result['fear']}, 'joy': {result['joy']} "
        f"and 'sadness': {result['sadness']}. The dominant emotion is {result['dominant_emotion']}."
    )

    # Return the formatted response
    return jsonify({"response": response_text})

if __name__ == '__main__':
    # Run the Flask application on localhost:5000
    app.run(host='0.0.0.0', port=5000)