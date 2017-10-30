# -*- coding: utf-8 -*-

import dark_horse.data.db_util as db_util
from urllib.parse import urlparse
import mysql.connector

def test_insert_data():
    db_uri = "mysql://miyanishi:miyanishi@127.0.0.1/horse"
    table_name = "insert_test"

    url = urlparse(db_uri)
    conn = mysql.connector.connect(
        host = url.hostname or 'localhost',
    port = url.port or 3306,
    user = url.username or 'miyanishi',
    password = url.password or 'miyanishi',
    database = url.path[1:]
    )
    cursor = conn.cursor()
    cursor.execute("drop table if exists insert_test")
    cursor.close()

    map_list = []
    map_list.append({"abc":111, "def":"test1"})
    map_list.append({"abc":235, "def":"test3"})

    db_util.insert_data(db_uri, table_name, map_list)

    cursor = conn.cursor()
    cursor.execute("select abc, def from insert_test")
    for row in cursor.fetchall():
        if row[0] == 111:
            assert row[1]=="test1"
        elif row[0] == 235:
            assert row[1]=="test3"
        else:
            assert False
    cursor.close()

    cursor = conn.cursor()
    cursor.execute("drop table insert_test")
    cursor.close()
