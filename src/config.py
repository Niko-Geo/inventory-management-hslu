"""Central paths and constants for the project."""
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]

DATA_RAW = PROJECT_ROOT / "data" / "raw"
DATA_PROCESSED = PROJECT_ROOT / "data" / "processed"
FIGURES = PROJECT_ROOT / "outputs" / "figures"
TABLES = PROJECT_ROOT / "outputs" / "tables"

TRANSACTIONS_PARQUET = DATA_PROCESSED / "transactions.parquet"

# Entry type codes (from the case study PDF)
ENTRY_TYPES = {
    0: "Procurement",
    1: "Sale",
    2: "Ingoing adjustment",
    3: "Outgoing adjustment",
    4: "Internal transaction",
    5: "Usage for production",
    6: "Ingoing from production",
}
DEMAND_TYPES = [1, 5]  # working assumption: demand = sales + usage for production

# --- Processed files ---
TRANSACTIONS_CLEAN = DATA_PROCESSED / "transactions_clean.parquet"   # inventory articles, up to reference date
ARTICLES = DATA_PROCESSED / "articles.parquet"                       # one row per inventory article
DEMAND_MONTHLY = DATA_PROCESSED / "demand_monthly.parquet"           # article x month demand, analysis window

# --- Time settings (decided in notebook 02) ---
REFERENCE_DATE = "2022-01-21"   # end of normal activity ("today" for the analysis)
ANALYSIS_START = "2019-01-01"   # 3-year window for demand statistics
ANALYSIS_END = "2021-12-31"     # last full month before the reference date

# --- Outlier capping (per article, on single demand transactions) ---
# Only clear one-off spikes are capped; recurring large orders are real (lumpy B2B) demand.
OUTLIER_MEDIAN_FACTOR = 10      # transaction > 10x the article's median demand transaction ...
OUTLIER_ISOLATION = 0.5         # ... AND no other transaction reaches 50% of its size (one-off)
OUTLIER_MIN_TRANSACTIONS = 10   # only cap articles with enough history

# --- Analysis outputs ---
ARTICLE_FEATURES = DATA_PROCESSED / "article_features.parquet"   # one row per article, all metrics
DAYS_PER_YEAR = 360             # as in the case study formula (quantity / 360)
ARTICLE_CLUSTERS = DATA_PROCESSED / "article_clusters.parquet"   # cluster label per article (notebook 04)

# --- Safety stock / reorder point (notebook 05) ---
SERVICE_Z = {"A": 2.05, "B": 1.65, "C": 1.28}   # ~98% / 95% / 90% cycle service level by ABC class
DAYS_PER_MONTH = 30
SIM_WARMUP_START = "2020-01-01"                 # simulation warm-up (not measured)
SIM_START, SIM_END = "2021-01-01", "2021-12-31" # simulated & evaluated year
PARAM_END = "2020-12-31"                        # backtest parameters estimated on 2019-2020 only (out-of-sample test)
