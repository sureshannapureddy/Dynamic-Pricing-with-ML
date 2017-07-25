import os
import pandas as pd
import numpy as np

df_raw = pd.read_csv(‘Vendor_Data.csv’)
#print(df_raw.head())
#print(df_raw.describe())
print(‘Matrix:’,df_raw.shape,’\n’)

increment = np.zeros(df_raw.shape[0], dtype=np.float64)
#print(increment)

# This function will get us the overall revenue for the given increment vector def find_rev(increment):
print(‘find rev function!!!’, round(increment[1],5))
price = df_raw[“Avg_Price_per_unit”] * (1 + increment)
volumes = df_raw[“Average_units_sold”] * (1 – (df_raw[“Increase_sale_volume”] * increment * 10))
multiplier = 1 – (df_raw[“Incremental_acquisition”] * increment * 10)
total_multiplier = np.prod(multiplier)
profit_wo_multiplier = 0.05 * (np.sum(price*volumes) – np.sum(volumes * df_raw[“Cost_per_unit”]))
profit_w_multiplier = total_multiplier * profit_wo_multiplier
net_profit = np.sum(profit_w_multiplier)
return net_profit

#This function tries to get the next best increment vector def incremental_new(initial_increments):
initial_rev = find_rev(initial_increments)
intermediate_rev = 0

for i in range(0,250):
print(‘CURRENT I’, i, increments)
increments = initial_increments

print(‘increments[i]’,increments[i],’initial_increments[i]’,initial_increments[i])
if increments[i] > -0.099:
print(“yes1”)
increments[i] = (increments[i] – 0.011) #0.01
print(“new i1”, increments[i])
rev = find_rev(increments)
#print(‘rev’,rev)
#final_increments = 0
if rev > initial_rev:
final_increments = increments
intermediate_rev = rev
if increments[i] np.max(initial_rev) or rev > np.max(intermediate_rev):
final_increments = increments

print(‘final’,final_increments)
return final_increments

flag = 0
increment_i = increment
#flag = 1 is a condition when the increment vector remains the same

while flag == 0:
print(‘Initial overall profit:’,find_rev(increment_i))
increment_iplus1 = incremental_new(increment_i)
if min(increment_iplus1) == min(increment_i):
if min(increment_iplus1) == 1:
flag = 1
increment_i = increment_iplus1

print(‘Product changes’, increment_i)
print(‘New net profit’,find_rev(increment_i)) print(‘Old net profit’,find_rev(increment)) price = increment_i

# optional save price as excel file
