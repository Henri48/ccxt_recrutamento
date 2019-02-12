# ccxt_recrutamento

A função book_price() cria um market.json para cada mercado com o Price Tickers e o OrderBook de cada Symbol que o mesmo possui. O json é estruturado conforme a seguir:

```bash
{Symbol_1: [Price Tickers, OrderBook], 
 Symbol_2: [Price Tickers, OrderBook], 
 ...}
 ```
 
A Execucao de ordem assumi que o pedido de ordem venha de um arquivo .json de estrutura:
```bash
{ "exchange": ' ',
  "symbol": ' ',
  "type": ' ',
  "side": ' ',
  "amount": float,
  "price": float,
  
  #overrides
  "params": {
              'stopPrice': float
              'type': float
   },
}
```

O Cancelamento de ordem assumi que o pedido de cancelamento de ordem venha de um arquivo .json de estrutura:
```bash
{ "exchange": ' ',
  "id": ' ',
  "symbol": ' ',
  "params": ' ',
 }
 ```
 As ordens do mercado [https://3xbit.com.br/](https://3xbit.com.br/) são salvas em um .json da forma:
 ```bash
 {market: [{"symbol": ,
            "buy_ordes": ,
            "sell_ordes": 
           }, 
           ...,
          ]
 }
 ```          
