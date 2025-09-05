#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from datetime import datetime
from clickhouse_driver import Client


# In[15]:


API_KEY = "e8aa8ff928f9028b27294ce00aa89c80"
CLICKHOUSE_HOST = 'localhost'   # or IP of server
CLICKHOUSE_PORT = 9000        # integer, not string
CLICKHOUSE_USER = 'sahil'
CLICKHOUSE_PASSWORD = '123'


# In[16]:


from clickhouse_driver import Client

client = Client(
    host=CLICKHOUSE_HOST,
    port=CLICKHOUSE_PORT,
    user=CLICKHOUSE_USER,
    password=CLICKHOUSE_PASSWORD
)

data = client.execute("SELECT * FROM weather_forecast2") 


# In[17]:


import pandas as pd

columns = ["country", "forecast_time", "temperature", "weather", "humidity", "wind_speed", "created_at"]

df = pd.DataFrame(data, columns=columns)

print(df.head())


# In[5]:


get_ipython().system('pip install matplotlib')


# In[18]:


import matplotlib.pyplot as plt
import numpy as np

df_plot = df.head(10)

x = np.arange(len(df_plot))  # the label locations
width = 0.25  # width of the bars

plt.figure(figsize=(15,6))


plt.bar(x - width, df_plot['temperature'], width, color='skyblue', label='Temperature (°C)')
plt.bar(x, df_plot['humidity'], width, color='lightgreen', label='Humidity (%)')
plt.bar(x + width, df_plot['wind_speed'], width, color='salmon', label='Wind Speed (m/s)')

plt.xlabel('Forecast Time')              
plt.ylabel('Values')
plt.title('Weather Data Bar Chart')
plt.xticks(x, [t.strftime('%Y-%m-%d %H:%M') for t in df_plot['forecast_time']], rotation=45)
plt.legend(frameon=True, edgecolor='black', shadow=True)


plt.grid(axis='y', linestyle='--', alpha=0.5)

for i in range(len(df_plot)):
    plt.text(i - width, df_plot['temperature'][i] + 0.5, f"{df_plot['temperature'][i]:.1f}", ha='center', fontsize=9)
    plt.text(i, df_plot['humidity'][i] + 0.5, f"{df_plot['humidity'][i]:.0f}", ha='center', fontsize=9)
    plt.text(i + width, df_plot['wind_speed'][i] + 0.1, f"{df_plot['wind_speed'][i]:.1f}", ha='center', fontsize=9)

plt.tight_layout()
plt.show()


# In[8]:


icecream_data = client.execute("SELECT * FROM icecream_sales")


# In[19]:


query = """
SELECT 
    w.City,
    corr(w.Temperature, s.SaleAmount) AS correlation
FROM weather_forecast2 AS w
JOIN icecream_sales AS s
ON w.City = s.City
GROUP BY w.City
ORDER BY correlation DESC;                
"""

# Execute query
icecream_data = client.execute(query)    

# Load into Pandas DataFrame
df_corr = pd.DataFrame(icecream_data, columns=['City', 'Correlation'])
print(df_corr)


# In[ ]:





# In[20]:


query = """
WITH monthly_country AS (
    SELECT
        Country,
        Month,
        TotalRevenue,
        AvgRevenuePerCity
    FROM country_monthly_revenue
),
ranked_country AS (
    SELECT
        *,
        RANK() OVER (PARTITION BY Month ORDER BY TotalRevenue DESC) AS RevenueRank
    FROM monthly_country
),
cumulative_country AS (
    SELECT
        Country,
        Month,
        TotalRevenue,
        AvgRevenuePerCity,
        RevenueRank,
        SUM(TotalRevenue) OVER (PARTITION BY Country ORDER BY Month) AS CumulativeRevenue
    FROM ranked_country
)
SELECT *
FROM cumulative_country
ORDER BY Month, RevenueRank;
"""

# Execute query
country_data = client.execute(query)

# Load into Pandas DataFrame
df_country = pd.DataFrame(country_data, columns=[
    'Country', 'Month', 'TotalRevenue', 'AvgRevenuePerCity', 'RevenueRank', 'CumulativeRevenue'
])
print(df_country)




