# Import fundamental libraries
import uvicorn
from prophet.serialize import model_from_json
from functions import format_prophet
from fastapi import FastAPI
from typing import Union
import warnings

# Warning about future deprecation of pandas function
warnings.filterwarnings("ignore", category=FutureWarning, module="prophet")

app = FastAPI()

@app.get("/")
def home():
    return {"Welcome": 'User'}


@app.get('/sales/{weeks}')
def future_sales(weeks: int):
    # Load model
    with open('../../OUTPUT/MODELS/total_sell_serialized_model.json', 'r') as fin:
        fitted_model_PROPHET = model_from_json(fin.read())  # Load model

    # Create a future dataframe for making predictions (half year)
    # Dataframe include previous dates (prophet format)
    future = fitted_model_PROPHET.make_future_dataframe(periods=weeks, freq='W-SUN')

    # Use the fitted model to make predictions on the future dataframe
    forecast = fitted_model_PROPHET.predict(future)

    # Format the Prophet forecast data
    predictions_ready = format_prophet(forecast, weeks)

    return predictions_ready

#if __name__ == "__main__":
#    uvicorn.run(app, host="127.0.0.1", port=8000)