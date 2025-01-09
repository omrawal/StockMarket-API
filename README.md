# StockMarket-API
API REST endpoints for live stock prices. 

## BASE PACKAGE Repo
[https://github.com/omrawal/Stock-Snap](https://github.com/omrawal/Stock-Snap)

# FastAPI Application

This document describes the API structure of the FastAPI application, which provides endpoints for retrieving stock quotes and various indices.

## OpenAPI Specification
- **Version**: 3.1.0
- **Title**: FastAPI
- **Version**: 0.1.0

## API Endpoints

### Home
- **Endpoint**: `/`
- **Method**: `GET`
- **Summary**: Home
- **Operation ID**: `home__get`
- **Responses**:
  - `200`: Successful Response

### Get Quote
- **Endpoint**: `/get_quote/{ticker_symbol}`
- **Method**: `GET`
- **Summary**: Get Quote
- **Operation ID**: `get_quote_get_quote__ticker_symbol__get`
- **Parameters**:
  - `ticker_symbol` (required, string): The stock ticker symbol.
- **Responses**:
  - `200`: Successful Response
  - `422`: Validation Error

### Get Quote With Exchange Symbol
- **Endpoint**: `/get_quote_with_exchange_symbol/{ticker_symbol}:{exchange_symbol}`
- **Method**: `GET`
- **Summary**: Get Quote With Exchange Symbol
- **Operation ID**: `get_quote_with_exchange_symbol_get_quote_with_exchange_symbol__ticker_symbol___exchange_symbol__get`
- **Parameters**:
  - `ticker_symbol` (required, string): The stock ticker symbol.
  - `exchange_symbol` (required, string): The exchange symbol.
- **Responses**:
  - `200`: Successful Response
  - `422`: Validation Error

### Get NSE Indices
- **Endpoint**: `/get_nse_indices`
- **Method**: `GET`
- **Summary**: Get NSE Indices
- **Operation ID**: `get_nse_indices_get_nse_indices_get`
- **Responses**:
  - `200`: Successful Response

### Get BSE Indices
- **Endpoint**: `/get_bse_indices`
- **Method**: `GET`
- **Summary**: Get BSE Indices
- **Operation ID**: `get_bse_indices_get_bse_indices_get`
- **Responses**:
  - `200`: Successful Response

### Get Global Indices
- **Endpoint**: `/get_global_indices`
- **Method**: `GET`
- **Summary**: Get Global Indices
- **Operation ID**: `get_global_indices_get_global_indices_get`
- **Responses**:
  - `200`: Successful Response

## Components

### Schemas

#### HTTPValidationError
- **Type**: `object`
- **Title**: HTTPValidationError
- **Properties**:
  - `detail` (array): An array of `ValidationError` objects.

#### ValidationError
- **Type**: `object`
- **Title**: ValidationError
- **Required**: `loc`, `msg`, `type`
- **Properties**:
  - `loc` (array): The location of the error, containing strings or integers.
  - `msg` (string): The error message.
  - `type` (string): The type of the error.

