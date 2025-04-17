import pandas as pd
import mysql.connector

# Load your cleaned dataset
df = pd.read_csv("cleaned_fraud_data.csv")

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="django_user",
    password="django_user12345@#",
    database="fraud_detection_db"
)
cursor = conn.cursor()

# Insert into MySQL
for _, row in df.iterrows():
    cursor.execute("""
        INSERT INTO fraud_transaction (
            step, type, amount, oldbalanceOrg, newbalanceOrig,
            oldbalanceDest, newbalanceDest, isFlaggedFraud, isFraud
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        int(row['step']),
        row['type'],
        float(row['amount']),
        float(row['oldbalanceOrg']),
        float(row['newbalanceOrig']),
        float(row['oldbalanceDest']),
        float(row['newbalanceDest']),
        int(row['isFlaggedFraud']),
        int(row['isFraud']) if not pd.isna(row['isFraud']) else None
    ))

# Commit and close
conn.commit()
cursor.close()
conn.close()

print("Data successfully inserted into MySQL!")
