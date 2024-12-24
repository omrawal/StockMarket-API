from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict, Optional
import json
from stocksnap import StockSnap

class QuoteDetails(BaseModel):
    ticker_symbol:str
    ticker_symbol:str
    exchange_symbol:str
    ltp: str
    desc: str
    previous_close: str
    currency: str
    percentage_change: str
    change_amount: float
    currency_symbol: str
    change_type: str

app = FastAPI()

@app.get("/")
def home():
    return {'message':'This is homepage for stock market api, please refer documentation.'}

@app.get("/get_quote/{ticker_symbol}")
def get_quote(ticker_symbol:str):
    ticker = StockSnap()
    ticker_response = ticker.fetch_details(ticker_symbol=ticker_symbol)

    ticker_response_json = json.loads(ticker_response)
    response_list = []
    for key in ticker_response_json:
        response_list.append( QuoteDetails(**ticker_response_json[key]))
    if len(response_list) < 1:
        raise HTTPException(status_code=404, detail=f"No Data found for the given ticker symbol:{ticker_symbol}")
    return response_list

@app.get("/get_quote_with_exchange_symbol/{ticker_symbol}:{exchange_symbol}")
def get_quote_with_exchange_symbol(ticker_symbol:str,exchange_symbol:str):
    ticker = StockSnap()
    ticker_response = ticker.fetch_details_by_exchange(ticker_symbol=ticker_symbol,exchange_symbol=exchange_symbol)
    ticker_response_json = json.loads(ticker_response)
    response_list = []
    for key in ticker_response_json:
        response_list.append( QuoteDetails(**ticker_response_json[key]))
    if len(response_list) < 1:
        raise HTTPException(status_code=404, detail=f"No Data found for the given combination of ticker symbol:{ticker_symbol} and exchange symbol:{exchange_symbol}")
    return response_list


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app,host='localhost',port=8000)
