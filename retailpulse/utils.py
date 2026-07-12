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