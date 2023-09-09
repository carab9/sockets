# Client socket class
import socket
import json
from UI import UI


class Client:
    def __init__(self,nport):
        self.host = socket.gethostname()  # as both code is running on same pc
        self.port = nport  # socket server port number
        self.client_socket = socket.socket()  # instantiate
        self.client_socket.connect((self.host, self.port))  # connect to the server
    def connect(self):
        message = input(" -> ")  # take input
        while message.lower().strip() != 'bye':
            self.client_socket.send(message.encode())  # send message
            data = self.client_socket.recv(1024).decode()  # receive response
            print('Received from server: ' + data)  # show in terminal
            message = input(" -> ")  # again take input
        self.client_socket.close()  # close the connection
    def execute_country_list(self):
        message = "GET COUNTRY LIST"
        self.client_socket.send(message.encode())  # send message
        data = self.client_socket.recv(1024).decode()  # receive response
        print('Received from server: ' + data)  # show in terminal
        country_list = json.loads(data)
        return country_list
    def execute_country_data(self, country, start_year, end_year):
        message = "GET COUNTRY DATA \"" + country + "\" " + str(start_year) + " " + str(end_year)
        print(message)
        self.client_socket.send(message.encode())  # send message
        data = self.client_socket.recv(1024).decode()  # receive response
        print('Received from server: ' + data)  # show in terminal
        country_data = json.loads(data)
        print(country_data)
        return country_data



if __name__ == '__main__':
    client = Client(5000)
    #client.connect()
    #client = None
    ui = UI(client)
    ui.run()
