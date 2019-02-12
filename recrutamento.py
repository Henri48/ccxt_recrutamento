import ccxt
import urllib
import json
import sys


exchanges =  ccxt.exchanges
print(exchanges)
# verfificar os precos dos livros.
def book_price(exchanges):
    for exchan in exchanges:
        if exchan != "acx":
            exchange = getattr(ccxt, exchan)()
            exchange.load_markets()

            with open("{}.json".format(exchan), "w") as write_file:
                data = {}

                for i in exchange.symbols:
                    if exchange.has['fetchTicker']:
                        Price_Tickers = exchange.fetch_ticker(i)
                    else:
                        Price_Tickers = "This exchange don't have fetch_ticker method"
                    orderbook = exchange.fetch_order_book(i)

                    data[i] = [Price_Tickers, orderbook]
                    print(i)

                json.dump(data, write_file)

# Ordem de Execucao
def excution_order(order):
    with open("{}.json".format(order), "r") as write_file:
        data = json.loads(write_file)
        exchange = getattr(ccxt, data.get("exchange"))()
        exchange.load_markets()
        order = exchange.create_order(data.get("symbol"), data.get("type"), data.get("side"), data.get("amount"),
                                      data.get("prince"), data.get("params"))

# Cacncelamento de Ordem
def cancel_order(order):
    with open("{}.json".format(order), "r") as write_file:
        data = json.loads(write_file)
        exchange = getattr(ccxt, data.get("exchange"))()
        exchange.load_markets()
        id = data.get("id")
        if len(exchange.fetch_order(id) > 0):
            try:
                exchange.cacel_order(id, data.get("symbol"), data.get("params"))
            except OrderNotFound:
                sys.stderr.write("Error: Canceling an already-closed order or an already-canceled order")
            except NetworkError:
                sys.stderr.write("Warnig: the request may or may not have been successfully canceled")



# Ordens em aberto da https://3xbit.com.br/

# Identificando as MARKET/SYMBOL presentes em https://3xbit.com.br/
market = {}
response = urllib.urlopen("https://api.exchange.3xbit.com.br/ticker/")
data = json.loads(response.read())
for i in data:
    dict = data["{}".format(i)]
    aux = {"{}".format(dict["market"]): "{}".format(dict["symbol"])}

    if not (dict["market"] in market):
        market[dict["market"]] = []

    market[dict["market"]].append(dict["symbol"])

# Determinando as Ordens em aberto
orders = {}
for i in market:
    dict = market["{}".format(i)]
    for symbol in dict:
        response = urllib.urlopen("https://api.exchange.3xbit.com.br/v1/orderbook/{}/{}/".format(i,symbol))
        data = json.loads(response.read())
        information = { "symbol": symbol,
                        "buy_ordes": data["buy_orders"],
                        "sell_ordes": data["sell_orders"]}

        if not (i in orders):
            orders[i] = []

        orders[i].append(information)

with open("orders.json", "w") as write_file:
    json.dump(orders, write_file)
