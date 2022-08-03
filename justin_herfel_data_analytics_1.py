import matplotlib.pyplot as plt
import pandas as pd
import os

df = pd.read_csv(os.path.join(
  os.path.dirname(__file__), 'assets', 'NationalProjections_ProjectedTotalPopulation_2020_2040_Updated12_2018.csv'))

df['2020'] = df['2020'].str.replace(",", "")
df['2020'] = df['2020'].astype('int')
# print(df.dtypes)
population = df.nlargest(5, '2020')
print(population)


x_axis = population["State"]
y_axis = population["2020"]

plt.figure(figsize=(12,6))
plt.bar(x_axis, y_axis, color='green')
plt.xlabel('Top 5 States')
plt.ylabel('Population in Tens of Millions')
plt.title('Top 5 State Populations in 2020')
plt.show()





