# Processed Data Directory

This directory contains processed data files for the **Instacart Market Basket Analysis** project. These files are the result of cleaning, transforming, and merging raw data into a format suitable for analysis and modeling.

---

## File Descriptions

### 1. `orders.csv`
- **Description**: Contains information about customer orders, including order IDs, user IDs, and order details.
- **Columns**:
  - `order_id`: Unique identifier for each order.
  - `user_id`: Unique identifier for each user.
  - `order_number`: The sequence number of the order for the user.
  - `order_dow`: Day of the week the order was placed.
  - `order_hour_of_day`: Hour of the day the order was placed.
  - `days_since_prior_order`: Number of days since the previous order.

### 2. `products.csv`
- **Description**: Contains information about the products available in the Instacart catalog.
- **Columns**:
  - `product_id`: Unique identifier for each product.
  - `product_name`: Name of the product.
  - `aisle_id`: Identifier for the aisle where the product is located.
  - `department_id`: Identifier for the department where the product is located.

### 3. `order_products__prior.csv`
- **Description**: Contains the products included in prior orders.
- **Columns**:
  - `order_id`: Unique identifier for the order.
  - `product_id`: Unique identifier for the product.
  - `add_to_cart_order`: The order in which the product was added to the cart.
  - `reordered`: Indicates whether the product was reordered (1) or not (0).

### 4. `final_merged_data.csv`
- **Description**: The final merged dataset combining `orders.csv`, `products.csv`, and `order_products__prior.csv`.
- **Columns**:
  - All columns from the original datasets, merged on `order_id` and `product_id`.

---

## Usage

To use these files in your analysis, simply load them into your Python environment using `pandas`

---

## فایل های  ایجاد شده در پوشه processed

### 1. cleaned_orders.csv:
  - `هدف`: ذخیره داده‌های سفارشات پس از تمیز کردن و آماده‌سازی.
  - `محتوا`: شامل ستون‌های order_id, user_id, product_id, reordered.

### 2. user_features.csv:
  - `هدف`: ذخیره ویژگی‌های استخراج‌شده برای هر کاربر.
  - `محتوا`: شامل ستون‌های user_id, total_orders, avg_days_between_orders, total_products_ordered.

### 3. product_features.csv:
  - `هدف`: ذخیره ویژگی‌های استخراج‌شده برای هر محصول.
  - `محتوا`: شامل ستون‌های product_id, order_count, reorder_rate.

### 4. user_product_matrix.csv:
  - `هدف`: نمایش تعاملات کاربران و محصولات به‌صورت ماتریس.
  - `محتوا`: هر سطر نشان‌دهنده یک کاربر و هر ستون نشان‌دهنده یک محصول. مقادیر می‌توانند تعداد سفارشات یا نشانگرهای باینری (0 یا 1) باشند.

### 5. summary_statistics.csv:
  - `هدف`: ذخیره آمار توصیفی یا خلاصه‌های مفید از داده‌ها.
  - `محتوا`: شامل ستون‌های total_users, total_products, total_orders, avg_products_per_order.

### 6. model_ready_data.csv:
  - `هدف`: ذخیره داده‌های آماده برای مدل‌سازی.
  - `محتوا`: شامل ستون‌های user_id, product_id, total_orders, avg_days_between_orders, total_products_ordered, order_count, reorder_rate.

