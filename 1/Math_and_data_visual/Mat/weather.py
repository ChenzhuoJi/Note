from pathlib import Path
import csv
import matplotlib.pyplot as plt
from datetime import datetime
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
fig,ax=plt.subplots()

ax.plot(dates,highs,color='red')
ax.plot(dates,lows,color='blue')
#ax.plot(dates,tem_differences,color='green')
ax.fill_between(dates,lows,highs,facecolor='blue',alpha=0.5)
ax.set_title("daily High")
fig.autofmt_xdate()
plt.show()