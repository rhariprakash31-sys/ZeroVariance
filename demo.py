"""Complete demo of the AI Expense Tracker."""

from src.database import ExpenseDatabase
from src.payment_integrations import get_payment_provider
from src.models import Expense, ExpenseCategory, SpendingLevel
from datetime import datetime
from decimal import Decimal
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()

# Initialize
print("\n" + "="*60)
print("🚀 AI EXPENSE TRACKER - COMPLETE DEMO")
print("="*60)

db = ExpenseDatabase("demo_expenses.db")

# Step 1: Import from Payment App
console.print("\n[bold cyan]Step 1: Importing transactions from Mock Payment App[/bold cyan]")
provider = get_payment_provider("mock")
transactions = provider.get_transactions(
    datetime(2024, 8, 1),
    datetime(2024, 8, 31)
)

for trans in transactions:
    db.add_expense(trans)
    console.print(f"  ✓ {trans.description} - ${trans.amount} ({trans.category})")

# Step 2: Add manual expenses
console.print("\n[bold cyan]Step 2: Adding manual expenses[/bold cyan]")
manual_expenses = [
    Expense(
        description="Lunch at restaurant",
        amount=Decimal("28.50"),
        category=ExpenseCategory.FOOD,
        spending_level=SpendingLevel.IMPORTANT,
        date=datetime(2024, 8, 15, 13, 0),
        payment_method="cash"
    ),
    Expense(
        description="Monthly gym subscription",
        amount=Decimal("49.99"),
        category=ExpenseCategory.HEALTH,
        spending_level=SpendingLevel.IMPORTANT,
        date=datetime(2024, 8, 5),
        payment_method="credit_card"
    ),
    Expense(
        description="Electronics gadget",
        amount=Decimal("89.99"),
        category=ExpenseCategory.SHOPPING,
        spending_level=SpendingLevel.UNNECESSARY,
        date=datetime(2024, 8, 20),
        payment_method="credit_card"
    ),
]

for exp in manual_expenses:
    db.add_expense(exp)
    console.print(f"  ✓ {exp.description} - ${exp.amount} ({exp.category})")

# Step 3: Set budget limits
console.print("\n[bold cyan]Step 3: Setting monthly budget limits[/bold cyan]")
budgets = {
    ExpenseCategory.FOOD: Decimal("300"),
    ExpenseCategory.TRANSPORT: Decimal("150"),
    ExpenseCategory.SUBSCRIPTION: Decimal("100"),
    ExpenseCategory.SHOPPING: Decimal("200"),
    ExpenseCategory.HEALTH: Decimal("100"),
}

for category, limit in budgets.items():
    db.set_budget_limit(category, "2024-08", limit)
    console.print(f"  ✓ {category.value}: ${limit}")

# Step 4: Generate monthly summary
console.print("\n[bold cyan]Step 4: Monthly Summary Report[/bold cyan]")
summary = db.get_monthly_summary(2024, 8)

# Create summary table
table = Table(title="📊 August 2024 Summary", show_header=True, header_style="bold")
table.add_column("Metric", style="cyan")
table.add_column("Value", justify="right", style="green")

table.add_row("Total Spent", f"${summary.total_spent:.2f}")
table.add_row("", "")
table.add_row("[bold]By Category:[/bold]", "")
for cat, amount in sorted(summary.total_by_category.items(), key=lambda x: x[1], reverse=True):
    table.add_row(f"  {cat}", f"${amount:.2f}")

table.add_row("", "")
table.add_row("[bold]Spending Classification:[/bold]", "")
table.add_row("  Essential", f"${summary.essential_vs_unnecessary['essential']:.2f}")
table.add_row("  Unnecessary", f"${summary.essential_vs_unnecessary['unnecessary']:.2f}")

console.print(table)

# Step 5: Budget Analysis
console.print("\n[bold cyan]Step 5: Budget Analysis[/bold cyan]")
budget_table = Table(title="💰 Budget vs Actual", show_header=True, header_style="bold")
budget_table.add_column("Category", style="cyan")
budget_table.add_column("Budget", justify="right")
budget_table.add_column("Spent", justify="right")
budget_table.add_column("Used %", justify="right")
budget_table.add_column("Status", justify="center")

for category, limit in budgets.items():
    spent = summary.total_by_category.get(category.value, Decimal("0"))
    pct = (spent / limit * 100) if limit > 0 else 0
    status = "✓ OK" if spent <= limit else "⚠️ OVER"
    status_color = "green" if spent <= limit else "red"
    
    budget_table.add_row(
        category.value,
        f"${limit:.2f}",
        f"${spent:.2f}",
        f"{pct:.1f}%",
        f"[{status_color}]{status}[/{status_color}]"
    )

console.print(budget_table)

# Step 6: Insights
console.print("\n[bold cyan]Step 6: AI Insights[/bold cyan]")
if summary.insights:
    for insight in summary.insights:
        console.print(f"  📈 {insight}")
else:
    console.print("  No special insights for this month")

# Step 7: Recommendations
console.print("\n[bold cyan]Step 7: Recommendations[/bold cyan]")
if summary.recommendations:
    for i, rec in enumerate(summary.recommendations, 1):
        console.print(f"  {i}. {rec}")
else:
    console.print("  Keep up your current spending patterns!")

# Summary Panel
console.print(Panel(
    f"[bold green]✓ Demo Complete![/bold green]\n\n"
    f"📊 Total Expenses: {len(db.get_expenses_by_month(2024, 8))}\n"
    f"💰 Total Spent: ${summary.total_spent:.2f}\n"
    f"⚖️ Essential: ${summary.essential_vs_unnecessary['essential']:.2f}\n"
    f"🛍️ Unnecessary: ${summary.essential_vs_unnecessary['unnecessary']:.2f}",
    title="[bold cyan]Summary[/bold cyan]"
))

db.close()
print("\n" + "="*60 + "\n")
