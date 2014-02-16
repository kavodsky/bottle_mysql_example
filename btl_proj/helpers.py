#!/usr/bin/env python

import MySQLdb

class MySQLConnect(object):

    def __init__(self):
        self.db = None        

    def connect(self, host="localhost", user="root", passwd="q", db="employees"):
        self.db = MySQLdb.connect(host, user, passwd, db)
        
    def execute(self, query):
        if self.db == None:
            self.connect()
        cur = self.db.cursor()
        cur.execute(query)
        rows = cur.fetchall()
        cur.close()
        return rows
