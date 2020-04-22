import pandas as pd
#读取表单
df = pd.read_excel('abc.xls',sheet_name=0) #可以通过sheet_name来指定读取的表单，其值可以是索引，也可以是表单名
data = df.head()#默认读取前5行的数据
#读取指定行
data = df.iloc[0].values[3] #0表示第一行，这里读取数据并不包含表头
#读取指定的多行，数据会存在嵌套的列表里面
data = df.iloc[[1,2]].values
#读取指定的行列
data = df.iloc[1,2] #读取第一行第二列的值
#读取指定的多行多列值
data = df.loc[[1,2],['个人名称','证件号码']].values
#读取所有行的指定列
data = df.loc[:,['个人名称','证件号码']].values
#获取行号并输出
print("行号",df.index.values)
print("列名",df.columns.values)
#获取指定行数的值
print(df.sample(3).values)

print("获取到所有的值：\n{0}".format(data))
