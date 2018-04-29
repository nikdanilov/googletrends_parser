import requests
from bs4 import BeautifulSoup as bs
from pytrends.request import TrendReq


class GoogleTrends():

    def __init__(self, query):
        self.query = query
        self.data = []
        self.process()

    def sum(self):
        sm = 0
        for item in self.data:
            sm += item[1]

        return sm

    def getData(self):
        return self.data

    def process(self):
        pytrend = TrendReq()
        pytrend.build_payload(kw_list=self.query, timeframe='2018-01-01 2018-4-29', geo='US', gprop='')
        res = pytrend.interest_over_time()
        print(res)
        # i = 0

        # for date in res.to_dict()[self.query]:

        #     j = 0
        #     for dg in res[self.query]:
        #         if j == i:
        #             self.data.append([str(date), dg])
        #         j += 1

        #     i += 1

ggd = GoogleTrends(['Bitcoin', 'Ethereum', 'Ripple', 'Neo', 'Tron'])
# print(ggd.getData())

'''
import sys
sys.exit()

for dd in data.split('\n'):
    sum = 0
    name, link = dd.split(',')

    pytrend = TrendReq()
    pytrend.build_payload(kw_list=[name])

    interest_over_time_df = pytrend.interest_over_time()

    try:
        for a in interest_over_time_df[name]:
            sum += a

        print(sum, name)

    except:
        print("Error ({})".format(name))

'''