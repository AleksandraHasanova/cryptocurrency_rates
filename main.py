from locale import currency
from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk
import requests
import datetime


cryptocurrency = {'Bitcoin': 'Биткоин', 'Ethereum': 'Эфириум', 'Litecoin': 'Лайткоин', 'Tether': 'Тезер',
                  'Solana': 'Солана', 'Dogecoin': 'Догекоин'}

traded_currency = {'USD': 'Доллар США', 'EUR': 'Евро', 'RUB': 'Российский рубль',
            'JPY': 'Японская иена', 'GBP': 'Британский фунт', 'CAD': 'Канадский доллар',
            'CHF': 'Швейцарский франк', 'CNY': 'Китайский юань'}

date = datetime.date.today().strftime('%d.%m.%Y')

def convert_currency():
    crypt = combo_crypt.get()
    currency = combo_currency.get()
    global date

    if crypt and currency:
        base = crypt.lower()
        target = currency.lower()
        try:
            response = requests.get(f"https://api.coingecko.com/api/v3/simple/price?ids={base}&vs_currencies={target}")
            response.raise_for_status()
            data_json = response.json()

            if data_json:
                result = data_json[base][target]
                label.config(text=f'Курс криптовалюты на {date}:\n 1 {cryptocurrency[crypt]} = {result} {traded_currency[currency]}')
            else:
                mb.showerror('Ошибка', 'Произошла ошибка: криптовалюта не найдена')

        except Exception as e:
            mb.showerror('Ошибка!', f'Произошла ошибка: {e}')


window = Tk()
window.title('Курс криптовалют')
window.geometry('400x300')
window.iconbitmap('coin.ico')

Label(text='Выберите базовую валюту').pack(pady=(10, 5))
combo_crypt = ttk.Combobox(values=list(cryptocurrency.keys()))
combo_crypt.pack(pady=(0,15))

Label(text='Выберите целевую валюту').pack(pady=(10, 5))
combo_currency = ttk.Combobox(values=list(traded_currency.keys()))
combo_currency.pack(pady=(0,15))

btn_convert = Button(text='Получить курс обмена', command=convert_currency)
btn_convert.pack(pady=20)

label = Label()
label.pack()

window.mainloop()