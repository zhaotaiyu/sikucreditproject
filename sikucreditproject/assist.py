# -*- coding: utf-8 -*-
import psycopg2
def getnum():
	num = []
	db=psycopg2.connect(database="sikuyitest", user="postgres", password="sikuyi", host="ecs-a025-0002", port=54321)
	cursor=db.cursor()
	sql="SELECT record_num FROM behavior_item"
	try:
		cursor.execute(sql)
		reslist = cursor.fetchall()
		for row in reslist:
			msg = ''.join(row).strip()
			if msg:
				num.append(msg)
	except Exception as e:
	    db.rollback()
	cursor.close()
	db.close()
	return num