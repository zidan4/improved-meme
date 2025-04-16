import pandas as pd

def clean_csv(file_path):
    df = pd.read_csv(file_path)

    # Drop empty rows
    df.dropna(how='all', inplace=True)

    # Trim whitespace
    df.columns = [col.strip() for col in df.columns]
    for col in df.select_dtypes(include='object'):
        df[col] = df[col].str.strip()

    # Rename columns to snake_case
    df.columns = [col.lower().replace(" ", "_") for col in df.columns]

    # Save cleaned version
    cleaned_path = file_path.replace(".csv", "_cleaned.csv")
    df.to_csv(cleaned_path, index=False)
    print(f"🧼 Cleaned file saved to: {cleaned_path}")

if __name__ == "__main__":
    clean_csv('dirty_data.csv')
