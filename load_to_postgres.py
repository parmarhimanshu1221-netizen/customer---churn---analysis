import pandas as pd
from sqlalchemy import create_engine

# Update the password below to match what you set during PostgreSQL install
engine = create_engine("postgresql://neondb_owner:npg_VvLc0kKrJO6R@ep-lively-art-b5zofvd4-pooler.c-7.us-east-2.aws.neon.tech/neondb?sslmode=require&channel_binding=require")

df = pd.read_csv("data/raw/telco_data.csv")
df.to_sql("customers", engine, if_exists="replace", index=False)

print(f"Loaded {len(df)} rows into churn_db.customers")
