import pandas as pd

merged_data = pd.read_csv(r"E:\data analysis project\InstacartMarketBasketAnalysisPortflio\data\processed\final_merged_data.csv")
# print(merged_data.columns)
# print(merged_data.head())  # بررسی ۵ رکورد اول

cleaned_orders = merged_data[['order_id', 'user_id', 'product_id', 'reordered']]

cleaned_orders.to_csv(r"E:\data analysis project\InstacartMarketBasketAnalysisPortflio\data\processed\cleaned_orders.csv", index=False)

