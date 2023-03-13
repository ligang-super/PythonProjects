import time

import requests
import datetime
import json
import hashlib
import xml.dom.minidom
import os
from collections import defaultdict
import shutil
import requests
import cv2
import requests
from PIL import Image

from common import common_file

def getPkgname(xmlpath):
    try:
        dom = xml.dom.minidom.parse(xmlpath)
        root = dom.documentElement
        elementLists = root.childNodes
    except Exception as e:
        print("[ERROR] Fail to parse xml : " + xmlpath)
        return None

    for node in elementLists:
        if isinstance(node, xml.dom.minidom.Element):
            pkgname = node.getAttribute('package')
            if pkgname != 'com.android.systemui':
                return pkgname

    return None


def getDirtoryPkgnames(dir=''):
    d = defaultdict(int)

    path = 'D:\\场景识别\\场景识别布局和截图数据\\3\\'
    filelist = os.listdir(path)
    for idx, fname in enumerate(filelist):
        if idx % 100 == 0:
            print('%d/%d' % (idx, len(filelist)))
        if fname.endswith('.xml'):
            pkgname = getPkgname(path + fname)

            d[pkgname] += 1

        # if idx >= 10000:
        #    break

    with open('res.txt', 'w') as f:
        for k, v in d.items():
            f.write('%s#%d\n' % (k, v))


def splitDataByPkgnames(dir=''):
    path = 'D:\\场景识别\\场景识别布局和截图数据\\3\\'
    newpath = 'D:/场景识别/场景识别布局和截图数据/data/'
    filelist = os.listdir(path)
    for idx, fname in enumerate(filelist):
        if idx % 100 == 0:
            print('%d/%d' % (idx, len(filelist)))
        if fname.endswith('.xml'):
            pkgname = getPkgname(path + fname)
            if not pkgname or pkgname in ('con.jdk.iih14', ):
                continue

            jpgname = fname.replace('.xml', '.jpg')
            if os.path.exists(path + jpgname):
                if pkgname.startswith('com.'):
                    prefix5 = pkgname[0:5]
                else:
                    prefix5 = '_0com'

                _tmppath = newpath + prefix5 + '/' + pkgname
                if not os.path.exists(_tmppath):
                    #print('not exist')
                    os.mkdir(_tmppath)
                #print(_tmppath)
                shutil.move(path + fname, _tmppath + '/' + fname)
                shutil.move(path + jpgname, _tmppath + '/' + jpgname)


    with open('res.txt', 'w') as f:
        for k, v in d.items():
            f.write('%s#%d\n' % (k, v))


def dedupDataByXml(src, dest):

    s = set()

    if not src.endswith('/') and not src.endswith('\\'):
        src += '/'
    if not dest.endswith('/') and not dest.endswith('\\'):
        dest += '/'

    filelist_dest = os.listdir(dest)
    md5 = hashlib.md5()
    for idx, fname in enumerate(filelist_dest):
        if idx % 100 == 0:
            print('%d/%d' % (idx, len(filelist_dest)))
        if fname.endswith('.xml'):
            with open(dest + fname, 'rb') as f:
                data = f.read()

            if not data:
                continue

            md5.update(data)

            #print(md5.hexdigest())
            s.add(md5.hexdigest())

    filelist_src = os.listdir(src)

    for idx, fname in enumerate(filelist_src):
        if idx % 100 == 0:
            print('%d/%d' % (idx, len(filelist_src)))
        if fname.endswith('.xml'):
            with open(src+fname, 'rb') as f:
                data = f.read()

            md5.update(data)
            #print(md5.hexdigest())
            #s.add(md5.hexdigest())

            if md5.hexdigest() and md5.hexdigest() not in s:
                jpgname = fname.replace('.xml', '.jpg')
                if os.path.exists(src + jpgname):
                    s.add(md5.hexdigest())
                    shutil.move(src+fname, dest + fname)
                    shutil.move(src + jpgname, dest + jpgname)


def dedupDataByXml_remove(src):

    s = set()

    if not src.endswith('/') and not src.endswith('\\'):
        src += '/'

    #md5 = hashlib.md5()
    filelist_src = os.listdir(src)

    del_cnt = 0
    for idx, fname in enumerate(filelist_src):
        #if idx % 100 == 0:
        #    print('%d/%d' % (idx, len(filelist_src)))
        if fname.endswith('.xml'):
            with open(src+fname, 'rb') as f:
                data = f.read()

            data = data.decode()
            #print(md5.hexdigest())
            #s.add(md5.hexdigest())

            if data and data not in s:
                s.add(data)
            else:
                jpgname = fname.replace('.xml', '.jpg')
                os.remove(src + fname)
                os.remove(src + jpgname)
                del_cnt += 1

                #print('delete %s, %s' %  (fname, jpgname))

    print('Xml_remove %d' % del_cnt)



