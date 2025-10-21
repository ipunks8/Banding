#!/usr/bin/env python3
import smtplib
from email.message import EmailMessage
import os

# Ambil data dari environment
EMAIL_SENDER = os.getenv("EMAIL_SENDER")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
EMAIL_RECEIVER = os.getenv("EMAIL_RECEIVER")
PHONE_NUMBER = os.getenv("PHONE_NUMBER")
YOUR_NAME = os.getenv("YOUR_NAME")

# Isi email (body)
body = f"""Здравствуйте, команда поддержки WhatsApp.

Обращаюсь к вам с серьёзной проблемой, связанной с моим номером WhatsApp. Каждый раз, когда я пытаюсь зарегистрироваться или войти в систему, появляется сообщение: «Вход недоступен в данный момент».

Прошу вас как можно скорее разобраться с этой проблемой и восстановить возможность использования моего номера [{PHONE_NUMBER}] без подобных ошибок.

С уважением,
{YOUR_NAME}
"""

# Membuat pesan email tanpa subjek
msg = EmailMessage()
# Tidak ada msg["Subject"]
msg["From"] = EMAIL_SENDER
msg["To"] = EMAIL_RECEIVER
msg.set_content(body)

# Kirim email
try:
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(EMAIL_SENDER, EMAIL_PASSWORD)
        smtp.send_message(msg)
    print(f"✅ Email tanpa subjek terkirim untuk nomor {PHONE_NUMBER}")
except Exception as e:
    print("❌ Gagal kirim email:", e)
