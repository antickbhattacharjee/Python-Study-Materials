def chatbot_reply(user_input):
    user_input = user_input.lower()  # Convert to lowercase to handle case-insensitive match

    if user_input == "hello":
        return "Hellooo! 🌟"
    elif user_input == "hi":
        return "Hi there, sunshine! ☀️"
    elif user_input == "how are you":
        return "I'm thriving like a bug in a rug! 😄 How about you?"
    elif user_input == "bye":
        return "See you later, alligator! 👋"
    elif user_input == "what's your name":
        return "I'm ChatMate — your tiny AI buddy! 🤖"
    elif user_input == "thank you":
        return "You're always welcome! 🙏"
    else:
        return "Hmm... I don't understand that yet. 🤔 Try saying 'hello' or 'bye'."

def run_chatbot():
    print("🤖 ChatBot: Hey there! I’m ChatMate, your tiny AI buddy. Type something to chat. (Type 'exit' to leave)")

    while True:
        user_input = input("\nYou: ")

        if user_input.lower() == "exit":
            print("🤖 ChatMate: Chat session ended. Take care! 💖")
            break  # Exit the loop and end chat
        else:
            response = chatbot_reply(user_input)
            print("🤖 ChatMate:", response)

user_input = input("Type 'start' to begin chatting or 'exit' to leave: ")
if user_input.lower() == "start":
    run_chatbot()
elif user_input.lower() == "exit":
    print("🤖 ChatMate: Goodbye! 👋")
else:
    print("🤖 ChatMate: I didn't understand that. Please type 'start' to chat or 'exit' to leave.")