from FileIO import FileIO
from SqliteDB import SqliteDB

class DataBase:
    def __init__(self):
        self.db = SqliteDB()
        self.db.connect("CIS41b")
        self.df = None

    def build(self, xml_file):
        df = FileIO.read_xml_file(xml_file)
        print(df)
        col_names = list(df.columns)
        print(col_names)

        cols = list()
        cols.append(("ID", "INTEGER"))
        cols.append((col_names[0], "TEXT"))
        cols.append((col_names[1], "INTEGER"))
        cols.append((col_names[2], "REAL"))
        print(cols)

        self.db.createTable(cols)

        for index, row in df.iterrows():
            row_tup = tuple(row)
            row_tup = (index,) + row_tup
            print("row list:", row_tup)
            self.db.insert(row_tup)

        print(self.db.readTableToDf())

    def get_country_list(self):
        countries = self.db.search_column("Country")
        print(countries)
        country_list = list(set(countries))
        print(country_list)
        country_list = [c[0] for c in country_list]
        print(country_list)
        return country_list

    def get_country_data(self, name, start_year, end_year):
        country_data = self.db.search_row(name, start_year, end_year)
        print(country_data)
        data_list = [c[3] for c in country_data]
        print(data_list)
        return data_list