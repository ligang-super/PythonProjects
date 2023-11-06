# -*- coding:utf-8 -*-
# __author__='LiGang'
import os
import sys
import datetime
from flask import render_template, request, redirect, url_for, make_response, jsonify, Blueprint
from model.HttpServer.web_server.mysql_lifedb import life_dbw
from flask_login import login_required
from conf.web_server_conf import SAI_KE_SI_TYPES


sys.path.append(os.getcwd() + '/HttpServer/')

saikesi_job = Blueprint('saikesi', __name__)

@saikesi_job.route('/list_s', methods=['POST', 'GET'])  # 添加路由
@login_required
def list_s():
    print("ip:", request.remote_addr, request.remote_user)
    tab_datas = life_dbw.get_data(table='sai_ke_si_info', orderby="mdate desc,id desc")

    mtype_desc = {}
    for item in SAI_KE_SI_TYPES:
        mtype_desc[int(item["mtype"])] = item["mdesc"]

    data_list = []
    for element in tab_datas:
        sex_type = mtype_desc.get(element["mtype"], "None")

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
    minfo_list = SAI_KE_SI_TYPES

    return render_template('web_server/list_saikesi.html',
                           data_list=data_list,
                           minfo_list=minfo_list,
                           default_daystr=default_daystr,
                           default_type=default_type,
                           default_location=default_location,
                           default_user=default_user)


@saikesi_job.route('/add_s', methods=['POST', 'GET'])  # 添加路由
@login_required
def add_s():
    make_date = request.args.get("make_date", "")
    make_place = request.args.get("make_place", "")
    make_user = request.args.get("make_user", "")
    make_type = int(request.args.get("make_type", 1))
    if make_type == 0:
        make_user = ""

    print(make_date, make_place, make_user, make_type)

    val_dict = {
        "user_name": make_user,
        "mtype": make_type,
        "location": make_place,
        "mdate": make_date,
    }
    life_dbw.insert_data(table='sai_ke_si_info', val_dict=val_dict, has_crtime=True)
    redirect_url = url_for('saikesi.list_s', make_date=make_date, make_place=make_place, make_user=make_user,
                           make_type=make_type)

    return redirect(redirect_url, code=302)


@saikesi_job.route('/delete_s', methods=['POST', 'GET'])  # 添加路由
@login_required
def delete_s():
    delid = request.args.get("delid", "")

    print("delid:", delid)
    life_dbw.delete_data_by_id(table='sai_ke_si_info', idx=delid)

    return make_response("1")



