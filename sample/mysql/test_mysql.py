#coding:utf-8
import os.path
import time
from operator import itemgetter
from collections import defaultdict
import pymysql
from common.mysql import common_pymysql
from config.config_logging import setup_logger


if __name__ == '__main__':
    print('Hello world!')
    print(os.getcwd())
    if not os.path.exists("../../model/Test/log/"):
        os.mkdir("../../model/Test/log/")
    mysql_logger = setup_logger("test_mysql", "../../model/Test/log/", "mysqldb")

    dbw = common_pymysql.MysqlClientPool(dbuser='root',
                                         dbpass='mysql_123456',
                                         pool_size=10,
                                         cls_name=common_pymysql.MysqlConnection,
                                         host='180.76.69.162',
                                         port=8306,
                                         dbname='life',
                                         enc='utf8mb4',
                                         logger=mysql_logger)
    if not dbw:
        print("dbw is none")
        exit(-1)

    r1 = dbw.get_data_by_id(table='sai_ke_si_info', idx=1)
    print(r1)

    rdata = dbw.get_data(table='sai_ke_si_info')
    print(rdata)

    '''
    ret = dbw.insert_data(table='test_table', val_dict={'uid': 100}, has_crtime=True)
    print(ret)
    r1 = dbw.get_data_by_id(table='test_table', idx=1)
    print(r1)

    r2 = dbw.get_data(table='test_table', conditions=['uid > %d'], condvalues=[5])
    print(r2)
    
    '''








