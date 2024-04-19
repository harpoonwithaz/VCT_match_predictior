# Valorant Prediction Algorithm

## Overview
The Valorant Prediction Algorithm project aims to develop a predictive model for predicting the outcomes of Valorant esports matches. The prediction model utilizes data collected from various sources, including the vlr.gg website and the **vlresports - Valorant Esports API** by __Orloxx23__. This README.md file provides an overview of the project structure, components, and instructions for getting started.

## Project Structure
The project is organized into the following directories:

- **data/**: Contains all data files, including raw data scraped from vlr.gg and data obtained from the Valorant API.
- **src/**: Contains Python source code files for scraping data, data preprocessing, model training, and prediction.
- **notebooks/**: Contains Jupyter notebooks for exploratory data analysis, model development, and visualization.

## Components
The main components of the project include:

- **Data Scraping**: Python scripts (`vlr_scraper.py`, `api.py`) for scraping match data from vlr.gg and fetching data from the Valorant API.
- **Data Processing**: Python script (`data_processing.py`) for preprocessing and cleaning the collected data.
- **Model Training**: Python script (`model_training.py`) for training machine learning models using the preprocessed data.
- **Prediction**: Python script (`prediction.py`) for making predictions using the trained models.
- **Notebooks**: Jupyter notebooks (`exploratory_data_analysis.ipynb`, `model_development.ipynb`, `visualization.ipynb`) for conducting exploratory data analysis, developing prediction models, and visualizing results.

## Getting Started
To set up the project, follow these steps:

1. Clone the repository: `git clone https://github.com/your_username/valorant-prediction.git`
2. Navigate to the project directory: `cd valorant-prediction`
3. Install dependencies: `pip install -r requirements.txt`
4. Run the scraping scripts (`vlr_scraper.py`, `api.py`) to collect data from vlr.gg and the Valorant API.
5. Preprocess the collected data using the `data_processing.py` script.
6. Train the prediction model using the `model_training.py` script.
7. Use the trained model to make predictions with the `prediction.py` script.

## Dependencies
The project requires the following dependencies:

- Python 3.x
- BeautifulSoup
- Pandas
- Scikit-learn
- Matplotlib
- Seaborn

You can install the dependencies using pip: