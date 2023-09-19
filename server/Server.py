import sys
import re
import socket
import json
from DataBase import DataBase

class Server:
    def __init__(self, port, db):
        self.host = socket.gethostname()
        self.port = port  # initiate port no above 1024
        self.server_socket = socket.socket()  # get instance
        self.server_socket.bind((self.host, self.port))  # bind host address and port together
        self.db = db
    def connect(self, nports):
        # configure how many client the server can listen simultaneously
        self.server_socket.listen(nports)
        conn, address = self.server_socket.accept()  # accept new connection
        print("Connection from: " + str(address))
        while True:
            # receive data stream. it won't accept data packet greater than 1024 bytes
            data = conn.recv(1024).decode()
            if not data:
                # if data is not received break
                break
            print("from connected user: " + str(data))
            if str(data) == "GET COUNTRY LIST":
                country_list = self.db.get_country_list()
                country_list.sort()
                print(country_list)
                country_js = json.dumps(country_list)
                print(country_js)
                conn.send(country_js.encode())  # send data to the client
            if str(data[0:17]) == "GET COUNTRY DATA ":
                data = re.search(r'"(.+)" (\d+) (\d+)', data[17:])
                if data:
                    country = data.group(1)
                    start_year = data.group(2)
                    end_year = data.group(3)
                    print(country)
                    print(start_year)
                    print(end_year)
                    data_list = self.db.get_country_data(country, start_year, end_year)
                    data_js = json.dumps(data_list)
                    print(data_js)
                    conn.send(data_js.encode())  # send data to the client

        conn.close()  # close the connection


def main():
    string = 'Hello "Bob"'
    print(re.findall(r'"(.*?)"', string))
    db = DataBase()
    db.build("UNData.xml")
    db.get_country_list()
    db.get_country_data("Australia", 1992, 2005)
    server = Server(5000, db)
    server.connect(2)

if __name__ == '__main__':
    main()