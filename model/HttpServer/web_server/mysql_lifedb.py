# -*- coding:utf-8 -*-
# __author__='LiGang'

from config.config_logging import setup_logger
from ggsdk.mysql import common_pymysql
from conf import lifedb_conf

def init_life_dbw():
    mysql_logger = setup_logger("web_server", "/mysql/", "lifedb")
    dbw = common_pymysql.MysqlClientPool(dbuser=lifedb_conf.dbuser,
                                         dbpass=lifedb_conf.dbpass,
                                         pool_size=lifedb_conf.pool_size,
                                         cls_name=common_pymysql.MysqlConnection,
                                         host=lifedb_conf.host,
                                         port=lifedb_conf.port,
                                         dbname=lifedb_conf.dbname,
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


life_dbw = init_life_dbw()


