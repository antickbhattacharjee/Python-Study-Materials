from google import genai    # pip install google-genai

API_KEY = "AIzaSyALgHqskSM3f-bYgx1jffluJjZ2WeVF2vg"

def main():
    client = genai.Client(api_key=API_KEY)
    chat = client.chats.create(model="gemini-2.5-flash")

    print("Google GenAI Chatbot (Interpreter Style)")
    print("Type 'exit' to quit.\n")

    while True:
        user = input("You: ").strip()
        if user.lower() in ["exit", "quit", "bye"]:
            print("Chatbot: Goodbye!")
            break

        try:
            resp = chat.send_message(user)
            print("\nChatbot:", resp.text, "\n")

        except Exception as e:
            print("Error:", e)
            break

    client.close()

if __name__ == "__main__":
    main()