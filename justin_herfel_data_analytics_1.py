import matplotlib.pyplot as plt
import pandas as pd
import os

df = pd.read_csv(os.path.join(
  os.path.dirname(__file__), 'assets', 'NationalProjections_ProjectedTotalPopulation_2020_2040_Updated12_2018.csv'))

website_list = pd.read_html('https://en.wikipedia.org/wiki/1920_United_States_census')
df_1920_state = website_list[1]
df_1920_pop = website_list[2]

# print(df_1920_pop.dtypes)
# print(df.dtypes)

df['2020'] = df['2020'].str.replace(",", "")
df['2020'] = df['2020'].astype('int')
population = df.nlargest(5, '2020')
print(population)
population["2020"] = population["2020"]/1000000
x_axis2 = population["State"]
y_axis2 = population["2020"]

# Layout 2x1
plt.figure(figsize=(12, 8))

plt.subplot(211)
# plt.bar(x_axis, y_axis, color='green')
# plt.xlabel('Top 5 States')
# plt.ylabel('Population in Millions')
# plt.title('Top 5 State Populations in 1920')

plt.subplot(212)
plt.bar(x_axis2, y_axis2, color='green')
plt.xlabel('Top 5 States')
plt.ylabel('Population in Millions')
plt.title('Top 5 State Populations in 2020')

plt.show()





