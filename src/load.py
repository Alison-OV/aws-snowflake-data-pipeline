import snowflake.connector

def load_to_snowflake(df):
    print("Loading data into Snowflake...")

    conn = snowflake.connector.connect(
        user="_USER",
        password="_PASSWORD",
        account="_ACCOUNT",
        warehouse="_WH",
        database="_DB",
        schema="PUBLIC"
    )

    cursor = conn.cursor()

    for _, row in df.iterrows():
        cursor.execute("""
            INSERT INTO SALES VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
        """, tuple(row))

    cursor.close()
    conn.close()
