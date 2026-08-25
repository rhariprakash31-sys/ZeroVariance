# 💰 AI Expense Tracker

An intelligent personal finance management system powered by Google Generative AI. Track expenses, get AI-powered categorization, receive spending suggestions, and manage your budget with smart insights.

## ✨ Features

### 🤖 AI-Powered Analysis
- **Automatic Categorization**: AI automatically categorizes expenses and assigns spending levels
- **Spending Insights**: Get monthly analysis of your spending patterns
- **Smart Recommendations**: Personalized suggestions to optimize your spending
- **Savings Opportunities**: Identify areas where you can save money

### 💳 Multi-Source Integration
- Manual expense entry
- Stripe payment integration
- PayPal transaction import
- Mock provider for testing

### 📊 Expense Tracking
- Track expenses by category (Food, Transport, Entertainment, Bills, Health, Shopping, etc.)
- Classify spending as Essential, Important, Unnecessary, or Waste
- Monthly and category-based summaries
- Recurring expense tracking

### 💰 Budget Management
- Set monthly budget limits per category
- Track spending against budgets
- Alert thresholds for overspending
- Budget progress visualization

### 🎯 Dual Interface
- **CLI Mode**: Command-line interface for quick operations
- **Web App**: Modern, responsive web interface with charts and visualizations

## 📋 Requirements

- Python 3.8+
- SQLite3
- Google Generative AI API Key
- Optional: Stripe/PayPal API credentials

## 🚀 Installation

1. Clone the repository:
```bash
git clone <repo-url>
cd ZeroVariance
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
```bash
# Create a .env file in the project root
GOOGLE_API_KEY=your_google_api_key_here
STRIPE_API_KEY=your_stripe_key_here  # Optional
PAYPAL_CLIENT_ID=your_paypal_id_here  # Optional
PAYPAL_CLIENT_SECRET=your_paypal_secret_here  # Optional
```

## 💻 Usage

### CLI Mode (Interactive)
```bash
python -m src.main --mode cli
```

The CLI provides an interactive menu for:
- Adding expenses manually
- Viewing monthly summaries
- Importing from payment apps
- Setting budget limits
- Getting AI recommendations

### Web App
```bash
python -m src.main --mode web --port 5000
```

Then open `http://localhost:5000` in your browser.

Features in the web app:
- **Dashboard**: Overview of monthly spending with charts
- **Add Expense**: Quick expense entry with AI analysis
- **Expenses**: View all expenses with filtering
- **Budget**: Set and track budget limits
- **Insights**: Get AI-powered recommendations

## 📁 Project Structure

```
├── src/
│   ├── models.py              # Data models (Expense, Budget, Summary)
│   ├── database.py            # SQLite database management
│   ├── ai_agent.py            # AI categorization and analysis
│   ├── payment_integrations.py # Payment app connectors
│   ├── cli.py                 # CLI interface
│   ├── web_app.py             # Flask web application
│   ├── main.py                # Entry point
│   ├── templates/
│   │   └── index.html         # Web app template
│   └── static/
│       ├── style.css          # Web app styles
│       └── app.js             # Web app JavaScript
├── data/                      # Sample data files
├── reports/                   # Generated reports
├── tests/                     # Test files
├── requirements.txt           # Python dependencies
└── README.md                  # This file
```

## 🔧 API Endpoints (Web App)

- `GET /api/expenses` - Get expenses for a month
- `POST /api/expenses` - Add a new expense
- `GET /api/summary` - Get monthly spending summary
- `POST /api/budget` - Set a budget limit
- `GET /api/recommendations` - Get AI recommendations
- `GET /api/categories` - Get available categories
- `GET /api/spending-levels` - Get spending levels

## 🎓 Example Workflow

### CLI Example:
```
1. Start the app: python -m src.main --mode cli
2. Select "Add Expense"
3. Enter details (description, amount, category)
4. AI automatically categorizes and suggests spending level
5. View monthly summary to see spending patterns
6. Get AI recommendations for optimization
```

### Web Example:
```
1. Start the web app: python -m src.main --mode web
2. Navigate to http://localhost:5000
3. Use the Dashboard tab to see overview
4. Add expenses using the Add Expense tab
5. Set budgets in the Budget tab
6. View AI insights in the Insights tab
```

## 🤖 AI Features

### Categorization
The AI agent analyzes expense descriptions and amounts to:
- Suggest the most appropriate category
- Assign a spending level (Essential/Important/Unnecessary/Waste)
- Calculate potential savings opportunities
- Provide reasoning for the classification

### Insights Generation
Monthly analysis includes:
- Spending patterns by category
- Essential vs unnecessary breakdown
- Budget adherence tracking
- Actionable recommendations
- Identified savings opportunities

## 💾 Data Storage

- **Database**: SQLite (`expenses.db`)
- **Tables**:
  - `expenses`: Individual expense records
  - `budget_limits`: Monthly budget limits
  - `monthly_summaries`: Cached summary data

## 🔒 Security Notes

- Never commit `.env` files with real API keys
- Use environment variables for sensitive data
- Consider using a secrets manager in production
- Encrypt the SQLite database in production environments

## 🐛 Troubleshooting

### AI Features Not Working
- Ensure `GOOGLE_API_KEY` is set in environment
- Check API key validity and quota limits
- Fall back to manual categorization if needed

### Payment Integration Issues
- Verify API credentials for payment providers
- Check API rate limits and quotas
- Test with mock provider first

### Web App Issues
- Ensure port 5000 is available
- Check browser console for JavaScript errors
- Verify CORS settings if running on different domain

## 📊 Sample Output

```
Monthly Summary - 2024-08
┌─────────────────────────────┬──────────────────┐
│ Metric                      │ Value            │
├─────────────────────────────┼──────────────────┤
│ Total Spent                 │ $1,245.50        │
│ By Category:                │                  │
│   Food                      │ $385.20          │
│   Transport                 │ $125.00          │
│   Entertainment             │ $95.30           │
│ Essential vs Unnecessary    │                  │
│   Essential                 │ $850.00          │
│   Unnecessary               │ $395.50          │
│ Insights:                   │                  │
│   ⚠️ High unnecessary       │ 31.7% of total   │
└─────────────────────────────┴──────────────────┘
```

## 🔄 Future Enhancements

- [ ] Multi-user support with authentication
- [ ] Cloud sync and backup
- [ ] Mobile app
- [ ] Advanced analytics and forecasting
- [ ] Integration with more payment platforms
- [ ] Custom budget rules and alerts
- [ ] Expense receipts and document storage

## 📝 License

This project is open source and available under the MIT License.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for bugs and feature requests.

## 📧 Support

For issues and questions, please open an issue on the GitHub repository.
