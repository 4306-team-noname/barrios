import csv
import matplotlib.pyplot as plt

dates = []
water_lvl = []
technical = []
total = []

with open("../../iss-data\csv\sus_weekly_consumable_water_summary_20220102-20230903.csv", 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader) 

    for row in csv_reader:
        date = row[0]
        water = float(row[1])
        tech = float(row[2])
        tot = float(row[3])
        dates.append(date)
        water_lvl.append(water)
        technical.append(tech)
        total.append(tot)

plt.figure(figsize=(10, 6))
plt.plot(dates, water_lvl, label='Water', marker='o', linestyle='-')
plt.plot(dates, technical, label='Technical', marker='o', linestyle='--')  # Add Technical line
plt.plot(dates, total, label='Total', marker='o', linestyle='--')  # Add Total line

plt.xlabel('Date')
plt.ylabel('Water Level')

plt.axhline(y=1000, color='orange', linestyle='--', label='Water Alert')  # Add orange dashed line at 1000
plt.axhline(y=818, color='red', linestyle='--', label='Water Critical')  # Add red dashed line at 818

plt.xticks(rotation=45)
plt.ylim(0, 5500)  # Increase y-axis limit to 5000
plt.legend()

plt.tight_layout()
plt.show()