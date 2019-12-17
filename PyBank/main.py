#PyBank 

# Modul acmak icin

import os
import csv

# Olusturacagimiz datalari store etmek icin liste aciyoruz

months = []
profit_loss = []

# Path aciyoruz

budget_csv = os.path.join('..','Resources','budget_data.csv')

# CSV leri aciyoruz

with open(budget_csv, newline="") as csvfile:
    budget_reader = csv.reader(csvfile, delimiter=",")

# Headeri skip etmek icin
  
    next(budget_reader)

# CSV icinde tekrarli islemler yapmak icin
    
    for row in budget_reader:

        
        months.append(row[0]) # Tarih

        
        profit_loss.append(float(row[1])) # Kazanc/Zarar


total_months = (len(months)) # Toplam aylar


net_amount = sum(profit_loss) # Net kazanc


avg_change = net_amount / total_months # Aylik ortalama degisim


max_profit = max(profit_loss) # En yuksek kazanc ve ayi


index_max = profit_loss.index(max_profit)
max_month = months[index_max]


min_profit = min(profit_loss) # En dusuk kazanc ve ayi


index_min = profit_loss.index(min_profit) # Index ile date bulunuyor------> en buyuk kayip icin
min_month = months[index_min]

financial_analysis = (f'''Financial Analysis
----------------------------------
Total Months: {total_months}
Total: ${net_amount:.2f}
Average Change: {avg_change:.2f}
Greatest Increase in Profits: {max_month} {max_profit:.2f}
Greatest Decrease in Profits: {min_month} {min_profit:.2f}''')


print(financial_analysis) #----------> analizin ciktisi


analysis = open('financial_analysis.txt', 'w') #--------------> .txt file yapmak icin

analysis.write(financial_analysis)

analysis.close()