# -*- coding: utf-8 -*-
import dataset

db_uri = "mysql://miyanishi:miyanishi@127.0.0.1/horse"
db = dataset.connect(db_uri)

def insert_data(db_uri, table_name, map_list):
    db = dataset.connect(db_uri)
    table = db[table_name]
    table.insert_many(map_list)

def insert_search_result(map_list):
    insert_data(db_uri, "search_result", map_list)
