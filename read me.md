# End-to-End Time Series Forecasting System with REST API

## Project Overview

This project is a production-style end-to-end time series forecasting system developed to forecast the next 8 weeks of sales for each state using historical sales data.

The system trains and compares multiple forecasting models, automatically selects the best-performing model for each state, and exposes future forecasts through a REST API using FastAPI.

The solution is designed to simulate a real backend forecasting service used in production environments.

---

# Business Problem

Organizations often need accurate sales forecasts to support:

- Inventory planning
- Demand forecasting
- Supply chain optimization
- Financial planning
- Resource allocation
- Strategic business decisions

The objective of this project is to forecast the next 8 weeks of sales for each state using historical sales data while handling seasonality, trend, missing values, and missing dates.

---

# Objectives

The forecasting system was built to:

- Train multiple forecasting algorithms
- Compare model performance automatically
- Select the best-performing model for each state
- Forecast future sales for the next 8 weeks
- Handle missing dates and missing values
- Capture seasonality and trend patterns
- Expose predictions through a REST API
- Follow a production-style backend architecture

---

# Dataset Information

The dataset contains weekly sales information for different states.

## Dataset Columns

| Column | Description |
|---|---|
| Date | Weekly sales date |
| State | State name |
| Total | Total sales value |
| Category | Product category |

---

# Technology Stack

| Category | Technology |
|---|---|
| Programming Language | Python |
| Notebook Environment | Google Colab |
| Data Processing | Pandas, NumPy |
| Statistical Forecasting | SARIMA |
| Trend Forecasting | Facebook Prophet |
| Machine Learning | XGBoost |
| Deep Learning | LSTM |
| API Framework | FastAPI |
| Deployment | ngrok |
| Visualization | Matplotlib |
| Model Serialization | Joblib |

---

# Project Architecture

```text
Historical Sales Data
          ↓
Data Cleaning & Preprocessing
          ↓
Missing Value Handling
          ↓
Missing Date Handling
          ↓
Feature Engineering
          ↓
Time Series Train/Test Split
          ↓
Train Multiple Forecasting Models
    ├── SARIMA
    ├── Prophet
    ├── XGBoost
    └── LSTM
          ↓
Model Evaluation (RMSE)
          ↓
Automatic Best Model Selection
          ↓
8-Week Future Forecasting
          ↓
Forecast Storage
          ↓
FastAPI REST API
          ↓
Prediction Endpoint
```

---

# Data Preprocessing

Several preprocessing techniques were applied to prepare the dataset for forecasting.

## 1. Date Conversion

The Date column was converted into datetime format to support time-series analysis.

## 2. Sorting

The dataset was sorted by:

- State
- Date

This preserves chronological order for forecasting.

## 3. Missing Value Handling

Missing sales values were handled using:

- Linear interpolation
- Forward fill
- Backward fill

This preserves:

- Trend
- Seasonal patterns
- Sales continuity

## 4. Missing Date Handling

Complete weekly date ranges were created for each state to ensure:

- No missing timestamps
- Continuous weekly forecasting
- Consistent time-series frequency

---

# Feature Engineering

Feature engineering is one of the most important parts of the forecasting system.

## Lag Features

Historical sales values were used as predictive signals.

| Feature | Description |
|---|---|
| lag_1 | Previous week sales |
| lag_7 | Sales 7 weeks ago |
| lag_30 | Sales 30 weeks ago |

## Rolling Features

Rolling statistics were created to capture trend and volatility.

| Feature | Description |
|---|---|
| rolling_mean_7 | 7-week rolling average |
| rolling_std_7 | 7-week rolling standard deviation |

## Date Features

Date-based features were extracted from the timestamp.

| Feature | Description |
|---|---|
| month | Month number |
| week | Week number |
| quarter | Quarter number |
| year | Year |
| day_of_week | Day of week |

## Holiday Feature

A holiday flag was created using the US Federal Holiday Calendar.

| Feature | Description |
|---|---|
| holiday_flag | Indicates whether the week contains a holiday |

---

# Time Series Validation Strategy

A proper time-series split strategy was used.

## Why Not Random Split?

Random splitting causes:

- Data leakage
- Unrealistic forecasting accuracy
- Future information leakage into training data

## Correct Approach

The dataset was split chronologically:

- First 80% → Training Data
- Last 20% → Validation Data

This preserves real-world forecasting behavior.

---

# Forecasting Models Implemented

## 1. SARIMA (Seasonal ARIMA)

SARIMA was implemented to capture:

- Trend
- Seasonality
- Autocorrelation
- Repeating patterns

### Advantages

- Excellent for seasonal forecasting
- Statistical forecasting approach
- Handles periodic behavior effectively

