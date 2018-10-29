import numpy as np
import mimetypes
from PIL import Image
import numpy as np
from spectral import *
import pandas as pd
from fbprophet import Prophet
from math import sqrt

# Prepare data for FB Prophet
def format_data(df):
    '''
    Takes in a dataframe with population and date data and returns a dataframe
    properly formated for fbprophet

    Args:
        df: Dataframe with population and date data

    Returns:
        Dataframe properly formated for facebook prophet
    '''
    df['date'] = pd.to_datetime(df['date'])
    return df.rename(columns={'date': 'ds', 'population': 'y'})

# Create FB Prophet instance & fit data
def make_model(X):
    '''
    Creates a fitted Prophet model

    Args:
        X: Dataframe properly formated for Prophet

    Returns:
        A fit Prophet model
    '''
    model = Prophet()  #daily_seasonality=True
    return model.fit(X)

# Forecast refugee camp population 3 months out
def forcast_pop(model, periods=3):
    '''
    Forcasts low, medium and high estimates for population in the next periods

    Args:
        model: The fit Prophet model to be used for forcasting
        periods: The next set of periods to predict for

    Returns:
        A data from containing date, population estimate, lower population
        estimate, and upper population estimate
        [DS, YHAT, YHAT_LOWER, YHAT_UPPER] respectivly
    '''
    future = model.make_future_dataframe(periods=periods)
    forecast = model.predict(future)
    return forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']]

def predict_pop(data_frame, period=3):
    '''
    Takes in a dataframe and period returns the predictions for the specified
    time period

    Args:
        data_frame: A pandas dataframe from containing date and population data
        periods: The next set of periods to predict for

    Returns:
        A data from containing date, population estimate, lower population
        estimate, and upper population estimate
        [DS, YHAT, YHAT_LOWER, YHAT_UPPER] respectivly
    '''
    df = format_data(data_frame)
    model = make_model(df)
    return forcast_pop(model, period)#.tail()?

if __name__ == '__main__':
    rukban_df = pd.read_csv('data/refugee-population.csv')
    print(predict_pop(rukban_df))
