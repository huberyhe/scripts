#!/usr/bin/env python
# -*- coding: utf-8 -*-

import MySQLdb

db = MySQLdb.connect("localhost", "root", "123456", "blog")
cursor = db.cursor()

# common sql execute
cursor.execute("SELECT VERSION()")
data = cursor.fetchone()
print "Database version : %s" % data

# insert
sql = 'INSERT INTO users (username, password, role, created, modified) values ("%s", password(%s), "reader", now(), now())' % ("tom", "123456")
try:
    cursor.execute(sql)
    print "%d rows affected" % cursor.rowcount
    db.commit()
except:
    db.rollback()

# query
sql = "SELECT * FROM users"
try:
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
        username = row[1]
        role = row[3]
        created = row[4]
        print "user %s was created at %s as %s" % (username, created, role)
except Exception, e:
    print "Err querying!", e

cursor.close()
db.close()
