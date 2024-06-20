import random
import re

# Define patterns and responses
patterns = [
    (r'hi|hello|hey', ['Hello!', 'Hi there!', 'Hey!']),
    (r'what is your name?', ['My name is SimpleBot.', 'You can call me SimpleBot.']),
    (r'how are you?', ['I am doing well, thank you!', 'I am great, thanks for asking!']),
    (r'bye|goodbye', ['Goodbye!', 'Talk to you later!', 'Bye bye!']),
    (r'what can you do?', ['I can have simple conversations and answer basic questions.', 'I am a simple chatbot that can engage in basic dialog.']),
    (r'tell me a joke', ['Why don\'t scientists trust atoms? Because they make up everything!', 'What do you call a bear with no teeth? A gummy bear!'])
]

def chatbot_response(user_input):
    for pattern, responses in patterns:
        if re.search(pattern, user_input, re.IGNORECASE):
            return random.choice(responses)
    return "I'm sorry, I didn't understand. Can you please rephrase?"

print("SimpleBot: Hi there! I'm SimpleBot. How can I assist you today?")
while True:
    user_input = input("User: ")
    if user_input.lower() == 'quit':
        print("SimpleBot: Goodbye! Have a great day!")
        break
    else:
        print("SimpleBot:", chatbot_response(user_input))