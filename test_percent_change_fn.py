# importing pandas as pd
import pandas as pd

# sample_2020 = [40438640, 29604099,21877257,20031150,12844885]
# sample_1920 = [10385227,8720017,6485280,5759394,4663228]

# def percentChange (startPoint, currentPoint):
#     return ((float(currentPoint)-startPoint)/abs(startPoint))*100

# for eachN in sample_2020:
#     pc = percentChange(sample_2020[0], eachN)
#     print(eachN, '||', pc)
  
# Creating the time-series index
ind = pd.date_range('01/01/2000', periods = 6, freq ='W')

# Creating the dataframe 
df = pd.DataFrame({"A":[14, 4, 5, 4, 1, 55],
                   "B":[5, 2, None, 3, 2, 32], 
                   "C":[20, 20, 7, 21, 8, None],
                   "D":[14, None, 6, 2, 6, 4]}, index = ind)
  
# apply the pct_change() method
# we use the forward fill method to
# fill the missing values in the dataframe
df.pct_change(fill_method ='ffill')
print(df.pct_change)