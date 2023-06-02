# -*- coding:utf-8 -*-
# __author__='ligang'
import json
import os.path
import re
from collections import defaultdict
from operator import itemgetter

from common import common_file, common_video
from common.common_file_ext import FileType
from ggsdk.mysql import common_pymysql
from ggsdk import utility, encoding
from config.config_logging import setup_logger


def generate_json_file_by_search_directory_files(src_path, json_file):
    print("read dirtories and files")
    all_dirs, all_files = common_file.getAllSubs(src_path)

    print("read from db")
    dbitems = dbw.get_data(table="adult_files", fields="file_name, drive_letter, file_path")
    already_insert = set()
    for item in dbitems:
        dir_path = item["drive_letter"] + ":" + item["file_path"] + "/" + item["file_name"]
        already_insert.add(dir_path)

    print("begin scan and insert...")

    fw = open(json_file, "w")
    total_cnt = len(all_files)
    for idx, absolute_path in enumerate(all_files):
        print("%d/%d: %s" % (idx, total_cnt, absolute_path))
        if not absolute_path:
            continue
        #if absolute_path in already_insert:
        #    continue
        drive_letter = absolute_path[0:1]
        file_path = os.path.dirname(absolute_path)[2:]

        file_name = os.path.basename(absolute_path)
        print(file_name)
        file_name = utility.str_to_unicode(file_name)
        #file_name = file_name.encode("utf-8")
        #print(file_name)

        download_time = common_file.get_file_crtime(absolute_path)
        file_size = common_file.getFileSize(absolute_path)
        if file_size >=  1024 * 1024:
            file_md5 = common_file.get_md5_of_big_file_prev1m(absolute_path)
        else:
            file_md5 = common_file.get_md5_of_small_file(absolute_path)

        file_ext, file_type = common_file.get_ext_and_filetype(absolute_path)
        if file_type == FileType.VIDEO:
            video_info = common_video.get_video_duration(absolute_path)
            video_duration = video_info.get("duration_ms", 0)
            video_duration = int(video_duration / 1000)
        else:
            video_duration = 0

        data_dict = {
            "file_name": file_name,
            "drive_letter": drive_letter,
            "file_path": file_path,
            "file_md5": file_md5,
            "file_size": file_size,
            "file_ext": file_ext,
            "file_type": int(file_type),
            "video_duration": video_duration,
            "download_time": download_time.strftime("%Y-%m-%d %H:%M:%S")
        }

        json_str = json.dumps(data_dict)
        fw.write(json_str)
        fw.write("\t\t\t\t")

    fw.close()

    return all_files


def read_json_file_and_insert(json_file, life_dbw):

    fr = open(json_file, "r")
    json_str = fr.read()
    fr.close()

    l = json_str.split("\t\t\t\t")
    total_cnt = len(l)

    for idx, item in enumerate(l):

        item = item.strip()
        if not item:
            continue
        print("%d/%d: item=%s" % (idx, total_cnt, item))
        item_dict = json.loads(item)
        #print(item_dict["file_name"])

        if item_dict.get("video_duration", 0) > common_pymysql.MAX_UNSIGNED_INT or item_dict.get("video_duration", 0) < 0:
            item_dict["video_duration"] = 0
        life_dbw.insert_data(table="adult_files", val_dict=item_dict, has_crtime=True)




def search_and_insert_directory_files(src_path, dbw):
    print("read dirtories and files")
    all_dirs, all_files = common_file.getAllSubs(src_path)

    print("read from db")
    dbitems = dbw.get_data(table="adult_files", fields="file_name, drive_letter, file_path")
    already_insert = set()
    for item in dbitems:
        dir_path = item["drive_letter"] + ":" + item["file_path"] + "/" + item["file_name"]
        already_insert.add(dir_path)

    print("begin scan and insert...")



    total_cnt = len(all_files)
    for idx, absolute_path in enumerate(all_files):
        print("%d/%d: %s" % (idx, total_cnt, absolute_path))
        if not absolute_path:
            continue
        if absolute_path in already_insert:
            continue
        drive_letter = absolute_path[0:1]
        file_path = os.path.dirname(absolute_path)[2:]
        file_name = os.path.basename(absolute_path)

        download_time = common_file.get_file_crtime(absolute_path)
        file_size = common_file.getFileSize(absolute_path)
        if file_size >= 100 * 1024 * 1024:
            file_md5 = common_file.get_md5_of_big_file_prev1m(absolute_path)
        else:
            file_md5 = common_file.get_md5_of_small_file(absolute_path)

        file_ext, file_type = common_file.get_ext_and_filetype(absolute_path)
        if file_type == FileType.VIDEO:
            video_info = common_video.get_video_duration(absolute_path)
            video_duration = video_info.get("duration_ms", 0)
            video_duration = int(video_duration / 1000)
        else:
            video_duration = 0

        data_dict = {
            "file_name": file_name,
            "drive_letter": drive_letter,
            "file_path": file_path,
            "file_md5": file_md5,
            "file_size": file_size,
            "file_ext": file_ext,
            "file_type": int(file_type),
            "video_duration": video_duration,
            "download_time": download_time
        }

        dbw.insert_data(table="adult_files", val_dict=data_dict, has_crtime=True)

    return all_files


