# justin_herfel_data_analytics_1

## Before running this project, please make sure os, matplotlib and pandas are installed on your computer.

1. *Read in data from a local csv, excel file, json, or any other file type.*
    - I used an Excel file from the University of Virginia Weldon Cooper Center for Public Service (https://demographics.coopercenter.org/national-population-projections/). Initially I converted the .xlsx file to .csv for practice purposes, but decided to use the .csv for the final project for reasons outline below.

2. *Use built-in pandas or numpy functions to do things like remove 0's and null values where they don't belong in your dataset.*
    - In the .csv dataset, the numbers contained commas due to the conversion process from .xlsx. I placed code in the Python file to clean the commas out of the numbers without changing the source data.
* *Scrape one piece of data from anywhere on the internet and utilize it in your project.*
    - I used a table from wikipedia (https://en.wikipedia.org/wiki/1920_United_States_census) to populate the top 5 most populous states in the U.S. for the year 1920.

3. *Write custom functions to operate on your data.*
    - There is a custom function that determines the percent change in population for two sets of data: 1920 and 2020 top 5 states. This is shown in Plot 4, the fourth bar graph where we see the states with the largest population growth as a percent over a 100-year period.

4. *Make 2 basic plots with matplotlib, seaborn, or any other kind of visualization library that you think looks interesting.*
    - I plotted 4 separate bar charts stacked on top of each other. The first chart shows the top 5 most populous states in 1920, the second chart shows the top 5 most populous states in 2020, and the third chart shows the top 5 projected most populous states in 2040. Finally, the fourth chart shows the top 5 states in terms of most percentage change in population from 1920 to 2020. This was done with matplotlib.

5. *Interpret your data and graphical output.*
    - From Plot 1 to Plot 2, we see New York fall from #1 to #4, and Pennsylvania falls from #2 to #5. Illinois and Ohio are at #3 and #4 in 1920 but fall out of the top 5 completely by 2020. We see California appear at #1 and Florida at #3 in 2020. Also, we see a sizeable increase in population for the state of Texas, as it moves from #5 to #2. So between 1920 and 2020, 3 states remain in the top 5, with only one of those states increasing its' ranking (Texas).
    - From Plot 2 to Plot 3, there is no change in ranking for the first 4 states, and the population has increased for each of those states. However, Pennsylvania falls out of the list, replaced by Georgia.
    - From Plot 3 to Plot 4, for me, was the most unexpected result. In terms of percentage change of population, which measures the percent of change from 1920 to 2020 for each state, only 2 of the 5 states in Plots 2 and 3 appear in this chart, and none of the states in Plot 1 appear in this chart. While California is ranked number 1 in Plots 2 and 3, it's ranked 5th in terms of population growth as a percentage from 1920 to 2020. Florida ranks #2 in growth and #3 in the top 5 population number for the previous two plots. #1 Nevada has seen incredible growth over the last 100 years, at almost 4000%! The next closest state is Florida, with a roughly 2000% growth and Arizona running a very close third place. At 4th place we have Alaska with a nearly 2000% growth, followed by California at #5, trailing Alaska only slighly.
    - What does this say to me? It seems the population is growing more in southern states than northern states, with the excepion of Alaska. Also, it also shows an increase of population to the western United States, with the exception of Florida. Overall, the U.S. population is trending south and west.
    - I find it notable that even though the largest population increase is centered in southern and western states, Alaska stands out as being the northernmost state in the U.S., and yet is ranked fourth in percentage change. Also, Florida stands out as being one of the easternmost states in the country and stands at #3 on the list.