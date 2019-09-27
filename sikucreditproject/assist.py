# -*- coding: utf-8 -*-
import psycopg2
def getnum():
    num = []
    db=psycopg2.connect(database="cic_database", user="postgres", password="sikuyi", host="ecs-a025-0002", port=54321)
    cursor=db.cursor()
    sql="SELECT record_num FROM sikuyi.behavioritem"
    try:
        cursor.execute(sql)
        reslist = cursor.fetchall()
        for row in reslist:
            if row[0]:
                num.append(row[0])
    except Exception as e:
        db.rollback()
    cursor.close()
    db.close()
    return num