#import packages
import pandas as pd ## import pandas for general file types 
import json ## imoprt json for json files
import bs4 ## import bs4 for html files
import requests ## import requests for web requests
import sqlalchemy ## import sqlalchemy for sql queries
from PIL import Image  ## import pillow for image files
import pydub ## import pydub for audio files
from pydub.playback import play
import playsound ## import playsound for audio files
import geopandas as gpd ## import geopandas for geospatial files
from google.cloud import bigquery ## import bigquery for bigquery files
import matplotlib
import xlrd ## import xlrd for excel files, tab names 
import PyPDF2 ## import PyPDF2 for pdf files

#Section 1
#Downloaded dataset from Kaggle
#import local excel file and define each tab 
tab1 = pd.read_excel('/Users/jennamui/Library/Containers/com.microsoft.Excel/Data/Downloads/COVID_diet_dataset.xls', sheet_name='Food_Supply_kcal_Data')
tab2 = pd.read_excel('/Users/jennamui/Library/Containers/com.microsoft.Excel/Data/Downloads/COVID_diet_dataset.xls', sheet_name='Fat_Supply_Quantity_Data')

#Section 2
#Found an open source json API via CMS
#imported requests and json
apiDataset = requests.get('https://data.cms.gov/data-api/v1/dataset/c8a139ee-9e31-444c-976f-bab6b287b871/data')
apiDataset = apiDataset.json()
                     
#Section 3
#create and load api key, enable api in GCP
#connect to bigquery
client = bigquery.Client.from_service_account_json('/Users/jennamui/Documents/GitHub/HHA-507-2022/ingestion/example_files/jenna-507-8d6d73550511.json')
#get bigquery public dataset
query_job = client.query("SELECT * FROM `bigquery-public-data.blackhole_database.sdss_dr7` LIMIT 100")
#get results of query1                   
results = query_job.result()
#put results of query1 into dataframe named bigquery1                                        
bigquery1 = pd.DataFrame(results.to_dataframe())

#repeat for second dataset
client = bigquery.Client.from_service_account_json('/Users/jennamui/Documents/GitHub/HHA-507-2022/ingestion/example_files/jenna-507-8d6d73550511.json')
query_job = client.query("SELECT * FROM `bigquery-public-data.chicago_crime.crime` LIMIT 100")
results = query_job.result()
bigquery2 = pd.DataFrame(results.to_dataframe())

#had to install db-dtypes
pip install db-dtypes
