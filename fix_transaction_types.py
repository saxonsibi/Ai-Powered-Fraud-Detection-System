# fix_transaction_types.py

import os
import django

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "fraud_detection_api.settings")  # Adjust if your project settings name is different
django.setup()

from fraud.models import Transaction  # Adjust 'fraud' if your app is named differently

# Define mapping of old numeric values to correct type strings
type_mapping = {
    0.0: 'PAYMENT',
    1.0: 'TRANSFER',
    2.0: 'CASH_OUT',
    3.0: 'CASH_IN',
    4.0: 'DEBIT'
}

def fix_types():
    updated = 0
    for txn in Transaction.objects.all():
        try:
            if isinstance(txn.type, (int, float)) and txn.type in type_mapping:
                print(f"Fixing Transaction ID {txn.id} from {txn.type} to {type_mapping[txn.type]}")
                txn.type = type_mapping[txn.type]
                txn.save()
                updated += 1
        except Exception as e:
            print(f"Error fixing Transaction ID {txn.id}: {e}")
    print(f"\n✅ Fixed {updated} transactions.")

if __name__ == "__main__":
    fix_types()
