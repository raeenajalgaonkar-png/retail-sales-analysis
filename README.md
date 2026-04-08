# 🛒 Retail Sales Analysis — Pandas Project

A complete, beginner-friendly pandas project covering every core data-analysis workflow:

| Task | Where |
|---|---|
| Read CSV/Excel → DataFrame & inspect head/tail/types | `src/analyze.py` → `load_and_inspect()` |
| Compute summary stats (mean, median, min, max, count) | `src/analyze.py` → `summary_statistics()` |
| Filter rows, select columns, slice subsets | `src/analyze.py` → `filter_and_slice()` |
| Save filtered results to CSV / Excel | `src/analyze.py` + `src/export_excel.py` |

---

## Project structure

```
retail_sales_project/
├── data/
│   ├── raw/                  ← generated CSV (git-ignored)
│   └── processed/            ← filtered output CSVs
├── notebooks/
│   └── exploration.ipynb     ← interactive walkthrough
├── outputs/
│   └── retail_sales_analysis.xlsx
├── src/
│   ├── generate_data.py      ← synthetic dataset generator
│   ├── analyze.py            ← all 4 pandas tasks
│   └── export_excel.py       ← styled Excel export
├── tests/
│   ├── test_generate.py
│   └── test_analyze.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## Quick start

```bash
# 1. Clone & install
git clone https://github.com/<your-username>/retail-sales-analysis.git
cd retail-sales-analysis
pip install -r requirements.txt

# 2. Generate the dataset
python src/generate_data.py

# 3. Run all analysis tasks (prints head, types, stats; saves CSVs)
python src/analyze.py

# 4. Export styled Excel workbook
python src/export_excel.py

# 5. Run tests
pytest tests/ -v

# 6. Open the notebook
jupyter notebook notebooks/exploration.ipynb
```

---

## Dataset overview

500 synthetic retail orders across 2024, with these columns:

| Column | Type | Description |
|---|---|---|
| OrderID | str | Unique order identifier |
| Date | datetime | Order date |
| Category | str | Electronics / Clothing / Food & Beverage / Home & Garden / Sports |
| Product | str | Product code (A–E) |
| Region | str | North / South / East / West |
| Quantity | int | Units ordered (1–14) |
| UnitPrice | float | Price per unit (₹50–₹5 000) |
| Discount | float | Discount rate (0–20 %) |
| PaymentMethod | str | Credit Card / Cash / UPI / Debit Card |
| CustomerAge | int | Buyer age (18–69) |
| Rating | float | Order rating (1.0–5.0) |
| Revenue | float | `Quantity × UnitPrice × (1 − Discount)` |
| Month | str | Month name |
| Quarter | str | e.g. `2024Q1` |

---

## Key pandas concepts demonstrated

```python
# Read & inspect
df = pd.read_csv('data/raw/retail_sales_raw.csv', parse_dates=['Date'])
df.head()          # first 5 rows
df.tail()          # last 5 rows
df.dtypes          # column types
df.info()          # non-null counts

# Summary statistics
df[numeric_cols].agg(['mean', 'median', 'min', 'max', 'count', 'std'])

# Filter rows (boolean indexing)
df[(df['Category'] == 'Electronics') & (df['Revenue'] > 10_000)]

# Select columns
df[['OrderID', 'Date', 'Revenue', 'Rating']]

# Slice rows by position
df.iloc[0:50]

# GroupBy aggregation
df.groupby('Category').agg(TotalRevenue=('Revenue', 'sum'))

# Pivot table
df.pivot_table(index='Region', columns='Category', values='Revenue', aggfunc='sum')

# Save results
filtered_df.to_csv('data/processed/electronics_high_value.csv', index=False)
```

---

## License

MIT
