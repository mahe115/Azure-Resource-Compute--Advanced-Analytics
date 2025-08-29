
## 📂 Project Structure

```
azure-demand-forecasting/
|
|── backend/
│   ├── routes/
|   |   ├── data_routes.py
|   |   ├── insights_routes.py
|   ├── app.py
|   └── requirements.txt
|
│
├── data/
│   ├── raw/
│   │   ├── azure_usage.csv
│   │   └── external_factors.csv
│   └── processed/
│       └── cleaned_merged.csv
│
├── notebooks/
│   ├── Data_Loading.ipynb
│   └── Data_Cleaning.ipynb
│
├── frontend/
│   ├── src/
│   └── ... (React application files)
│
├── reports/
│   ├── eda.md
│   └── current_work.md
│
└── README.md
```

## ⚙️ Backend & Data Analysis Setup

The backend part involves data loading, cleaning, and exploratory data analysis using Jupyter notebooks.

### Prerequisites
- Python 3.x
- pip

### Instructions
1.  **Clone the repository** to your local machine.

2.  **Install Python dependencies** from the backend directory of the project:
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the Jupyter Notebooks**:
    - Start the Jupyter Notebook server.
    - Navigate to the `notebooks/` directory.
    - Execute the notebooks in the following order:
      1. `01_data_loading_eda.ipynb`
      2. `02_data_cleaning_merging.ipynb`
    - The final cleaned dataset will be saved as `data/processed/cleaned_merged.csv`.

4.  **Start the backend** from the backend directory of the project:
    ```bash
    python app.py
    ```


## 🖥️ Frontend Setup

The frontend is a React application built with Vite for visualizing the analytics.

### Prerequisites
- Node.js (v18 or higher)
- npm (or yarn/pnpm)

### Instructions
1.  **Navigate to the frontend directory**:
    ```bash
    cd frontend
    ```

2.  **Install Node.js dependencies**:
    ```bash
    npm install
    ```

3.  **Start the development server**:
    ```bash
    npm run dev
    ```
    The application will be running at `http://localhost:5173` (or the next available port).

## ✅ Key Outputs
- A cleaned and merged dataset located at `data/processed/cleaned_merged.csv`.
- An EDA report in `reports/eda_report.md`.
- A running React application for data visualization.

## ⚡ Current Application Capabilities

- Backend (Flask API)
  - Provides REST endpoints under /api for analytics:
    - usage-trends (avg CPU by region)
    - usage-trends-storage (avg Storage by region)
    - top-regions, top-regions-storage (top regions by CPU / Storage demand)
    - peak-demand, peak-demand-storage (monthly peak CPU / Storage)
    - regional-comparison (aggregated stats per region)
    - monthly-trends (month × region × resource_type averages)
    - holiday-impact (comparisons for holiday vs non-holiday)
    - insights, insights-storage (summary metrics)
  - Loads cleaned data from data/processed/cleaned_merged.csv and returns JSON-safe payloads.
  - Basic data-sanitization helpers to ensure JSON serializability.

- Frontend (React + Vite)
  - Dashboard with three main views:
    - Overview: quick insights, CPU/Storage toggle, usage trends, top regions, peak demand.
    - Resources: monthly trends and holiday impact charts.
    - Regions: regional comparison and per-region top lists.
  - Chart components include: InsightsSummary, UsageTrends, TopRegions, PeakDemand, RegionalComparison, MonthlyTrends, HolidayImpact.
  - Fetches data from backend endpoints and maps them to charts (uses endpoints listed in frontend/src/services/api.js).

- Notebooks & Data Pipelines
  - Data_Loading.ipynb: loads raw CSVs and inspects structure.
  - Data_visualizing.ipynb: plotting and visualization for EDA.
  - Feature_Engineering.ipynb: one-hot encoding and exports encoded dataset to Data/Processed/Encoded_Cleaned_Data.csv.

- Artifacts
  - Cleaned dataset: data/processed/cleaned_merged.csv
  - Encoded dataset for modeling: Data/Processed/Encoded_Cleaned_Data.csv
  - EDA report: reports/eda.md

## 🏁 Quick Run Summary

- Start backend API (default port 5000) so frontend can fetch endpoints:
  - From backend folder: run your Flask app (e.g., export FLASK_APP=app.py && flask run --port 5000) or the project's prescribed start command.
- Start frontend:
  - cd frontend && npm install && npm run dev
- Open the dashboard in a browser and switch views / resources to explore data.
