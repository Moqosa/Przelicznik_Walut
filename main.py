import requests
from bs4 import BeautifulSoup
import tkinter as tk

# Link do strony z kursami walut
url_euro = 'https://cinkciarz.pl/wymiana-walut/kursy-walut/eur/pln'
url_dolar = 'https://cinkciarz.pl/wymiana-walut/kursy-walut/usd/pln'
url_funt = 'https://cinkciarz.pl/wymiana-walut/kursy-walut/gbp/pln'

#Wysyłanie zapytania do strony
response_euro = requests.get(url_euro)
response_dolar = requests.get(url_dolar)
response_funt = requests.get(url_funt)

# Sprawdzanie statusu
if response_euro.status_code and response_dolar.status_code == 200:
    # Element do pobrania euro
    soup_euro = BeautifulSoup(response_euro.text, 'html.parser')

    elements_with_class_euro = soup_euro.find_all(class_='up')

    kurs_euro = []
    for euros in elements_with_class_euro:
        kurs_euro.append(euros.text)

    soup_dolar = BeautifulSoup(response_dolar.text, 'html.parser')

    # Element do pobrania dolar

    elements_with_class_dolar = soup_dolar.find_all(class_='up')

    kurs_dolara = []
    for dolars in elements_with_class_dolar:
        kurs_dolara.append(dolars.text)

    #Elementy do pobrania funt

    soup_funt = BeautifulSoup(response_funt.text, 'html.parser')
    elements_with_class_funt = soup_funt.find_all(class_='up')

    kurs_funt = []
    for funts in elements_with_class_funt:
        kurs_funt.append(funts.text)



# Instrukcja co w przypadku gdy będzie błąd serwera strony
else:
    print(f'Błąd pobierania strony. Kod statusu: {response.status_code}')

#Tworzenie GUI
root = tk.Tk()
root.geometry('500x500')
root.title("Kalkulator walut")


# Input

text_label = tk.Label(root, text="Enter the amount of PLN", font=('Arial', 20))
text_label.pack()

entry = tk.Entry(root)
entry.pack()

#Funkcja dla przeliczania euro

class exchange_rate:

    #Euro
    def euro_funkcja():
        try:
            exchange_rate_euro = float(kurs_euro[0].replace(',', '.'))
            entry_int_exchange = int(entry.get())
            result_euro = entry_int_exchange / exchange_rate_euro
            if result_euro >= 2:
                output.config(text=f"For {entry_int_exchange} PLN you can buy {result_euro} euros")
            else:
                output.config(text=f"For {entry_int_exchange} PLN you can buy {result_euro} euro")
        except ValueError:
            output.config(text='Error')

    button_euro = tk.Button(root, text="Euro", command=euro_funkcja, font=('Arial', 18), bg='green')
    button_euro.pack()

    #Dolar
    def dolar_funkcja():
        try:
            exchange_rate_dolar = float(kurs_dolara[0].replace(',', '.'))
            entry_int_exchange = int(entry.get())
            result_dolar = entry_int_exchange / exchange_rate_dolar
            if result_dolar >= 2:
                output.config(text=f"For {entry_int_exchange} PLN you can buy {result_dolar} dolars")
            else:
                output.config(text=f"For {entry_int_exchange} PLN you can buy {result_dolar} dolar")
        except ValueError:
            output.config("Error")
    button_dolar = tk.Button(root, text="Dollar", command=dolar_funkcja, font=('Arial, 18'), bg='green')
    button_dolar.pack()

    #Funt
    def funt_funkcja():
        try:
            exchange_rate_funt = float(kurs_funt[0].replace(',', '.'))
            entry_int_exchange = int(entry.get())
            result_funt = entry_int_exchange / exchange_rate_funt
            if result_funt >= 2:
                output.config(text=f"For {entry_int_exchange} PLN you can buy {result_funt} funts")
            else:
                output.config(text=f"For {entry_int_exchange} PLN you can buy {result_funt} funt")
        except ValueError:
            output.config("Error")

    button_funt = tk.Button(root, text='Funt', command=funt_funkcja, font=('Arial, 18'), bg='green')
    button_funt.pack()


output = tk.Label(root, font=('Arial, 12')) #output
output.pack()

root.mainloop()
