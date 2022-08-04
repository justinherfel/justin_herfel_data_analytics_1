import os
import matplotlib.pyplot as plt
import pandas as pd


def data_cleanup(df):
    for column in df:
        if column != "State":
            # print(df[column])
            df[column] = df[column].str.replace(",", "")
            df[column] = df[column].astype('int')
    return df


def data_massage(df, column):
    df = df.nlargest(5, column)
    # Maybe create a separate function to go through and compare 1920 state data to 2020 state data
    # 2020/1920 = possible or google percentage change
    df[column] = df[column]/1000000
    return df

# Potential new formula for finding percent increase between 2020 & 1920
def percent_change(df, column):
    df[column] = df[column]
    pass

df = pd.read_csv(os.path.join(
    os.path.dirname(__file__), 'assets', 'NationalProjections_ProjectedTotalPopulation_2020_2040_Updated12_2018.csv'))

website_list = pd.read_html(
    'https://en.wikipedia.org/wiki/1920_United_States_census')
df_1920_pop = website_list[2]
df_1920_pop = data_massage(df_1920_pop, "Population as of1920 census")
print(df_1920_pop)
x_axis1 = df_1920_pop["State"]
y_axis1 = df_1920_pop["Population as of1920 census"]
# print(df.dtypes)

df = data_cleanup(df)

population2 = data_massage(df, "2020")
# print(population2)
x_axis2 = population2["State"]
y_axis2 = population2["2020"]
population_2040 = data_massage(df, '2040')
x_axis3 = population2["State"]
y_axis3 = population2["2040"]

# Layout 2x1
plt.figure(figsize=(12, 8))

plt.subplot(311)
plt.bar(x_axis1, y_axis1, color='green')
plt.xlabel('Top 5 States')
plt.ylabel('Population in Millions')
plt.title('Top 5 State Populations in 1920')

plt.subplot(312)
plt.bar(x_axis2, y_axis2, color='green')
plt.xlabel('Top 5 States')
plt.ylabel('Population in Millions')
plt.title('Top 5 State Populations in 2020')

plt.subplot(313)
plt.bar(x_axis3, y_axis3, color='green')
plt.xlabel('Top 5 States')
plt.ylabel('Population in Millions')
plt.title('Top 5 State Populations in 2040')

plt.show()
