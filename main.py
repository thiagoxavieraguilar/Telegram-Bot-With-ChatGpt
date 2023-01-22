import openai
import telebot

#api telebot
bot = telebot.TeleBot("")

# OpenAI API key
openai.api_key = ""


@bot.message_handler(content_types=["text"])
def chatbot_response(message):
    # get user's message
    user_message = message.text
    
    # use OpenAI to generate response
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"{user_message}",
        max_tokens=2048,
        n = 1,
        stop=None,
        temperature=0.8
    )
    
    # send response back to user
    bot.reply_to(message, response["choices"][0]["text"])

bot.polling()