---

## 2. Facebook Prophet

Prophet was implemented to model:

- Trend changes
- Seasonality
- Holidays
- Weekly patterns

### Advantages

- Robust forecasting model
- Handles missing values well
- Easy future forecasting
- Business forecasting friendly

---

## 3. XGBoost

XGBoost was implemented using engineered lag features.

### Features Used

- Lag features
- Rolling statistics
- Date features
- Holiday features

### Recursive Forecasting

Future forecasting was implemented recursively.

Predicted future values become future lag inputs.

### Advantages

- Handles nonlinear relationships
- Powerful machine learning model
- Strong predictive performance

---

## 4. LSTM (Long Short-Term Memory)

LSTM was implemented for deep learning-based sequential forecasting.

### Pipeline

- Scaling using MinMaxScaler
- Sequence generation
- Neural network training
- Recursive forecasting

### Advantages

- Learns sequential dependencies
- Captures long-term patterns
- Effective for temporal forecasting

---

# Model Evaluation

All models were evaluated using:

## Evaluation Metrics

| Metric | Description |
|---|---|
| MAE | Mean Absolute Error |
| RMSE | Root Mean Squared Error |

## Why RMSE?

RMSE penalizes larger forecasting errors more heavily, making it ideal for evaluating forecasting systems.

---

# Automatic Best Model Selection

The system automatically selected the best-performing model for each state using the lowest RMSE.

## Example

| State | Best Model |
|---|---|
| California | Prophet |
| Texas | XGBoost |
| Florida | LSTM |
| Arizona | SARIMA |

This state-wise selection approach ensures:

- Higher forecasting accuracy
- State-specific optimization
- Better production performance

---

# Future Forecasting

After model selection, the system generated:

## Next 8 Weeks Forecast

for every state.

## Forecast Output Example

| State | Forecast_Date | Forecast | Best_Model |
|---|---|---|---|
| California | 2026-01-04 | 456789 | Prophet |
| California | 2026-01-11 | 467890 | Prophet |

---

# REST API Implementation

The forecasting system exposes predictions using FastAPI.

## API Endpoint

```text
/forecast/{state}
```

## Example

```text
/forecast/California
```

## Sample Response

```json
[
  {
    "State": "California",
    "Forecast_Date": "2026-01-04",
    "Forecast": 456789,
    "Best_Model": "Prophet"
  }
]
```

---

# Production Features

The system includes several production-grade engineering concepts.

## Implemented Features

- State-wise forecasting pipeline
- Multi-model orchestration
- Recursive forecasting logic
- Automated model selection
- REST API deployment
- Production folder structure
- Reusable forecasting architecture
- Backend-style service design

---

# Folder Structure

```text
forecasting-system/
│
├── data/
│   └── Forecasting Case- Study(1).xlsx
│
├── notebooks/
│   └── forecasting_system.ipynb
│
├── outputs/
│   ├── future_forecasts.csv
│   ├── best_models.csv
│   └── all_model_results.csv
│
├── api/
│   └── app.py
│
├── screenshots/
│
├── requirements.txt
│
└── README.md
```

---

# Key Learnings

This project provided practical experience in:

- Time-series forecasting
- Feature engineering
- Statistical forecasting models
- Machine learning forecasting
- Deep learning forecasting
- Recursive prediction systems
- API deployment
- Production ML architecture
- Backend service development

---

# Challenges Faced

## 1. Missing Dates

Challenge:
- Inconsistent weekly timestamps

Solution:
- Generated complete weekly date ranges

## 2. Future Forecasting with ML Models

Challenge:
- Future lag features do not exist

Solution:
- Implemented recursive forecasting logic

## 3. State-Wise Forecasting

Challenge:
- Different states behave differently

Solution:
- Built independent state-wise forecasting pipelines

## 4. API Deployment in Google Colab

Challenge:
- Asyncio event loop conflict

Solution:
- Used nest_asyncio and threading

---

# Future Improvements

Possible enhancements include:

- Hyperparameter tuning
- Automated SARIMA parameter optimization
- Real-time forecasting pipeline
- Docker deployment
- Cloud deployment
- CI/CD integration
- Streamlit dashboard
- Forecast monitoring system
- Model retraining pipeline

---

# Conclusion

This project successfully implemented a production-style end-to-end forecasting system capable of:

- Training multiple forecasting models
- Comparing forecasting performance
- Selecting the best model automatically
- Forecasting future sales for each state
- Exposing forecasts through a REST API

The solution demonstrates strong understanding of:

- Time-series forecasting
- Machine learning engineering
- Deep learning forecasting
- Backend API development
- Production ML system design

---

# Author

Kiran BR

Data Science & Machine Learning Project

