def get_response(message):
    message = message.lower()

    if "hello" in message or "hi" in message or "hey" in message:
        return "Hi! How are you?"
    elif "how are you" in message:
        return "I'm fine, thanks! How about you?"
    elif "your name" in message or "who are you" in message:
        return "I am a simple chatbot made with Python!"
    elif "joke" in message:
        return "Why do programmers prefer dark mode? Because light attracts bugs!"
    elif "help" in message:
        return "I can chat with you! Try saying hello, ask how I am, or say bye."
    elif "bye" in message or "goodbye" in message:
        return "Goodbye! Have a nice day!"
    else:
        return "I don't understand that. Can you try something else?"


print("Chatbot is running! Type 'bye' to exit.")

while True:
    user_input = input("You: ")
    response = get_response(user_input)
    print("Bot:", response)

    if "bye" in user_input.lower() or "goodbye" in user_input.lower():
        break
