import pandas as pd
from scipy.sparse import csr_matrix

merged_data = pd.read_csv(r"E:\data analysis project\InstacartMarketBasketAnalysisPortflio\data\processed\final_merged_data.csv")
# print(merged_data.columns)
# print(merged_data.head())  # بررسی ۵ رکورد اول



# ایجاد ماتریس اسپارس به جای ماتریس کامل
#این ماتریس کامل نشان می‌دهد که هر کاربر چه تعداد سفارش برای هر محصول داشته است.
user_product_matrix_sparse = csr_matrix(
    (merged_data['order_id'], 
     (merged_data['user_id'].astype('category').cat.codes, 
      merged_data['product_id'].astype('category').cat.codes))
)


# print(user_product_matrix_sparse)


