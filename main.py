from src.extract import extract_from_s3
from src.transform import transform_data
from src.load import load_to_csv

BUCKET_NAME = "tu-bucket"
FILE_KEY = "raw/data.csv"
AWS_ACCESS_KEY_ID = "TU_ACCESS_KEY"
AWS_SECRET_ACCESS_KEY = "TU_SECRET_KEY"

df_raw = extract_from_s3(BUCKET_NAME, FILE_KEY, AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY)
df_transformed = transform_data(df_raw)
load_to_csv(df_transformed, "processed/data_final.csv")
