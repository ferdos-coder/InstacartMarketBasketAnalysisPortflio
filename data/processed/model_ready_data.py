import pandas as pd

import pandas as pd

# بارگیری فایل‌های ویژگی‌ها
user_features = pd.read_csv(r"E:\data analysis project\InstacartMarketBasketAnalysisPortflio\data\processed\user_features.csv")
product_features = pd.read_csv(r"E:\data analysis project\InstacartMarketBasketAnalysisPortflio\data\processed\product_features.csv")

# بارگیری داده‌های اصلی
merged_data = pd.read_csv(r"E:\data analysis project\InstacartMarketBasketAnalysisPortflio\data\processed\final_merged_data.csv")

# ادغام داده‌ها با ویژگی‌های کاربر و محصول
model_ready_data = pd.merge(merged_data, user_features, on='user_id')
model_ready_data = pd.merge(model_ready_data, product_features, on='product_id')

# ذخیره داده‌های آماده برای مدل‌سازی
model_ready_data.to_csv(r"E:\data analysis project\InstacartMarketBasketAnalysisPortflio\data\processed\model_ready_data.csv", index=False)

