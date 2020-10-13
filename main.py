from cleaner import clean_dataframe
from cleaner import export_dataset
import pandas as pd

try:
    export_dataset(None, None)
    print("Success")
except:
    print("no deal")
