import pandas as pd


def find_products(products: pd.DataFrame) -> pd.DataFrame:
    i = 0
    result_ids = []  # List to store product IDs that meet the criteria

    while i < len(products):
        if (products.iloc[i]['low_fats'] == 'Y') & (products.iloc[i]['recyclable'] == 'Y'):
            result_ids.append(products.iloc[i]['product_id'])
        i += 1

    return pd.DataFrame({'product_id': result_ids})
