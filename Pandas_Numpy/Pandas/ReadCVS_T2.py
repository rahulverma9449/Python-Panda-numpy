# import pandas as pd

# df = pd.read_csv('data1.csv')

# print(df)
# print(df.to_string())
# import pandas as pd

# pd.options.display.max_rows = 9999

# df = pd.read_csv('data.csv')

# print(df)
import pandas as pd

df = pd.read_json('data2.json')
df.dropna(inplace = True)
df["Calories"].fillna(130, inplace = True)

print(df.to_string())