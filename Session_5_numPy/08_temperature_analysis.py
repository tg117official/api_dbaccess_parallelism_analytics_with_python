import numpy as np

# --------------------------------------------------------
# 🌤️ Simulated temperature data (°C) for 7 days across 4 cities
# Each row = a day (Mon to Sun), each column = a city
# --------------------------------------------------------

cities = ['Delhi', 'Mumbai', 'Bangalore', 'Kolkata']
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

temperature_data = np.array([
    [22.1, 23.4, 21.7, 24.5],  # Monday
    [22.5, 23.8, 21.1, 24.8],  # Tuesday
    [21.7, 23.3, 20.9, 24.2],  # Wednesday
    [22.6, 23.5, 21.8, 24.9],  # Thursday
    [22.1, 23.6, 21.2, 24.4],  # Friday
    [21.9, 23.4, 21.5, 24.5],  # Saturday
    [22.2, 23.5, 21.7, 24.6]   # Sunday
])

# --------------------------------------------------------
# 🔎 Average temperature for each city over the week
# --------------------------------------------------------
mean_temperatures = np.mean(temperature_data, axis=0)
print("📊 Weekly Average Temperature per City:")
for i, city in enumerate(cities):
    print(f" - {city}: {mean_temperatures[i]:.2f}°C")

# --------------------------------------------------------
# 🔎 Min & Max temperature across all data
# --------------------------------------------------------
min_temp = np.min(temperature_data)
max_temp = np.max(temperature_data)
print(f"\n🌡️ Lowest temperature recorded during the week: {min_temp:.2f}°C")
print(f"🔥 Highest temperature recorded during the week: {max_temp:.2f}°C")

# --------------------------------------------------------
# 🔎 Standard deviation: how much temperature varied in each city
# --------------------------------------------------------
std_temperatures = np.std(temperature_data, axis=0)
print("\n📈 Temperature Fluctuation (Standard Deviation):")
for i, city in enumerate(cities):
    print(f" - {city}: ±{std_temperatures[i]:.2f}°C")

# --------------------------------------------------------
# 📌 Hottest and Coldest Cities based on Average Temperature
# --------------------------------------------------------
hottest_city_index = np.argmax(mean_temperatures)
coldest_city_index = np.argmin(mean_temperatures)
print(f"\n🏙️ Hottest city this week: {cities[hottest_city_index]} with avg {mean_temperatures[hottest_city_index]:.2f}°C")
print(f"❄️ Coldest city this week: {cities[coldest_city_index]} with avg {mean_temperatures[coldest_city_index]:.2f}°C")

# --------------------------------------------------------
# 🔍 Identify above-average days for Delhi (city index 0)
# --------------------------------------------------------
delhi_temps = temperature_data[:, 0]
delhi_mean = np.mean(delhi_temps)
above_avg_days = np.where(delhi_temps > delhi_mean)[0]
print(f"\n📅 Days when Delhi was hotter than average ({delhi_mean:.2f}°C):")
for i in above_avg_days:
    print(f" - {days[i]}: {delhi_temps[i]}°C")

# --------------------------------------------------------
# 🔁 Convert the entire dataset to Fahrenheit
# --------------------------------------------------------
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

fahrenheit_data = celsius_to_fahrenheit(temperature_data)
print("\n🌡️ Weekly Temperature Data in Fahrenheit:")
for i in range(len(days)):
    print(f"{days[i]}: {fahrenheit_data[i]}")

# --------------------------------------------------------
# 🧠 BONUS INSIGHT: Day-wise average across cities
# --------------------------------------------------------
day_wise_avg = np.mean(temperature_data, axis=1)
hottest_day_index = np.argmax(day_wise_avg)
coldest_day_index = np.argmin(day_wise_avg)
print(f"\n📆 Hottest day overall: {days[hottest_day_index]} with avg {day_wise_avg[hottest_day_index]:.2f}°C")
print(f"📆 Coolest day overall: {days[coldest_day_index]} with avg {day_wise_avg[coldest_day_index]:.2f}°C")

# --------------------------------------------------------
# 📊 Optional Plotting (enable if matplotlib is installed)
# --------------------------------------------------------
# import matplotlib.pyplot as plt
# for i in range(len(cities)):
#     plt.plot(days, temperature_data[:, i], marker='o', label=cities[i])
# plt.title("Daily Temperatures Across Cities")
# plt.xlabel("Day")
# plt.ylabel("Temperature (°C)")
# plt.legend()
# plt.grid(True)
# plt.tight_layout()
# plt.show()
