emotions = {"Happy":["joy","happy","glad","smiling"],
            "Sad":["sad","sorrow","unhappy","cry"],
            "Angry":["angry","mad","furious","annoyed"],
            "Surprise":["surprised","amazed","shocked","stunned"],
            "Fear":["fear","afraid","anxious","horror"],
            "Love":["love","like","caring","friendship"]
            }
sentence = str(input("Enter a sentence :"))
words = sentence.lower().split()

for emotion,keywords in emotions.items():
    for word in words:
        if word in keywords:
            print(f"The emotion expressed in the sentence is: {emotion}")
            break