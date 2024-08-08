import os
import zipfile
from src.logger import logging

zip_file_path = 'C:\\Users\\DARZI\\Downloads\\archive.zip'
extract_dir = 'C:\\Users\\DARZI\\OneDrive\\Documents\\ml\\customer-churn-prediction\\data\\raw'

with zipfile.ZipFile(zip_file_path, 'r') as zip_file:
        zip_file.extractall(extract_dir)
        logging.info('CSV Extracted and placed in data/raw directory')