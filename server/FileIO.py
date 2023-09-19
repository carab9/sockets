from bs4 import BeautifulSoup
import pandas as pd

class FileIO:
    def __init__(self):
        pass

    @staticmethod
    def read_xml_file(xml_file):
        xml = open(xml_file, "r")
        #df = pd.read_xml(xml)
        #print(df)
        contents = xml.read()
        soup = BeautifulSoup(contents, "xml")

        df = pd.DataFrame(columns=["Country", "Year", "Value"])

        counter = 0
        for data in soup.find_all('data'):
            for record in soup.find_all('record'):
                # for testing
                #counter += 1
                #if counter > 84:
                    #break
                print(record)
                country = record.find('Country').string
                #print(country)
                year = record.find('Year').string
                #print(year)
                value = record.find('Value').string
                #print(value)
                df.loc[len(df.index)] = [country, year, value]

        xml.close()

        #print(df)
        return df