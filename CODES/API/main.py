# Import fundamental libraries
from typing import Dict
from fastapi import FastAPI, Request
from models.total_sales import predict_pipeline
from models.total_sales import __version__ as total_sales_model_version
from http import HTTPStatus

app = FastAPI()


def format_response(data):
    response = {
        "message": HTTPStatus.OK.phrase,
        "status-code": HTTPStatus.OK,
        "data": data
    }
    return response


@app.get("/")
def home() -> Dict:
    data = {
        "total_sales_model_version": total_sales_model_version
    }
    response = format_response(data)
    return response


@app.get('/sales/{weeks}')
def future_sales(weeks: int) -> Dict:
    predictions = predict_pipeline(weeks)
    data = {
        "predictions": predictions
    }
    response = format_response(data)
    return response

# if __name__ == "__main__":
#    uvicorn.run(app, host="127.0.0.1", port=8000)
