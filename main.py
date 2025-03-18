import requests
import random
import time
import os
from colorama import Fore

print("░▒▓███████▓▒░░▒▓████████▓▒░▒▓███████▓▒░░▒▓███████▓▒░ ░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓███████▓▒░░▒▓██████▓▒░  ")
print("░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ ")
print("░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ ")
print("░▒▓███████▓▒░░▒▓██████▓▒░ ░▒▓███████▓▒░░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░ ░▒▓██████▓▒░░▒▓████████▓▒░ ")
print("░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ")
print("░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ")
print("░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░ ")
author = "Reproksa"
print("Author: " + author)
script = "Push Rank Discord"
print("Script: " + script)

time.sleep(1)

# Channel ID (langsung diisi)
channelnya = "846678373635457024"
channel_id = channelnya  # Langsung menggunakan nilai yang sudah ditentukan

# Waktu hapus dan kirim pesan (langsung diisi)
waktu1 = 7150  # Waktu hapus pesan (dalam detik)
waktu2 = 50  # Waktu kirim pesan (dalam detik)

time.sleep(1)
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)

os.system('cls' if os.name == 'nt' else 'clear')

# Baca file pesan.txt
with open("pesan.txt", "r") as f:
    words = f.readlines()

# Baca file token.txt
with open("token.txt", "r") as f:
    authorization = f.readline().strip()

# Loop utama
while True:
    channel_id = channel_id.strip()

    # Payload untuk mengirim pesan
    payload = {
        'content': random.choice(words).strip()
    }

    headers = {
        'Authorization': authorization
    }

    # Kirim pesan
    r = requests.post(f"https://discord.com/api/v9/channels/{channel_id}/messages", data=payload, headers=headers)
    print(Fore.WHITE + "Sent message: ")
    print(Fore.YELLOW + payload['content'])

    # Ambil pesan terbaru
    response = requests.get(f'https://discord.com/api/v9/channels/{channel_id}/messages', headers=headers)

    if response.status_code == 200:
        messages = response.json()
        if len(messages) == 0:
            is_running = False
            break
        else:
            time.sleep(waktu1)

            # Hapus pesan terbaru
            message_id = messages[0]['id']
            response = requests.delete(f'https://discord.com/api/v9/channels/{channel_id}/messages/{message_id}', headers=headers)
            if response.status_code == 204:
                print(Fore.GREEN + f'Pesan dengan ID {message_id} berhasil dihapus')
            else:
                print(Fore.RED + f'Gagal menghapus pesan dengan ID {message_id}: {response.status_code}')
    else:
        print(f'Gagal mendapatkan pesan di channel: {response.status_code}')

    time.sleep(waktu2)