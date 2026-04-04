from airflow.sdk import dag, task
from pendulum import datetime
from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator
from airflow.providers.amazon.aws.hooks.s3 import S3Hook
from airflow.sdk.definitions.context import get_current_context
from src.etl.extraction.extraction import Extractor


@dag(
    dag_id="process_studies",
    start_date=datetime(2026, 2, 16),
    catchup=False,
    schedule=None,
    tags=["ctgov"],
    template_searchpath=["/opt/airflow/src"],
)
def process_ct_gov():

    @task
    def extract_ctgov():
        context = get_current_context()
        s3_hook = S3Hook(aws_conn_id="aws_airflow")

        e = Extractor(context=context, s3_hook=s3_hook)

        return e.make_requests()


    extract_task = extract_ctgov()



process_ct_gov()
