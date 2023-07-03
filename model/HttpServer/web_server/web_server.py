# -*- coding:utf-8 -*-
# __author__='LiGang'
import os
import sys
import datetime
from datetime import timedelta
from flask import Flask, render_template, request, redirect, url_for, make_response, jsonify

from config.config_logging import setup_logger
from ggsdk.mysql import common_pymysql

sys.path.append(os.getcwd() + '/HttpServer/')

server = Flask(__name__, template_folder='../templates', static_folder='../static')
# 设置静态文件缓存过期时间
server.config.send_file_max_age_default = timedelta(seconds=1)


@server.route('/list_s', methods=['POST', 'GET'])  # 添加路由
def list_s():
    global life_dbw
    print("ip:", request.remote_addr, request.remote_user)
    tab_datas = life_dbw.get_data(table='sai_ke_si_info', orderby="id desc")

    data_list = []
    for element in tab_datas:
        if element["mtype"] == 0:
            sex_type = "Lu"
        elif element["mtype"] == 1:
            sex_type = "Wai"
        elif element["mtype"] == 2:
            sex_type = "Kou"
        elif element["mtype"] == 3:
            sex_type = "Nei"
        elif element["mtype"] == 4:
            sex_type = "Tun"
        else:
            sex_type = "None"

        date_str = element["mdate"].strftime("%Y-%m-%d")
        data_list.append({
            "sex_type": sex_type,
            "date_str": date_str,
            "who": element["user_name"],
            "where": element["location"],
            "id": element["id"]
        })

    default_daystr = request.args.get("make_date", datetime.datetime.now().strftime("%Y-%m-%d"))
    default_location = request.args.get("make_place", "北京")
    default_user = request.args.get("make_user", "Hua")
    default_type = request.args.get("make_type", "1")

    return render_template('web_server/list_saikesi.html',
                           data_list=data_list,
                           default_daystr=default_daystr,
                           default_type=default_type,
                           default_location=default_location,
                           default_user=default_user)


@server.route('/add_s', methods=['POST', 'GET'])  # 添加路由
def add_s():
    global life_dbw

    make_date = request.args.get("make_date", "")
    make_place = request.args.get("make_place", "")
    make_user = request.args.get("make_user", "")
    make_type = request.args.get("make_type", 1)
    print(make_date, make_place, make_user, make_type)

    val_dict = {
        "user_name": make_user,
        "mtype": int(make_type),
        "location": make_place,
        "mdate": make_date,
    }
    life_dbw.insert_data(table='sai_ke_si_info', val_dict=val_dict, has_crtime=True)
    redirect_url = url_for('list_s', make_date=make_date, make_place=make_place, make_user=make_user,
                           make_type=make_type)

    return redirect(redirect_url, code=302)


@server.route('/delete_s', methods=['POST', 'GET'])  # 添加路由
def delete_s():
    global life_dbw

    delid = request.args.get("delid", "")

    print("delid:", delid)
    life_dbw.delete_data_by_id(table='sai_ke_si_info', idx=delid)

    return make_response("1")


def init_life_dbw():
    mysql_logger = setup_logger("web_server", "/mysql/", "lifedb")
    dbw = common_pymysql.MysqlClientPool(dbuser='root',
                                         dbpass='mysql_123456',
                                         pool_size=10,
                                         cls_name=common_pymysql.MysqlConnection,
                                         host='106.12.153.94',
                                         port=8306,
                                         dbname='life',
                                         enc='utf8mb4',
                                         logger=mysql_logger)
    if not dbw:
        print("dbw is none")
        exit(-1)

    r1 = dbw.get_data_by_id(table='sai_ke_si_info', idx=1)
    print(r1)

    # rdata = dbw.get_data(table='sai_ke_si_info')
    # print(rdata)

    '''
    ret = dbw.insert_data(table='test_table', val_dict={'uid': 100}, has_crtime=True)
    print(ret)
    r1 = dbw.get_data_by_id(table='test_table', idx=1)
    print(r1)

    r2 = dbw.get_data(table='test_table', conditions=['uid > %d'], condvalues=[5])
    print(r2)

    '''
    return dbw


life_dbw = None

if __name__ == '__main__':
    life_dbw = init_life_dbw()
    server.run(host='0.0.0.0', port=8999, debug=False)
