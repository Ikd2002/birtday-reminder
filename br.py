import telebot
from datetime import datetime, timedelta
import gspread
from oauth2client.service_account import ServiceAccountCredentials

TOKEN = '7.......0:A..........................U'
CHAT_ID = '-4........0'

# Получаем credentials файл, который содержит информацию для авторизации
scope = ['https://www.googleapis.com/auth/drive', 'https://www.googleapis.com/auth/spreadsheets']
creds = ServiceAccountCredentials.from_json_keyfile_name('/root/scripts/birthday-reminder-420216-b........d.json', scope)

# Создаем клиент для работы с Google Sheets
client = gspread.authorize(creds)

# Открываем рабочую книгу по ее имени или URL
sheet_url = 'https://docs.google.com/spreadsheets/d/1tkHAG-m............................Q/edit#gid=0' # Замените на URL вашего Google Sheet
workbook = client.open_by_url(sheet_url)

# Получаем рабочий лист по его имени
sheet = workbook.worksheet('Лист2')

print (datetime.now().date().strftime("%d.%m"))
print ((datetime.now().today() + timedelta(days=3)).strftime("%d.%m"))

# Обработка данных
for row in sheet.get_all_values():
   name = {row[0]}
   birthday = {row[1]}

# Проверка дня рождения
   print(f"Имя: {row[0]}, Дата рождения: {row[1]}")
   if datetime.now().date().strftime("%d.%m") == str(row[1]):
   # Отправка уведомления через Telegram
      bot = telebot.TeleBot(TOKEN)
      bot.send_message(CHAT_ID, f'{row[0]} сегодня отмечает свой день рождения!')

# Проверка дня рождения через 3 дня
   if (datetime.now().today() + timedelta(days=3)).strftime("%d.%m") == str(row[1]):
    # Отправка уведомления через Telegram
      bot = telebot.TeleBot(TOKEN)
      bot.send_message(CHAT_ID, f'{row[0]} через 3 дня отмечает свой день рождения!')
