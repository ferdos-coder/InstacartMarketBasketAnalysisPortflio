import pandas as pd

merged_data = pd.read_csv(r"E:\data analysis project\InstacartMarketBasketAnalysisPortflio\data\processed\final_merged_data.csv")
# print(merged_data.head())  # بررسی ۵ رکورد اول


user_features = merged_data.groupby('user_id').agg(
    total_orders=('order_id', 'nunique'),
    avg_days_between_orders=('days_since_prior_order', 'mean'),
    total_products_ordered=('product_id', 'count')
).reset_index()

#total_orders: تعداد کل سفارشات هر کاربر.
#avg_days_between_orders: میانگین فاصله زمانی بین سفارشات هر کاربر.
#total_products_ordered: تعداد کل محصولاتی که هر کاربر سفارش داده است.
# print(user_features)

user_features.to_csv(r"E:\data analysis project\InstacartMarketBasketAnalysisPortflio\data\processed\user_features.csv", index=False)