def getApkType():
    with open('D:/code/PaddlePaddle/Projects/dataDealer/res.txt', 'r') as f:
        lines = f.readlines()

    fw = open('apptype.txt', 'w')
    for line in lines:
        apkname = line.split('#')[0]
        print('------------------')
        print(apkname)
        url = 'https://app.diandian.com/app/4qpizuqeppegu7n/android?market=2&country=75&id=' + apkname
        content = requests.get(url).content
        content = content.decode()

        pos1 = content.find('<title>')

        if pos1 < 0:
            print('can not find <title>')
            continue
        pos2 = content.find('</title>', pos1)
        if pos2 < 0:
            print('can not find </title>')
            continue

        title = content[pos1 + 7:pos2]
        app = title.split('-')[0]
        if app == 'Server error':
            print('download %s failed' % url)
            continue
        print(app)

        #typestring_pos = content.find(typestring)
        #if typestring_pos < 0:
        #    continue


        pos1 = content.find('<span class=\"tag-item\" data-v-364c3759>')
        if pos1 < 0:
            print('can not find tag-item')
            continue

        pos2 = content.find('</span>', pos1)
        if pos2 < 0:
            print('can not find </span>')
            continue

        apptype = content[pos1+39:pos2]
        print(apptype)

        fw.write('%s\t%s\t%s\n' % (apkname, app, apptype))
        fw.flush()

        #break

    fw.close()

from operator import itemgetter

def sortResTxt():
    with open('res_back.txt', 'r') as f:
        lines = f.readlines()

    data = []
    for line in lines:
        l = line.split('#')
        data.append({'app': l[0], 'cnt': int(l[1])})

    data.sort(key=itemgetter('cnt'), reverse=True)
    #print(data)

    with open('res_sort.txt', 'w') as f:
        for d in data:
            f.write('%s#%d\n' % (d['app'], d['cnt']))

def dedupDataImg_remove(src):
    filelist = os.listdir(src)
    nplist = []

    total = len(filelist)
    delete_cnt = 0
    for fname in filelist:
        if fname.endswith('.jpg'):
            jpg_path = src + fname
            imgnp = cv2.imread(jpg_path)
            imgnp = cv2.resize(imgnp, (100, 100))

            find_equal = False
            for _img in nplist:
                equation = calc_equation(_img, imgnp)
                if equation > 0.95:
                    find_equal = True
                    break

            if find_equal:
                xml_path = jpg_path.replace('.jpg', '.xml')
                os.remove(jpg_path)
                os.remove(xml_path)
                delete_cnt += 1
            else:
                nplist.append(imgnp)

    print('    total=%d, delete=%d' % (total, delete_cnt))


def dedupImgs():
    all_dirs = []
    path = 'D:/scene_data/data/'
    path_f1 = os.listdir(path)
    for _dir1 in path_f1:
        path_f2 = os.listdir(path + _dir1)
        for _dir2 in path_f2:
            if _dir2.startswith('com.android'):
                continue
            all_dirs.append(path + _dir1 + '/' + _dir2 + '/')

    print('sub directory count is %d' % len(all_dirs))


    for _dir in all_dirs:
        if _dir < 'D:/scene_data/data/com.s/com.smile.gifmaker/':
            continue
        print('dealing %s' % _dir)
        dedupDataByXml_remove(_dir)
        continue

        dedupDataImg_remove(_dir)


def calc_equation(img1, img2, shape=(100, 100)):
    if img1.shape[0] == shape[0] and img1.shape[1] == shape[1]:
        pass
    else:
        img1 = cv2.resize(img1, shape)

    if img2.shape[0] == shape[0] and img2.shape[1] == shape[1]:
        pass
    else:
        img2 = cv2.resize(img2, shape)

    even_cnt = 0
    for i in range(shape[0]):
        for j in range(shape[1]):
            if img1[i][j].tolist() == img2[i][j].tolist():
                even_cnt += 1

    return float(even_cnt) / float(shape[0] * shape[1])


def getImgsCnt():
    all_dirs = []
    path = 'D:/scene_data/data/'
    path_f1 = os.listdir(path)
    for _dir1 in path_f1:
        path_f2 = os.listdir(path + _dir1)
        for _dir2 in path_f2:
            if _dir2.startswith('com.android'):
                continue
            absolute_path = path + _dir1 + '/' + _dir2 + '/'

            cnt = len(os.listdir(absolute_path))

            if cnt >= 0:
                all_dirs.append({'pkg': _dir2, 'cnt': cnt, 'path': absolute_path})


    all_dirs.sort(key=itemgetter('cnt'), reverse=True)

    #for i in all_dirs:
    #    dedupDataImg_remove(i['path'])

    with open('sorted_imgcnt.txt', 'w') as f:
        for i in all_dirs:
            f.write('%s\t%d\n' % (i['pkg'], i['cnt']))


