#!/usr/bin/env python3
import os
import sys

if len(sys.argv) < 2:
    print("❌ Masukkan nomor WhatsApp! Contoh:\n   python kirim.py +6281234567890")
    sys.exit(1)

phone_number = sys.argv[1]
your_name = "Mateus"  # bisa kamu ubah kalau mau

print(f"🚀 Menjalankan workflow untuk nomor: {phone_number}")
os.system(f'gh workflow run "Kirim Email ke WhatsApp Support" -f phone_number="{phone_number}" -f your_name="{your_name}"')
