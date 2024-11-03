from locale import currency
from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk
import requests
import datetime




window = Tk()
window.title('Курс криптовалют')
window.geometry('400x300')
window.iconbitmap('coin.ico')

cryptocurrency = ['Bitcoin', 'Ethereum', 'Tether', 'BNB', 'Solana', 'USDC',
                  'XRP', 'Lido Staked Ether', 'Dogecoin', 'TRON']
currency = ['USD', 'EUR', 'RUB', 'JPY', 'GBP', 'CAD', 'CHF', 'CNY']

Label(text='Выберите базовую валюту').pack(pady=(10, 5))
combo_crypt = ttk.Combobox(values=cryptocurrency)
combo_crypt.pack(pady=(0,15))

Label(text='Выберите целевую валюту').pack(pady=(10, 5))
combo_currency = ttk.Combobox(values=currency)
combo_currency.pack(pady=(0,15))

btn_convert = Button(text='Получить курс обмена')
btn_convert.pack(pady=20)

label = Label(text='Test')
label.pack()


window.mainloop()