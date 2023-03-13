# -*- coding:utf-8 -*-
# __author__='LiGang'
import os

from common.common_mp3 import changeMp3Tag, getRecordTime, getReadingTimeInterval

PATH_LUYINBI_ROOT = "E:/Music/录音笔"
PATH_RENSHENGZHIYOUYIJIANSHI = "E:/Music/录音笔/《人生只有一件事》-金惟纯/"
PATH_XINDAOSHENGHEFUDEYISHENGZHUTUO = "E:/Music/录音笔/《心，稻盛和夫一生嘱托》-稻盛和夫/"

def deal_Mp3_20230211():
    path = "E:/Music/录音笔/《人生只有一件事》-金惟纯/"
    files = os.listdir(path)
    names = [ \
        '自序 学怎么活',
        '看不见自己',
        '不能做小事',
        '被宠坏的中年男人',
        '祸由想出',
        '子里的傲慢',
        '我感觉良好',
        '就跟你说过了 ',
        '颠倒了',
        '受自己',
        '生活需要空和闲',
        '君君臣臣，才能幸福',
        '半成品人生',
        '人生只有一件事',
        '放下评判心',
        '叫停的机制',
        '爱自己的方式',
        '选择焦虑',
        '从小事做起',
        '别错过百花齐放',
        '揪出不愿意',
        '修原意',
        '执念即地域',
        '管好念头',
        '找回真心',
        '逆境的三句咒语',
        '决定要快乐',
        '人生总是不得不',
        '好为人师',
        '人人都该改个性',
        '开窍之路',
        '如何放下',
        '怕麻烦才麻烦',
        '太多我认为',
        '自己最厉害',
        '为学日益，为道日损',
        '先搞定自己',
        '自我评分降为零',
        '在跟随中突破',
        '自我了解的镜子',
        '认错必修课',
        '听话的效能',
        '解忧之法',
        '被动人生未必不好',
        '认真求人',
        '一切都是最好的安排',
        '感谢的力量',
        '努力无极限',
        '站在巨人的肩膀上',
        '一百万分的人生',
        '学不讲道理',
        '学感同身受',
        '学面对脾气',
        '学说对不起',
        '学听话',
        '学说话',
        '学赞美',
        '学感恩',
        '学信任',
        '学助人',
        '学不计较',
        '学记名字',
        '善根',
        '母亲的苦肉计',
        '贵人正解',
        '怎样教出好孩子',
        '事事关心而不担心',
        '童蒙养正',
        '从家族业力中解脱',
        '成为你的样子',
        '从进食顺序开始',
        '父母难为的根源',
        '尽孝即进化',
        '甘愿受，欢喜做',
        '心真则事实，愿广则行深',
        '离苦得乐的药方',
        '像孩子一样',
        '培养洞察力',
        '任性误解，觉性突破',
        '以假修真（一）',
        '以假修真（二）',
        '恢复正常就对了',
        '把自己捐出去',
        '人生实业家',
        '五随人生观',
        '对人就不累',
        '活在当下就不忙',
        '事上练心',
        '开发内在，更有力量',
        '归零即突破',
        '都是我的错',
        '反求诸己',
        '领导者的考验',
        '以空间换时间',
        '给人空间',
        '用愿意换愿意',
        '带出愿意的团队',
        '企业的刚需',
        '企业文化是头等大事',
        '压力来自业力',
        '创新是果，不是因',
        '赚到做',
        '用脑太多，用心太少',
        '把公司卖给巴菲特',
        '传承之道',
        '向禅宗五祖学交班',
        '摆地摊，跑江湖',
        '玩真的，一定成',
        '真有效能',
        '最高效能的学习',
        '喜欢的威力',
        '企业要修简单',
        '成功恐惧症侯群',
        '追求极致价值',
        '组织的秘密',
        '后记 重返童年',
    ]

    files.sort()
    print(files)

    #for f in files:
    #    if f.startswith('0'):
    #        print('\''+f[14:].replace('.mp3', '')+'\',')
    print(len(files))


    dedup = set()
    for idx, file in enumerate(files):
        sidx = '%03d' % idx

        if not file.startswith(sidx):
            print(sidx)

        if idx < 30:
            if names[idx] not in file:
                print('ERROR: %d' % idx)
            continue
        if idx >= 30 and idx < 41:
            start_title = 'P2C04S'
        elif idx >= 30 and idx < 41:
            start_title = 'P2C04S'
        elif idx >= 41 and idx < 50:
            start_title = 'P2C05S'
        elif idx >= 50 and idx < 62:
            start_title = 'P2C06S'
        elif idx >= 62 and idx < 73:
            start_title = 'P3C07S'
        elif idx >= 73 and idx < 85:
            start_title = 'P3C08S'
        elif idx >= 85 and idx < 97:
            start_title = 'P3C09S'
        elif idx >= 97:
            start_title = 'P3C10S'

        if start_title not in dedup:
            dedup.add(start_title)
            section_idx = 1
        else:
            section_idx += 1

        fname = '%s. %s%02d %s.mp3' % (sidx, start_title, section_idx, names[idx])

        print(fname)

        os.rename(path+file, path+fname)


def statReadingTime():
    reading_ignore_dir = [
        "E:/Music/录音笔/录音备份/",
        "E:/Music/录音笔/LeetCode/",
        "E:/Music/录音笔/爸爸妈妈和可乐/",
        "E:/Music/录音笔/大周仙吏/",
        "E:/Music/录音笔/面试/",
        "E:/Music/录音笔/我的小说/",
        "E:/Music/录音笔/讲书/",
    ]
    getRecordTime(path=PATH_LUYINBI_ROOT, mode='year', ignore_dir=reading_ignore_dir)
    getReadingTimeInterval(PATH_LUYINBI_ROOT)

if __name__ == '__main__':
    statReadingTime()
    #deal_Mp3_20230211()
    #changeMp3Tag(PATH_RENSHENGZHIYOUYIJIANSHI)
    #changeMp3Tag(PATH_XINDAOSHENGHEFUDEYISHENGZHUTUO)


