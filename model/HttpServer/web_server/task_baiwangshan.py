# -*- coding:utf-8 -*-
# __author__='LiGang'
import os
import sys
import datetime
from flask import render_template, request, redirect, url_for, make_response, jsonify, Blueprint
from model.HttpServer.web_server.mysql_lifedb import life_dbw
from flask_login import login_required

sys.path.append(os.getcwd() + '/HttpServer/')

baiwangshan_job = Blueprint('baiwangshan', __name__)

@baiwangshan_job.route('/list_bws', methods=['POST', 'GET'])  # 添加路由
@login_required
def list_bws():
    print("ip:", request.remote_addr, request.remote_user)
    tab_datas = life_dbw.get_data(table='bai_wang_shan_info', orderby="mdate, id")

    data_list = []

    total_idx = 1
    month_idx = 1
    current_month = 0
    for idx, element in enumerate(tab_datas):
        date_str = element["mdate"].strftime("%Y-%m-%d")
        if element["mdate"].month != current_month:
            month_idx = 1
            current_month = element["mdate"].month

        data_list.append({
            "total_idx": total_idx,
            "month_idx": month_idx,
            "date_str": date_str,
            "id": element["id"]
        })
        total_idx += 1
        month_idx += 1

    data_list.reverse()

    default_daystr = request.args.get("make_date", datetime.datetime.now().strftime("%Y-%m-%d"))


    return render_template('web_server/list_baiwangshan.html',
                           data_list=data_list,
                           default_daystr=default_daystr
                           )


@baiwangshan_job.route('/add_bws', methods=['POST', 'GET'])  # 添加路由
@login_required
def add_bws():
    make_date = request.args.get("make_date", "")


    val_dict = {
        "mdate": make_date,
    }
    life_dbw.insert_data(table='bai_wang_shan_info', val_dict=val_dict, has_crtime=True)
    redirect_url = url_for('baiwangshan.list_bws', make_date=make_date)

    return redirect(redirect_url, code=302)


@baiwangshan_job.route('/delete_bws', methods=['POST', 'GET'])  # 添加路由
@login_required
def delete_bws():
    delid = request.args.get("delid", "")

    print("delid:", delid)
    life_dbw.delete_data_by_id(table='bai_wang_shan_info', idx=delid)

    return make_response("1")

