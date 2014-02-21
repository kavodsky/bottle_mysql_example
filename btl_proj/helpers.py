#!/usr/bin/env python

import MySQLdb

class MySQLConnect(object):

    def __init__(self, host="localhost", user="atti", passwd="q", db="employees"):
        self.host = host
	self.user = user
	self.passwd = passwd
	self.db = db
	self.db_conn = MySQLdb.connect(host, user, passwd, db)
        
    def execute(self, query):
        cur = self.db_conn.cursor()
        cur.execute(query)
        rows = cur.fetchall()
        cur.close()
        return rows
