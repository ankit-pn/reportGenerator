import requests
from dataIndexerReport.generate_report import generate_pdf

bot_token = 'YOUR_TELEGRAM_BOT_TOKEN'
chat_id = 'YOUR_CHAT_ID'


def send_file_to_telegram_bot(token, chat_id):
    path = generate_pdf()
    file_path = f'../dataIndexerReport/{path}'
    url = f'https://api.telegram.org/bot{token}/sendDocument'
    with open(file_path, 'rb') as file:
        response = requests.post(url, data={'chat_id': chat_id}, files={'document': file})
    
    return response.json()



response = send_file_to_telegram_bot(bot_token, chat_id)
print(response)

