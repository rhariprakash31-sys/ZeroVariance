"""Quick test of the expense tracker."""

from src.database import ExpenseDatabase
from src.models import Expense, ExpenseCategory, SpendingLevel
from datetime import datetime
from decimal import Decimal

# Initialize database
db = ExpenseDatabase("test_expenses.db")

# Add some sample expenses
expenses = [
    Expense(
        description="Coffee at Starbucks",
        amount=Decimal("5.50"),
        category=ExpenseCategory.FOOD,
        spending_level=SpendingLevel.IMPORTANT,
        date=datetime(2024, 8, 15, 10, 30),
        payment_method="credit_card",
    ),
    Expense(
        description="Uber ride to office",
        amount=Decimal("12.75"),
        category=ExpenseCategory.TRANSPORT,
        spending_level=SpendingLevel.ESSENTIAL,
        date=datetime(2024, 8, 15, 18, 45),
        payment_method="debit_card",
    ),
    Expense(
        description="Netflix subscription",
        amount=Decimal("15.99"),
        category=ExpenseCategory.SUBSCRIPTION,
        spending_level=SpendingLevel.UNNECESSARY,
        date=datetime(2024, 8, 1),
        payment_method="credit_card",
    ),
    Expense(
        description="Lunch at restaurant",
        amount=Decimal("28.50"),
        category=ExpenseCategory.FOOD,
        spending_level=SpendingLevel.IMPORTANT,
        date=datetime(2024, 8, 15, 13, 0),
        payment_method="cash",
    ),
]

# Add expenses to database
print("Adding sample expenses...")
for exp in expenses:
    exp_id = db.add_expense(exp)
    print(f"  Added: {exp.description} - ${exp.amount} ({exp.category})")

# Get monthly summary
print("\n=== Monthly Summary (2024-08) ===")
summary = db.get_monthly_summary(2024, 8)
print(f"Total Spent: ${summary.total_spent}")
print("\nBy Category:")
for cat, amount in summary.total_by_category.items():
    print(f"  {cat}: ${amount}")
print("\nEssential vs Unnecessary:")
print(f"  Essential: ${summary.essential_vs_unnecessary['essential']}")
print(f"  Unnecessary: ${summary.essential_vs_unnecessary['unnecessary']}")

db.close()
print("\n✓ Database test completed successfully!")
