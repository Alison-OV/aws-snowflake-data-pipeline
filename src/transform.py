import pandas as pd

def transform_data(df):
    """
    Aplica transformaciones al DataFrame:
    - Calcula columnas adicionales
    - Limpieza de datos
    - Preparación para carga
    """
    # Ejemplo: calcular TOTAL_AMOUNT si no existe
    if 'TOTAL_AMOUNT' not in df.columns and 'PRICE' in df.columns and 'QUANTITY' in df.columns:
        df['TOTAL_AMOUNT'] = df['PRICE'] * df['QUANTITY']
    
    # Ejemplo: convertir fechas
    if 'ORDER_DATE' in df.columns:
        df['ORDER_DATE'] = pd.to_datetime(df['ORDER_DATE'])
    
    # Ejemplo: limpieza de nulos
    df = df.fillna({'PRODUCT': 'Unknown', 'QUANTITY': 0, 'PRICE': 0.0, 'TOTAL_AMOUNT': 0.0})
    
    print(f"Transformación completa: {df.shape[0]} filas y {df.shape[1]} columnas")
    return df

if __name__ == "__main__":
    # Test rápido con un CSV local
    df = pd.read_csv("raw/data.csv")
    df_transformed = transform_data(df)
    print(df_transformed.head())
