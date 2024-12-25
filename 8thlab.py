

# Lab 8- NUMPY AND MULTIDIMENSIONAL ARRAYS

# Q1. You are given a dataset that contains daily COVID-19 cases for five countries over a 7-day period. Each row represents a day, and each column represents a country. The data is as follows:
# covid_data = np.array([ [1500, 2000, 1800, 1200, 900], # Day 1 
# [1600, 2100, 1900, 1300, 950], 	# Day 2 
# [1700, 2200, 2000, 1400, 1000], 	# Day 3 
# [1650, 2150, 1950, 1350, 980], 	# Day 4 
# [1750, 2250, 2050, 1450, 1020], 	# Day 5 
# [1800, 2300, 2100, 1500, 1050], 	# Day 6 
# [1900, 2400, 2200, 1600, 1100], 	# Day 7 
# ])
# Each column corresponds to:
# Country 1: Country_A
# Country 2: Country_B
# Country 3: Country_C
# Country 4: Country_D
# Country 5: Country_E
# Perform following tasks:
# Basic Statistics:
# Calculate the total number of cases reported in each country over the 7 days.
# Determine the country with the highest total cases.
# Daily Analysis:
# Calculate the average number of cases reported per day across all countries.
# Identify the day with the highest total number of cases across all countries.
# Trends:
# Calculate the percentage increase or decrease in cases for each country from Day 1 to Day 7.
# Find the country with the highest percentage increase.
# Data Transformation:
# Normalize the data (scale all values between 0 and 1) for each country to compare trends more effectively.
# Provide the normalized dataset.
# Visualize the data:
# A line chart showing daily cases for each country
# Highlight the day with the highest total cases across all countries using an annotation or marker.


import numpy as np
import matplotlib.pyplot as plt

# Dataset
covid_data = np.array([
    [1500, 2000, 1800, 1200, 900],  # Day 1
    [1600, 2100, 1900, 1300, 950],  # Day 2
    [1700, 2200, 2000, 1400, 1000],  # Day 3
    [1650, 2150, 1950, 1350, 980],  # Day 4
    [1750, 2250, 2050, 1450, 1020],  # Day 5
    [1800, 2300, 2100, 1500, 1050],  # Day 6
    [1900, 2400, 2200, 1600, 1100],  # Day 7
])

countries = ["Country_A", "Country_B", "Country_C", "Country_D", "Country_E"]

# Basic Statistics
total_cases_per_country = np.sum(covid_data, axis=0)
highest_total_country = countries[np.argmax(total_cases_per_country)]

# Daily Analysis
average_cases_per_day = np.mean(covid_data, axis=1)
highest_total_day = np.argmax(np.sum(covid_data, axis=1)) + 1

# Trends
percentage_change = ((covid_data[-1] - covid_data[0]) / covid_data[0]) * 100
highest_percentage_increase_country = countries[np.argmax(percentage_change)]

# Data Transformation: Normalization
min_values = np.min(covid_data, axis=0)
max_values = np.max(covid_data, axis=0)
normalized_data = (covid_data - min_values) / (max_values - min_values)

# Visualization
plt.figure(figsize=(12, 6))

# Line chart for daily cases
for i, country in enumerate(countries):
    plt.plot(range(1, 8), covid_data[:, i], label=country, marker='o')

# Highlight the day with the highest total cases
highest_day_total_cases = np.argmax(np.sum(covid_data, axis=1))
plt.axvline(x=highest_day_total_cases + 1, color='red', linestyle='--', alpha=0.7, label="Highest Total Cases Day")
plt.annotate(f'Day {highest_day_total_cases + 1}',
             xy=(highest_day_total_cases + 1, np.max(np.sum(covid_data, axis=1))),
             xytext=(highest_day_total_cases + 1.5, np.max(np.sum(covid_data, axis=1)) + 500),
             arrowprops=dict(facecolor='black', arrowstyle='->'))

# Chart settings
plt.title("Daily COVID-19 Cases for Each Country")
plt.xlabel("Day")
plt.ylabel("Number of Cases")
plt.legend()
plt.grid(True)
plt.tight_layout()

# Display visualization
plt.show()

# Results
total_cases_per_country, highest_total_country, average_cases_per_day, highest_total_day, percentage_change, highest_percentage_increase_country, normalized_data
