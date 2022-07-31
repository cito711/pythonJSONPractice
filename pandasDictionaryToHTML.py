import pandas as pd

a = open("converted.txt")

df = pd.DataFrame(data=a)
# df = df.fillna(' ').T
with open("htmlOutput.html", "w") as htmlData:
    htmlData.write(df.to_html())