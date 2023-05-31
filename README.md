# Overview
The sales_forecasting project aims to predict the future sales of a company that is venturing into data science. It focuses on leveraging machine learning techniques for sales forecasting. The project is divided into three main folders: DATA, CODES, and OUTPUT.

## DATA
This folder contains a CSV file with the historical records of the company's total sales. For privacy reasons, sensitive information such as branch, salesperson, and customer details have been removed.

## CODES
### models_evaluation.ipynb
The "models_evaluation.ipynb" Jupyter Notebook compares and evaluates four different prediction models based on time series analysis. The notebook analyzes the data in more detail, looking for seasonality, trends, moving averages, etc. All resulting plots and visualizations are saved in the OUTPUT folder.

### prophet_pipeline.ipynb
The "prophet_pipeline.ipynb" Jupyter Notebook defines the entire pipeline for the prediction algorithm using the Prophet library from Facebook. The notebook also exports the serialized model to a JSON file. The main purpose of this notebook is to retrain and evaluate the final model.

### API
This folder contains code for a REST API deployment of the final model. The REST API is built using the FASTAPI library and utilizes uvicorn as the server. The functions and models are added using another script inside the "models" subfolder. The main file, named "main.py," focuses solely on the REST API implementation and is designed to easily incorporate additional functionalities and endpoints in the future.

### Dockerfile
The Dockerfile provided allows for the creation of a Docker image for easy deployment and containerization of the application. It includes the necessary requirements.txt file with the required libraries for the container.

## OUTPUT
The OUTPUT folder stores the generated graphs, the serialized model, and a CSV file containing the predictions.

** Please refer to the individual files and folders for more detailed information and instructions on running the project. **
