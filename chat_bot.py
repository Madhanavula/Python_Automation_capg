from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create a chatbot instance
bot = ChatBot('MyBot')

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(bot)

# Train the chatbot on English language data
trainer.train('chatterbot.corpus.english')

# Function to get bot response
def get_bot_response(user_input):
    return bot.get_response(user_input)

# Example usage
while True:
    user_input = input("You: ")
    
    if user_input.lower() == 'exit':
        print("Exiting...")
        break
    
    response = get_bot_response(user_input)
    print("Bot:", response)



