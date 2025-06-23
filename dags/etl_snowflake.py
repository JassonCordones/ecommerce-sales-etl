from airflow import DAG
from airflow.providers.snowflake.operators.snowflake import SnowflakeOperator
from airflow.providers.amazon.aws.transfers.local_to_s3 import LocalFilesystemToS3Operator
from airflow.utils.dates import days_ago

default_agrs = {"owner":"airflow", "start_date":days_ago(1)}
dag = DAG("etl_s3_to_snowflake", schedule_interval="@daily", default_agrs=default_agrs)

upload = LocalFilesystemToS3Operator(
    task_id="upload_csv",
    filename="/opt/airflow/snowflake/sample_data.csv",
    dest_key="raw/sales.csv",
    dest_bucket="{{ var.value.s3bucket }}",
    aws_conn_id="aws_default",
    dag=dag
)

create_stage = SnowflakeOperator(
    task_id="create_stage",
    sql="""
        CREATE OR REPLACE STAGE {{ var.value.s3_stage_name }}
        URL='s3://{{ var.value.s3bucket }}/raw/'
        FILE_FORMAT = (TYPE = CSV FIELD_OPTIONALLY_ENCLOSED_BY = '"' SKIP_HEADER = 1);
    """,
    snowflake_conn_id="snowflake_default",
    dag=dag
)

copy_data = SnowflakeOperator(
    task_id="copy_into_sales",
    sql="""
    COPY INTO ecommerce.sales
    FROM @{{ var.value.s3_stage_name }}/sales.csv
    FILE_FORMAT = (TYPE = CSV FIELD_OPTIONALLY_ENCLOSED_BY = '"', SKIP_HEADER = 1)
    ON_ERROR = 'skip_file';
    """,
    snowflake_conn_id="snowflake_default",
    dag=dag
)

upload >> create_stage >> copy_data