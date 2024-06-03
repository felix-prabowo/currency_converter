import requests
from pprint import PrettyPrinter

beacon_api_key = '78P7yaKkAVCyHXVbrt0HIdK5NrF5F68c'
beacon_base_url = 'https://api.currencybeacon.com/v1/'

def get_currencies():
    endpoint = f'currencies?type=fiat&api_key={beacon_api_key}'
    url = beacon_base_url + endpoint
    data = requests.get(url).json()['response']

    return data
    

def print_currencies(currencies):
    for data in currencies:
        name = data['name']
        _id = data['short_code']
        symbol = data['symbol']
        number = currencies.index(data) + 1
        print(f'{number} - {_id} - {name} - {symbol}')
    print()
    

def exchange_rate(currency1, currency2, currencies):
    endpoint = f'convert?from={currency1}&to={currency2}&amount=1&api_key={beacon_api_key}'
    url = beacon_base_url + endpoint
    
    try:
        data = requests.get(url).json()['response']
        secondary_data = currencies
        currency1_name = [d['name'] for d in secondary_data if currency1 in d.values()][0]
        currency2_name = [d['name'] for d in secondary_data if currency2 in d.values()][0]
    except:
        print('Invalid currencies. Please enter the proper three-letter currency code')
        print()
    else:
        rate = round(data['value'], 2)
        print(f'1 {currency1_name} ({currency1}) is equal to {rate:,.2f} {currency2_name} ({currency2})')
        print()

        return rate

    
def convert(currency1, currency2, amount, currencies):
    endpoint = f'convert?from={currency1}&to={currency2}&amount={amount}&api_key={beacon_api_key}'
    url = beacon_base_url + endpoint

    try:
        data = requests.get(url).json()['response']
        secondary_data = currencies
        currency1_name = [d['name'] for d in secondary_data if currency1 in d.values()][0]
        currency2_name = [d['name'] for d in secondary_data if currency2 in d.values()][0]
    except:
        print('Invalid currencies or amount entered. Please enter the proper three-letter currency code and amount')
        print()
    else:
        converted_amount = data['value']
        print(f'{float(amount):,.2f} {currency1_name} ({currency1}) is equal to {converted_amount:,.2f} {currency2_name} ({currency2})')
        print()

        return converted_amount

# exchange_rate('SGD', 'IDR')

# print_currencies(currencies)
# convert('SGD', 'USD', 100.75)

def main():
    currencies = get_currencies()


    while True:
        print('Welcome to the currency converter!')
        print('List - lists the different currencies')
        print('Convert - convert from one currency to another')
        print('Rate - get the exchange rate of two currencies')
        print()
        command = input('Enter a command (q to quit): ').lower()

        if command == 'q':
            break
        elif command == 'list':
            print_currencies(currencies)
        elif command == 'convert':
            currency1 = input('Enter a base currency: ').upper()
            amount = input(f'Enter an amount in {currency1}: ')
            currency2 = input('Enter a currency to convert to: ').upper()
            convert(currency1, currency2, amount, currencies)
        elif command == 'rate':
            currency1 = input('Enter a base currency: ').upper()
            currency2 = input('Enter a currency to convert to: ').upper()
            exchange_rate(currency1, currency2, currencies)
        else:
            print('Unrecognized command!')
            print()

if __name__ == '__main__':
    main()    