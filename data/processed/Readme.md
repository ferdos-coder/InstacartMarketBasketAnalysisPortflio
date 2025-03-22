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

To use these files in your analysis, simply load them into your Python environment using `pandas`:

