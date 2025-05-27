from flask import Flask, render_template, request
from EmotionDetection import emotion_detector # Import the emotion_detector function from your package

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
    processes it using the emotion_detector, and returns a formatted string response.
    """
    # Get the text to analyze from the query parameters
    text_to_analyze = request.args.get('textToAnalyze')

    # Check if text_to_analyze is provided
    if not text_to_analyze:
        return "Invalid text provided. Please provide text to analyze.", 400

    # Call the emotion_detector function
    response = emotion_detector(text_to_analyze)

    # Check if the emotion_detector returned valid data (not all Nones due to API error)
    if all(value is None for value in response.values()):
        return "Error: Could not process emotion for the given text. Please try again later.", 500

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

