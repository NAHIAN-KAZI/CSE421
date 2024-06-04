import socket

format = 'utf-8'
data_size = 16
disconn_msg = 'End'
port = 5010   
hostname = socket.gethostname() 
host_addr = socket.gethostbyname(hostname) 
server_socket_address = (host_addr, port) 
client = socket.socket(socket.AF_INET ,  socket.SOCK_STREAM)                                                        
client.connect(server_socket_address)

def msg_send(msg):
    message = msg.encode(format)
    msg_length = str(len(message)).encode(format)
    msg_length += b" "*(data_size - len(msg_length))
    
    client.send(msg_length)
    client.send(message)

    print(client.recv(2048).decode(format))
    
while True:
    input_msg = input('enter your message ')
    if input_msg == 'Done':
        msg_send(disconn_msg)
        break
    else:
        msg_send(input_msg)



msg_send(f'IP address of the client {host_addr} and the device name is {hostname}.')
msg_send(disconn_msg)