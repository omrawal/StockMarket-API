from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict, Optional
import json
from stocksnap import StockSnap
from indices import Indices


class QuoteDetails(BaseModel):
    ticker_symbol: str
    ticker_symbol: str
    exchange_symbol: str
    ltp: str
    desc: str
    long_desc: Optional[str] = None
    previous_close: str
    currency: Optional[str] = None
    percentage_change: str
    change_amount: float
    currency_symbol: Optional[str] = None
    change_type: str


app = FastAPI()


@app.get("/")
def home():
    return {'message': 'This is homepage for stock market api, please refer documentation.'}


@app.get("/get_quote/{ticker_symbol}")
def get_quote(ticker_symbol: str):
    ticker = StockSnap()
    ticker_response = ticker.fetch_details(ticker_symbol=ticker_symbol)
    ticker_response_json = json.loads(ticker_response)

    response_list = []
    for key in ticker_response_json:
        response_list.append(QuoteDetails(**ticker_response_json[key]))

    if len(response_list) < 1:
        raise HTTPException(status_code=404, detail=f"No Data found for the given ticker symbol:{ticker_symbol}")

    return response_list


@app.get("/get_quote_with_exchange_symbol/{ticker_symbol}:{exchange_symbol}")
def get_quote_with_exchange_symbol(ticker_symbol: str, exchange_symbol: str):
    ticker = StockSnap()
    ticker_response = ticker.fetch_details_by_exchange(ticker_symbol=ticker_symbol, exchange_symbol=exchange_symbol)
    ticker_response_json = json.loads(ticker_response)

    response_list = []
    for key in ticker_response_json:
        response_list.append(QuoteDetails(**ticker_response_json[key]))

    if len(response_list) < 1:
        raise HTTPException(status_code=404,
                            detail=f"No Data found for the given combination of ticker symbol:{ticker_symbol} and exchange symbol:{exchange_symbol}")

    return response_list


@app.get('/get_nse_indices')
def get_nse_indices():
    nse_index = Indices()
    nse_index_response_list = nse_index.get_all_nse_indices()

    response_list = []
    for nse_index_response in nse_index_response_list:
        ticker_response_json = json.loads(nse_index_response)
        for key in ticker_response_json:
            response_list.append(QuoteDetails(**ticker_response_json[key]))

    if len(response_list) < 1:
        raise HTTPException(status_code=404,
                            detail=f"No Data found for NSE indices")

    return response_list


@app.get('/get_bse_indices')
def get_bse_indices():
    bse_index = Indices()
    bse_index_response_list = bse_index.get_all_bse_indices()
    response_list = []
    for bse_index_response in bse_index_response_list:
        ticker_response_json = json.loads(bse_index_response)
        for key in ticker_response_json:
            print(key, "->>", ticker_response_json[key])
            response_list.append(QuoteDetails(**ticker_response_json[key]))
    if len(response_list) < 1:
        raise HTTPException(status_code=404,
                            detail=f"No Data found for BSE indices")
    return response_list


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, host='localhost', port=8000)
