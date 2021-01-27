import pandas as pd
import plotly.express as px
import math
import csv
from collections import Counter

with open('data.csv') as f:
    reader = csv.reader(f)
    data = list(reader)

newData = []

for i in range(len(data)):
    num = data[i][0]
    newData.append(float(num))
n = len(newData)
sum = 0
for x in newData:
    sum = sum + x
mean = sum/n

sqaurelist = []

for number in newData:
  e  = int(number) - mean
  e = e ** 2
  sqaurelist.append(e)

total = 0
for l in sqaurelist:
    total = total + l

result = total/n-1
standardDeviation = math.sqrt(result)
print(standardDeviation)
print(mean)
    
