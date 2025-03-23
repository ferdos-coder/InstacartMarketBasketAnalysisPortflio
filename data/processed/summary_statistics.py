import pandas as pd


merged_data = pd.read_csv(r"E:\data analysis project\InstacartMarketBasketAnalysisPortflio\data\processed\final_merged_data.csv")
# print(merged_data.columns)
# print(merged_data.head())  # بررسی ۵ رکورد اول

#ذخیره آمار توصیفی یا خلاصه‌های مفید از داده‌ها.
summary_stats = pd.DataFrame({
    'total_users': [merged_data['user_id'].nunique()],
    'total_products': [merged_data['product_id'].nunique()],
    'total_orders': [merged_data['order_id'].nunique()],
    'avg_products_per_order': [merged_data.groupby('order_id')['product_id'].count().mean()]
})
print(summary_stats)

summary_stats.to_csv(r"E:\data analysis project\InstacartMarketBasketAnalysisPortflio\data\processed\summary_statistics.csv", index=False)


