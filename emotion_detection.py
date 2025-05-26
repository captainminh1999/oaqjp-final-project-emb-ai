import requests
import json # Used for constructing the JSON payload

def emotion_detector(text_to_analyze):
    """
    Detects emotions in the given text using the Watson NLP Emotion Predict API.

    Args:
        text_to_analyze (str): The text string to be analyzed for emotions.

    Returns:
        str or None: The raw JSON response as a string from the Watson NLP API if successful,
                     otherwise None if an error occurs during the request.
                     The API response will contain the predicted emotion scores.
    """
    # Define the API endpoint URL
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # Define the headers required by the API
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Construct the input JSON payload with the text to be analyzed
    input_json = { "raw_document": { "text": text_to_analyze } }

    try:
        # Make the POST request to the Watson NLP API
        # The 'json' parameter automatically sets Content-Type to application/json
        response = requests.post(url, headers=headers, json=input_json)

        # Raise an HTTPError for bad responses (4xx or 5xx status codes)
        response.raise_for_status()

        # As per the instructions, return the 'text' attribute of the response object.
        # For a requests.Response object, `response.text` provides the raw response body
        # as a string, which in this case will be the JSON string from the API.
        return response.text

    except requests.exceptions.RequestException as e:
        # Catch any request-related errors (e.g., network issues, invalid URL, bad status codes)
        print(f"Error during API request: {e}")
        return None # Return None to indicate failure

    except Exception as e:
        # Catch any other unexpected errors
        print(f"An unexpected error occurred: {e}")
        return None

