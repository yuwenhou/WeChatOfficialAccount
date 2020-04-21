import pandas as pd

file_name = 'python_book2.csv'

df = pd.read_csv(file_name, encoding='utf-8')
print(df)
# df.to_csv('zhihu_book.csv',encoding="utf_8_sig")