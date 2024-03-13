from dotenv import load_dotenv
import os


# Получение значений переменных окружения
load_dotenv()

telegram_token = os.getenv('telegram_token')
gigachat_token = os.getenv('gigachat_token')
kandinsky_token = os.getenv('kandinsky_token')
kandinsky_secret_token = os.getenv('kandinsky_secret_token')
