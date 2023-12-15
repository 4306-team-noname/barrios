import csv
import matplotlib.pyplot as plt

dates = []
o2_levels = []
adjusted_o2 = []
n2_levels = []


with open("../../iss-data\csv\s_us_rs_weekly_consumable_gas_summary_20220102-20230903.csv", 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader) 

    for row in csv_reader:
        date = row[0]
        o2 = float(row[1])
        ao2 = float(row[5])
        n2 = float(row[3])
        dates.append(date)
        o2_levels.append(o2)
        adjusted_o2.append(ao2)
        n2_levels.append(n2)

plt.figure(figsize=(10, 6))
plt.plot(dates, o2_levels, label='USOS O2 (kg)', marker='o', linestyle='-')
plt.plot(dates, adjusted_o2, label='Adjusted O2 (kg)', marker='o', linestyle='-')

plt.xlabel('Date')
plt.ylabel('Oxygen Level')
plt.title('Oxygen Levels Over Time')


plt.xticks(rotation=45)
plt.ylim(0,400)
plt.legend()

plt.tight_layout()
plt.show()
 




