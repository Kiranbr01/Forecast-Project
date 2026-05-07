

from fastapi import FastAPI
import pandas as pd

app = FastAPI()

# Load forecast data
forecast_df = pd.read_csv(
    'future_forecasts.csv'
)

# Home endpoint
@app.get('/')

def home():

    return {

        'message':
        'Forecast API Running Successfully'

    }

# Forecast endpoint
@app.get('/forecast/{state}')

def get_forecast(state: str):

    result = forecast_df[

        forecast_df['State']
        .str.lower()
        ==
        state.lower()

    ]

    return result.to_dict(
        orient='records'
    )

