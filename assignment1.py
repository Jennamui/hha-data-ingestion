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
tabl = pd.read_excel('/Users/jennamui/Library/Containers/com.microsoft.Excel/Data/Downloads/COVID_diet_dataset.xls', sheet_name='Food_Supply_kcal_Data')
tab2 = pd.read_excel('/Users/jennamui/Library/Containers/com.microsoft.Excel/Data/Downloads/COVID_diet_dataset.xls', sheet_name='Fat_Supply_Quantity_Data'

#Section 2
#Found an open source json API via CMS
#imported requests and json
apiDataset = requests.get('https://data.cms.gov/data-api/v1/dataset/c8a139ee-9e31-444c-976f-bab6b287b871/data')
apiDataset = apiDataset.json()
                     
#Section 3

