#! /usr/bin/python

import yfinance as yf
import json
import boto3
import os
import subprocess
import sys
import pandas as pd

data = yf.download(tickers='TSLA', period='1d', interval='15m')
json_data = data.reset_index().to_json(orient='records')

kinesis = boto3.client('kinesis', region_name='us-east-2')

for article in json.loads(json_data):
    article_json = json.dumps(article)
    kinesis.put_record(StreamName='TSLA-Stock-Stream',Data =article_json,PartitionKey='partitionkey')
