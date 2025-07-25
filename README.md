# 💸 Self Finance Dashboard

An interactive web-based personal finance tracker that helps you visualize and categorize your expenses and payments from bank transaction CSV files.

## 🔍 Features

- 📁 Upload transaction CSV files and view debits and credits separately
- 🧠 Smart categorization of expenses based on transaction details
- 📝 Manual category editing with persistent storage (JSON-based)
- 📊 Visual summaries using Plotly (Pie Charts and Metrics)
- 🖱️ Interactive UI with tab-based navigation and real-time editing

## 🛠️ Built With

- [Streamlit](https://streamlit.io/)
- [Pandas](https://pandas.pydata.org/)
- [Plotly](https://plotly.com/)
- [NumPy](https://numpy.org/)

## 🚀 Getting Started

### Prerequisites

Make sure you have Python 3.7+ installed.

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/self-finance-dashboard.git
   cd self-finance-dashboard
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

### Run the App

```bash
streamlit run main.py
```

Then, open the URL provided in your terminal to access the dashboard in your browser.

## 🧾 CSV Format Expected

The uploaded CSV file must have the following columns:

- `Date` (e.g., `12 Jan 2024`)
- `Details` (transaction description)
- `Amount` (e.g., `1,500.00`)
- `Debit/Credit` (either `"Debit"` or `"Credit"`)

## 📂 File Persistence

- Categories and keywords are saved locally in `categories.json` to persist across sessions.

## 📌 Screenshots

*Add screenshots here if available*

## 🧑‍💻 Author

**Your Name**  
[GitHub](https://github.com/yourusername) • [LinkedIn](https://linkedin.com/in/yourprofile)

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).
#   P e r s o n a l - F i n a n c e - A u t o m a t i o n - T o o l  
 