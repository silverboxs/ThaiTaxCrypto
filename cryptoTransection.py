import json
from textwrap import indent
import pandas as pd
import datetime
class taxCryptoEasy:
    def __init__(self,filename):
        self.f = open(filename,'r+')
        self.data_action = json.load(self.f)
        self.ntime = datetime.datetime.now()

    def write_recorde(self,strAction,data_recorde):
        self.data_action['Bitcoin'][strAction].update(data_recorde)
        self.f.seek(0)
        json.dump(self.data_action,self.f,indent=4)

    def time_to_string(self):
        txt_time = "{}-{}-{}".format(self.ntime.year,self.ntime.month,self.ntime.day)
        return txt_time

a = taxCryptoEasy("crypto_transection_records.json")
test_txt = {a.time_to_string():{"amount":0.05,"price":40150}}
text_txt_sell = {a.time_to_string():{"amount":0.005,"price":43150}}

a.write_recorde('SELL',text_txt_sell)
'''
with open("crypto_transection_records.json",'r+') as file:
    file_data = json.load(file)
    file_data['Bitcoin']['BUY'].update(test_txt)
    file.seek(0)
    json.dump(file_data,file,indent=4)
'''