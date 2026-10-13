# Sales ETL & Analytics Pipeline

An end-to-end data engineering and analytics project that processes retail sales data using Python, Pandas, and PostgreSQL, then visualizes the results through an interactive Power BI dashboard.

The project demonstrates how raw sales data can be extracted, transformed, loaded into a relational database, and prepared for business intelligence and reporting.

## Project Overview

Retail sales datasets contain valuable information about orders, products, regions, and revenue. However, raw data must be processed and stored appropriately before it can be used for meaningful analysis.

This project implements an ETL (Extract, Transform, Load) workflow to move sales data from a CSV file into PostgreSQL using Python and Pandas. The resulting database serves as the data source for a Power BI dashboard, enabling interactive exploration of sales performance.

## Dataset

The project uses a retail sales dataset sourced from Kaggle, containing sales records used to demonstrate the ETL workflow.

* **Source:** Kaggle
* **Format:** CSV
* **Records processed:** 9,789

The dataset is extracted from the source file, processed using Python and Pandas, and loaded into PostgreSQL for downstream analysis and Power BI visualization.

**Dataset reference: https://www.kaggle.com/datasets/bravehart101/sample-supermarket-dataset


### Key Highlights

* Processed **9,789 retail sales records** through the ETL pipeline.
* Used Python and Pandas for data processing and transformation.
* Loaded processed sales data into PostgreSQL.
* Connected the database to Power BI for visualization.
* Created an interactive dashboard with slicers for exploring sales performance.
* Connected data engineering concepts with practical business analytics.

## Architecture

The project follows a straightforward ETL architecture:

```text
        Raw Sales Dataset
             (CSV)
               |
               v
      EXTRACT & TRANSFORM
        Python + Pandas
               |
               v
             LOAD
          PostgreSQL
               |
               v
       DATA VISUALIZATION
            Power BI
               |
               v
     Interactive Sales Dashboard
```

## Technology Stack

| Technology   | Purpose                                              |
| ------------ | ---------------------------------------------------- |
| Python       | ETL implementation and data processing               |
| Pandas       | Data manipulation and transformation                 |
| PostgreSQL   | Relational database for storing processed sales data |
| SQL          | Database operations and data querying                |
| Power BI     | Interactive sales visualization and reporting        |
| Git & GitHub | Version control and project documentation            |

## ETL Workflow

### 1. Extract

The pipeline reads retail sales data from a CSV dataset.

The input data serves as the source for the subsequent processing and database-loading stages.

### 2. Transform

Python and Pandas are used to process and prepare the sales data for database storage.

This stage forms the data preparation layer between the raw CSV input and the PostgreSQL database.

### 3. Load

The processed records are loaded into PostgreSQL, providing a structured relational database for querying and downstream analysis.

The pipeline successfully loaded **9,789 records** into PostgreSQL.

### 4. Visualize

Power BI connects to the database to present sales information through an interactive dashboard.

The dashboard includes sales analysis views and an interactive slicer that allows users to explore the available data.

## Power BI Dashboard

The dashboard provides a visual interface for exploring the processed sales dataset.

Its purpose is to make the data easier to interpret and support interactive analysis of sales performance.

**Dashboard features:**

* Visual analysis of sales data.
* Interactive filtering using a slicer.
* Exploration of the processed dataset through Power BI.

> To include a dashboard preview, add a screenshot of the existing Power BI dashboard to your repository and embed it here. No changes to the dashboard itself are required.

<!-- Optional: Uncomment after uploading your existing dashboard screenshot.
![Sales ETL Power BI Dashboard](images/sales-dashboard.png)
-->

## Getting Started

Follow these steps to set up the project using its existing implementation.

### Prerequisites

* Python installed on your system.
* PostgreSQL installed and accessible.
* The existing project source files and CSV dataset.
* Power BI Desktop for opening and exploring the dashboard.

### 1. Clone the Repository

```bash
git clone https://github.com/Raheeemm/sales-etl-pipeline.git
cd sales-etl-pipeline
```

### 2. Set Up the Python Environment

Create a virtual environment:

```bash
python -m venv venv
```

Activate it on Windows:

```powershell
.\venv\Scripts\Activate.ps1
```

Activate it on Linux or macOS:

```bash
source venv/bin/activate
```

### 3. Install Dependencies

If the repository includes a `requirements.txt` file, install the dependencies listed in it:

```bash
pip install -r requirements.txt
```

If the project does not include this file, install the dependencies required by the existing implementation instead of adding unnecessary packages.

### 4. Configure PostgreSQL

Ensure PostgreSQL is running and that the database configuration matches the existing project setup.

Use the connection settings and database name expected by the original implementation.

Do not commit database passwords or other sensitive credentials to GitHub.

### 5. Run the ETL Pipeline

Run the existing Python entry-point script used by the project.

For example, if the entry-point file is `main.py`:

```bash
python main.py
```

Replace `main.py` with the actual entry-point filename if your repository uses a different one.

### 6. Explore the Dashboard

Open the existing Power BI dashboard in Power BI Desktop and use its interactive slicer to explore the available sales data.

## Skills Demonstrated

This project demonstrates practical experience with:

* ETL pipeline fundamentals.
* Python-based data processing.
* Pandas data manipulation.
* Relational database concepts and PostgreSQL.
* SQL-based data storage and querying.
* Database-to-BI integration.
* Interactive dashboard development using Power BI.
* Data engineering and analytics workflows.

## Project Scope

The project focuses on a foundational data engineering workflow:

**CSV ingestion → Python/Pandas processing → PostgreSQL storage → Power BI visualization**

It demonstrates how data moves from a raw file into a database and becomes accessible for interactive business analysis.

## Author

**Abdul Raheem**

Electronics and Communication Engineering Graduate | 2026

Interested in Data Engineering, Cloud Infrastructure, DevOps, and Analytics.

GitHub: [Raheeemm](https://github.com/Raheeemm)

## License

Refer to the license included in the repository, if applicable.
