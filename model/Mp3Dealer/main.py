# -*- coding:utf-8 -*-
# __author__='LiGang'
import os

from common.common_mp3 import changeMp3Tag, getRecordTime, getReadingTimeInterval

PATH_LUYINBI_ROOT = "E:/Music/录音笔"
PATH_RENSHENGZHIYOUYIJIANSHI = "E:/Music/录音笔/《人生只有一件事》-金惟纯/"
PATH_XINDAOSHENGHEFUDEYISHENGZHUTUO = "E:/Music/录音笔/《心，稻盛和夫一生嘱托》-稻盛和夫/"
PATH_RENJIANZHIDE = "E:/Music/录音笔/《人间值得》-中村恒子、奥田弘美/"

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


def deal_Mp3_20230623():
    path = "E:/Music/录音笔/《人间值得》-中村恒子、奥田弘美/"
    files = os.listdir(path)
    names = [
        '前言',
        '笔者的话',
        '第1章 工作是为了什么 01 “为了钱而工作”，这是理所当然的',
        '02 在思考“这份工作不适合我”之前，先试着挑战一下。不那样的话，人就会止步不前',
        '03 即使你不喜欢工作，也没有关系，尽可能去做总比瞎想强',
        '04 工作的去留自己决定，别人无从干涉',
        '故事1 终战之前，一名少女独自从广岛前往大阪',
        '第2章 不要期待过多，对生活中的小事心存感激 05“必须要幸福”，不这样想的话才会幸福，放下人生多余的行囊',
        '06 不强求改变别人，不如把心力放在“自己如何才能快乐生活”',
        '07 即便是家人也要分清彼此，强迫他人，自己和对方都很痛苦',
        '08 不要认为别人的给予理所当然，感谢你所得到的，并且不再奢求更多',
        '09 尊重别人，别人也会尊重你',
        '10 机会源于偶然，如果有人助力，就顺势而为',
        '故事2 虽经历时代煎熬，却无悔地走上医生的道路',
        '第3章 恰到好处的人际关系 11 如果悲伤时有人倾听，将有助于恢复心情',
        '12 不要小气，接受小小的请求，让微小的善意流转',
        '13 争执之后先道歉才是胜者，如果一遇事就发飙，你将无法立足',
        '14 交朋友要根据自己的喜好来选择，通过权衡得失来交往是不可取的',
        '15 和那个人该交往还是远离，不要急于寻找答案，调整心理的距离感就够了',
        '16 就算一个人设计好自己的生活方式，也不会照着做，因此，人生没必要详细计划',
        '故事3 为什么精神科医生成为我的终身职业',
        '第4章 让心归于平静 17 对未来担心也没用，你有忽略眼前的事吗？我只关心眼前的事',
        '18 痛苦会成为今后重要的经验，所以一次也不要浪费',
        '19 接连发生不顺的时候，也不要停下脚步，停下来就无法前进',
        '20 晚上好好睡觉，确有急事时快速处理，其他一概不管',
        '21 “没有自信”并非坏事，盲目自信才是最危险的',
        '22 从悲伤或打击中走出来，要依靠“日药”而非建议',
        '23 人很难不与他人比较，即便健康有活力的人，未必没有烦恼',
        '24 不得不努力的时刻，一定会到来。所以，如果不是这样的时候，就无须太过努力',
        '故事4 从结婚、生孩子、当家庭主妇到重新上班',
        '第5章 生活和工作的平衡之道 25 工作质量不完美没关系，调整思路也可以，关键是不要中途放弃',
        '26 家庭和睦比什么都重要，只要守护它，其他都会慢慢变好',
        '27 人生常常需要忍耐，思考可以轻松忍耐的方法',
        '28 所谓育儿，其实也是成长',
        '29 对于养育孩子，比起技巧，更重要的是行动',
        '30 不要阻碍别人自立，如果全面掌控，成长就会停止',
        '31 孤独地死去非常好，担心死亡的方式毫无意义',
        '故事5 烦恼、痛苦，即使在人生最糟糕的时候，也必须持续工作',
        '第6章 简单生活每一天 32 遇到困难时要想“没关系，一定会有办法的”',
        '33 他人有他人的人生，自己有自己的人生，界限分明，冲突、压力就会减少',
        '34 人际关系的秘密在于“距离感”，不可逾越的界限，一定要保持住',
        '35 孤独不等于寂寞，接受孤独的美妙，生活处处有乐趣',
        '36 事情不会马上有结果，焦虑的时候心里不要七上八下，也不要思考过去和未来，而是珍惜当下',
        '故事6 送走丈夫后，即使上了年纪依然是被需要的“工作之神”',
        '37 不求功成名就，只要能照亮某个角落就够了',
        '笔者后记：莲花微动',
    ]

    files.sort()
    print(files)

    #return

    #for f in files:
    #    if f.startswith('0'):
    #        print('\''+f[14:].replace('.mp3', '')+'\',')
    print(len(files))


    for idx, file in enumerate(files):
        sidx = '%03d' % idx

        if not file.startswith(sidx):
            print(sidx)


        fname = '%s. %s.mp3' % (sidx,  names[idx])

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

    #deal_Mp3_20230623()
    #changeMp3Tag(PATH_RENJIANZHIDE)


