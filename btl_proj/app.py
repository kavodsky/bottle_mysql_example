#!/usr/bin/env python
import os
import re
from bottle import Bottle, run, template, static_file, request
from helpers import MySQLConnect

CURRENT_PATH = os.path.abspath(os.path.dirname(__file__).decode("utf-8")) 
STATIC_PATH = os.path.join(CURRENT_PATH, "static")


app = Bottle()

@app.route("/")
def welcome():
    return template("index")

@app.route("/static/<filepath:path>")
def server_static(filepath):
    return static_file(filepath, root=STATIC_PATH)

@app.route("/salary")
def get_salary():
    name = request.query.name
    name = ''.join(re.findall("[a-zA-z]+", name))
    query = "SELECT * fROM employees WHERE last_name LIKE '{0}%' LIMIT 10".format(name)
    query = """ SELECT e.first_name, e.last_name, ROUND(s.salary, 2)
                 FROM employees as e
                 INNER JOIN 
                    (SELECT emp_no, AVG(salary) as salary
                     FROM salaries
                     GROUP BY emp_no) as s
                 USING(emp_no)                                                
                 WHERE e.last_name LIKE '{0}%'
                 LIMIT 10 """.format(name)

    rows = MySQLConnect().execute(query)    
    return template("stuff", rows=rows)


run(app, host="localhost", port=8000, debug=True, reloader=True)
