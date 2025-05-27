import requests
import json

def emotion_detector(text_to_analyze):
    """
    Detects emotions in the given text using the Watson NLP Emotion Predict API,
    parses the response, finds the dominant emotion, and returns a formatted dictionary.

    Args:
        text_to_analyze (str): The text string to be analyzed for emotions.

    Returns:
        dict: A dictionary containing scores for anger, disgust, fear, joy, sadness,
              and the name of the dominant emotion. Returns None for scores/dominant_emotion
              if an error occurs during the API request or JSON parsing.
    """
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }

    try:
        response = requests.post(url, headers=headers, json=input_json)
        response.raise_for_status() # Raises HTTPError for bad responses (4xx or 5xx)

        # Parse the JSON response text into a Python dictionary
        formatted_response = response.json()

        # --- MODIFIED LOGIC START ---
        # The raw API response shows emotions under 'emotionPredictions'
        emotions_data = {}
        if 'emotionPredictions' in formatted_response and formatted_response['emotionPredictions']:
            # Assuming we want the first prediction's emotion
            emotions_data = formatted_response['emotionPredictions'][0].get('emotion', {})
        # --- MODIFIED LOGIC END ---

        # Extract individual emotion scores, defaulting to 0.0 if a score is missing
        anger_score = emotions_data.get('anger', 0.0)
        disgust_score = emotions_data.get('disgust', 0.0)
        fear_score = emotions_data.get('fear', 0.0)
        joy_score = emotions_data.get('joy', 0.0)
        sadness_score = emotions_data.get('sadness', 0.0)

        # Store scores in a dictionary to easily find the dominant emotion
        scores_dict = {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score
        }

        # Find the dominant emotion (the one with the highest score)
        dominant_emotion = max(scores_dict, key=scores_dict.get)

        # Return the formatted dictionary
        return {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score,
            'dominant_emotion': dominant_emotion
        }

    except requests.exceptions.RequestException as e:
        print(f"API request error: {e}")
        return {
            'anger': None, 'disgust': None, 'fear': None, 'joy': None, 'sadness': None, 'dominant_emotion': None
        }
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON response: {e}. Raw response: {response.text if 'response' in locals() else 'No response'}")
        return {
            'anger': None, 'disgust': None, 'fear': None, 'joy': None, 'sadness': None, 'dominant_emotion': None
        }
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return {
            'anger': None, 'disgust': None, 'fear': None, 'joy': None, 'sadness': None, 'dominant_emotion': None
        }

