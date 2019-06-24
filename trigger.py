from pythonosc import udp_client
import time

RAPID_SYNCS = 5

def play(ip, filename):
    try:
        client = udp_client.SimpleUDPClient(ip, 5432)
        client.send_message("/play", filename)
    except OSError:
        print("No network")

def play_all():
    print("Play all")
    play("192.168.42.60", "menu1.mp4")
    play("192.168.42.61", "menu2.mp4")
    play("192.168.42.62", "menu3.mp4")

network_up = False
while not network_up:
    try:
        play_all()
        network_up = True
    except OSError:
        print("No network")

i = RAPID_SYNCS
while i > 0:
    time.sleep(10)
    play_all()
    i -= 1

while True:
    play_all()
    time.sleep(300)