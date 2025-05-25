# Rule-Based Chatbot for Answering Predefined Questions

print("Hello! I'm a simple chatbot. Type 'menu' to see what you can ask. Type 'exit' to end the chat.")

while True:
    # Step 1: Get user input
    user_input = input("You: ").lower().strip()

    # Step 2: Exit condition
    if user_input in ['exit', 'quit', 'bye']:
        print("Chatbot: See you next time! Take care!")
        break

    # Step 3: Menu/Help option
    elif user_input in ["help", "menu", "options"]:
        print("Chatbot: Here's what you can ask me:")
        print("- What are your working hours?")
        print("- How to reset your password?")
        print("- Where are you located?")
        print("- What services do you offer?")
        print("- What's your name?")
        print("- Tell me a joke!")
        print("- Can you solve 2+2 or other math questions?")

    # Step 4: Predefined Q&A responses
    elif "your name" in user_input:
        print("Chatbot: I'm ChatBot 1.0!")
    elif "how are you" in user_input:
        print("Chatbot: I'm doing great, thank you!")
    elif "working hours" in user_input:
        print("Chatbot: Our working hours are 9 AM to 5 PM, Monday through Friday.")
    elif "reset password" in user_input:
        print("Chatbot: To reset your password, click on 'Forgot Password' on the login screen.")
    elif "location" in user_input:
        print("Chatbot: We are located in Hyderabad, Telangana.")
    elif "services" in user_input:
        print("Chatbot: We offer IT consulting, software development, and training services.")
    elif "creator" in user_input or "who made you" in user_input:
        print("Chatbot: I was created by Samyuktha for a Generative AI project!")
    elif "version" in user_input:
        print("Chatbot: You're chatting with ChatBot v1.0 — powered by rule-based logic!")
    elif "joke" in user_input:
        print("Chatbot: Why don’t programmers like nature? It has too many bugs. 😄")
    elif "thank you" in user_input or "thanks" in user_input:
        print("Chatbot: You're welcome! 😊 Happy to help!")

    # Step 5: Basic math evaluation
    elif any(char.isdigit() for char in user_input):
        try:
            result = eval(user_input)
            print(f"Chatbot: The answer is {result}")
        except:
            print("Chatbot: Hmm, I couldn’t calculate that. Please try a valid math expression.")

    # Step 6: Fallback for unknown input
    else:
        print("Chatbot: I'm sorry, I don't understand that yet. Type 'menu' to see what I can do.")
