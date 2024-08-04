import matplotlib.pyplot as plt
from pathlib import Path
from datetime import datetime
import csv
import pytest
path=Path("wetherdate\sitka_weather_2021_full.csv")
lines=path.read_text().splitlines()
reader=csv.reader(lines)
hearder_row=next(reader)
for index,column_header in enumerate(hearder_row):
    print(index,column_header)
rainfalls,dates=[],[]
for row in reader:
    try:
        rainfall=float(row[5])
        date=datetime.strptime(row[2],"%Y-%m-%d")
    except ValueError:
        pass
    else:
        rainfalls.append(rainfall)
        dates.append(date)
fig,ax=plt.subplots()
ax.plot(dates,rainfalls,color='blue')
fig.autofmt_xdate()
plt.show()
print(sum(rainfalls))