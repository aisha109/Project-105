import math
import csv


with open('data.csv', newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)


data = file_data[0]

def mean(data):
     n = len(data)
     total = 0

     for x in data:
        total += int(x)
     mean = total/n
     return mean



squaredlist = []
for number in data:
    sn=int(number)-mean(data)
    sn = sn**2
    squaredlist.append(sn)

#step3 - getting sum

sum = 0
for my in squaredlist:
    sum = sum+my

#step 4 - dividing the sum by total values

result= sum/(len(data)-1)

#step5- getting the sd for the data by taking the square root of the result

sd = math.sqrt(result)

print(sd)
