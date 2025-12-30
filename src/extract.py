import boto3
import pandas as pd
from io import StringIO

def extract_from_s3(bucket_name, file_key, aws_access_key_id, aws_secret_access_key):
    """
    Extrae un CSV desde un bucket S3 y devuelve un DataFrame.
    """
    s3_client = boto3.client(
        's3',
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key
    )
    
    csv_obj = s3_client.get_object(Bucket=bucket_name, Key=file_key)
    body = csv_obj['Body'].read().decode('utf-8')
    
    df = pd.read_csv(StringIO(body))
    print(f"Datos extraídos: {df.shape[0]} filas y {df.shape[1]} columnas")
    return df

if __name__ == "__main__":
    # Test de extracción
    BUCKET_NAME = "tu-bucket"
    FILE_KEY = "raw/data.csv"
    AWS_ACCESS_KEY_ID = "TU_ACCESS_KEY"
    AWS_SECRET_ACCESS_KEY = "TU_SECRET_KEY"
    
    df = extract_from_s3(BUCKET_NAME, FILE_KEY, AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY)
    print(df.head())
