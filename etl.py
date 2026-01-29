import pandas as pd
from sqlalchemy import create_engine

df=pd.read_csv("sales.csv")
df["Order Date"]=pd.to_datetime(df["Order Date"],dayfirst=True)
df["Ship Date"]=pd.to_datetime(df["Ship Date"],dayfirst=True)
df["Sales"]=df["Sales"].astype(float)
df=df.dropna()

engine=create_engine("postgresql://postgres:postgres@localhost:5432/salesdb")
df.to_sql("sales",engine,if_exists="replace",index=False)
print("Superstore ETL completed successfully")