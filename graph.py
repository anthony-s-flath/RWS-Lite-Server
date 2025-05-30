import pandas as pd
import plotly.express as px
import plotly.io as pio

#DIYgm-Server-Version/data/RWSlite-data-collection/RyanRWSlite-rws_lite_data1698869545.1947374.csv


class Graph:
    def __init__(self, query):
        print(query)
        if (len(dict (query)) == 0):
            self.data = pd.read_csv("data.csv")
            self.fig = px.scatter(x=self.data['time'], y=self.data['in_temp'])

    def as_html(self):
        return pio.to_html(self.fig, include_plotlyjs='cdn').encode()



def main():
    print('Starting graph.py')

if __name__=='__main__':
    main()