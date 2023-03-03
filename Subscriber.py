import threading
import socket

alias = input('Choose Subscriber-id: ')

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_port=59000
client.connect(('127.0.0.1', my_port))

#my_choices=[]

print("Enter your choices of Producer codes:",end='')
#taking i/p:
my_choices=str(input())

def Client_Recv_Sub():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message == "alias?":
                client.send(alias.encode('utf-8'))
            
            else:
                if message[1] in my_choices:#inbuilt broker selective 
                    print(message)
        except:
            print('Some Error!')
            client.close()
            break


def Client_Send_Sub():
    while True:
        message = f'{alias}: {input("")}'
        


receive_thread = threading.Thread(target=Client_Recv_Sub)
receive_thread.start()

send_thread = threading.Thread(target=Client_Send_Sub)
send_thread.start()