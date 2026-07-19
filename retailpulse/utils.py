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
        
        
        
import matplotlib.pyplot as plt


def analyze_outliers(df, column):
    """
    Analyze outliers in a numerical column using the IQR method.
    """

    # Quartiles
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)

    # Interquartile Range
    IQR = Q3 - Q1

    # Bounds
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    # Outliers
    outliers = df[
        (df[column] < lower_bound) |
        (df[column] > upper_bound)
    ]

    print(f"\n----- {column.upper()} -----")
    print(f"Q1: {Q1:.2f}")
    print(f"Q3: {Q3:.2f}")
    print(f"IQR: {IQR:.2f}")
    print(f"Lower Bound: {lower_bound:.2f}")
    print(f"Upper Bound: {upper_bound:.2f}")
    print(f"Number of Outliers: {len(outliers)}")
    print(f"Percentage: {(len(outliers)/len(df))*100:.2f}%")

    display(outliers.nlargest(10, column))

    plt.figure(figsize=(8, 4))
    df.boxplot(column=column)
    plt.title(f"Box Plot of {column}")
    plt.ylabel(column)
    plt.show()      
    
    

def validate_foreign_keys(child_df, child_key, parent_df, parent_key):
    """
    Validate that all foreign key values exist in the parent table.
    """

    # Find records with missing foreign keys
    invalid_records = child_df[
        ~child_df[child_key].isin(parent_df[parent_key])
    ]

    # Display results
    if invalid_records.empty:
        print(f" All '{child_key}' values exist in '{parent_key}'.")
    else:
        print(f" Found {len(invalid_records)} invalid records.")
        display(invalid_records)