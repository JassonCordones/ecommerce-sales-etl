# E-commerce Sales ETL Pipeline

This project shows how to build a daily ETL pipeline that:
1. Uploads raw sales data to S3
2. Loads it into Snowflake using Airflow

## Tech Stack
- Snowflake
- Apache Airflow
- AWS S3
- Python (Pandas, Boto3)

## Getting Started
- Create a Snowflake account & table from `schema.sql`
- Add credentials to `.env`
- Run upload script
- Launch Airflow with `docker-compose up`
- Trigger DAG `etl_s3_to_snowflake`

## DAG Flow
[upload_csv] --> [create_stage] --> [copy_into_sales]
