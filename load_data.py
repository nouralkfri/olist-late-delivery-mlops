import pandas as pd
from sqlalchemy import create_engine
import glob, os

engine = create_engine("postgresql://nour:olist123@localhost:5432/olist")

for path in glob.glob("./archive/*.csv"):
    table_name = os.path.basename(path).replace(".csv", "")
    df = pd.read_csv(path)
    df.to_sql(table_name, engine, if_exists="replace", index=False)
    print(f"loaded {table_name}: {len(df)} rows")

print("done!")