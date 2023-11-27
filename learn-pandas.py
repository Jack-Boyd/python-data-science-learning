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
df.info()
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
xdf = pd.DataFrame(randn(6,2),index=hier_index,columns=['A','B']) #Multi level index
multi_index_outside_selection = xdf.loc['G1']
multi_index_outside_inside_selection = xdf.loc['G1'].loc[1]
xdf.index.names = ['Group','Num'] #Name outside and inside index
get_section_outer = xdf.xs('G1') #Have to start with outer index if accessing without level
get_section_outer_inner = xdf.xs(('G1', 1))
get_section_by_level = xdf.xs(1,level='Num')


incomplete_df = pd.DataFrame({'A':[1,2,np.nan], 'B':[5,np.nan,np.nan], 'C':[1,2,3]})
incomplete_df.dropna() #Drop rows with NA
incomplete_df.dropna(axis=1) #Drop cols with NA
incomplete_df.dropna(thresh=2) #Drop rows with 2 or more NA values
incomplete_df.fillna(value='FILL VALUE') #Replace NA with 'FILL VALUE'
incomplete_df['A'].fillna(value=incomplete_df['A'].mean()) #Specific logic


data = {'Company':['GOOG','GOOG','MSFT','MSFT','FB','FB'],
       'Person':['Sam','Charlie','Amy','Vanessa','Carl','Sarah'],
       'Sales':[200,120,340,124,243,350]}
g_df = pd.DataFrame(data)
by_comp = g_df.groupby('Company') #Creates DFGroupBy Object
by_comp.mean(numeric_only=True) #Agg funcitons
by_comp.std(numeric_only=True)
by_comp.min(numeric_only=True)
by_comp.max(numeric_only=True)
by_comp.count()
by_comp.describe() #Collection of agg functions displayed
by_comp.describe().transpose() #Displayed horizontally (easier to read)
by_comp.describe().transpose()['GOOG'] #Show specific companies collection

df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                    'B': ['B0', 'B1', 'B2', 'B3'],
                    'C': ['C0', 'C1', 'C2', 'C3'],
                    'D': ['D0', 'D1', 'D2', 'D3']},
                    index=[0, 1, 2, 3])

df2 = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'],
                    'B': ['B4', 'B5', 'B6', 'B7'],
                    'C': ['C4', 'C5', 'C6', 'C7'],
                    'D': ['D4', 'D5', 'D6', 'D7']},
                    index=[4, 5, 6, 7]) 
df3 = pd.DataFrame({'A': ['A8', 'A9', 'A10', 'A11'],
                    'B': ['B8', 'B9', 'B10', 'B11'],
                    'C': ['C8', 'C9', 'C10', 'C11'],
                    'D': ['D8', 'D9', 'D10', 'D11']},
                    index=[8, 9, 10, 11])

c_df = pd.concat([df1, df2, df3])
c_col_df = pd.concat([df1, df2, df3],axis=1) #Concat by columns
c_col_df = pd.concat([df1, df2, df3],axis=1,keys=['X','Y','Z']) #Add keys to columns

left = pd.DataFrame({'key1': ['K0', 'K0', 'K1', 'K2'],
                    'key2': ['K0', 'K1', 'K0', 'K1'],
                    'A': ['A0', 'A1', 'A2', 'A3'],
                    'B': ['B0', 'B1', 'B2', 'B3']})
right = pd.DataFrame({'key1': ['K0', 'K1', 'K1', 'K2'],
                      'key2': ['K0', 'K0', 'K0', 'K0'],
                      'C': ['C0', 'C1', 'C2', 'C3'],
                      'D': ['D0', 'D1', 'D2', 'D3']})

m_df = pd.merge(left, right, on=['key1', 'key2']) #Merge on single column
m_df2 = pd.merge(left, right, how='outer', on=['key1', 'key2']) #Merge on multiple columns outer join
m_m_df = pd.merge(left, right, how='right',on=['key1','key2']) #Merge on multiple columns right join
m_m_df = pd.merge(left, right, how='left',on=['key1','key2']) #Merge on multiple columns left join

j_left = pd.DataFrame({'A': ['A0', 'A1', 'A2'],
                      'B': ['B0', 'B1', 'B2']},
                      index=['K0', 'K1', 'K2']) 

j_right = pd.DataFrame({'C': ['C0', 'C2', 'C3'],
                      	'D': ['D0', 'D2', 'D3']},
                        index=['K0', 'K2', 'K3'])

left_join_right = j_left.join(j_right) #join
left_join_right_outer = j_left.join(j_right, how='outer') #outer join
left_join_right_inner = j_left.join(j_right, how='inner') #inner join
print(left_join_right_inner)


op = pd.DataFrame({'col1':[1,2,3,4],'col2':[444,555,666,444],'col3':['abc','def','ghi','xyz']})
op.head()
op['col2'].unique() #Unique values in column
op['col2'].nunique() #Number of unique values in column
op['col2'].value_counts() #Number of times each unique value appears in column

newdf = op[(op['col1']>2) & (op['col2']==444)] #Filtering

def times2(x):
  return x*2

op['col1'].apply(times2) #Apply function to column
op['col3'].apply(len) #Apply len function to column
op['col1'].sum() #Sum of column
del op['col1'] #Delete column
op.columns #Columns
op.index #Index
sorted = op.sort_values(by='col2') #Sort by column
isnull = op.isnull() #Check for null values
dropna = op.dropna() #Drop null values
nan = pd.DataFrame({'col1':[1,2,3,np.nan],
                   'col2':[np.nan,555,666,444],
                   'col3':['abc','def','ghi','xyz']})
nan.fillna(value='FILL VALUE') #Fill null values

data = {'A':['foo','foo','foo','bar','bar','bar'],
     'B':['one','one','two','two','one','one'],
       'C':['x','y','x','y','x','y'],
       'D':[1,3,2,5,4,1]}

pivot = pd.DataFrame(data)
pivot.pivot_table(values='D',index=['A', 'B'],columns=['C']) #Pivot table