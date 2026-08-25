"""Quick CLI test - non-interactive demo."""

from src.cli import ExpenseTrackerCLI
from src.database import ExpenseDatabase
from src.models import Expense, ExpenseCategory, SpendingLevel
from datetime import datetime
from decimal import Decimal

# Create a fresh database for demo
db = ExpenseDatabase("cli_demo.db")

# Add some test expenses
print("=" * 60)
print("AI EXPENSE TRACKER - CLI DEMO")
print("=" * 60)

test_expenses = [
    ("Coffee at Starbucks", Decimal("5.50"), ExpenseCategory.FOOD),
    ("Monthly Netflix", Decimal("15.99"), ExpenseCategory.SUBSCRIPTION),
    ("Gas for car", Decimal("45.00"), ExpenseCategory.TRANSPORT),
    ("Grocery shopping", Decimal("78.50"), ExpenseCategory.FOOD),
    ("Gym membership", Decimal("49.99"), ExpenseCategory.HEALTH),
    ("Movie tickets", Decimal("25.00"), ExpenseCategory.ENTERTAINMENT),
]

print("\n📝 Adding expenses...")
for desc, amount, category in test_expenses:
    exp = Expense(
        description=desc,
        amount=amount,
        category=category,
        date=datetime(2024, 8, 15),  # Use consistent date
        payment_method="credit_card"
    )
    db.add_expense(exp)
    print(f"  ✓ {desc}: ${amount}")

# Show summary
print("\n📊 Monthly Summary (August 2024):")
summary = db.get_monthly_summary(2024, 8)

print(f"\nTotal Spent: ${summary.total_spent:.2f}")
print("\nBy Category:")
for cat, amount in sorted(summary.total_by_category.items(), key=lambda x: x[1], reverse=True):
    print(f"  • {cat}: ${amount:.2f}")

print("\nSpending Classification:")
print(f"  • Essential: ${summary.essential_vs_unnecessary['essential']:.2f}")
print(f"  • Unnecessary: ${summary.essential_vs_unnecessary['unnecessary']:.2f}")

print("\n💡 Insights:")
if summary.insights:
    for insight in summary.insights:
        print(f"  • {insight}")
else:
    print("  • No special insights")

print("\n🎯 Recommendations:")
# Generate recommendations using AI agent
from src.ai_agent import ExpenseAIAgent
ai = ExpenseAIAgent()
recommendations = ai.analyze_monthly_spending(summary)
for i, rec in enumerate(recommendations, 1):
    print(f"  {i}. {rec}")

# Show savings opportunity
savings_tip = ai.get_savings_opportunity(summary)
if savings_tip:
    print(f"\n💰 {savings_tip}")

db.close()
print("\n" + "=" * 60)
print("✓ Demo completed successfully!")
print("=" * 60)
