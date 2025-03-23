import pandas as pd


merged_data = pd.read_csv(r"E:\data analysis project\InstacartMarketBasketAnalysisPortflio\data\processed\final_merged_data.csv")
print(merged_data.head())  # بررسی ۵ رکورد اول


# استخراج تعداد کل سفارشات هر مشتری
user_orders = merged_data.groupby('user_id')['order_id'].count().reset_index()

user_orders.columns = ['user_id', 'total_orders']
print(user_orders)

# ذخیره نتایج در یک فایل CSV
user_orders.to_csv(r"E:\data analysis project\InstacartMarketBasketAnalysisPortflio\data\processed\user_orders.csv", index=False)


#استخراج محبوب ترین محصولات، محصولاتی که بیشترین سفارش را دارند
popular_products = merged_data.groupby('product_id')['order_id'].count().reset_index()
popular_products.columns = ['product_id', 'order_count']
print(popular_products)


# ذخیره نتایج در یک فایل CSV
popular_products.to_csv(r"E:\data analysis project\InstacartMarketBasketAnalysisPortflio\data\processed\product_features.csv", index=False)


