import pandas as pd
data ={'A':[10,20,30],'B':[2,5,0]}
df=pd.DataFrame(data)
df['add']=df['A']+df['B']
df['sub']=df['A']-df['B']
df['mul']=df['A']*df['B']
df['div']=df['A']/df['B'].replace(0,float('nan'))
df.to_excel('arithmetic_operations_result_with_nan.xlsx',index=False,na_rep="NaN")
print('arithematic oprations completed and saved to "arithmetic_operations_result_with_nan.xlsx"')