import pandas as pd

merged_data = pd.read_csv(r"E:\data analysis project\InstacartMarketBasketAnalysisPortflio\data\processed\final_merged_data.csv")
# print(merged_data.head())  # بررسی ۵ رکورد اول



product_features = merged_data.groupby('product_id').agg(
    order_count=('order_id', 'count'),
    reorder_rate=('reordered', 'mean')
).reset_index()
# print(product_features)

#order_count: تعداد دفعاتی که محصول سفارش داده شده است.
#reorder_rate: نسبت سفارش‌های مجدد به کل سفارش‌های محصول.

product_features.to_csv(r"E:\data analysis project\InstacartMarketBasketAnalysisPortflio\data\processed\product_features.csv", index=False)


