import sqlite3
import pandas as pd
import logging 

def ingest_db(df, table_name, engine):
    '''this function will ingest the data frame into database table'''
    df.to_sql(table_name, con= engine, if_exists = 'replace', index = False)

logging.basicConfig(
    filename="logs/get_partner_summary.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filemode='a'
)

def create_partner_summary(conn):
    '''this function will merge the different tables to get the overall partner summary and adding new columns in the resultant data'''
    commercial_partner_summary= pd.read_sql_query("""WITH FreightSummary AS(

        SELECT
            VendorNumber,
            SUM(Freight) as FreightCost 
        FROM vendor_invoice
        GROUP BY VendorNumber
    ),
    PurchaseSummary AS (
        SELECT 
            p.VendorNumber,
            p.VendorName,
            p.Brand,
            p.Description,
            p.PurchasePrice,
            pp.Price as ActualPrice,
            pp.Volume,
            SUM(p.Quantity) as TotalPurchaseQuantity,
            SUM(p.dollars) as TotalPurchaseDollars
        FROM purchases p
        JOIN purchase_prices pp
            ON p.Brand = pp.Brand
        WHERE p.PurchasePrice>0
        GROUP BY p.VendorNumber, p.VendorName, p.Brand, p.Description, p.PurchasePrice, pp.Price, pp.Volume
    ),
    
    SalesSummary AS (
        SELECT
            VendorNo,
            Brand,
            SUM(SalesQuantity) as TotalSalesQuantity,
            SUM(SalesDollars)as TotalSalesDollars,
            SUM(SalesPrice) as TotalSalesPrice,
            SUM(ExciseTax) as TotalExciseTax
        FROM sale
        GROUP BY VendorNo, Brand
    )
    SELECT
        ps.VendorNumber,
        ps.VendorName,
        ps.Brand,
        ps.Description,
        ps.PurchasePrice,
        ps.ActualPrice,
        ps.Volume,
        ps.TotalPurchaseQuantity,
        ps.TotalPurchaseDollars,
        ss.TotalSalesQuantity,
        ss.TotalSalesDollars,
        ss.TotalSalesPrice,
        ss.TotalExciseTax,
        fs.FreightCost
    FROM PurchaseSummary ps
    LEFT JOIN SalesSummary ss
        ON ps.VendorNumber = ss.VendorNo
        AND ps.Brand = ss.Brand
    LEFT JOIN FreightSummary fs
        ON ps.VendorNumber = fs.VendorNumber
    ORDER BY ps.TotalPurchaseDollars DESC""",conn)

    return commercial_partner_summary

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Clean and enrich vendor summary with derived metrics."""

    df = df.copy()

    # types
    df["Volume"] = pd.to_numeric(df["Volume"], errors="coerce")

    # trim text cols (safe even if 0-filled later)
    for col in ["VendorName", "Description", "Brand"]:
        if col in df.columns:
            df[col] = df[col].astype(str).str.strip()

    # fill missing numerics with 0
    numeric_cols = df.select_dtypes(include=["number"]).columns
    df[numeric_cols] = df[numeric_cols].fillna(0)

    # derived metrics
    df["GrossProfit"] = df["TotalSalesDollars"] - df["TotalPurchaseDollars"]

    # avoid div-by-zero
    df["ProfitMargin"] = df.apply(
        lambda x: (x["GrossProfit"] / x["TotalSalesDollars"] * 100) if x["TotalSalesDollars"] > 0 else 0,
        axis=1
    )

    df["StockTurnover"] = df.apply(
        lambda x: (x["TotalSalesQuantity"] / x["TotalPurchaseQuantity"]) if x["TotalPurchaseQuantity"] > 0 else 0,
        axis=1
    )

    df["SalesToPurchaseRatio"] = df.apply(
        lambda x: (x["TotalSalesDollars"] / x["TotalPurchaseDollars"]) if x["TotalPurchaseDollars"] > 0 else 0,
        axis=1
    )

    return df


if __name__ =='__main__':
    #creating database connection
    conn = sqlite3.connect('inventory.db')

    logging.info('Creating Partner Summary Table...')
    summary_df = create_partner_summary(conn)
    logging.info(summary_df.head())

    logging.info('Cleaning Data....')
    clean_df = clean_data(summary_df)
    logging.info(clean_df.head())

    logging.info('Ingesting Data....')
    ingest_db(clean_df,'partner_sales_summary',conn)
    logging.info('Completed')