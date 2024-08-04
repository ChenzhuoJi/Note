from pathlib import Path
import csv
from datetime import datetime
import plotly.express as px
path=Path("wetherdate\sitka_weather_2021_simple.csv")
lines=path.read_text().splitlines()
reader=csv.reader(lines)
herder_row=next(reader)
dates,highs,lows,tem_differences=[],[],[],[]
for row in reader:
    date=datetime.strptime(row[2],'%Y-%m-%d')
    high=(int(row[4])-32)*5/9
    low=(int(row[5])-32)*5/9
    tem_difference=high-low
    dates.append(date)
    highs.append(high)
    lows.append(low)
    tem_differences.append(tem_difference)
fig=px.bar(x=dates,y=highs)
fig.show()