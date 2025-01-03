# Sales Commission Calculation

## Description
This program is designed to calculate commissions, performance incentives, and product points based on sales data at various managerial hierarchy levels: Sales Person (SP), Sales Manager (SM), and General Manager (GM). The program reads data from an Excel file, processes it, and generates results based on predefined rules.

## Requirements
Ensure you have installed:
- Python 3.10
- The following libraries:
  - `numpy`
  - `pandas`

### How to Install Libraries
Use the following command to install the required libraries:
```bash
pip install numpy pandas
```

## How to Run the Application
To run the program, use the following command:
```bash
python3 index.py
```

## Program Flow
The program processes data in three managerial levels: SP, SM, and GM. Below is the flow:

1. **Data Reading:**
   - The program reads the sales data from an Excel file named `sales_commission_data.xlsx`.
   - The data is grouped and sorted by SP, SM, and GM levels.

2. **Data Aggregation:**
   - **SP Level:**
     - Calculates `product_point` and `sales_point` for each SP based on the products they sold.
     - Determines the commission and performance incentive for SP.
   - **SM Level:**
     - Aggregates the `product_point` and `sales_point` from all active SPs under each SM.
     - Determines the commission and performance incentive for SM based on these aggregated values.
   - **GM Level:**
     - Aggregates the `product_point` and `sales_point` from all active SMs under each GM.
     - Determines the commission and performance incentive for GM based on these aggregated values.

3. **Calculation Rules:**
   - Product Points and Sales Points are determined by the type and quantity of products sold.
   - Each managerial level has specific rules for calculating:
     - **Commission Points**
     - **Performance Incentives**
   - These rules are predefined and coded into the program.

4. **Output:**
   - The program outputs processed data for each managerial level, including:
     - Name
     - Managerial Level
     - Total `product_point`
     - Total `sales_point`
     - Commission Points
     - Performance Incentives
     - Basic Commission

## Excel Data Structure
The Excel file `sales_commission_data.xlsx` should have the following columns:
- `SP`: Name of the Sales Person.
- `Item`: Product name (e.g., Red, Blue, Yellow).
- `SO`: Sales Order number.
- `SM`: Name of the Sales Manager.
- `GM`: Name of the General Manager.

## Example
### Input Data (Excel):
| SP      | Item   | SO   | SM       | GM        |
|---------|--------|------|----------|-----------|
| John    | Red    | 001  | Michael  | Jessica   |
| Sarah   | Blue   | 002  | Michael  | Jessica   |
| Daniel  | Yellow | 003  | Sophia   | Benjamin  |

### Processed Output:
#### SP Level:
- John:
  - `product_point`: 5000
  - `sales_point`: 1
  - `commission_point`: 75
  - `performance_incentive`: 0
  - `basic_commission`: 375

#### SM Level:
- Michael:
  - Aggregates points from John and Sarah.
  - `product_point`: 15000
  - `sales_point`: 3
  - `commission_point`: 75
  - `performance_incentive`: 100000

#### GM Level:
- Jessica:
  - Aggregates points from Michael.
  - `product_point`: 15000
  - `sales_point`: 3
  - `commission_point`: 75
  - `performance_incentive`: 300000

This README provides a comprehensive guide to understanding and running the program effectively.

