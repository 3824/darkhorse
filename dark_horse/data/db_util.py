# -*- coding: utf-8 -*-
import dataset

db_uri = "mysql://miyanishi:miyanishi@127.0.0.1/horse"
db = dataset.connect(db_uri)

def insert_search_result(map_list):
    table = db["search_result"]
    table.insert_many(map_list)
