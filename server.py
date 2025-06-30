import socket

HOST="127.0.0.1" #change this to your server ip
PORT=12345 #change this to your server port

# Create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST,PORT))
s.listen(1)

print(f"[+] Server is Listening on {HOST} : {PORT}")

while True:
    client,addr=s.accept()
    data=client.recv(1024).decode()
    print(f"{addr} {data}")
    with open("logs.txt","a") as file:
        file.write(data)
    client.close()