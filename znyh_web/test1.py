from django.http import HttpResponse
from django.shortcuts import render
import pymysql
import time


def hello(request):
    return HttpResponse("Hello World !")


def state(request):
    context = {}
    db = pymysql.connect("127.0.0.1", "root", "admin", "fengxiang")
    cursor = db.cursor()
    sql = '''select tem,hum,time from state 
             order by id desc 
             limit 1
        '''
    try:
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
        for i in result:
            print(i)
            tem = i[0]
            tem = str(tem)
            hum = i[1]
            hum = str(hum)
            rtime = i[2]
            # print(tem + "--" + hum)
            # print(type(tem))
            # print(type(hum))
            # print(type(rtime))

            # 时间戳转换为日期
            rtime = int(rtime)
            rtime = float(rtime/1000)
            print(type(rtime))
            timeArray = time.localtime(rtime)
            dtime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
            print(type(dtime))
            print(dtime)

            context['tem'] = tem
            context['hum'] = hum
            context['time'] = dtime
    except:
        print("error!")

    db.close()

    return render(request, "znyh_web/index.html", context)




