import os
from pythonosc import dispatcher
from pythonosc import osc_server

PLAYER = "omxplayer"

PLAYER_ARGS = {
    "totem": "",
    "omxplayer": "--loop --no-osd"
}

def play(addr, args, value):
    print("Play file: {}".format(value))
    stop(addr, args, value)
    os.system("{} media/{} {}".format(PLAYER, value, PLAYER_ARGS[PLAYER]))

def stop(addr, args, value):
    print("Stop")
    os.system("pkill {}".format(PLAYER))
    pass

dispatcher = dispatcher.Dispatcher()
dispatcher.map("/play", play, "play")
dispatcher.map("/stop", stop, "stop")

server = osc_server.ThreadingOSCUDPServer((os.popen("hostname -I").read().strip(), 5432), dispatcher)
print("Listening for OSC on {}".format(server.server_address))
server.serve_forever()
