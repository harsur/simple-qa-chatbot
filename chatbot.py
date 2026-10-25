print("CampusHelper: Hello! Ask me something, or type 'quit' to stop.")

while True:
    message = input("You: ").strip()

    if message.lower() in ["quit", "exit", "bye"]:
        print("CampusHelper: Goodbye!")
        break
    elif message == "":
        print("CampusHelper: Please enter a message.")
    elif "hello" in message.lower() or "good morning" in message.lower():
        print("CampusHelper: Hello! How can I help you?")
    else:
        print("CampusHelper: I am a simple chatbot. Please ask me another question.")