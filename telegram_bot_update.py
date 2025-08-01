import telebot
import pandas as pd
# Token dari BotFather
API_TOKEN = '8303052079:AAHg6qJvEuZax8dRft_0PqnpEQwzU-2DIr0'

# Inisialisasi bot
bot = telebot.TeleBot(API_TOKEN)

#load respon.csv sebagai database
data = pd.read_csv('respon_02.csv', sep=';')
print(data.columns)
respon_dict=dict(zip(data['keyword'], data['respon']))
print(respon_dict)

# Print untuk memastikan script mulai jalan
print("🤖 Bot sedang berjalan... Tekan Ctrl+C untuk berhenti.")

# Handler saat /start dikirim
@bot.message_handler(commands=['start'])
def welcome(message):
    print(f"[START] Pesan dari: {message.from_user.username} ({message.chat.id})")
    bot.reply_to(message, "Halo! Aku bot dari PC kamu 😄")

# Handler untuk semua pesan teks
@bot.message_handler(func=lambda message: True)
def handle_all_messages(message):
    teks = message.text.lower()
    print(f"[PESAN MASUK] {message.text} dari {message.from_user.username}")
    
    if teks in respon_dict:
        bot.reply_to(message, respon_dict[teks])#balas sesuai jawaban
    else:
        bot.reply_to(message,"maaf, aku masih belajar jawab itu 😄")
        
# Jalankan bot
bot.infinity_polling()
