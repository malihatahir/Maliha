import os
import sys

from sodapy import Socrata

from config import mappings as es_mappings
from elastic_helper import (
    ElasticHelperException, 
    insert_doc,
    try_create_index,
)

"""

  
"""

DATASET_ID = "k397-673e"
APP_TOKEN = os.environ.get("APP_TOKEN")
ES_HOST = os.environ.get("ES_HOST") 
ES_USERNAME = os.environ.get("ES_USERNAME")
ES_PASSWORD = os.environ.get("ES_PASSWORD") 

if __name__ == '__main__':
    args = sys.argv[1:]
    
    limit = int(args[0])
    try:
        offset = int(args[1])
    except:
        offset = 0

    client = Socrata(
        "data.cityofnewyork.us",
        APP_TOKEN,
    )


    try:
        try_create_index(
            "payroll", 
            ES_HOST, 
            mappings=es_mappings,
            es_user=ES_USERNAME,
            es_pw=ES_PASSWORD,
        )
    except ElasticHelperException as e:
        print("Index already exists! skipping")
        print(f"{e}")
        
    
    rows = client.get(DATASET_ID, limit=limit, offset=offset, order=":id")
    
    
    for row in rows:
        try:
            row['fiscal_year'] = float(row['fiscal_year'])
            row['base_salary'] = float(row['base_salary'])
            row['regular_hours'] = float(row['regular_hours'])
            row['regular_gross_paid'] = float(row['regular_gross_paid'])
            row['ot_hours'] = float(row['ot_hours'])
            row['total_ot_paid'] = float(row['total_ot_paid'])
            row['total_other_pay'] = float(row['total_other_pay'])
        except Exception as e:
            print("SKIPPING! Failed to transform row: {row}. Reason: {e}")
            continue
        
        
        try:
            ret = insert_doc(
                "payroll", 
                ES_HOST,
                data=row,
                es_user=ES_USERNAME,
                es_pw=ES_PASSWORD,
            )
            print(ret)
        except ElasticHelperException as e:
            print(e)

