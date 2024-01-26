from flask import Flask, request, jsonify
from flask_cors import CORS  # If needed for cross-origin requests
from test import detect_emotion # Import your emotion recognition logic

app = Flask(__name__)
CORS(app)  # Enable CORS if your frontend is on a different domain

@app.route('/detect-emotion', methods=['POST'])
def detect_emotion_endpoint():
    try:
        # Assuming the frontend sends the image data in the 'image' field
        image_data = request.json['image']
        
        # Perform emotion recognition
        detected_emotion = detect_emotion(image_data)

        # Return the detected emotion as JSON
        return jsonify({'emotion': detected_emotion})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
