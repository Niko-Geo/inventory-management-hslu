# Inventory Optimisation – HSLU Case Study

Data-driven Supply Chain Management and Logistics module.

**Goal:** reduce inventory capital lockup through data analysis, article
classification, and safety stock / reorder point optimisation, with
detailed recommendations for 10 selected articles. Deliverable: PDF report.

## Structure

```
data/raw/          original CSV + XLS (not in git)
data/processed/    cleaned Parquet files (not in git)
notebooks/         one notebook per step, run in order
src/               shared code (paths, helpers)
outputs/figures/   charts for the report
outputs/tables/    summary tables, overview text files
report/            PDF report source
```

## Setup (macOS)

```bash
cd /Users/nikolaosgeorgantopoulos/Repositories/inventory-optimization
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

In VS Code: open the folder, open a notebook, select the `.venv` kernel.

## Notebooks

1. `01_load_and_overview.ipynb` – load raw data, basic overview, save Parquet
2. `02_clean_and_demand.ipynb` – checks, cleaning, article table, monthly demand 2019–2021
3. `03_data_analysis.ipynb` – capital lockup, ABC/XYZ, demand patterns, dead stock, lead time, reorder points; feature table
4. `04_classification.ipynb` – feature selection, clustering (k-means / GMM / Ward), evaluation, cluster profiles
5. `05_recommendations.ipynb` – strategies, SS/ROP (case formula + textbook), backtest simulation, capital effect, 10 articles, export

## Report (PDF)

From the project root:

```bash
quarto render report/report.qmd
```

Creates `report/report.pdf` (Typst engine, no LaTeX needed). Figures are read from `outputs/figures/`,
so run notebooks 03–05 first. `_quarto.yml` in the root is required so the report can access `outputs/`.
