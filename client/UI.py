from tkinter import ttk
import tkinter as tk
from tkinter import *
import pandas as pd
from Graph import Graph

class UI:
    blackboard = None

    def __init__(self, client):
        self.client = client
        self.window = tk.Tk()
        self.window.title("Lab4")
        self.window.geometry('900x600')
        self.combobox = ttk.Combobox(self.window, width=25)
        self.combobox.bind('<<ComboboxSelected>>', self.get_country)
        self.combobox['state'] = 'readonly'
        self.label = Label(text="Countries")
        # pack the widgets
        self.label.pack()
        self.combobox.pack()
        self.graph = Graph(self.window)

    def get_country(self, event):
        country = self.combobox.get()
        print(country)
        values = self.client.execute_country_data(country, 1990, 2017)
        df = pd.DataFrame(columns=["Year", "Value"])
        index = 0
        for year in range(1990, 2018, 1):
            index = year - 1990
            df.loc[len(df.index)] = [year, values[index]]
        print(df)
        self.graph.display_lin_reg(df, 0, 1)

    def get_country_list(self):
        #countries = ['Australia', 'Austria', 'Belarus']
        countries = self.client.execute_country_list()
        self.combobox['values'] = tuple(countries)

    def run(self):
        self.get_country_list()
        self.window.mainloop()