# In[21]:


# -----------------------------
# Plot: Total Revenue per Month by Country
plt.figure(figsize=(12,6))
for country in df_country['Country'].unique():
    df_plot = df_country[df_country['Country'] == country]
    plt.plot(df_plot['Month'], df_plot['TotalRevenue'], marker='o', label=country)

plt.xlabel('Month')
plt.ylabel('Total Revenue')
plt.title('Monthly Total Revenue per Country')
plt.xticks(rotation=45)
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()


# In[22]:


plt.figure(figsize=(12,6))
for country in df_country['Country'].unique():
    df_plot = df_country[df_country['Country'] == country]
    plt.plot(df_plot['Month'], df_plot['CumulativeRevenue'], marker='o', linestyle='--', label=country)

plt.xlabel('Month')
plt.ylabel('Cumulative Revenue')
plt.title('Cumulative Revenue per Country Over Time')
plt.xticks(rotation=45)
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()


# In[31]:


# ROI query per city per day
query = """
SELECT
    s.City,
    toDate(s.SaleDateTime) AS SaleDate,
    SUM(s.UnitsSold) AS TotalUnitsSold,
    SUM(s.SaleAmount) / SUM(s.UnitsSold) AS AvgPrice,
    SUM(s.SaleAmount) AS Revenue,
    (1000 / 10.0) * 1 AS DieselCost,
    SUM(s.SaleAmount) - ((1000 / 10.0) * 1) AS ROI
FROM icecream_sales s
JOIN weather_forecast2 w
    ON s.City = w.City
GROUP BY s.City, SaleDate
ORDER BY SaleDate, ROI DESC;
"""

# Execute query
data = client.execute(query)

# Load into Pandas DataFrame
df = pd.DataFrame(data, columns=[
    'City', 'SaleDate', 'TotalUnitsSold', 'AvgPrice', 'Revenue', 'DieselCost', 'ROI'
])

# Preview data
print(df.head())




# In[32]:


# -----------------------------
# Plot: ROI per city over days
plt.figure(figsize=(12,6))

for city in df['City'].unique():
    df_city = df[df['City'] == city]
    plt.plot(df_city['SaleDate'], df_city['ROI'], marker='o', label=city)

plt.xlabel('Date')
plt.ylabel('ROI')
plt.title('Daily ROI per City')
plt.xticks(rotation=45)
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()


# In[33]:


import matplotlib.pyplot as plt
import numpy as np

# Get unique dates and cities
dates = sorted(df['SaleDate'].unique())
cities = df['City'].unique()

# Set width for each bar
bar_width = 0.2
x = np.arange(len(dates))  # X-axis positions

plt.figure(figsize=(14,6))

# Plot bars for each city
for i, city in enumerate(cities):
    df_city = df[df['City'] == city].set_index('SaleDate').reindex(dates, fill_value=0)
    plt.bar(x + i*bar_width, df_city['ROI'], width=bar_width, label=city)

plt.xlabel('Date')
plt.ylabel('ROI')
plt.title('Daily ROI per City (Bar Chart)')
plt.xticks(x + bar_width*(len(cities)-1)/2, dates, rotation=45)
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()


# In[34]:


query = """
WITH country_revenue AS (
    SELECT
        w.City AS Country,  -- assuming City represents country
        SUM(s.SaleAmount) AS TotalRevenue
    FROM icecream_sales s
    JOIN weather_forecast2 w
        ON s.City = w.City
    GROUP BY w.City
)
SELECT
    Country,
    TotalRevenue,
    RANK() OVER (ORDER BY TotalRevenue DESC) AS RevenueRank
FROM country_revenue
ORDER BY RevenueRank;
"""

# Execute query
data = client.execute(query)

# Load into Pandas DataFrame
df = pd.DataFrame(data, columns=['Country', 'TotalRevenue', 'RevenueRank'])
print(df)


# In[36]:


import matplotlib.pyplot as plt

plt.figure(figsize=(10,6))
plt.bar(df['Country'], df['TotalRevenue'], color='skyblue')
plt.xlabel('Country')
plt.ylabel('Total Revenue')
plt.title('Total Ice Cream Revenue per Country')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

