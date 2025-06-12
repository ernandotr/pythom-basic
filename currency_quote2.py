import requests

from tkinter import Tk, Label, Button
def get_currency_quote():
    """
    Fetches the current exchange rates for USD, EUR, GBP, and BTC to BRL from AwesomeAPI.
    
    :return: A formatted string with the exchange rates.
    """
    request = requests.get("https://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL,GBP-BRL,BTC-BRL")
    data = request.json()
    usd_brl = data['USDBRL']['bid']
    eur_brl = data['EURBRL']['bid']
    gbp_brl = data['GBPBRL']['bid']
    btc_brl = data['BTCBRL']['bid']
    
    text = f'''
    Dollar (USD) to Real (BRL): {usd_brl}
    Euro (EUR) to Real (BRL): {eur_brl}
    Pound (GBP) to Real (BRL): {gbp_brl}
    Bitcoin (BTC) to Real (BRL): {btc_brl}
    '''
    print(text)
    text_result["text"] = text


window = Tk()
window.title("Currency Exchange Rates")
label = Label(window, text="Click the button to get the latest currency exchange rates", fg="white")
label.grid(row=0, column=0)

button = Button(window, text="Get last currency rates", command=get_currency_quote)
button.grid(row=1, column=0, padx=10, pady=10)

text_result = Label(window, text="", fg="white", bg="black", justify="left")
text_result.grid(row=2, column=0)


window.mainloop()
# This code fetches the exchange rates for USD to BRL and EUR to BRL from the AwesomeAPI.