"""Test payment integrations."""

from src.payment_integrations import get_payment_provider
from datetime import datetime, timedelta

# Test mock provider
print("Testing Mock Payment Provider...")
provider = get_payment_provider("mock")

start_date = datetime(2024, 8, 1)
end_date = datetime(2024, 8, 31)

transactions = provider.get_transactions(start_date, end_date)

print(f"\nFetched {len(transactions)} transactions:")
for i, trans in enumerate(transactions, 1):
    print(f"  {i}. {trans.description} - ${trans.amount} ({trans.category}) - {trans.date.strftime('%Y-%m-%d')}")

print("\n✓ Payment integration test completed!")
