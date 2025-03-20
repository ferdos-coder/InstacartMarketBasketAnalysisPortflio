# Raw Data Directory

## Overview
This directory contains the raw, unprocessed data files for the Instacart Market Basket Analysis project. These files are sourced directly from the Instacart dataset and serve as the foundation for our analysis.

## Contents
The raw data includes the following files:
- aisles.csv
- departments.csv
- order_products__prior.csv
- order_products__train.csv
- orders.csv
- products.csv

## Data Description
- aisles.csv: Contains aisle names and IDs
- departments.csv: Contains department names and IDs
- order_products__prior.csv: Contains previous order contents for all customers
- order_products__train.csv: Contains order contents for the training set of customers
- orders.csv: Contains all orders, including order IDs, user IDs, order number, and other order details
- products.csv: Contains product names, IDs, and associated aisle and department IDs

## Usage
These raw data files should not be modified. All data cleaning, preprocessing, and feature engineering should be performed on copies of these files, with the results stored in the `processed` directory.

## Source
The data is sourced from the "The Instacart Online Grocery Shopping Dataset 2017", accessed via [Kaggle](https://www.kaggle.com/c/instacart-market-basket-analysis).

## Notes
- Due to the large size of these files, they are not included in the Git repository. 
- To reproduce the analysis, download the dataset from the source mentioned above and place the files in this directory.
- Ensure you comply with Instacart's terms of use when using this data.
