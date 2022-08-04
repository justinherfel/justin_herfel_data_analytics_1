# justin_herfel_data_analytics_1

Make sure matplotlib, pandas and numpy are installed on your computer.

*Read in data from a local csv, excel file, json, or any other file type.
    - I used an a file from the University of Virginia Weldon Cooper Center for Public Service (https://demographics.coopercenter.org/national-population-projections/). I converted that file to a CSV, which I placed in the assets folder in the Git repository. I converted the file so that the numbers would be converted to objects that I would have to clean, outlined in bullet point 2 below. (This is complete)

*Use built-in pandas or numpy functions to do things like remove 0's and null values where they don't belong in your dataset.
    - In the CSV dataset the numbers were read as objects due to commas. I placed code in the Python file to clean the commas out of the numbers, and the chart was able to be successfully read.
*Scrape one piece of data from anywhere on the internet and utilize it in your project.
    - I used a table from wikipedia (https://en.wikipedia.org/wiki/1920_United_States_census) to populate the data for the top 5 most populous states in the U.S. for the year 1920.

*Write custom functions to operate on your data.
    - I wrote a custom function of my data to show the overal percentage increase between the two dates that the census was taken. It simply takes the top 5 spots and calculates the increase in percentage for each spot for the 100-year period between 1920 and 2020.

*Make 2 basic plots with matplotlib, seaborn, or any other kind of visualization library that you think looks interesting.
    - I plotted two separate bar charts on top of each other. The top chart is the top 5 most populous states from 1920 and the bottom chart is the top 5 most populous states from 2020. The top chart has data pulled in from the wikipedia page, and the bottom chart has data pulled from the CSV file included in the assets folder in the Git repository.

*Interpret your data and graphical output.
    - It is interesting that the total increase in population for each of the 5 states is xx% for the 100-year period between 1920 and 2020.