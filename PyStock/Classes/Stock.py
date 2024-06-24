import yfinance as yf

class Stock():
    def __init__(self):
        self.ticker = input("Digite o ticker: ").upper() + ".SA"
        self.acao = yf.Ticker(self.ticker)

        self.info = self.acao.info
        print("Informações gerais:", self.info)
        print(self.info["currentPrice"])