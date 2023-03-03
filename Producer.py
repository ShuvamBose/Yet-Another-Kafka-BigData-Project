import threading
import socket


alias = input('Choose Producer-id: ')
#setting up socket connection
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_port=59000
client.connect(('127.0.0.1', my_port))


def Client_Recv():
    while 1:
        try:
            message = client.recv(1024).decode('utf-8')
            if message == "alias?":
                client.send(alias.encode('utf-8'))
            
        except:
            print('Error!')
            client.close()
            break


def Client_Send():
    while 1:
        message = f'{alias}: {input("")}'
        client.send(message.encode('utf-8'))


Client_Recv_Thread = threading.Thread(target=Client_Recv)
Client_Recv_Thread.start()

Client_Send_Thread = threading.Thread(target=Client_Send)
Client_Send_Thread.start()