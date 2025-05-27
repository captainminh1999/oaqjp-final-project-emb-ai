"""
This Flask application serves an emotion detection web interface.

It leverages the EmotionDetection package to analyze text input and display
the dominant emotion along with individual emotion scores. Includes basic
error handling for blank text input.
"""
from flask import Flask, render_template, request
from EmotionDetection import emotion_detector # Import emotion_detector function

# Initialize the Flask application
app = Flask(__name__)

@app.route("/")
def render_index_page():
    """
    Renders the main index.html page when the root URL is accessed.
    This page will contain the user interface for inputting text.
    """
    return render_template('index.html')

@app.route("/emotionDetector")
def emotion_detector_route():
    """
    Handles requests to the /emotionDetector endpoint.

    It takes 'textToAnalyze' as a query parameter,
    processes it using the emotion_detector, and returns a formatted
    string response. Includes error handling for invalid/blank text input.
    """
    # Get the text to analyze from the query parameters
    text_to_analyze = request.args.get('textToAnalyze')

    # Call the emotion_detector function
    response = emotion_detector(text_to_analyze)

    # If dominant_emotion is None, it indicates an error or invalid input
    # (e.g., from a blank entry handled by emotion_detector's 400 status code check)
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    # Extract the emotion scores and dominant emotion
    anger = response.get('anger')
    disgust = response.get('disgust')
    fear = response.get('fear')
    joy = response.get('joy')
    sadness = response.get('sadness')
    dominant_emotion = response.get('dominant_emotion')

    # Format the output string as requested by the customer
    formatted_output = (
        f"For the given statement, the system response is 'anger': {anger}, "
        f"'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and "
        f"'sadness': {sadness}. The dominant emotion is {dominant_emotion}."
    )

    return formatted_output

if __name__ == "__main__":
    # Run the Flask application on localhost:5000
    # debug=True allows for automatic reloading on code changes and provides a debugger
    app.run(host="0.0.0.0", port=5000, debug=True)
