from pathlib import Path
import pandas as pd

def load_datasets():
    """
    Load all Olist datasets.
    """

    data_path = Path("../data/raw")

    orders = pd.read_csv(data_path / "olist_orders_dataset.csv")
    customers = pd.read_csv(data_path / "olist_customers_dataset.csv")
    geolocation = pd.read_csv(data_path / "olist_geolocation_dataset.csv")
    items = pd.read_csv(data_path / "olist_order_items_dataset.csv")
    payments = pd.read_csv(data_path / "olist_order_payments_dataset.csv")
    reviews = pd.read_csv(data_path / "olist_order_reviews_dataset.csv")
    products = pd.read_csv(data_path / "olist_products_dataset.csv")
    sellers = pd.read_csv(data_path / "olist_sellers_dataset.csv")
    categories = pd.read_csv(data_path / "product_category_name_translation.csv")

    return (
        orders,
        customers,
        geolocation,
        items,
        payments,
        reviews,
        products,
        sellers,
        categories,
    )


def explore_dataframe(df, name):
    print("=" * 60)
    print(f"Dataset: {name}")
    print("=" * 60)

    print("\nFirst 5 Rows:")
    display(df.head())

    print("\nShape:")
    print(df.shape)

    print("\nData Information:")
    df.info()

    print("\nMissing Values:")
    print(df.isnull().sum())

    print("\nDuplicate Rows:")
    print(df.duplicated().sum())
    
    
def check_data_types(df, name):
    """
    Display the data types of each column.
    """

    print("=" * 60)
    print(f"Dataset: {name}")
    print("=" * 60)

    print(df.dtypes)    
    
    
def convert_to_datetime(df, columns):
    """
    Convert multiple columns to datetime.
    """

    for column in columns:
        df[column] = pd.to_datetime(df[column])

    return df    



def analyze_missing_values(df, name):
    """
    Display missing values count and percentage for each column.
    """

    missing_count = df.isnull().sum()
    missing_percent = (missing_count / len(df) * 100).round(2)

    missing_summary = pd.DataFrame({
        "Missing Values": missing_count,
        "Percentage (%)": missing_percent
    })

    missing_summary = missing_summary[missing_summary["Missing Values"] > 0]
    missing_summary = missing_summary.sort_values(
        by="Missing Values",
        ascending=False
    )

    print("=" * 60)
    print(f"Dataset: {name}")
    

    if missing_summary.empty:
        print("No missing values found")
    else:
        print(missing_summary)
        
        
        
def check_duplicates(df, name):
    print("=" * 60)
    print(f"Dataset: {name}")
    print("=" * 60)

    duplicate_count = df.duplicated().sum()

    print(f"Duplicate Rows: {duplicate_count}")

    if duplicate_count > 0:
        display(df[df.duplicated()].head())        