def get_video_pre_tags(file_name: str = "") -> list:
    idx1 = file_name.find("[")
    if idx1 < 0:
        return []

    r = []
    while idx1 >= 0:
        idx2 = file_name.find("]", idx1 + 1)
        if idx2 < 0:
            break
        r.append(file_name[idx1 + 1:idx2].upper())

        idx1 = file_name.find("[", idx2 + 1)

    return r


def stat_pre_tags(life_dbw: common_pymysql.MysqlClientPool) -> defaultdict(int):
    stat_dict = defaultdict(int)

    idx = 0
    while 1:
        items = life_dbw.get_data(table="adult_files",
                                  fields="id, file_name",
                                  conditions=["id > %d"],
                                  condvalues=[idx],
                                  orderby="id",
                                  limit=1000)
        if not items:
            break

        for item in items:
            tags = get_video_pre_tags(item.get("file_name", ""))
            for tag in tags:
                stat_dict[tag] += 1

        idx = items[-1]["id"]
    return stat_dict


def insert_feature_type(stat_dict: defaultdict(int)):
    tag_list = []
    for tag, cnt in stat_dict.items():
        tag_list.append({"tag": tag, "cnt": cnt})

    tag_list.sort(key=itemgetter('cnt'), reverse=True)

    for idx, item in enumerate(tag_list):
        feature_id = idx + 1
        feature_desc = item.get("tag", "")


def get_tag_of_videoes(life_dbw):
    search_items = life_dbw.get_data(table="adult_files", fields="id, file_name, file_ext", conditions=["file_type=1"])
    print(len(search_items))

    stat_dict = defaultdict(list)
    unit_list = []
    for item in search_items:
        afid = item.get("id", 0)
        file_name = item.get("file_name", "")
        file_ext = item.get("file_ext", "")
        if not file_name or not file_ext:
            continue

        file_name = file_name[0:len(file_name)-len(file_ext)-1]

        unit_no = re.findall('([a-zA-Z]{2,5}[- _][0-9]{2,5})', file_name)
        if unit_no:
            unit_list.append([unit_no[0], file_name, afid])

        if not file_name.startswith("["):
            continue
        if "-" not in file_name and file_name[-1] != "]":
            continue

        idx1 = 0
        idx2 = 0
        while 1:
            idx1 = file_name.find("[", idx2)
            if idx1 < 0:
                break
            idx2 = file_name.find("]", idx1 + 1)
            if idx2 < 0:
                break

            tag = file_name[idx1 + 1: idx2]
            if not tag:
                continue

            tag = tag.upper()
            if tag.startswith("LCOUNT"):
                tag = "LCOUNT"
            if tag.startswith("KCOUNT"):
                tag = "KCOUNT"
            stat_dict[tag].append(file_name)

    tag_list = []
    for tag, names in stat_dict.items():
        tag_list.append({"tag": tag, "cnt": len(names), "names": names})

    print("tag count:", len(tag_list))
    tag_list.sort(key=itemgetter('cnt'), reverse=True)
    for tag_info in tag_list:
        print(tag_info)

    print("-" * 30)
    for unit_info in unit_list:
        unit_no, file_name, afid = unit_info[0], unit_info[1], unit_info[2]
        if " " in unit_no:
            l = unit_no.split(" ")
        elif "-" in unit_no:
            l = unit_no.split("-")
        elif "_" in unit_no:
            l = unit_no.split("_")
        else:
            continue
        unit_str = l[0]
        unit_num = int(l[1])
        val_dict = {
            "afid": afid,
            "unit_str": unit_str.upper(),
            "unit_num": unit_num
        }
        print(val_dict)

        life_dbw.insert_data(table="jap_unit_num", val_dict=val_dict, has_crtime=True)


def init_dbw():
    if not os.path.exists("./log/"):
        os.mkdir("./log/")
    mysql_logger = setup_logger("test_mysql", "./log/", "mysqldb")

    life_dbw = common_pymysql.MysqlClientPool(dbuser='root',
                                              dbpass='mysql_123456',
                                              pool_size=16,
                                              cls_name=common_pymysql.MysqlConnection,
                                              host='106.12.153.94',  # 百度云
                                              #host='192.168.87.15', # 虚拟机
                                              port=8306,
                                              dbname='life',
                                              enc='utf8mb4',
                                              logger=mysql_logger,
                                              timeout=15)

    return life_dbw


if __name__ == '__main__':
    dbw = init_dbw()

    #search_and_insert_directory_files(search_dir1, dbw)
    #generate_json_file_by_search_directory_files(search_dir1, "./json_file.txt")

    #read_json_file_and_insert("./json_file_V.txt", dbw)
    get_tag_of_videoes(dbw)


