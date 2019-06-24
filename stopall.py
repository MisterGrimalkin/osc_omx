from pythonosc import udp_client
import time

def stop(ip):
    client = udp_client.SimpleUDPClient(ip, 5432)
    client.send_message("/stop", "1")

stop("192.168.42.62")
stop("192.168.42.61")
stop("192.168.42.60")
