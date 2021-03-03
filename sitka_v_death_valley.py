import csv
from datetime import datetime

# open 2 files
open_file1 = open("sitka_weather_2018_simple.csv", "r")
open_file2 = open("death_valley_2018_simple.csv", "r")

# assign each open file to a csv
csv_1 = csv.reader(open_file1, delimiter=",")
csv_2 = csv.reader(open_file2, delimiter=",")

# create headers for ease of access
header1 = next(csv_1)
header2 = next(csv_2)


n_index1 = header1.index("NAME")
h_index1 = header1.index("TMAX")
l_index1 = header1.index("TMIN")
d_index1 = header1.index("DATE")

n_index2 = header2.index("NAME")
h_index2 = header2.index("TMAX")
l_index2 = header2.index("TMIN")
d_index2 = header2.index("DATE")

# create name variables, set to 0, used in upcoming for loop
name1 = 0
name2 = 0

# create lists
dates1 = []
highs1 = []
lows1 = []

dates2 = []
highs2 = []
lows2 = []

# using for loop append to lists, first checks if the name has been changed
# if name hasn't been changed, changes name to whatever is under the name column
# in the csv file. Then uses try function to make sure data is fileld
# otherwise return print function for missing data, otherwise appends data to lists
for row in csv_1:
    if name1 == 0:
        name1 = row[n_index1]

    try:
        high = int(row[h_index1])
        low = int(row[l_index1])
        converted_date = datetime.strptime(row[d_index1], "%Y-%m-%d")
    except ValueError:
        print(f"Missing data for {converted_date}")
    else:
        highs1.append(int(row[h_index1]))
        lows1.append(int(row[l_index1]))
        dates1.append(converted_date)


for row in csv_2:
    if name2 == 0:
        name2 = row[n_index2]
    try:
        high2 = int(row[h_index2])
        low2 = int(row[l_index2])
        converted_date2 = datetime.strptime(row[d_index2], "%Y-%m-%d")
    except ValueError:
        print(f"Missing data for {converted_date}")
    else:
        highs2.append(int(row[h_index2]))
        lows2.append(int(row[l_index2]))
        dates2.append(converted_date2)

import matplotlib.pyplot as plt

fig, a = plt.subplots(2)

a[0].plot(dates1, highs1, c="red")
a[0].plot(dates1, lows1, c="blue")
a[0].fill_between(dates1, highs1, lows1, facecolor="blue", alpha=0.1)
a[0].set_title(name1, fontsize=14)

a[1].plot(dates2, highs2, c="red")
a[1].plot(dates2, lows2, c="blue")
a[1].fill_between(dates2, highs2, lows2, facecolor="blue", alpha=0.1)
a[1].set_title(name2, fontsize=14)

fig.suptitle("Temperature comparison between " + name1 + " and " + name2, fontsize=14)

plt.show()