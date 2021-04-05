import os
import sys
import argparse

from sodapy import Socrata

from config import mappings as es_mappings
from elastic_helper import (
    ElasticHelperException, 
    insert_doc,
    try_create_index,
)

parser = argparse.ArgumentParser(description='Data Processing')
parser.add_argument('--page_size', type=int, required=True)
parser.add_argument('--num_pages', type=int)
args = parser.parse_args(sys.argv[1:])

"""

  
"""

DATASET_ID = "nc67-uf89"
APP_TOKEN = os.environ.get("APP_TOKEN")
ES_HOST = os.environ.get("ES_HOST") 
ES_USERNAME = os.environ.get("ES_USERNAME")
ES_PASSWORD = os.environ.get("ES_PASSWORD") 

if __name__ == '__main__':
    try:
        try_create_index(
            "violations7", 
            ES_HOST, 
            mappings=es_mappings,
            es_user=ES_USERNAME,
            es_pw=ES_PASSWORD,
        )
    except ElasticHelperException as e:
        print("Index already exists! skipping")
        print(f"{e}")
        

    
    for i in range(0, args.num_pages):
        rows = Socrata("data.cityofnewyork.us", APP_TOKEN).get(DATASET_ID, limit=args.page_size, offset=i*(args.page_size))
    # rows = client.get(DATASET_ID, )
    
        for row in rows:
            try:
                row["summons_number"] = float(row["summons_number"])
                row["fine_amount"] = float(row["fine_amount"])
                row["penalty_amount"] = float(row["penalty_amount"])
                row["interest_amount"] = float(row["interest_amount"])
                row["reduction_amount"] = float(row["reduction_amount"])
                row["payment_amount"] = float(row["payment_amount"])
                row["amount_due"] = float(row["amount_due"])
            except Exception as e:
                print("SKIPPING! Failed to transform row: {row}. Reason: {e}")
                continue
        
            try:
            # index_name, host, data=None, es_user=None, es_pw=None
                ret = insert_doc(
                    "violations7", 
                    ES_HOST,
                    data=row,
                    es_user=ES_USERNAME,
                    es_pw=ES_PASSWORD,
                )
                print(ret)
            except ElasticHelperException as e:
                print(e)

