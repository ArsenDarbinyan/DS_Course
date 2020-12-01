import matplotlib.ticker as ticker
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import googletrans as gt
import csv


def cleaning():
    with open('Data-Project-2.csv', 'r+', newline='') as file:
        read = csv.reader(file)
        wri = csv.writer(open("Data-Project-2.csv", 'r+', newline=''))
        for row in read:
            if '.' in row[3]:
                row[3] = row[3].replace('.', '')
                wri.writerow(row)
            else:
                wri.writerow(row)


df = pd.read_csv('Data Project 2.csv')
df['number'].replace(0, np.nan, inplace=True)
df.dropna(subset=['number'], inplace=True)



fig = plt.figure()
ax1 = fig.add_subplot(1, 2, 1)
ax2 = fig.add_subplot(1, 2, 2)
ax1.barh(df['year'], width=df['number'])
ax2.barh(df['month'], width=df['number'])
ax1.xaxis.set_major_locator(ticker.MultipleLocator(5000))
ax1.yaxis.set_major_locator(ticker.MultipleLocator(1))
ax1.xaxis.set_minor_locator(ticker.MultipleLocator(2500))
ax2.xaxis.set_major_locator(ticker.MultipleLocator(5000))
ax2.yaxis.set_major_locator(ticker.MultipleLocator(1))
ax2.xaxis.set_minor_locator(ticker.MultipleLocator(2500))
df_month = pd.DataFrame(df[['month', 'number']])
numbers_sum = df_month.groupby(['month']).sum()
translator = gt.Translator(service_urls=['translate.google.com', 'translate.google.co.kr'])
months = numbers_sum.index.tolist()
translate = translator.translate(months, src='pt')


translate1 = []
for i in translate:
    translate1.append(i.text)


x = pd.DataFrame(numbers_sum)
df_trans_month = pd.DataFrame(x.values, index=translate1, columns=['number'])


fig = plt.figure()
ax3 = fig.add_subplot(1, 1, 1)
ax3.barh(df_trans_month.index, width=df_trans_month['number'])
plt.show()