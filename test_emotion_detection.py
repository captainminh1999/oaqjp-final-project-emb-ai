from EmotionDetection import emotion_detector

def run_visual_emotion_check():
    """
    Runs emotion detection for a predefined set of statements and prints
    the statement and the detected dominant emotion in a columnar format
    for visual inspection.
    """
    # Define statements and their expected dominant emotions for testing
    # The expected emotion is included here for clarity, but the script
    # will dynamically determine the dominant emotion from the API response.
    statements_to_test = [
        "I am glad this happened",        # Expected: joy
        "I am really mad about this",     # Expected: anger
        "I feel disgusted just hearing about this", # Expected: disgust
        "I am so sad about this",         # Expected: sadness
        "I am really afraid that this will happen" # Expected: fear
    ]

    print(f"{'Statement':<50} | {'Dominant Emotion':<20}")
    print(f"{'-'*50} | {'-'*20}")

    for statement in statements_to_test:
        result = emotion_detector(statement)
        dominant_emotion = result.get('dominant_emotion', 'N/A') # Handle cases where dominant_emotion might be missing

        print(f"{statement:<50} | {dominant_emotion:<20}")

if __name__ == '__main__':
    run_visual_emotion_check()

