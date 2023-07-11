import asyncio
import tkinter as tk
from tkinter import ttk, Menu
import threading
import os
from indicator_manager import IndicatorManager
import talib
from config import *
from data_acquisition import DataAcquisition
import customtkinter as ctk
from stream_data import StreamData
import re

class GUI:
    all_indicators = talib.get_function_groups()

    def __init__(self, root):
        self.root = root
        self.root.title("Dranzer")
        ctk.set_appearance_mode('dark')
        ctk.set_default_color_theme('dark-blue')


        # Objects
        self.data_acquisition = DataAcquisition()
        self.stream = StreamData(self.data_acquisition.public_key, self.data_acquisition.private_key)
        self.indicator_manager = IndicatorManager()



    # Setup
    def historical_setup_multiple_symbol(self):
        self.clearFrame()
        self.historical_menu_frame()
        self.historical_data_frame()
        self.historical_interval_frame()
        self.historical_days_frame()

    def go_back_dashboard(self):
        self.clearFrame()
        self.navigate_to_dashboard()

    def validate(self):
        username = self.username_entry.get()
        password = self.password_entry.get()


        if username == "" and password == "":
            self.clearFrame()
            self.navigate_to_dashboard()
        else:
            print("Invalid credentials")



    def login(self):

        self.frame = ctk.CTkFrame(master=self.root)
        self.frame.pack(pady=20, padx=60, fill='both', expand=True)
        self.label = ctk.CTkLabel(master=self.frame, text='Login system')
        self.label.pack(pady=12, padx=10)

        self.username_entry = ctk.CTkEntry(master=self.frame, placeholder_text='Username')
        self.username_entry.pack(pady=12, padx=10)
        self.password_entry = ctk.CTkEntry(master=self.frame, placeholder_text='Password', show='*')
        self.password_entry.pack(pady=12, padx=10)

        self.button = ctk.CTkButton(master=self.frame, text='login', command=self.validate)
        self.button.pack(pady=12, padx=10)

        self.bottom_frame = ctk.CTkFrame(master=self.frame)
        self.bottom_frame.pack(pady=60, padx=20, fill='both', expand=True)

        self.symbol1 = ctk.CTkLabel(master=self.bottom_frame, text='BTCUSDT')
        self.symbol1.grid(row=0, column=0, padx=60, pady=40)

        self.symbol2 = ctk.CTkLabel(master=self.bottom_frame, text='ETHUSDT')
        self.symbol2.grid(row=0, column=1, padx=60, pady=40)

        self.symbol3 = ctk.CTkLabel(master=self.bottom_frame, text='LINKUSDT')
        self.symbol3.grid(row=0, column=2, padx=60, pady=40)

        self.symbol4 = ctk.CTkLabel(master=self.bottom_frame, text='AVAXUSDT')
        self.symbol4.grid(row=0, column=3, padx=60, pady=40)

        self.price1 = ctk.CTkLabel(master=self.bottom_frame, text='123.45')
        self.price1.grid(row=1, column=0, padx=60, pady=40)

        self.price2 = ctk.CTkLabel(master=self.bottom_frame, text='678.90')
        self.price2.grid(row=1, column=1, padx=60, pady=40)

        self.price3 = ctk.CTkLabel(master=self.bottom_frame, text='543.21')
        self.price3.grid(row=1, column=2, padx=60, pady=40)

        self.price4 = ctk.CTkLabel(master=self.bottom_frame, text='987.65')
        self.price4.grid(row=1, column=3, padx=60, pady=40)

    # Historical - Frames
    def clearFrame(self):
        # destroy all widgets from frame
        # self.frame.pack_forget()
        for widget in self.frame.winfo_children():
            widget.destroy()

        self.frame.pack_forget()

    def historical_interval_frame(self):
        self.interval_frame = ctk.CTkFrame(master=self.data_frame, width=175, height=100)
        self.interval_frame.pack(padx=70, pady=(20, 5), fill='both')

        self.interval_label = ctk.CTkLabel(self.interval_frame, text='Chose Interval', font=ctk.CTkFont(weight='bold'))
        self.interval_label.grid(row=0, column=0, padx=10, pady=10)

        self.interval_value = ctk.StringVar(value='1m')

        self.radiobutton1 = ctk.CTkRadioButton(self.interval_frame, text='1m', variable=self.interval_value, value='1m')
        self.radiobutton1.grid(row=1, column=0, padx=(10, 10), pady=10)

        self.radiobutton2 = ctk.CTkRadioButton(self.interval_frame, text='5m', variable=self.interval_value, value='5m')
        self.radiobutton2.grid(row=1, column=1, padx=(10, 10), pady=10)

        self.radiobutton3 = ctk.CTkRadioButton(self.interval_frame, text='15m', variable=self.interval_value,
                                               value='15m')
        self.radiobutton3.grid(row=1, column=2, padx=(10, 10), pady=10)

        self.radiobutton4 = ctk.CTkRadioButton(self.interval_frame, text='30m', variable=self.interval_value,
                                               value='30m')
        self.radiobutton4.grid(row=1, column=3, padx=(10, 10), pady=10)

        self.radiobutton5 = ctk.CTkRadioButton(self.interval_frame, text='1h', variable=self.interval_value, value='1h')
        self.radiobutton5.grid(row=2, column=0, padx=(10, 10), pady=10)

        self.radiobutton6 = ctk.CTkRadioButton(self.interval_frame, text='4h', variable=self.interval_value, value='4h')
        self.radiobutton6.grid(row=2, column=1, padx=(10, 10), pady=10)

        self.radiobutton7 = ctk.CTkRadioButton(self.interval_frame, text='1d', variable=self.interval_value, value='1d')
        self.radiobutton7.grid(row=2, column=2, padx=(10, 10), pady=10)

        self.radiobutton8 = ctk.CTkRadioButton(self.interval_frame, text='1w', variable=self.interval_value, value='1w')
        self.radiobutton8.grid(row=2, column=3, padx=(10, 10), pady=10)

    def historical_menu_frame(self):
        self.frame = ctk.CTkFrame(master=self.root)
        self.frame.pack(fill='both', expand=True)

        self.menu_frame = ctk.CTkFrame(master=self.frame)
        self.menu_frame.pack(side='left', fill='both')

        self.button = ctk.CTkButton(master=self.menu_frame, text='Go back', command=self.go_back_dashboard)
        self.button.pack(padx=10, pady=12)

        self.button2 = ctk.CTkButton(master=self.menu_frame, text='Go For 1', command=self.historical_data1)
        self.button2.pack(padx=10, pady=12)

        self.button3 = ctk.CTkButton(master=self.menu_frame, text='All Pair', command=self.historical_all_pairs)
        self.button3.pack(padx=10, pady=12)

        self.button4 = ctk.CTkButton(master=self.menu_frame, text='Only Usdt Pairs', command=self.historical_only_usdt)
        self.button4.pack(padx=10, pady=12)

        self.button5 = ctk.CTkButton(master=self.menu_frame, text='Margin Usdt Pairs',
                                     command=self.historical_margin_usdt)
        self.button5.pack(padx=10, pady=12)

    def historical_data_frame(self):
        self.data_frame = ctk.CTkFrame(master=self.frame, width=700, height=700)
        self.data_frame.pack(pady=40, padx=40)
        self.data_frame.pack_propagate(False)

    def historical_days_frame(self):
        self.days_frame = ctk.CTkFrame(master=self.data_frame, width=175, height=130)
        self.days_frame.pack(padx=70, pady=(20, 5), fill='both')
        self.days_frame.pack_propagate(False)

        self.days_label = ctk.CTkLabel(self.days_frame, text='Days', font=ctk.CTkFont(weight='bold'))
        self.days_label.pack()
        days_default = tk.StringVar()
        days_default.set("2")
        self.days_entry = ctk.CTkEntry(master=self.days_frame, placeholder_text='Number of Days',
                                       textvariable=days_default)
        self.days_entry.pack(pady=12, padx=10)

    def historical_symbol_frame(self):
        self.symbol_frame = ctk.CTkFrame(master=self.data_frame, width=175, height=100)
        self.symbol_frame.pack(padx=70, pady=(20, 5), fill='both')

        self.symbol_label = ctk.CTkLabel(self.symbol_frame, text='Enter Symbol Name', font=ctk.CTkFont(weight='bold'))
        self.symbol_label.pack()
        self.symbol_frame.pack_propagate(False)

        symbol_default = tk.StringVar()
        symbol_default.set("BTCUSDT")
        self.symbol_entry = ctk.CTkEntry(master=self.symbol_frame, placeholder_text='BTCUSDT',
                                         textvariable=symbol_default)
        self.symbol_entry.pack(pady=12, padx=10)

    # Indicator Frames

    def setup_indicator(self):
        self.clearFrame()
        self.indicator_menu_frame()
        self.historical_data_frame()
        self.chose_symbol_frame()
        self.chose_indicator_number_frame()

        self.submit_button = ctk.CTkButton(self.data_frame, text='Select', command=self.get_indicator_values_wrapper)
        self.submit_button.pack(padx=70, pady=20, fill='x')


    def get_about(self):
        with open(about_indicator_path, 'r') as file:
            text = file.read()
        return text

    def scrollbar_frame(self):

        self.deneme = ctk.CTkTextbox(self.frame, width=540,height=500)
        self.deneme.pack(pady=30, padx=20)
        text = self.get_about()
        self.deneme.insert("0.0",text)



    def about_indicators(self):
        self.clearFrame()
        self.indicator_menu_frame()
        self.scrollbar_frame()



    def indicator_cyle(self):
        # self.indicator_group = self.button4.cget("text")
        self.indicator_group = 'Cycle Indicators'
        self.setup_indicator()


    def indicator_math(self):
        self.indicator_group = self.button5.cget("text")
        self.setup_indicator()

    def indicator_math_transform(self):
        self.indicator_group = self.button6.cget("text")
        self.setup_indicator()
    def indicator_momentum(self):
        self.indicator_group = self.button7.cget("text")
        self.setup_indicator()

    def indicator_overlap(self):
        self.indicator_group = self.button8.cget("text")
        self.setup_indicator()

    def indicator_pattern_recog(self):
        self.indicator_group = self.button9.cget("text")
        self.setup_indicator()


    def  indicator_price_transform(self):
        self.indicator_group = self.button10.cget("text")
        self.setup_indicator()

    def indicator_volatility(self):
        self.indicator_group = self.button11.cget("text")
        self.setup_indicator()

    def indicator_volume(self):
        self.indicator_group = self.button12.cget("text")
        self.setup_indicator()

    def indicator_menu_frame(self):
        self.frame = ctk.CTkFrame(master=self.root)
        self.frame.pack(fill='both', expand=True)


        self.menu_frame = ctk.CTkFrame(master=self.frame)
        self.menu_frame.pack(side='left', fill='both')

        self.button = ctk.CTkButton(master=self.menu_frame, text='Go back', command=self.go_back_dashboard)
        self.button.pack(padx=10, pady=12)

        self.button3 = ctk.CTkButton(master=self.menu_frame, text='About Indicators', command=self.about_indicators)
        self.button3.pack(padx=10, pady=12)

        self.button4 = ctk.CTkButton(master=self.menu_frame, text='Cycle Indicators', command=self.indicator_cyle)
        self.button4.pack(padx=10, pady=12)

        self.button5 = ctk.CTkButton(master=self.menu_frame, text='Math Operators', command=self.indicator_math)
        self.button5.pack(padx=10, pady=12)

        self.button6 = ctk.CTkButton(master=self.menu_frame, text='Math Transform', command=self.indicator_math_transform)
        self.button6.pack(padx=10, pady=12)

        self.button7 = ctk.CTkButton(master=self.menu_frame, text='Momentum Indicators', command=self.indicator_momentum)
        self.button7.pack(padx=10, pady=12)

        self.button8 = ctk.CTkButton(master=self.menu_frame, text='Overlap Studies', command=self.indicator_overlap)
        self.button8.pack(padx=10, pady=12)

        self.button9 = ctk.CTkButton(master=self.menu_frame, text='Pattern Recognition', command=self.indicator_pattern_recog)
        self.button9.pack(padx=10, pady=12)

        self.button10 = ctk.CTkButton(master=self.menu_frame, text='Price Transform', command=self.indicator_price_transform)
        self.button10.pack(padx=10, pady=12)

        self.button11 = ctk.CTkButton(master=self.menu_frame, text='Volatility Indicators',
                                      command=self.indicator_volatility)
        self.button11.pack(padx=10, pady=12)

        self.button12 = ctk.CTkButton(master=self.menu_frame, text='Volume Indicators', command=self.indicator_volume)
        self.button12.pack(padx=10, pady=12)

    def chose_symbol_frame(self):
        self.indicator_frame = ctk.CTkFrame(master=self.data_frame, width=175, height=150)
        self.indicator_frame.pack(padx=70, pady=(20, 5), fill='both')
        self.indicator_frame.pack_propagate(False)

        self.chose_indicator_label = ctk.CTkLabel(self.indicator_frame, text='Chose File For Indicator',
                                                  font=ctk.CTkFont(weight='bold'))
        self.chose_indicator_label.pack(padx=12, pady=12)
        files = os.listdir('historical_data')

        self.file_combobox = ctk.CTkComboBox(self.indicator_frame, values=files)
        self.file_combobox.set(files[0])  # Set default value
        self.file_combobox.pack()

    def chose_indicator_number_frame(self):
        self.indicator_frame = ctk.CTkFrame(master=self.data_frame, width=175, height=150)
        self.indicator_frame.pack(padx=70, pady=(20, 5), fill='both')
        self.indicator_frame.pack_propagate(False)

        self.chose_indicator_label = ctk.CTkLabel(self.indicator_frame, text='Number of Indicators',
                                                  font=ctk.CTkFont(weight='bold'))
        self.chose_indicator_label.pack(padx=12, pady=12)

        values = list(str(i) for i in range(1, 7))


        self.value_combobox = ctk.CTkComboBox(self.indicator_frame, values=values)
        self.value_combobox.set(values[0])  # Set default value


        self.value_combobox.pack()
        # # self.value_combobox.config(width=20, height=30)

    # Backtest- Frames
    def backtest_menu_frame(self):
        self.frame = ctk.CTkFrame(master=self.root)
        self.frame.pack(fill='both', expand=True)

        self.menu_frame = ctk.CTkFrame(master=self.frame)
        self.menu_frame.pack(side='left', fill='both')

        self.button = ctk.CTkButton(master=self.menu_frame, text='Go back', command=self.go_back_dashboard)
        self.button.pack(padx=10, pady=12)

        self.button1 = ctk.CTkButton(master=self.menu_frame, text='Chose File', command=self.go_back_dashboard)
        self.button1.pack(padx=10, pady=12)

        self.button2 = ctk.CTkButton(master=self.menu_frame, text='All the Market', command=self.go_back_dashboard)
        self.button2.pack(padx=10, pady=12)

    # Wrapper
    def get_symbol_interval_wrapper(self):
        symbol_name = str(self.symbol_entry.get())
        interval = str(self.interval_value.get())
        days = int(self.days_entry.get())
        self.data_acquisition.get_symbol_interval(symbol_name, interval, days)

    def get_all_wrapper(self):
        interval = str(self.interval_value.get())  # Ensure interval is a string
        days = int(self.days_entry.get())
        self.data_acquisition.get_all_symbols(interval, days)

    def get_indicator_values_wrapper(self):
        self.file_name = self.file_combobox.get()
        self.num_indicators = int(self.value_combobox.get())

        self.indicator_data2()

    # Historical
    def historical_data1(self):
        self.clearFrame()
        self.historical_menu_frame()
        self.historical_data_frame()
        self.historical_symbol_frame()
        self.historical_interval_frame()
        self.historical_days_frame()
        self.submit_button = ctk.CTkButton(self.data_frame, text='Download Candlestick',
                                           command=lambda: threading.Thread(
                                               target=self.get_symbol_interval_wrapper).start())

        self.submit_button.pack(padx=70, pady=20, fill='x')

    def historical_all_pairs(self):
        self.historical_setup_multiple_symbol()
        self.submit_button = ctk.CTkButton(self.data_frame, text='Download Candlestick',
                                           command=lambda: threading.Thread(target=self.get_all_wrapper).start())

        self.submit_button.pack(padx=70, pady=20, fill='x')

    def historical_only_usdt(self):
        self.historical_setup_multiple_symbol()
        self.submit_button = ctk.CTkButton(self.data_frame, text='Download Candlestick',
                                           command=self.get_symbol_interval_wrapper)

        self.submit_button.pack(padx=70, pady=20, fill='x')

    def historical_margin_usdt(self):
        self.historical_setup_multiple_symbol()
        self.submit_button = ctk.CTkButton(self.data_frame, text='Download Candlestick',
                                           command=self.get_symbol_interval_wrapper)

        self.submit_button.pack(padx=70, pady=20, fill='x')


    def get_indicator_names_wrapper(self):
        self.indicators = {}
        for i in self.comboboxes:
            indicator = i.get()
            self.indicators[indicator] = self.indicator_manager.get_params(indicator)

        self.display_params_frame()


    def display_params_frame(self):
        self.clearFrame()
        self.indicator_menu_frame()
        self.historical_data_frame()
        self.display_each_param()

    def display_each_param(self):

        self.current_indicator_index = 0
        self.display_params_for_indicator()

    def display_params_for_indicator(self):
        self.indicator_key = list(self.indicators.keys())[self.current_indicator_index]
        params = self.indicators[self.indicator_key]

        indicator_label = ctk.CTkLabel(self.data_frame, text=self.indicator_key, font=ctk.CTkFont(weight='bold'))
        indicator_label.pack()

        values_frame = ctk.CTkFrame(self.data_frame, width=120, height=200)
        values_frame.pack(padx=70, pady=(20, 5), fill='both')
        values_frame.pack_propagate(False)

        self.temp_value=[]
        self.temp_params=[]
        row = 1
        for param, value in params.items():
            self.temp_params.append(param)
            param_label = ctk.CTkLabel(values_frame, text=param, anchor='w', font=ctk.CTkFont(weight='bold'))
            param_label.grid(row=row, column=0, padx=30)


            value_entry = ctk.CTkEntry(values_frame)
            value_entry.insert(0, value)  # Set the default value
            value_entry.grid(row=row, column=1, padx=30, pady=10)
            self.temp_value.append(value_entry)

            row += 1

        # Add a "Next" button for navigating to the next indicator
        next_button = ctk.CTkButton(self.data_frame, text="Next", command=self.next_indicator, width=440)
        next_button.pack(padx=70, pady=20, fill='x')

    def update_values(self):
        updated_values = {param: int(value.get()) for param, value in zip(self.temp_params, self.temp_value)}
        self.indicators[self.indicator_key] = updated_values


    def next_indicator(self):
        self.update_values()
        self.current_indicator_index += 1

        for widget in self.data_frame.winfo_children():
            widget.destroy()

        # Check if there are more indicators to display
        if self.current_indicator_index < len(self.indicators):
            self.display_params_for_indicator()

        else:
            self.review()


    def review(self):
        self.clearFrame()
        self.indicator_menu_frame()
        self.historical_data_frame()
        self.apply()



    def apply(self):

        df = self.data_acquisition.read_coin(self.file_name)
        self.indicator_manager.add_indicators(df,self.indicators,self.file_name)




    def select_n_indicator_frame(self):
        self.label = ctk.CTkLabel(master=self.data_frame, text='Select Indicators', font=ctk.CTkFont(weight='bold'))
        self.label.pack(padx=12, pady=(30, 10))
        self.indicator_frame = ctk.CTkScrollableFrame(master=self.data_frame, width=175, height=125)
        self.indicator_frame.pack(padx=70, pady=(20, 20), fill='both', expand=True)
        self.indicator_frame.pack_propagate(False)

        self.create_n_indicators_dropdown()
        self.submit_button = ctk.CTkButton(self.data_frame, text='Select', command=self.get_indicator_names_wrapper)
        self.submit_button.pack(padx=70, pady=20, fill='x')

    def create_n_indicators_dropdown(self):
        self.comboboxes = []  # List to store comboboxes
        group = self.all_indicators[self.indicator_group]



        for i in range(self.num_indicators):
            label = ctk.CTkLabel(master=self.indicator_frame, text=f'{i + 1}.', font=ctk.CTkFont(weight='bold'))
            label.grid(row=i, column=0, padx=12, pady=(30, 30))


            combobox = ctk.CTkComboBox(self.indicator_frame, values=group)

            combobox.set(group[0])  # Set default value
            combobox.grid(row=i, column=1, padx=20, pady=40)

            # Add the combobox to the list
            self.comboboxes.append(combobox)

    # Indicator



    def indicator_data2(self):
        self.clearFrame()
        self.indicator_menu_frame()
        self.historical_data_frame()
        self.select_n_indicator_frame()

    def check_regex(self,files):
        pattern=r'^(.*?)_\d+[a-z]*_\d+._'
        filtered_files = [filename for filename in files if re.search(pattern, filename)]
        return filtered_files



    def chose_strat_frame(self):

        self.indicator_frame = ctk.CTkFrame(master=self.data_frame, width=175, height=150)
        self.indicator_frame.pack(padx=70, pady=(20, 5), fill='both')
        self.indicator_frame.pack_propagate(False)

        self.chose_indicator_label = ctk.CTkLabel(self.indicator_frame, text='Chose File For Strat',
                                                      font=ctk.CTkFont(weight='bold'))
        self.chose_indicator_label.pack(padx=12, pady=12)
        files = os.listdir('historical_data')
        files = self.check_regex(files)


        self.file_combobox = ctk.CTkComboBox(self.indicator_frame, values=files)
        self.file_combobox.set(files[0])  # Set default value
        self.file_combobox.pack()

    # Backtest
    def backtest(self):
        self.clearFrame()
        self.backtest_menu_frame()
        self.historical_data_frame()
        self.chose_strat_frame()



    def get_strat(self):
        self.file_name = self.file_combobox.get()
        self.strat_page_2()


    def strat_save_params(self):
        name = self.strategy_name_entry.get()
        capital = self.capital_entry.get()
        leverage = self.leverage_entry.get()
        stop_loss = self.stop_loss_entry.get()






    def strat_page_2(self):
        self.clearFrame()
        self.backtest_menu_frame()
        self.historical_data_frame()
        self.strat_values_frame()
        self.submit_button = ctk.CTkButton(self.data_frame, text='Select', command=self.strat_save_params)
        self.submit_button.pack(padx=40, fill='x')

    def strat_values_frame(self):

        self.form_frame = ctk.CTkFrame(master=self.data_frame, width=700, height=700)
        self.form_frame.pack(pady=30, padx=40, fill='x')
        self.form_frame.pack_propagate(False)

        self.strat_name_label = ctk.CTkLabel(self.form_frame, text='Strategy Name', font=ctk.CTkFont(weight='bold'))

        self.strat_name_label.grid(row=0, column=0, padx=10, pady=(20,10))
        self.strategy_name_entry = ctk.CTkEntry(self.form_frame)
        self.strategy_name_entry.grid(row=0, column=1, padx=10, pady=(20,10))

        label = ctk.CTkLabel(self.form_frame, text='.py file name')
        label.grid(row=0, column=2, padx=10, pady=(20, 10))

        self.capital_label = ctk.CTkLabel(self.form_frame, text='Initial Capital',  anchor='w', font=ctk.CTkFont(weight='bold'))
        self.capital_label.grid(row=1, column=0, padx=10, pady=10)
        self.capital_entry = ctk.CTkEntry(self.form_frame)
        self.capital_entry.grid(row=1, column=1, padx=10, pady=10)

        label1 = ctk.CTkLabel(self.form_frame, text='Only integer')
        label1.grid(row=1, column=2, padx=10, pady=(20, 10))

        self.leverage = ctk.CTkLabel(self.form_frame, text='Leverage',font=ctk.CTkFont(weight='bold'))
        self.leverage.grid(row=2, column=0, padx=10, pady=10)
        self.leverage_entry = ctk.CTkEntry(self.form_frame)
        self.leverage_entry.grid(row=2, column=1, padx=10, pady=10)



        label2 = ctk.CTkLabel(self.form_frame, text='Only integer')
        label2.grid(row=2, column=2, padx=10, pady=(20, 10))

        self.stop_loss_label = ctk.CTkLabel(self.form_frame, text='Stop Loss',font=ctk.CTkFont(weight='bold'))
        self.stop_loss_label.grid(row=3, column=0, padx=10,pady=(10,20))
        self.stop_loss_entry = ctk.CTkEntry(self.form_frame)
        self.stop_loss_entry.grid(row=3, column=1, padx=10,pady=(10,20))

        label3 = ctk.CTkLabel(self.form_frame, text='Only integer')

        label3.grid(row=3,column=2, padx=10, pady=(20, 10))

    def create_strat(self):
        self.clearFrame()
        self.backtest_menu_frame()
        self.historical_data_frame()
        self.chose_strat_frame()
        self.submit_button = ctk.CTkButton(self.data_frame, text='Select', command=self.get_strat)
        self.submit_button.pack(padx=70, pady=20, fill='x')




    def navigate_to_dashboard(self):

        self.frame = ctk.CTkFrame(master=self.root)
        self.frame.pack(side='left', padx=10, fill='both', )

        # Create and add widgets to the dashboard_left_frame for the menu

        # Example: Create a button
        self.button = ctk.CTkButton(master=self.frame, text="Historical Data", command=self.historical_data1)
        self.button.pack(pady=10, padx=12)





        self.button1 = ctk.CTkButton(master=self.frame, text="Add Indicator", command=self.indicator_cyle)
        self.button1.pack(pady=10, padx=12)

        self.button2 = ctk.CTkButton(master=self.frame, text="Create Strat", command=self.create_strat)
        self.button2.pack(pady=10, padx=12)

        self.button3 = ctk.CTkButton(master=self.frame, text="Backtest", command=self.backtest)
        self.button3.pack(pady=10, padx=12)

        self.button4 = ctk.CTkButton(master=self.frame, text="Publish Script")
        self.button4.pack(pady=10, padx=12)

        self.button5 = ctk.CTkButton(master=self.frame, text="Live price")
        self.button5.pack(pady=10, padx=12)

    def run(self):
        self.root.geometry("1000x700")  # Adjust the width and height here
        self.login()  # Call the login method
        self.root.mainloop()
