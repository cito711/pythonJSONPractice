from cgitb import html
import pandas as pd
import json

df = pd.read_json("jsonData/meteorite_landings.json")

htmlHead = "<head><style>table {font-family: sans-serif;}th {font-size: 24px;}tr {font-size: 18px;}</style></head>"

with open("pandasDFToHTML.html", "w", encoding="utf-8") as html_file:
    html_file.write(htmlHead)
    html_file.write(df.to_html())



