import nltk
import random
from nltk.chat.util import Chat, reflections

# Define chatbot responses using pairs of patterns and responses
pairs = [
    ["hi|hello|hey", ["Hello!", "Hi there!", "Hey!"]],
    ["how are you", ["I'm doing well, how about you?", "I'm fine, thanks for asking!"]],
    ["what is your name", ["I'm a chatbot!", "You can call me ChatBot."]],
    ["bye|goodbye", ["Goodbye!", "See you later!", "Have a great day!"]],
]

# Create chatbot
chatbot = Chat(pairs, reflections)

# Start chat
print("🤖 Chatbot: Hello! Type 'bye' to exit.")
while True:
    user_input = input("You: ").lower()
    if user_input == "bye":
        print("🤖 Chatbot: Goodbye! Have a nice day.")
        break
    response = chatbot.respond(user_input)
    print("🤖 Chatbot:", response)
