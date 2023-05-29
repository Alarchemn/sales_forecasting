import pandas as pd
import re
from pathlib import Path
from prophet.serialize import model_from_json

__version__ "0.1.0"

BASE_DIR = Path(__file__).resolve(strict=True).parent




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