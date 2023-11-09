import numpy as np
import pandas as pd
from numpy.random import randn
np.random.seed(101)

#Series
labels = ['a','b','c']
my_list = [10, 20, 30]
arr = np.array([10,20,30])
d = {'a': 10, 'b': 20, 'c': 30}

series_by_list = pd.Series(data=my_list, index=labels)
series_by_np_array = pd.Series(arr, labels)
series_by_dict = pd.Series(d)

ser1 = pd.Series([1,2,3,4],index = ['USA', 'Germany','USSR', 'Japan'])
ser2 = pd.Series([1,2,5,4],index = ['USA', 'Germany','Italy', 'Japan'])
get_item_by_label = ser1['USA']
add_series = ser1 + ser2

#DataFrames
df = pd.DataFrame(randn(5,4),index='A B C D E'.split(),columns='W X Y Z'.split())
column_w = df['W']
columns_w_z = df[['W','Z']]
a_column_is_a_series = type(df['W'])

df['new'] = df['W'] + df['Y']
df_without_new_column = df.drop('new',axis=1) #Column isn't dropped from df, only value returned has dropped column
df.drop('new',axis=1,inplace=True) #Column now dropped in df
df_without_e_row = df.drop('E',axis=0)#Doesn't have inplace so df not effected

get_row_by_label = df.loc['A']
get_row_by_index = df.iloc[2]
value_at_row_col = df.loc['B','Y']
subset_of_rows_cols = df.loc[['A','B'],['W','Y']]

true_false_df = df > 0
df_with_only_true_values = df[df > 0]
only_show_rows_true_condition = df[df['W'] > 0]
above_df_different_column = df[df['W']>0]['Y']
above_df_different_columns = df[df['W']>0][['Y','X']]
above_df_complex_filter = df[(df['W']>0) & (df['Y'] > 1)]

df.reset_index() #reset index to 0,1,2,..,n
newind = 'CA NY WY OR CO'.split()
df['States'] = newind
df.set_index('States') #return df with new index
df.set_index('States',inplace=True) #set new index to df


outside = ['G1','G1','G1','G2','G2','G2']
inside = [1,2,3,1,2,3]
hier_index = list(zip(outside,inside))
hier_index = pd.MultiIndex.from_tuples(hier_index)
df = pd.DataFrame(randn(6,2),index=hier_index,columns=['A','B']) #Multi level index
multi_index_outside_selection = df.loc['G1']
multi_index_outside_inside_selection = df.loc['G1'].loc[1]
df.index.names = ['Group','Num'] #Name outside and inside index
get_section_outer = df.xs('G1') #Have to start with outer index if accessing without level
get_section_outer_inner = df.xs(['G1', 1])
get_section_by_level = df.xs(1,level='Num')