'Chat Room Connection - Client-To-Client'
import threading
import socket

host = '127.0.0.1'
port = 59000

#setting up socket for server:
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))

#active lsitening
server.listen()
#keeping rec. of necessary data to commu.
clients = []
aliases = []

#Zookeeper broadcasts what ever it recv.
def broadcast(message):
    for client in clients:
        client.send(message)

# Function clients'connections

# Welcomming new clients & removing them also:
def handle_client(client):
    while 1:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            
            alias = aliases[index]
            
            #broadcast(f'{alias} has left the chat room!'.encode('utf-8'))
            print(f'{alias} has left the chat room!'.encode('utf-8'))
            aliases.remove(alias)
            break
#function -receive the clients connection


def receive():
    while 1:
        print('Server is running and listening ...')
        client, address = server.accept()
        
        print(f'connection is established with {str(address)}')
        client.send('alias?'.encode('utf-8'))
        
        alias = client.recv(1024)
        aliases.append(alias)
        clients.append(client)
        
        print(f'The alias of this client is {alias}'.encode('utf-8'))
        broadcast(f'{alias} has connected to the chat room'.encode('utf-8'))
        
        client.send('you are now connected!'.encode('utf-8'))
        my_thread = threading.Thread(target=handle_client, args=(client,))
        
        my_thread.start()


if __name__ == "__main__":
    receive()