'''
📘 Python Assignment: Emotion Detector using Function and List
Problem Statement:

Write a Python program that detects emotions from a given sentence using functions and lists/dictionaries.

Requirements:

Define a function emotion_detector(sentence) that:
Accepts a sentence (string) as input.
Contains a dictionary of emotion keywords where each key is an emotion (e.g., "happy", "sad", "angry", "fear", "love") and the value is a list of words related to that emotion.
Scans the sentence, checks for the presence of these words, and counts how many times each emotion appears.
Returns the strongest emotion(s) (the one with the highest count).
If no emotion is detected, return "neutral".
Test your function with at least 5 sample sentences covering different emotions.

Example Input/Output:

print(emotion_detector("I am very happy and excited today!"))
Output:
['happy']

print(emotion_detector("He made me so angry and furious yesterday."))
Output:
['angry']

print(emotion_detector("I love and admire her a lot, she makes me so happy."))
Output:
['love']

Expected Skills Tested:

✔ Function creation and usage
✔ Working with lists and dictionaries
✔ String manipulation (lowercasing, splitting words)
✔ Conditional logic for multiple outcomes
'''


def emotion_detector(sentence):
    # Emotion keyword dictionary
    emotion_words = {
        "happy": ["happy", "joy", "glad", "delighted", "excited", "pleased"],
        "sad": ["sad", "unhappy", "down", "depressed", "cry", "lonely"],
        "angry": ["angry", "mad", "furious", "irritated", "annoyed", "rage"],
        "fear": ["scared", "afraid", "fear", "nervous", "worried", "anxious"],
        "love": ["love", "affection", "caring", "fond", "romantic", "admire"]
    }

    # Normalize sentence
    sentence = sentence.lower().split()

    # Count emotions
    emotion_count = {emotion: 0 for emotion in emotion_words}

    for word in sentence:
        for emotion, keywords in emotion_words.items():
            if word in keywords:
                emotion_count[emotion] += 1

    # Find the strongest emotion(s)
    max_count = max(emotion_count.values())
    
    if max_count == 0:
        return ["neutral"]

    strongest_emotions = [emotion for emotion, count in emotion_count.items() if count == max_count]
    
    return strongest_emotions


# Example Tests
print(emotion_detector("I am very happy and excited today!"))
print(emotion_detector("He made me so angry and furious yesterday."))
print(emotion_detector("I am scared and nervous about my exams."))
print(emotion_detector("This is just a normal boring day."))
print(emotion_detector("I love and admire her a lot, she makes me so happy."))
