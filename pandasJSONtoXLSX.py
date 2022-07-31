import pandas as pd
import json
import xlsxwriter

df = pd.read_json("jsonData/meteorite_landings.json")
df.to_excel("pandasDFToXLS.xlsx")
