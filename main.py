from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk
import requests
import datetime
from PIL import Image, ImageTk
from io import BytesIO


cryptocurrency = {'Bitcoin': 'Биткоин', 'Ethereum': 'Эфириум', 'Litecoin': 'Лайткоин', 'Tether': 'Тезер',
                  'Solana': 'Солана', 'Dogecoin': 'Догекоин'}

traded_currency = {'USD': 'Доллар США', 'EUR': 'Евро', 'RUB': 'Российский рубль',
            'JPY': 'Японская иена', 'GBP': 'Британский фунт', 'CAD': 'Канадский доллар',
            'CHF': 'Швейцарский франк', 'CNY': 'Китайский юань'}

date = datetime.date.today().strftime('%d.%m.%Y')
crypt = ''
currency = ''

def convert_currency():
    global crypt, currency
    global date
    crypt = combo_crypt.get()
    currency = combo_currency.get()

    if crypt and currency:
        base = crypt.lower()
        target = currency.lower()
        try:
            response = requests.get(f"https://api.coingecko.com/api/v3/simple/price?ids={base}&vs_currencies={target}")
            response.raise_for_status()
            data_json = response.json()

            if data_json:
                result = data_json[base][target]
                return result

            else:
                mb.showerror('Ошибка!', f'Валюта {crypt} или {currency} не найдена')
                return None

        except Exception as e:
            mb.showerror('Ошибка!', f'Произошла ошибка: {e}')
    else:
        mb.showwarning('Пустые поля!', 'Выберите базовую и целевую валюту из предложенного списка')


def load_icon():
    label_icon.config(image='')
    if crypt and currency:
        try:
            response = requests.get(f"https://api.coingecko.com/api/v3/coins/{crypt.lower()}")
            response.raise_for_status()
            data_json = response.json()
            icon_url = data_json['image']['small']
            try:
                response = requests.get(icon_url)
                response.raise_for_status()
                image_data = BytesIO(response.content)
                img = Image.open(image_data)
                img = ImageTk.PhotoImage(img)
                if img:
                    return img
                else:
                    return None
            except Exception as e:
                mb.showerror('Ошибка!', f'Ошибка загрузки иконки: {e}')
        except Exception as e:
            mb.showerror('Ошибка!', f'Ошибка: {e}')



def output_result():
    result = convert_currency()
    if result:
        label_result.config(text=f'Курс криптовалюты на {date}:\n 1 {cryptocurrency[crypt]} = {result} {traded_currency[currency]}')
    img = load_icon()
    if img:
        label_icon.config(image=img)
        label_icon.image = img


window = Tk()
window.title('Курс криптовалют')
window.geometry('400x400')
window.iconbitmap('coin.ico')

Label(text='Выберите базовую криптовалюту').pack(pady=(10, 5))
combo_crypt = ttk.Combobox(values=list(cryptocurrency.keys()))
combo_crypt.pack(pady=(0,15))

Label(text='Выберите целевую валюту').pack(pady=(10, 5))
combo_currency = ttk.Combobox(values=list(traded_currency.keys()))
combo_currency.pack(pady=(0,15))

btn_convert = Button(text='Получить курс обмена', command=output_result)
btn_convert.pack(pady=20)

label_icon = Label()
label_icon.pack(pady=10)

label_result = Label()
label_result.pack(pady=10)

window.mainloop()