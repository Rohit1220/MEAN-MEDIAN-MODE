import csv
with open("SOCR-HeightWeight.csv",newline='')as file:
    file_data = csv.reader(file) 
    data = list(file_data)
data.pop(0)
h_list = []
for i in range(len(data)):
    num = data[i][1]
    h_list.append(float(num))
total_data = len(h_list)
sum = 0
for i in h_list:
    sum += i
mean = sum/total_data
print("mean of the data is :" + str(mean))
h_list.sort()
if total_data%2 == 0:
    m1 = float(h_list[total_data//2])
    m2 = float(h_list[total_data//2-1])
    median = (m1+m2)/2
else :
    median = (h_list[total_data//2])
print("median of the data is :" + str(median))
from collections import Counter
#Calculating Mode
data = Counter(h_list)
mode_data_for_range = {
                        "50-60": 0,
                        "60-70": 0,
                        "70-80": 0
                    }
for height, occurence in data.items():
    if 50 < float(height) < 60:
        mode_data_for_range["50-60"] += occurence
    elif 60 < float(height) < 70:
        mode_data_for_range["60-70"] += occurence
    elif 70 < float(height) < 80:
        mode_data_for_range["70-80"] += occurence

mode_range, mode_occurence = 0, 0
for range, occurence in mode_data_for_range.items():
    if occurence > mode_occurence:
        mode_range, mode_occurence = [int(range.split("-")[0]), int(range.split("-")[1])], occurence
mode = float((mode_range[0] + mode_range[1]) / 2)
print(f"Mode is -> {mode:2f}")