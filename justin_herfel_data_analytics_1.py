import os
import matplotlib.pyplot as plt
import pandas as pd

def data_cleanup(df):
    for column in df:
        if column != "State" and df[column].dtype != 'int64':
            df[column] = df[column].str.replace(",", "")
            df[column] = df[column].astype('int')
    return df

def data_massage(df):
    for column in df:
        if df[column].dtype == 'int64':
            df[column] = df[column]/1000000
    return df

def percent_change(df):
    """Formula for finding percent increase (or decrease) between 2020 & 1920
    :param df: dataframe to calculate percentage change of data"""

    for i, row in df.iterrows():
        percentage_change = 0
        if row["2020"] > row["1920"]:
            percentage_change = ((row["2020"]-row["1920"])/row["1920"])*100
        elif row["2020"] < row["1920"]:
            percentage_change = -(((row["1920"]-row["2020"])/row["1920"])*100)
        df.at[i, 'percent_change'] = percentage_change
    return df

df = pd.read_csv(os.path.join(
    os.path.dirname(__file__), 'assets', 'NationalProjections_ProjectedTotalPopulation_2020_2040_Updated12_2018.csv'))

website_list = pd.read_html(
    'https://en.wikipedia.org/wiki/1920_United_States_census')
df_1920_pop = website_list[2]
df_1920_pop = df_1920_pop.sort_values(by=['State'], ignore_index=True)

data = {'State': df["State"],
        '1920': df_1920_pop["Population as of1920 census"],
        '2020': df["2020"],
        '2040': df["2040"]}

my_data = pd.DataFrame(data)
my_data = data_cleanup(my_data)
my_data["percent_change"] = " "
my_data = percent_change(my_data)
my_data = data_massage(my_data)

# Print the output.
print(my_data)

my_data["percent_change"] = my_data["percent_change"].astype('int')

data_1920 = my_data.nlargest(5, '1920')
data_2020 = my_data.nlargest(5, '2020')
data_2040 = my_data.nlargest(5, '2040')
data_percent_change = my_data.nlargest(5, 'percent_change')

x_axis1 = data_1920["State"]
y_axis1 = data_1920["1920"]

x_axis2 = data_2020["State"]
y_axis2 = data_2020["2020"]

x_axis3 = data_2040["State"]
y_axis3 = data_2040["2040"]

x_axis4 = data_percent_change["State"]
y_axis4 = data_percent_change["percent_change"]

# Layout 4x1
plt.figure(figsize=(12, 8))

plt.subplot(411)
plt.bar(x_axis1, y_axis1, color='blue')
plt.xlabel('Top 5 States')
plt.ylabel('Population in Millions')
plt.title('Top 5 States by Population in 1920 (Plot 1)')

plt.subplot(412)
plt.bar(x_axis2, y_axis2, color='green')
plt.xlabel('Top 5 States')
plt.ylabel('Population in Millions')
plt.title('Top 5 States by Population in 2020 (Plot 2)')

plt.subplot(413)
plt.bar(x_axis3, y_axis3, color='purple')
plt.xlabel('Top 5 States')
plt.ylabel('Population in Millions')
plt.title('Top 5 States by Projected Population in 2040 (Plot 3)')

plt.subplot(414)
plt.bar(x_axis4, y_axis4, color='red')
plt.xlabel('Top 5 States')
plt.ylabel('Percentage Change')
plt.title("Top 5 States by Percentage Change from 1920 to 2020 (Plot 4)")

plt.tight_layout()
plt.show()
