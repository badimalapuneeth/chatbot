import json

# Load responses
def load_data():
    with open("responses.json", "r") as f:
        return json.load(f)


def get_response(user_input, data):
    user_input = user_input.lower()

    for key, patterns in data.items():
        for pattern in patterns:
            if pattern in user_input:
                return generate_reply(key)

    return "I don't understand. Please try again."


def generate_reply(intent):
    responses = {
        "greeting": "Hello! How can I help you?",
        "name": "I am a Python chatbot 🤖",
        "bye": "Goodbye! Have a nice day!",
        "thanks": "You're welcome!"
    }
    return responses.get(intent, "Okay")


def chatbot():
    data = load_data()

    print("Chatbot: Hello! Type 'exit' to quit.")

    while True:
        try:
            user_input = input("You: ")

            if user_input.lower() == "exit":
                print("Chatbot: Goodbye!")
                break

            reply = get_response(user_input, data)
            print("Chatbot:", reply)

        except Exception as e:
            print("Error:", e)


if __name__ == "__main__":
    chatbot()