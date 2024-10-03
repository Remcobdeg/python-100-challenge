#exercise 1

with open("weather_data.csv") as file:
    content = file.readlines()

table = []
for line in content:
    line = line.strip()
    line = line.split(',')
    table.append(line)

print(table)

#alternative by Angela Yu:

import csv
with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    for row in data:
        print(row)

#exercise 2: extract temperatures as integers
import csv
with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperatures = []
    for row in data:
        if row[1] != 'temp':
            temperatures.append(int(row[1]))

print(temperatures)

#with pandas

import pandas
data = pandas.read_csv("weather_data.csv")
print(data.temp.max()) #print(data['temp']max())

#get the row of the max temperature
print(data[data.temp == data.temp.max()])

#Monday's temperature in Fahrenheit (C × (9/5) + 32
def C_to_F(C):
    return C * (9 / 5) + 32
monday = data[data.day == "Monday"]
print(C_to_F(monday.temp[0]))

#creating a pd dataframe
data_dict = {
    "students" : ["Yu", "Yan", "Yo"],
    "scores" : [1,2,3]
}
data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")
