# changing file to include all data for the year 2018
# change title to daily high and low temperatues
# extract low temps from the file and add to chart
# shade in the areas between high and low

import csv
from datetime import datetime

open_file = open("sitka_weather_2018_simple.csv", "r")

csv_file = csv.reader(open_file, delimiter=",")

header_row = next(csv_file)

# The enumerate() function returns both the index of each tiem and the value of
# each item as you loop through a list

for index, column_header in enumerate(header_row):
    print("Index: ", index, "Column Name:", column_header)

dates = []
highs = []
lows = []
# as an example
# somedate = "2018-07-01"
# onverted_date = datetime.strptime(somedate, "%Y-%m-%d")

# print(converted_date)


for row in csv_file:
    highs.append(int(row[5]))
    converted_date = datetime.strptime(row[2], "%Y-%m-%d")
    dates.append(converted_date)
    lows.append(int(row[6]))

# print(highs)

import matplotlib.pyplot as plt

fig = plt.figure()

plt.plot(dates, highs, c="red")
plt.plot(dates, lows, c="blue")

plt.fill_between(dates, highs, lows, facecolor="blue", alpha=0.1)

plt.title("Daily high and low temperatues - 2018", fontsize=16)
plt.xlabel("", fontsize=12)
plt.ylabel("Temperature (F)", fontsize=12)
plt.tick_params(axis="both", labelsize=12)

fig.autofmt_xdate()

plt.show()


# matplotlib's pyplot API has a convenience function called subplots() where
# utility wrapper and helps in creating common layouts of subplots, including
# enclosing figure objects in a single cell

fig2, a = plt.subplots(2)

a[0].plot(dates, highs, c="red")
a[1].plot(dates, lows, c="blue")

plt.show()
