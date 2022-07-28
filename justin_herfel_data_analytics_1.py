import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os

df = pd.read_csv(os.path.join(
  os.path.dirname(__file__), 'assets', 'NationalProjections_ProjectedTotalPopulation_2020_2040_Updated12_2018.csv'))

population = df.nlargest(5, '2040')
print(population)

x_axis = population["State"]
y_axis = population["2040"]

plt.figure(figsize=(12,6))
plt.bar(x_axis, y_axis, color='green')
plt.xlabel('Top 5 States')
plt.ylabel('Population')
plt.title('Projected State Population by 2040')
plt.show()





