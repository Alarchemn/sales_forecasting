import pandas as pd
from pathlib import Path
from prophet.serialize import model_from_json
import warnings

# Warning about future deprecation of pandas function
warnings.filterwarnings("ignore", category=FutureWarning, module="prophet")

__version__ = "0.1.0"

BASE_DIR = Path(__file__).resolve(strict=True).parent

# Load model
with open(f'{BASE_DIR}/total_sales_trained-{__version__}.json', 'r') as fin:
    fitted_model_PROPHET = model_from_json(fin.read())  # Load model


def format_prophet(forecast, periods, freq='W-SUN', cvs_name='prediction'):
    """
    Format the Prophet forecast data and save it to a CSV file.

    Parameters:
        forecast (DataFrame): The forecast data obtained from Prophet.
        periods (int): The number of periods to include in the formatted data.
        freq (str): The frequency of the data. Default is 'W-SUN'.
        cvs_name (str): The name of the CSV file to save the formatted data. Default is 'prediction'.

    Returns:
        DataFrame: The formatted prediction data with 'FECHA' as the index.

    """

    # Extract the relevant columns from the forecast
    predicted_data = forecast.tail(periods)[['ds', 'yhat', 'yhat_lower', 'yhat_upper']]

    # Create a dictionary for the formatted prediction data
    dic = {
        'DATE': predicted_data['ds'],
        'PRED': predicted_data['yhat'],
        'MIN': predicted_data['yhat_lower'],
        'MAX': predicted_data['yhat_upper']}

    # Create a DataFrame from the dictionary with DATE as index with specified freq
    prediction_formated = pd.DataFrame(dic)
    prediction_formated.set_index('DATE', inplace=True)
    prediction_formated.index.freq = freq

    return prediction_formated


def predict_pipeline(weeks):
    """
    Make a prediction using the previously fitted Prophet model.

    Parameters:
        weeks (int): Number of weeks into the future to make the prediction.

    Returns:
        pandas.DataFrame: Dataframe with the predictions ready for use.

    """
    # Create a future dataframe for making predictions (half year)
    # Dataframe include previous dates (prophet format)
    future = fitted_model_PROPHET.make_future_dataframe(periods=weeks, freq='W-SUN')

    # Use the fitted model to make predictions on the future dataframe
    forecast = fitted_model_PROPHET.predict(future)

    # Format the Prophet forecast data
    predictions_ready = format_prophet(forecast, weeks)

    return predictions_ready
