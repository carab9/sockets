# Sockets

This project includes a client program and a server program.  The server starts out building a database by reading a XML file containing yearly climate data (1990-2017) for a list of countries and then waits for the client to send a request to the server through sockets to request all of the  yearly climate data for a specific country. The client sends a request through a socket with a country name selected by the user from GUI to the server and waits for the server to send back the climate data for the country and then displays it in the GUI. The client also runs linear regression on the data and displays the regression line for year vs value.

## Architecture

My code has an architecture with 3 layers: a UI layer that contains components required to enable user interaction with the application; a Business Layer that processes the input data; and a Data Layer that controls access logic components to access the data.

![image](https://github.com/carab9/sockets/blob/main/architecture.png)

The UI layer consists of the UI and Graph classes. The Graph Class creates and displays  the pie graphs. The UI class creates the interface that the user interacts with: the main window in the client program.

The Business layer consists of the FileIO and Database classes. The FileIO class scrapes the necessary data from the webpage and processes it. The Database class creates a database and stores the data into the database. It also gets the data from the database for the UI layer to graph the data.

The Data layer consists of the SqliteDB class, which provides the SQL APIs to create, store and access the SQLite database 

![image](https://github.com/carab9/sockets/blob/main/client_server.png)

The UI layer is in the client program and the Business layer and the Data layer are in the server program. The client and the server communicate through sockets.

## Requirements

Client:
Python, and Python Libraries: pandas, socket, json, pandas, matplotlib.figure, matplotlib.backends.backend_tkagg, tkinter
Run the program: python Client.py

Server:
Python and Python Libraries: re, pandas, socket, json, sqlite3, bs4.BeautifulSoup
Run the program: python main.py

## Technical Skills

Socket and json for interprocess communication and data transmission, bs4.BeautifulSoup for web scraping, pandas dataframe for data processing, SQLite for database, matplotlib Figure and FigureCanvasTkAgg for plotting graphs. Tkinter for GUIs.

## Results

This chart shows the linear regression between climate data levels and year, displayed alongside a scatter plot for the country Australia.

![image](https://github.com/carab9/sockets/blob/main/linreg_graph.png)


![image](https://github.com/carab9/sockets/blob/main/linreg_graph_menu.png)
