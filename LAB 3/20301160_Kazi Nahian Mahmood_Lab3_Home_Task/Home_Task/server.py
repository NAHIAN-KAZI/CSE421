import socket


port = 5090
data = 16
format = "utf-8"
disconnected_msg = 'End'
hostname = socket.gethostname()
host_addr = socket.gethostbyname(hostname)

server_socket_address = (host_addr, port)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(server_socket_address)

server.listen()
print('Our server is listening')

while True:
    conn,addr = server.accept()
    print(f"Connected to {addr}")
    connected = True
    while connected:
        initial = conn.recv(data).decode(format)
        print("Length of the message to be sent ", initial)
        if initial:
            msg_length = int(initial)
            msg = conn.recv(msg_length).decode(format)

            if msg == 'End':
                print('Terminating connection with ',addr)
                conn.send('Connection ended\n'.encode(format))
                connected = False
            else:
                hour = int(msg)
                if hour <= 40:
                    salary = hour * 200
                    conn.send(f'Salary: {salary}tk'.encode(format))
                elif hour > 40:
                    salary = 8000 + ((hour - 40) * 300)
                    conn.send(f'Salary: {salary}tk'.encode(format))
            
conn.close()
