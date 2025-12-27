import pandas as pd 
from datetime import datetime, timedelta
import random

data = []

for i in range(1, 150000):
    data.append({
        "order_id": i,
        "customer_id": random.randint(1, 10),
        "order_date": datetime.now().strftime("%Y-%m-%d"),
        "product": random.choice(["Laptop", "Phone", "Tablet"]),
        "quantity": random.randint(1, 5),
        "price": random.randint(200, 1200),
        "country": random.choice(["USA", "Canada", "Mexico"])
    })

    df = pd.DataFrame(data)
    df.to_csv("data/orders.csv", index=False)