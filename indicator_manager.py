import pandas as pd
import talib
import os
from talib import abstract
from config import historical_data_path

class IndicatorManager():

    def get_params(self,indicator):
        func =(abstract.Function(indicator))
        params = dict(func.parameters)
        return params

    def add_indicators(self,df,indicators:dict,filename):
        self.df = df

        self.filename = filename

        for name,param in indicators.items():
            self.create_indicator(name,param)


        self.save_to_csv()


    def save_to_csv(self):

        output_path = os.path.join(f'historical_data/{self.filename}')
        self.df.to_csv(output_path)









    def create_indicator(self,name,param):
        if hasattr(talib,name):
            self.method = getattr(talib,name)
            indicator_inputs = self.check_input(name)
            args = self.method(*indicator_inputs,**param)
            self.save_indicators(args,name)


    def save_indicators(self,args,name):
        indicator = abstract.Function(name)
        name =  indicator.info['name']
        self.filename = self.filename[:-4] + f"_{name}" + self.filename[-4:]
        columns = indicator.output_names
        args_list = list(args)

        for column,values in zip(columns,args_list):
            self.df[column] = values



    # def read_coin(self):
    #     file_path = os.path.join(f"historical_data/{self.filename}")
    #     data = pd.read_csv(file_path, parse_dates=['timestamp'])
    #     data.set_index('timestamp', inplace=True)
    #     return data

        # print(args)
    def check_input(self,name):
        indicator = abstract.Function(name)
        inputs = (dict(indicator.input_names))

        if 'price' in inputs:
            headers = list(inputs.values())
        elif 'prices' in inputs:
            headers = list(inputs.values())[0]

        indicator_inputs =[self.df[i] for i in headers]
        return indicator_inputs










