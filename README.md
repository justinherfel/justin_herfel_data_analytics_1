# justin_herfel_data_analytics_1

1. Make sure matplotlib, pandas and numpy are installed on your computer.

2. Read in data from a local csv, excel file, json, or any other file type.
    - I will use a csv file from which I will pull data to make a bar chart. So far I have acquired a dataset for 2020 through 2040. I am still looking for a data set for 1920 through 1940. (This is complete)
3. (Proposed Requirement) Use built-in pandas or numpy functions to do things like remove 0's and null values where they don't belong in your dataset.
    - My csv dataset is found at this link (https://demographics.coopercenter.org/sites/demographics/files/2019-01/NationalProjections_ProjectedTotalPopulation_2020-2040_Updated12-2018.xls). I converted this dataset into a CSV file. After doing this, Python wasn't able to read the numbers because commas had been inserted into the actual numbers. I'm going to write a function that ignores the commas and allows the data to be read into the charts. (This is not complete)
4. (Proposed Requirement) Make 2 basic plots with matplotlib, seaborn, or any other kind of visualization library that you think looks interesting.
    - I'm going to chart both time periods together, in two separate clustered bar chart series. The chart on the left will have a clustered bar chart with 1920, 1930 and 1940. Above each chart will be the clustered bars of each 5 states, showing the progression over each 10 year period of population growth and changes in the population growth. The chart on the right will have a similar layout with the years 2020, 2030 and 2040. (This is not complete)