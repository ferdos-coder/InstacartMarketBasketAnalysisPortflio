import pandas as pd


# خواندن فایل‌ها
orders = pd.read_csv(r"E:\data analysis project\InstacartMarketBasketAnalysisPortflio\data\processed\orders.csv")
products = pd.read_csv(r"E:\data analysis project\InstacartMarketBasketAnalysisPortflio\data\processed\products.csv")
order_products_prior = pd.read_csv(r"E:\data analysis project\InstacartMarketBasketAnalysisPortflio\data\processed\order_products__prior.csv")

# ادغام داده‌ها
merged_data = pd.merge(orders, order_products_prior, on='order_id')
final_merged_data = pd.merge(merged_data, products, on='product_id')

# ذخیره فایل در مسیر مشخص
final_merged_data.to_csv(r"E:\data analysis project\InstacartMarketBasketAnalysisPortflio\data\processed\final_merged_data.csv", index=False)

# چاپ داده‌ها
print(final_merged_data)