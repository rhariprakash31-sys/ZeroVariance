"""Debug database operations."""

from src.database import ExpenseDatabase
from src.models import Expense, ExpenseCategory, SpendingLevel
from datetime import datetime
from decimal import Decimal

db = ExpenseDatabase("debug_db.db")

# Add test expense
exp = Expense(
    description="Test expense",
    amount=Decimal("50.00"),
    category=ExpenseCategory.FOOD,
    date=datetime(2024, 8, 15),
    payment_method="cash"
)

print(f"Adding expense: {exp.description} on {exp.date}")
exp_id = db.add_expense(exp)
print(f"Expense ID: {exp_id}")

# Try to retrieve it
retrieved = db.get_expense(exp_id)
print(f"Retrieved: {retrieved}")

# Get by month
expenses_august = db.get_expenses_by_month(2024, 8)
print(f"August 2024 expenses: {len(expenses_august)}")
for e in expenses_august:
    print(f"  - {e.description}: ${e.amount} on {e.date}")

# Get summary
summary = db.get_monthly_summary(2024, 8)
print(f"August summary total: ${summary.total_spent}")

db.close()
