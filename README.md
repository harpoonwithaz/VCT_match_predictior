# Valorant Prediction Algorithm

# Overview
The Valorant Prediction Algorithm project aims to develop a predictive model for predicting the outcomes of Valorant esports matches. The prediction model utilizes data collected from various sources, including the vlr.gg website and the <a href="https://github.com/Orloxx23/vlresports">vlresports - Valorant Esports API</a> by <a href="https://github.com/Orloxx23">__Orloxx23__</a>. This README.md file provides an overview of the project structure, components, and instructions for getting started.

# Project Structure
The project is organized into the following directories:

- **data/**: Contains all data files, including raw data scraped from vlr.gg and data obtained from the Valorant API.
- **src/**: Contains Python source code files for scraping data, data preprocessing, model training, and prediction.

# Components
The main components of the project include:

- **Data Scraping**: Python scripts (`vlr_scraper.py`, `api.py`) for scraping match data from vlr.gg and fetching data from the Valorant API.
- **Data Processing**: Python script (`data_processing.py`) for preprocessing and cleaning the collected data.  (NOT A FEATURE YET)
- **Model Training**: Python script (`model_training.py`) for training machine learning models using the preprocessed data.  (NOT A FEATURE YET)
- **Prediction**: Python script (`prediction.py`) for making predictions using the trained models.  (NOT A FEATURE YET)

# Getting Started
To set up the project, follow these steps:

1. Clone the repository: `git clone https://github.com/your_username/valorant-prediction.git`
2. Navigate to the project directory: `cd valorant-prediction`
3. Install dependencies: `pip install -r requirements.txt`
4. Run the scraping scripts (`vlr_scraper.py`, `api.py`) to collect data from vlr.gg and the Valorant API.
5. Preprocess the collected data using the `data_processing.py` script.
6. Train the prediction model using the `model_training.py` script.
7. Use the trained model to make predictions with the `prediction.py` script.

# Dependencies
The project requires the following dependencies:

- Python 3.12.2
- BeautifulSoup
- Pandas
- Scikit-learn

You can install the dependencies using pip:

```bash
pip install -r requirements.txt
```

This command will install all the required packages listed in the requirements.txt file. Make sure to run this command in your project's virtual environment or add the --user flag to install the packages globally.