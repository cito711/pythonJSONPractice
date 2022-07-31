from json2html import *
import json

#input = {
#    "name" : "json2html",
#    "description" : "converts JSON to HTML tabular expression"
#}
with open("jsonData/meteorite_landings.json", "r", encoding="utf-8") as json_file:
    input = json.load(json_file)


with open("json2htmlExampleHTML.html", "w", encoding="utf-8") as html_file:
    html_file.write(json2html.convert(json = input))