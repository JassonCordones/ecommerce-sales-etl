CREATE OR REPLACE table ecommerce.sales(
    invoice_no      STRING,
    stock_code      STRING,
    description     STRING,
    quantity        INTEGER,
    invoice_date    TIMESTAMP,
    unit_price      FLOAT,
    customer_id     STRING,
    country         STRING
);