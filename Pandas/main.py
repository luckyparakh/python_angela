# Process this file with open

# with open('weather_data.csv') as data_file:
#     data = data_file.readlines()
# # Prints of a row as one element of List & also has whitespaces. Let us use csv library
# print(data)

import csv

# with open('weather_data.csv') as data_file:
#     rows = csv.reader(data_file)
#     print(rows)  # CSV object
#     # Let us get temp out of it
#     for row in rows:
#         if row[1] != 'temp':
#             print(int(row[1]))

import pandas

# Same thing with Pandas as done above by CSV reader
# data = pandas.read_csv('weather_data.csv')
# print(data['temp'])
# print(type(data))
# print(type(data['temp']))
#
# temp_list = data['temp'].to_list()
# print(temp_list)
#
# print(data['temp'].mean())
# print(data['temp'].max())
#
# # Print a row with condition
# print(data[data.temp == data.temp.max()])
#
# max_temp = data[data.temp == data.temp.max()]
# print(max_temp['day'])

# Find count of squirrel on basis of Fur Color

data = pandas.read_csv("squirrel_data.csv")
fur_count_grey = len(data[data["Primary Fur Color"] == 'Gray'])
fur_count_black = len(data[data["Primary Fur Color"] == 'Black'])
fur_count_cinnamon = len(data[data["Primary Fur Color"] == 'Cinnamon'])

data_dict = {
    "Fur Color": ['Gray', 'Cinnamon', 'Black'],
    "Count": [fur_count_grey, fur_count_cinnamon, fur_count_black]
}
# data_dict = {'Gray': 0, 'Cinnamon': 0, 'Black': 0}
# for fur in fur_count:
#     if fur == 'Gray':
#         data_dict['Gray'] += 1
#     if fur == 'Cinnamon':
#         data_dict['Cinnamon'] += 1
#     if fur == 'Black':
#         data_dict['Black'] += 1
# #print(data_dict)
df = pandas.DataFrame(data_dict)
print(df)