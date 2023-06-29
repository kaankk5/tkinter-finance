import numpy as np
import talib
from talib import abstract
from talib.test_data import ford_2012

# close_prices = 10*[12.12,23.2,43.1,3.1,1.0,2.2]
# close_prices = np.array(close_prices)
#
#
#



given1 = 'STOCHRSI'
given2 = 'MACD'
given3 = 'ADX'

dict1= {'STOCHRSI': {'timeperiod': '11', 'fastk_period': '22', 'fastd_period': '33', 'fastd_matype': '44'}, 'ADX': {'timeperiod': '14141'}}

# for value,keys in dict1.items():
#     if hasattr(talib,value):
#         method1_funct = getattr(talib,value)
#         args = method1_funct()


indicator = abstract.Function(given1)
print(indicator.output_names)

#
# indicator2 = abstract.Function((given2))
# input2 = (dict(indicator2.input_names))
#
# values = list(input2.values())
# print(values)



# print(input2)







# print(params)
# inputs = dict(indicator.input_names)

my_array = np.array([12.12,13.13,14.14,12.12,13.13,14.14,12.12,13.13,14.14,12.12,13.13,14.14,12.12,13.13,14.14]*10)
#
# if hasattr(talib, given1):
#     method1_func = getattr(talib, given1)
#     args = method1_func(my_array,**params)

# print(args)




