import json
from stocksnap import StockSnap


class Indices:
    def __init__(self):
        self.ticker = StockSnap()
        self.NSE_EXCHANGE_SYMBOL = 'INDEXNSE'
        self.BSE_EXCHANGE_SYMBOL = 'INDEXBOM'

    def get_all_nse_indices(self):
        with open("./assets/nse_indices_list.json", "r") as symbols_file:
            index_symbol_list = json.load(symbols_file)

        response_list = []
        for index_symbol in index_symbol_list:
            # print(f"Checking for index_symbol: {index_symbol}")
            quote_data = self.ticker.fetch_details_by_exchange(ticker_symbol=index_symbol,
                                                               exchange_symbol=self.NSE_EXCHANGE_SYMBOL)
            # print({index_symbol: quote_data})
            response_list.append(quote_data)
        return response_list

    def get_all_bse_indices(self):
        with open("./assets/bse_indices_list.json", "r") as symbols_file:
            index_symbol_list = json.load(symbols_file)

        response_list = []
        for index_symbol in index_symbol_list:
            # print(f"Checking for index_symbol: {index_symbol}")
            quote_data = self.ticker.fetch_details_by_exchange(ticker_symbol=index_symbol,
                                                               exchange_symbol=self.BSE_EXCHANGE_SYMBOL)
            # print({index_symbol: quote_data})
            response_list.append(quote_data)
        return response_list