def getImgWithXml(save_path='./'):
    if not os.path.exists(save_path):
        os.mkdir(save_path)
    save_path = save_path.replace('\\', '/')
    if not save_path.endswith('/'):
        save_path += '/'

    nowtime = datetime.datetime.now()
    fname = nowtime.strftime('%Y%m%d_%H%M%S')

    pngname = fname + '.png'
    jpgname = fname + '.jpg'
    xmlname = fname + '.xml'

    screenshot_url = 'http://127.0.0.1:7912/screenshot/0'
    hierarchy_url = 'http://127.0.0.1:7912/dump/hierarchy'

    _res1 = requests.get(url=screenshot_url)
    with open(save_path + pngname, 'wb') as fimg:
        fimg.write(_res1.content)

    img = Image.open(save_path + pngname)
    img = img.convert('RGB')

    img.save(save_path + jpgname)
    img.close()

    _res2 = requests.get(url=hierarchy_url)

    r = _res2.content
    d = json.loads(r.decode('UTF-8'))

    with open(save_path + xmlname, 'w', encoding='utf-8') as fxml:
        fxml.write(d['result'])

    print('DONE!')


def getImg(save_path='./', fname=''):
    screenshot_url = 'http://127.0.0.1:7912/screenshot/0'
    pngname = fname + '.png'
    jpgname = fname + '.jpg'

    _res1 = requests.get(url=screenshot_url)
    with open(save_path + pngname, 'wb') as fimg:
        fimg.write(_res1.content)

    img = Image.open(save_path + pngname)
    img = img.convert('RGB')

    img.save(save_path + jpgname)
    img.close()

def getXml(save_path='./', fname=''):
    hierarchy_url = 'http://127.0.0.1:7912/dump/hierarchy'
    xmlname = fname + '.xml'

    _res2 = requests.get(url=hierarchy_url)

    r = _res2.content
    d = json.loads(r.decode('UTF-8'))

    with open(save_path + xmlname, 'w', encoding='utf-8') as fxml:
        fxml.write(d['result'])


import multiprocessing

def is_same_xml(file1, file2):
    f1 = open(file1, 'rb')
    xml1 = f1.read()
    f1.close()

    f2 = open(file2, 'rb')
    xml2 = f2.read()
    f2.close()

    if xml1 == xml2:
        return True
    else:
        return False

def getImgWithXml_MutipleProcess(save_path='./'):
    if not os.path.exists(save_path):
        os.mkdir(save_path)
    save_path = save_path.replace('\\', '/')
    if not save_path.endswith('/'):
        save_path += '/'

    nowtime = datetime.datetime.now()
    fname = nowtime.strftime('%Y%m%d_%H%M%S')

    xml_process = multiprocessing.Process(target=getXml, args=(save_path, fname))
    xml_process.start()
    img_process = multiprocessing.Process(target=getImg, args=(save_path, fname))
    img_process.start()

    xml_process.join()
    img_process.join()

    last_xml = './last_xml.xml'
    if os.path.exists(last_xml):
        if is_same_xml(last_xml, save_path + fname + '.xml'):
            print('ERROR: get old xml!!!')
            os.remove(save_path + fname + '.jpg')
            os.remove(save_path + fname + '.png')
            os.remove(save_path + fname + '.xml')
        else:
            os.remove(last_xml)
            os.remove(save_path + fname + '.png')
            shutil.copyfile(save_path + fname + '.xml', last_xml)

    else:
        os.remove(save_path + fname + '.png')
        shutil.copyfile(save_path + fname + '.xml', last_xml)



    for i in range(5):
        print('DONE!')


def deletePng(path=''):
    dirs, files = common_file.getAllSubs(path)

    del_cnt = 0
    for file_path in files:
        if file_path.endswith('.png'):
            os.remove(file_path)
            print('delete %s' % file_path)
            del_cnt += 1

    print('total delte: %d' % del_cnt)




if __name__ == '__main__':
    print('----------dataDealer----------')

    #print(os.path.abspath(os.path.join(__file__, *(['..'] * 2))))


    #deletePng(path='D:/场景识别/场景识别布局和截图数据/标注')
    #dedupDataByXml('D:/场景识别/场景识别布局和截图数据/3', 'D:/场景识别/场景识别布局和截图数据/deduped')
    #getApkType()

    #splitDataByPkgnames()
    #sortResTxt()

    #dedupImgs()

    #getImgsCnt()

    #getImgWithXml('./apk')
    for i in range(1):
        getImgWithXml_MutipleProcess('./apk')
    #    for t in range(3):
    #        print(t)
            #time.sleep(1)

    #print('显示机型信息：')
    #os.system('C:/Users/ligang33/AppData/Local/Android/Sdk/platform-tools/adb.exe shell wm size')
    #os.system('C:/Users/ligang33/AppData/Local/Android/Sdk/platform-tools/adb.exe shell wm size')



