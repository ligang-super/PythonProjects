# -*- coding:utf-8 -*-
# __author__='ligang'

import os
import sys
from common.common_download import download_html



html_temp = '''
<ul id="chapterList">           
            <li><a href="/b/154580/70949.html" title="贫僧不想当影帝 番外三 林嘉篇（7）" target="_blank">番外三 林嘉篇（7）</a></li>
            <li><a href="/b/154580/70948.html" title="贫僧不想当影帝 番外三 林嘉篇（6）" target="_blank">番外三 林嘉篇（6）</a></li>
            <li><a href="/b/154580/70751.html" title="贫僧不想当影帝 番外三 林嘉篇（5）" target="_blank">番外三 林嘉篇（5）</a></li>
            <li><a href="/b/154580/70629.html" title="贫僧不想当影帝 番外三 林嘉篇（4）" target="_blank">番外三 林嘉篇（4）</a></li>
            <li><a href="/b/154580/70487.html" title="贫僧不想当影帝 番外三 林嘉篇（中下）" target="_blank">番外三 林嘉篇（中下）</a></li>
            <li><a href="/b/154580/70338.html" title="贫僧不想当影帝 番外三 林嘉篇（中）" target="_blank">番外三 林嘉篇（中）</a></li>
            <li><a href="/b/154580/70183.html" title="贫僧不想当影帝 番外三 林嘉篇（上）" target="_blank">番外三 林嘉篇（上）</a></li>
            <li><a href="/b/154580/70027.html" title="贫僧不想当影帝 番外二 师父追星记（下）" target="_blank">番外二 师父追星记（下）</a></li>
            <li><a href="/b/154580/69994.html" title="贫僧不想当影帝 番外二 师父追星记（中下）" target="_blank">番外二 师父追星记（中下）</a></li>
            <li><a href="/b/154580/69835.html" title="贫僧不想当影帝 番外二 师父追星记（中）" target="_blank">番外二 师父追星记（中）</a></li>
            <li><a href="/b/154580/69691.html" title="贫僧不想当影帝 番外二 师父追星记（上）" target="_blank">番外二 师父追星记（上）</a></li>
            <li><a href="/b/154580/69538.html" title="贫僧不想当影帝 番外一 许致远篇（下）" target="_blank">番外一 许致远篇（下）</a></li>
            <li><a href="/b/154580/69515.html" title="贫僧不想当影帝 番外一 许致远篇（中）" target="_blank">番外一 许致远篇（中）</a></li>
            <li><a href="/b/154580/69514.html" title="贫僧不想当影帝 番外一 许致远篇（上）" target="_blank">番外一 许致远篇（上）</a></li>
            <li class="volume">番外</li>
            <li><a href="/b/154580/69366.html" title="贫僧不想当影帝 热爱可抵岁月长" target="_blank">热爱可抵岁月长</a></li>
            <li><a href="/b/154580/69365.html" title="贫僧不想当影帝 第六百一十章 许臻的舞台" target="_blank">第六百一十章 许臻的舞台</a></li>
            <li><a href="/b/154580/69349.html" title="贫僧不想当影帝 第六百零九章 3代人" target="_blank">第六百零九章 3代人</a></li>
            <li><a href="/b/154580/69344.html" title="贫僧不想当影帝 第六百零八章 平等竞争（感谢nana不说话成为本书盟主）" target="_blank">第六百零八章 平等竞争（感谢nana不说话成为本书盟…</a></li>
            <li><a href="/b/154580/69332.html" title="贫僧不想当影帝 第六百零七章 我想见他" target="_blank">第六百零七章 我想见他</a></li>
            <li><a href="/b/154580/69327.html" title="贫僧不想当影帝 第六百零六章 昭然若揭" target="_blank">第六百零六章 昭然若揭</a></li>
            <li><a href="/b/154580/69308.html" title="贫僧不想当影帝 第六百零五章 这才叫“史诗级大战”" target="_blank">第六百零五章 这才叫“史诗级大战”</a></li>
            <li><a href="/b/154580/69304.html" title="贫僧不想当影帝 第六百零四章 史诗级大战" target="_blank">第六百零四章 史诗级大战</a></li>
            <li><a href="/b/154580/69287.html" title="贫僧不想当影帝 第六百零三章 食铁兽永不为奴" target="_blank">第六百零三章 食铁兽永不为奴</a></li>
            <li><a href="/b/154580/69276.html" title="贫僧不想当影帝 第六百零二章 谁不喜欢孙大圣呢" target="_blank">第六百零二章 谁不喜欢孙大圣呢</a></li>
            <li><a href="/b/154580/69251.html" title="贫僧不想当影帝 第六百零一章 影展活动" target="_blank">第六百零一章 影展活动</a></li>
            <li><a href="/b/154580/69250.html" title="贫僧不想当影帝 第六百章 影帝提名" target="_blank">第六百章 影帝提名</a></li>
            <li><a href="/b/154580/69249.html" title="贫僧不想当影帝 第五百九十九章 打工吧，2郎神！" target="_blank">第五百九十九章 打工吧，2郎神！</a></li>
            <li><a href="/b/154580/69248.html" title="贫僧不想当影帝 第五百九十八章 该死的入戏感" target="_blank">第五百九十八章 该死的入戏感</a></li>
            <li><a href="/b/154580/69247.html" title="贫僧不想当影帝 第五百九十七章 这是谁家的化妆师？" target="_blank">第五百九十七章 这是谁家的化妆师？</a></li>
            <li><a href="/b/154580/69196.html" title="贫僧不想当影帝 第五百九十六章 巧手娜" target="_blank">第五百九十六章 巧手娜</a></li>
            <li><a href="/b/154580/69189.html" title="贫僧不想当影帝 木有写完，劝睡，早上发" target="_blank">木有写完，劝睡，早上发</a></li>
            <li><a href="/b/154580/69175.html" title="贫僧不想当影帝 第五百九十五章 2郎神与哮天犬" target="_blank">第五百九十五章 2郎神与哮天犬</a></li>
            <li><a href="/b/154580/69170.html" title="贫僧不想当影帝 第五百九十四章 配音也没什么了不起的" target="_blank">第五百九十四章 配音也没什么了不起的</a></li>
            <li><a href="/b/154580/69147.html" title="贫僧不想当影帝 第五百九十三章 1人、1麦" target="_blank">第五百九十三章 1人、1麦</a></li>
            <li><a href="/b/154580/69137.html" title="贫僧不想当影帝 劝睡贴" target="_blank">劝睡贴</a></li>
            <li><a href="/b/154580/69123.html" title="贫僧不想当影帝 第五百九十二章 录音棚里的许臻们" target="_blank">第五百九十二章 录音棚里的许臻们</a></li>
            <li><a href="/b/154580/69122.html" title="贫僧不想当影帝 第五百九十一章 过节了，炫个许臻吧" target="_blank">第五百九十一章 过节了，炫个许臻吧</a></li>
            <li><a href="/b/154580/69098.html" title="贫僧不想当影帝 第五百九十章 开幕电影之争" target="_blank">第五百九十章 开幕电影之争</a></li>
            <li><a href="/b/154580/69079.html" title="贫僧不想当影帝 第五百八十九章 封神" target="_blank">第五百八十九章 封神</a></li>
            <li><a href="/b/154580/69046.html" title="贫僧不想当影帝 第五百八十八章 渔舟唱晚" target="_blank">第五百八十八章 渔舟唱晚</a></li>
            <li><a href="/b/154580/69032.html" title="贫僧不想当影帝 第五百八十七章 欸乃1声山水绿" target="_blank">第五百八十七章 欸乃1声山水绿</a></li>
            <li><a href="/b/154580/69008.html" title="贫僧不想当影帝 第五百八十六章 华夏通" target="_blank">第五百八十六章 华夏通</a></li>
            <li><a href="/b/154580/68982.html" title="贫僧不想当影帝 第五百八十五章 特效师威廉先生" target="_blank">第五百八十五章 特效师威廉先生</a></li>
            <li><a href="/b/154580/68950.html" title="贫僧不想当影帝 第五百八十四章 来自高缜导演的戏约" target="_blank">第五百八十四章 来自高缜导演的戏约</a></li>
            <li><a href="/b/154580/68930.html" title="贫僧不想当影帝 第五百八十三章 梦里啥都有" target="_blank">第五百八十三章 梦里啥都有</a></li>
            <li><a href="/b/154580/68907.html" title="贫僧不想当影帝 第五百八十二章 许式卡点法" target="_blank">第五百八十二章 许式卡点法</a></li>
            <li><a href="/b/154580/68878.html" title="贫僧不想当影帝 第五百八十一章 恭迎刁影后" target="_blank">第五百八十一章 恭迎刁影后</a></li>
            <li><a href="/b/154580/68850.html" title="贫僧不想当影帝 第五百八十章 光秃秃" target="_blank">第五百八十章 光秃秃</a></li>
            <li><a href="/b/154580/68833.html" title="贫僧不想当影帝 第五百七十九章 似是送钱来？" target="_blank">第五百七十九章 似是送钱来？</a></li>
            <li><a href="/b/154580/68800.html" title="贫僧不想当影帝 第五百七十八章 全员叛变" target="_blank">第五百七十八章 全员叛变</a></li>
            <li><a href="/b/154580/68771.html" title="贫僧不想当影帝 第五百七十七章 许总的格局" target="_blank">第五百七十七章 许总的格局</a></li>
            <li><a href="/b/154580/68755.html" title="贫僧不想当影帝 第五百七十六章 它会火的" target="_blank">第五百七十六章 它会火的</a></li>
            <li><a href="/b/154580/68725.html" title="贫僧不想当影帝 第五百七十五章 什么叫附体式演技" target="_blank">第五百七十五章 什么叫附体式演技</a></li>
            <li><a href="/b/154580/68691.html" title="贫僧不想当影帝 第五百七十四章 琅琊阁的赚钱能力" target="_blank">第五百七十四章 琅琊阁的赚钱能力</a></li>
            <li><a href="/b/154580/68673.html" title="贫僧不想当影帝 第五百七十三章 实力征服" target="_blank">第五百七十三章 实力征服</a></li>
            <li><a href="/b/154580/68667.html" title="贫僧不想当影帝 第五百七十二章 万事俱备，就差钱了" target="_blank">第五百七十二章 万事俱备，就差钱了</a></li>
            <li><a href="/b/154580/68652.html" title="贫僧不想当影帝 第五百七十一章 无双" target="_blank">第五百七十一章 无双</a></li>
            <li><a href="/b/154580/68651.html" title="贫僧不想当影帝 第五百七十章 这是个亿万富翁？" target="_blank">第五百七十章 这是个亿万富翁？</a></li>
            <li><a href="/b/154580/68623.html" title="贫僧不想当影帝 第五百六十九章 来自香江的客人" target="_blank">第五百六十九章 来自香江的客人</a></li>
            <li><a href="/b/154580/68601.html" title="贫僧不想当影帝 第五百六十八章 许叔叔您好" target="_blank">第五百六十八章 许叔叔您好</a></li>
            <li><a href="/b/154580/68573.html" title="贫僧不想当影帝 第五百六十七章 间歇性顶流" target="_blank">第五百六十七章 间歇性顶流</a></li>
            <li><a href="/b/154580/68550.html" title="贫僧不想当影帝 第五百六十六章 什么叫带戏之神" target="_blank">第五百六十六章 什么叫带戏之神</a></li>
            <li><a href="/b/154580/68501.html" title="贫僧不想当影帝 第五百六十五章 体验派蔡总" target="_blank">第五百六十五章 体验派蔡总</a></li>
            <li><a href="/b/154580/68494.html" title="贫僧不想当影帝 第五百六十四章 大佬带飞" target="_blank">第五百六十四章 大佬带飞</a></li>
            <li><a href="/b/154580/68466.html" title="贫僧不想当影帝 第五百六十三章 1人单扛全片" target="_blank">第五百六十三章 1人单扛全片</a></li>
            <li><a href="/b/154580/68454.html" title="贫僧不想当影帝 第五百六十二章 演艺圈知名帽子" target="_blank">第五百六十二章 演艺圈知名帽子</a></li>
            <li><a href="/b/154580/68418.html" title="贫僧不想当影帝 第五百六十一章 归来仍是少年（发书1周年啦！）" target="_blank">第五百六十一章 归来仍是少年（发书1周年啦！）</a></li>
            <li><a href="/b/154580/68405.html" title="贫僧不想当影帝 第五百六十一章 摆平" target="_blank">第五百六十一章 摆平</a></li>
            <li><a href="/b/154580/68373.html" title="贫僧不想当影帝 第五百五十九章 少年许臻（感谢火舞炽凤的盟主！）" target="_blank">第五百五十九章 少年许臻（感谢火舞炽凤的盟主！）</a></li>
            <li><a href="/b/154580/68364.html" title="贫僧不想当影帝 没写完，早上发" target="_blank">没写完，早上发</a></li>
            <li><a href="/b/154580/68328.html" title="贫僧不想当影帝 第五百五十八章 影后的自我修养" target="_blank">第五百五十八章 影后的自我修养</a></li>
            <li><a href="/b/154580/68300.html" title="贫僧不想当影帝 第五百五十七章 为救李郎离家园（感谢老腰的盟主！）" target="_blank">第五百五十七章 为救李郎离家园（感谢老腰的盟主！）</a></li>
            <li><a href="/b/154580/68280.html" title="贫僧不想当影帝 第五百五十六章 梅子黄时雨" target="_blank">第五百五十六章 梅子黄时雨</a></li>
            <li><a href="/b/154580/68257.html" title="贫僧不想当影帝 第五百五十五章 台上3分钟" target="_blank">第五百五十五章 台上3分钟</a></li>
            <li><a href="/b/154580/68251.html" title="贫僧不想当影帝 第五百五十四章 黄梅戏剧院（感谢红有角的盟主！）" target="_blank">第五百五十四章 黄梅戏剧院（感谢红有角的盟主！）</a></li>
            <li><a href="/b/154580/68214.html" title="贫僧不想当影帝 第五百五十三章 送货上门（感谢懒胖癌晚期的盟主！）" target="_blank">第五百五十三章 送货上门（感谢懒胖癌晚期的盟主！）</a></li>
            <li><a href="/b/154580/68202.html" title="贫僧不想当影帝 第五百五十二章 3缺1" target="_blank">第五百五十二章 3缺1</a></li>
            <li><a href="/b/154580/68196.html" title="贫僧不想当影帝 第五百五十一章 万事俱备" target="_blank">第五百五十一章 万事俱备</a></li>
            <li><a href="/b/154580/68182.html" title="贫僧不想当影帝 劝睡贴" target="_blank">劝睡贴</a></li>
            <li><a href="/b/154580/68160.html" title="贫僧不想当影帝 第五百五十章 别人家的孩子（感谢、宿殇的盟主！）" target="_blank">第五百五十章 别人家的孩子（感谢、宿殇的盟主！）</a></li>
            <li><a href="/b/154580/68137.html" title="贫僧不想当影帝 第五百四十九章 羁绊" target="_blank">第五百四十九章 羁绊</a></li>
            <li><a href="/b/154580/68122.html" title="贫僧不想当影帝 第五百四十八章 你管这叫残障文化节" target="_blank">第五百四十八章 你管这叫残障文化节</a></li>
            <li><a href="/b/154580/68094.html" title="贫僧不想当影帝 第五百四十七章 托儿（圣诞快乐！）" target="_blank">第五百四十七章 托儿（圣诞快乐！）</a></li>
            <li><a href="/b/154580/68063.html" title="贫僧不想当影帝 第五百四十六章 表演的魅力" target="_blank">第五百四十六章 表演的魅力</a></li>
            <li><a href="/b/154580/68040.html" title="贫僧不想当影帝 第五百四十五章 神似徐浩宇的少年" target="_blank">第五百四十五章 神似徐浩宇的少年</a></li>
            <li><a href="/b/154580/68010.html" title="贫僧不想当影帝 第五百四十四章 光明艺术文化街区" target="_blank">第五百四十四章 光明艺术文化街区</a></li>
            <li><a href="/b/154580/67972.html" title="贫僧不想当影帝 第五百四十三章 痛改前非" target="_blank">第五百四十三章 痛改前非</a></li>
            <li><a href="/b/154580/67946.html" title="贫僧不想当影帝 第五百四十二章 虐心天花板" target="_blank">第五百四十二章 虐心天花板</a></li>
            <li><a href="/b/154580/67909.html" title="贫僧不想当影帝 第五百四十一章 宫庶与他的食物" target="_blank">第五百四十一章 宫庶与他的食物</a></li>
            <li><a href="/b/154580/67881.html" title="贫僧不想当影帝 第五百四十章 断了线的风筝" target="_blank">第五百四十章 断了线的风筝</a></li>
            <li><a href="/b/154580/67848.html" title="贫僧不想当影帝 第五百三十九章 全面沦陷" target="_blank">第五百三十九章 全面沦陷</a></li>
            <li><a href="/b/154580/67818.html" title="贫僧不想当影帝 第五百三十八章 总有人帮我们做宣传" target="_blank">第五百三十八章 总有人帮我们做宣传</a></li>
            <li><a href="/b/154580/67786.html" title="贫僧不想当影帝 第五百三十七章 物超所值的综艺节目" target="_blank">第五百三十七章 物超所值的综艺节目</a></li>
            <li><a href="/b/154580/67750.html" title="贫僧不想当影帝 第五百三十六章 专坑老同学" target="_blank">第五百三十六章 专坑老同学</a></li>
            <li><a href="/b/154580/67718.html" title="贫僧不想当影帝 第五百三十五章 谁还不是个特工（感谢胖子郁闷的盟主！！）" target="_blank">第五百三十五章 谁还不是个特工（感谢胖子郁闷的盟主！…</a></li>
            <li><a href="/b/154580/67693.html" title="贫僧不想当影帝 第五百三十四章 真真假假" target="_blank">第五百三十四章 真真假假</a></li>
            <li><a href="/b/154580/67689.html" title="贫僧不想当影帝 第五百三十三章 温故而知新" target="_blank">第五百三十三章 温故而知新</a></li>
            <li><a href="/b/154580/67658.html" title="贫僧不想当影帝 第五百三十二章 挑战自我" target="_blank">第五百三十二章 挑战自我</a></li>
            <li><a href="/b/154580/67652.html" title="贫僧不想当影帝 请几个小时的假" target="_blank">请几个小时的假</a></li>
            <li><a href="/b/154580/67628.html" title="贫僧不想当影帝 第五百三十一章 凡尔赛大赏" target="_blank">第五百三十一章 凡尔赛大赏</a></li>
            <li><a href="/b/154580/67620.html" title="贫僧不想当影帝 第五百三十章 老铁666" target="_blank">第五百三十章 老铁666</a></li>
            <li><a href="/b/154580/67585.html" title="贫僧不想当影帝 第五百二十九章 英雄所见略同" target="_blank">第五百二十九章 英雄所见略同</a></li>
            <li><a href="/b/154580/67557.html" title="贫僧不想当影帝 第五百二十八章 人算不如天算" target="_blank">第五百二十八章 人算不如天算</a></li>
            <li><a href="/b/154580/67526.html" title="贫僧不想当影帝 第五百二十七章 偷偷修炼，惊艳所有人？" target="_blank">第五百二十七章 偷偷修炼，惊艳所有人？</a></li>
            <li><a href="/b/154580/67493.html" title="贫僧不想当影帝 第五百二十六章 经典重现" target="_blank">第五百二十六章 经典重现</a></li>
            <li><a href="/b/154580/67466.html" title="贫僧不想当影帝 第五百二十五章 声声入耳" target="_blank">第五百二十五章 声声入耳</a></li>
            <li><a href="/b/154580/67460.html" title="贫僧不想当影帝 第五百二十四章 日常系谍战" target="_blank">第五百二十四章 日常系谍战</a></li>
            <li><a href="/b/154580/67426.html" title="贫僧不想当影帝 第五百二十三章 压力山大的柳导" target="_blank">第五百二十三章 压力山大的柳导</a></li>
            <li><a href="/b/154580/67420.html" title="贫僧不想当影帝 第五百二十二章 谍战天花板" target="_blank">第五百二十二章 谍战天花板</a></li>
            <li><a href="/b/154580/67387.html" title="贫僧不想当影帝 第五百二十一章 鹅肝还热着" target="_blank">第五百二十一章 鹅肝还热着</a></li>
            <li><a href="/b/154580/67366.html" title="贫僧不想当影帝 第五百二十章 顶级穷酸特工" target="_blank">第五百二十章 顶级穷酸特工</a></li>
            <li><a href="/b/154580/67339.html" title="贫僧不想当影帝 第五百一十九章 我臻不可能这么穷酸" target="_blank">第五百一十九章 我臻不可能这么穷酸</a></li>
            <li><a href="/b/154580/67323.html" title="贫僧不想当影帝 第五百一十八章 劝你们不要看《风筝》" target="_blank">第五百一十八章 劝你们不要看《风筝》</a></li>
            <li><a href="/b/154580/67322.html" title="贫僧不想当影帝 由于有请假条了，所以我决定写完再发" target="_blank">由于有请假条了，所以我决定写完再发</a></li>
            <li><a href="/b/154580/67288.html" title="贫僧不想当影帝 第五百一十七章 许总的反向宣传（感谢明镜成雪的盟主！）" target="_blank">第五百一十七章 许总的反向宣传（感谢明镜成雪的盟主！…</a></li>
            <li><a href="/b/154580/67253.html" title="贫僧不想当影帝 第五百一十六章 这盛世" target="_blank">第五百一十六章 这盛世</a></li>
            <li><a href="/b/154580/67213.html" title="贫僧不想当影帝 第五百一十五章 自古英雄有血性" target="_blank">第五百一十五章 自古英雄有血性</a></li>
            <li><a href="/b/154580/67180.html" title="贫僧不想当影帝 第五百一十四章 华夏式英雄" target="_blank">第五百一十四章 华夏式英雄</a></li>
            <li><a href="/b/154580/67148.html" title="贫僧不想当影帝 第五百一十三章 戏中戏中戏" target="_blank">第五百一十三章 戏中戏中戏</a></li>
            <li><a href="/b/154580/67118.html" title="贫僧不想当影帝 第五百一十二章 社交牛叉症" target="_blank">第五百一十二章 社交牛叉症</a></li>
            <li><a href="/b/154580/67079.html" title="贫僧不想当影帝 第五百一十一章 围炉闲话" target="_blank">第五百一十一章 围炉闲话</a></li>
            <li><a href="/b/154580/67050.html" title="贫僧不想当影帝 第五百一十章 穿林海跨雪原" target="_blank">第五百一十章 穿林海跨雪原</a></li>
            <li><a href="/b/154580/67010.html" title="贫僧不想当影帝 第五百零九章 转发这个臻臻" target="_blank">第五百零九章 转发这个臻臻</a></li>
            <li><a href="/b/154580/66974.html" title="贫僧不想当影帝 第五百零八章 指路冥灯" target="_blank">第五百零八章 指路冥灯</a></li>
            <li><a href="/b/154580/66953.html" title="贫僧不想当影帝 第五百零七章 演艺圈的尽头是法云寺" target="_blank">第五百零七章 演艺圈的尽头是法云寺</a></li>
            <li><a href="/b/154580/66939.html" title="贫僧不想当影帝 第五百零六章 同戏不同命" target="_blank">第五百零六章 同戏不同命</a></li>
            <li><a href="/b/154580/66905.html" title="贫僧不想当影帝 第五百零五章 撞钟的林晓波" target="_blank">第五百零五章 撞钟的林晓波</a></li>
            <li><a href="/b/154580/66866.html" title="贫僧不想当影帝 第五百零四章 佛缘路" target="_blank">第五百零四章 佛缘路</a></li>
            <li><a href="/b/154580/66830.html" title="贫僧不想当影帝 第五百零三章 总有英灵护河川" target="_blank">第五百零三章 总有英灵护河川</a></li>
            <li><a href="/b/154580/66797.html" title="贫僧不想当影帝 第五百零二章 国破山河在" target="_blank">第五百零二章 国破山河在</a></li>
            <li><a href="/b/154580/66763.html" title="贫僧不想当影帝 第五百零一章 许臻居然没死？" target="_blank">第五百零一章 许臻居然没死？</a></li>
            <li><a href="/b/154580/66726.html" title="贫僧不想当影帝 第五百章 神补刀" target="_blank">第五百章 神补刀</a></li>
            <li><a href="/b/154580/66690.html" title="贫僧不想当影帝 第四百九十九章 毛毛观察日记" target="_blank">第四百九十九章 毛毛观察日记</a></li>
            <li><a href="/b/154580/66688.html" title="贫僧不想当影帝 第四百九十八章 回忆杀" target="_blank">第四百九十八章 回忆杀</a></li>
            <li><a href="/b/154580/66649.html" title="贫僧不想当影帝 第四百九十七章 战长沙，又名闯关东二" target="_blank">第四百九十七章 战长沙，又名闯关东二</a></li>
            <li><a href="/b/154580/66613.html" title="贫僧不想当影帝 第四百九十六章 续作的困境" target="_blank">第四百九十六章 续作的困境</a></li>
            <li><a href="/b/154580/66607.html" title="贫僧不想当影帝 第四百九十五章 我的1级亲爹" target="_blank">第四百九十五章 我的1级亲爹</a></li>
            <li><a href="/b/154580/66564.html" title="贫僧不想当影帝 第四百九十四章 所谓父亲" target="_blank">第四百九十四章 所谓父亲</a></li>
            <li><a href="/b/154580/66526.html" title="贫僧不想当影帝 第四百九十三章 热搜狂欢" target="_blank">第四百九十三章 热搜狂欢</a></li>
            <li><a href="/b/154580/66486.html" title="贫僧不想当影帝 第四百九十二章 掌声响起来" target="_blank">第四百九十二章 掌声响起来</a></li>
            <li><a href="/b/154580/66485.html" title="贫僧不想当影帝 第四百九十一章 揭晓" target="_blank">第四百九十一章 揭晓</a></li>
            <li><a href="/b/154580/66444.html" title="贫僧不想当影帝 第四百九十章 华夏影史上最隆重的社死" target="_blank">第四百九十章 华夏影史上最隆重的社死</a></li>
            <li><a href="/b/154580/66443.html" title="贫僧不想当影帝 第四百八十九章 故人重逢" target="_blank">第四百八十九章 故人重逢</a></li>
            <li><a href="/b/154580/66409.html" title="贫僧不想当影帝 第四百八十八章 人潮汹涌" target="_blank">第四百八十八章 人潮汹涌</a></li>
            <li><a href="/b/154580/66370.html" title="贫僧不想当影帝 第四百八十七章 父与子与金鸡奖" target="_blank">第四百八十七章 父与子与金鸡奖</a></li>
            <li><a href="/b/154580/66350.html" title="贫僧不想当影帝 第四百八十六章 最佳福将" target="_blank">第四百八十六章 最佳福将</a></li>
            <li><a href="/b/154580/66312.html" title="贫僧不想当影帝 第四百八十五章 社牛社死，1字之差" target="_blank">第四百八十五章 社牛社死，1字之差</a></li>
            <li><a href="/b/154580/66280.html" title="贫僧不想当影帝 第四百八十四章 你大爷还是你大爷" target="_blank">第四百八十四章 你大爷还是你大爷</a></li>
            <li><a href="/b/154580/66279.html" title="贫僧不想当影帝 第四百八十三章 民族的才是世界的" target="_blank">第四百八十三章 民族的才是世界的</a></li>
            <li><a href="/b/154580/66236.html" title="贫僧不想当影帝 第四百八十二章 金鸡奖开幕" target="_blank">第四百八十二章 金鸡奖开幕</a></li>
            <li><a href="/b/154580/66185.html" title="贫僧不想当影帝 第四百八十一章 你所看不见的角落" target="_blank">第四百八十一章 你所看不见的角落</a></li>
            <li><a href="/b/154580/66184.html" title="贫僧不想当影帝 第四百八十章 自以为的1厢情愿" target="_blank">第四百八十章 自以为的1厢情愿</a></li>
            <li><a href="/b/154580/66143.html" title="贫僧不想当影帝 第四百七十九章 金鸡奖提名" target="_blank">第四百七十九章 金鸡奖提名</a></li>
            <li><a href="/b/154580/66103.html" title="贫僧不想当影帝 第四百七十八章 《失孤》的名场面" target="_blank">第四百七十八章 《失孤》的名场面</a></li>
            <li><a href="/b/154580/66051.html" title="贫僧不想当影帝 第四百七十七章 许小臻和他的赞助商" target="_blank">第四百七十七章 许小臻和他的赞助商</a></li>
            <li><a href="/b/154580/66001.html" title="贫僧不想当影帝 第四百七十六章 锣鼓喧天，鞭炮齐鸣" target="_blank">第四百七十六章 锣鼓喧天，鞭炮齐鸣</a></li>
            <li><a href="/b/154580/65935.html" title="贫僧不想当影帝 第四百七十五章 小爷我可是练过的" target="_blank">第四百七十五章 小爷我可是练过的</a></li>
            <li><a href="/b/154580/65898.html" title="贫僧不想当影帝 第四百七十四章 治愈系打拐" target="_blank">第四百七十四章 治愈系打拐</a></li>
            <li><a href="/b/154580/65840.html" title="贫僧不想当影帝 第四百七十三章 紫金冠与金箍棒" target="_blank">第四百七十三章 紫金冠与金箍棒</a></li>
            <li><a href="/b/154580/65804.html" title="贫僧不想当影帝 第四百七十二章 扭转口碑之作" target="_blank">第四百七十二章 扭转口碑之作</a></li>
            <li><a href="/b/154580/65747.html" title="贫僧不想当影帝 第四百七十一章 叔叔给你表演杂技" target="_blank">第四百七十一章 叔叔给你表演杂技</a></li>
            <li><a href="/b/154580/65704.html" title="贫僧不想当影帝 第四百七十章 看好你的孩子" target="_blank">第四百七十章 看好你的孩子</a></li>
            <li><a href="/b/154580/65632.html" title="贫僧不想当影帝 第四百六十九章 宝贝守护计划" target="_blank">第四百六十九章 宝贝守护计划</a></li>
            <li><a href="/b/154580/65586.html" title="贫僧不想当影帝 第四百六十八章 来自隔壁剧组的宣传助攻" target="_blank">第四百六十八章 来自隔壁剧组的宣传助攻</a></li>
            <li><a href="/b/154580/65535.html" title="贫僧不想当影帝 第四百六十七章 许总是个厚道人" target="_blank">第四百六十七章 许总是个厚道人</a></li>
            <li><a href="/b/154580/65478.html" title="贫僧不想当影帝 第四百六十六章 不入虎穴焉被虎吃" target="_blank">第四百六十六章 不入虎穴焉被虎吃</a></li>
            <li><a href="/b/154580/65427.html" title="贫僧不想当影帝 第四百六十五章 刁蛮与刚烈" target="_blank">第四百六十五章 刁蛮与刚烈</a></li>
            <li><a href="/b/154580/65373.html" title="贫僧不想当影帝 第四百六十四章 许老师的付费课堂" target="_blank">第四百六十四章 许老师的付费课堂</a></li>
            <li><a href="/b/154580/65318.html" title="贫僧不想当影帝 第四百六十三章 战长沙，开拔！" target="_blank">第四百六十三章 战长沙，开拔！</a></li>
            <li><a href="/b/154580/65247.html" title="贫僧不想当影帝 第四百六十二章 反客为主" target="_blank">第四百六十二章 反客为主</a></li>
            <li><a href="/b/154580/65236.html" title="贫僧不想当影帝 第四百六十一章 为人父母" target="_blank">第四百六十一章 为人父母</a></li>
            <li><a href="/b/154580/65206.html" title="贫僧不想当影帝 第四百六十章 打动人心的关键" target="_blank">第四百六十章 打动人心的关键</a></li>
            <li><a href="/b/154580/65142.html" title="贫僧不想当影帝 第四百五十九章 评委许老师" target="_blank">第四百五十九章 评委许老师</a></li>
            <li><a href="/b/154580/65095.html" title="贫僧不想当影帝 第四百五十八章 琅琊阁欢迎你" target="_blank">第四百五十八章 琅琊阁欢迎你</a></li>
            <li><a href="/b/154580/65089.html" title="贫僧不想当影帝 第四百五十七章 演技派副总" target="_blank">第四百五十七章 演技派副总</a></li>
            <li><a href="/b/154580/65033.html" title="贫僧不想当影帝 第四百五十六章 许总的算盘啪啪响" target="_blank">第四百五十六章 许总的算盘啪啪响</a></li>
            <li><a href="/b/154580/65011.html" title="贫僧不想当影帝 第四百五十五章 无谓侠" target="_blank">第四百五十五章 无谓侠</a></li>
            <li><a href="/b/154580/64951.html" title="贫僧不想当影帝 第四百五十四章 尘封的剧本" target="_blank">第四百五十四章 尘封的剧本</a></li>
            <li><a href="/b/154580/64944.html" title="贫僧不想当影帝 第四百五十三章 武侠情怀总是诗" target="_blank">第四百五十三章 武侠情怀总是诗</a></li>
            <li><a href="/b/154580/64910.html" title="贫僧不想当影帝 第四百五十二章 金花婆婆与银叶先生" target="_blank">第四百五十二章 金花婆婆与银叶先生</a></li>
            <li><a href="/b/154580/64867.html" title="贫僧不想当影帝 第四百五十一章 白衣胜雪" target="_blank">第四百五十一章 白衣胜雪</a></li>
            <li><a href="/b/154580/64851.html" title="贫僧不想当影帝 第四百五十章 武侠剧的衰落" target="_blank">第四百五十章 武侠剧的衰落</a></li>
            <li><a href="/b/154580/64800.html" title="贫僧不想当影帝 第四百四十九章 这个联动我不想要" target="_blank">第四百四十九章 这个联动我不想要</a></li>
            <li><a href="/b/154580/64751.html" title="贫僧不想当影帝 第四百四十八章 我不擅长哭戏" target="_blank">第四百四十八章 我不擅长哭戏</a></li>
            <li><a href="/b/154580/64744.html" title="贫僧不想当影帝 第四百四十七章 无实物表演" target="_blank">第四百四十七章 无实物表演</a></li>
            <li><a href="/b/154580/64702.html" title="贫僧不想当影帝 第四百四十六章 扎心高手" target="_blank">第四百四十六章 扎心高手</a></li>
            <li><a href="/b/154580/64635.html" title="贫僧不想当影帝 第四百四十五章 行业壁垒" target="_blank">第四百四十五章 行业壁垒</a></li>
            <li><a href="/b/154580/64587.html" title="贫僧不想当影帝 第四百四十四章 真·梦幻联动" target="_blank">第四百四十四章 真·梦幻联动</a></li>
            <li><a href="/b/154580/64564.html" title="贫僧不想当影帝 第四百四十三章 以后，你叫靳1川（感谢是在下ru了的盟主打赏！）" target="_blank">第四百四十三章 以后，你叫靳1川（感谢是在下ru了的…</a></li>
            <li><a href="/b/154580/64549.html" title="贫僧不想当影帝 第四百四十二章 流水落花春去也" target="_blank">第四百四十二章 流水落花春去也</a></li>
            <li><a href="/b/154580/64504.html" title="贫僧不想当影帝 第四百四十一章 绝地反杀" target="_blank">第四百四十一章 绝地反杀</a></li>
            <li><a href="/b/154580/64275.html" title="贫僧不想当影帝 第四百四十章 墙头马上遥相顾" target="_blank">第四百四十章 墙头马上遥相顾</a></li>
            <li><a href="/b/154580/64219.html" title="贫僧不想当影帝 第四百三十九章 锦衣夜行" target="_blank">第四百三十九章 锦衣夜行</a></li>
            <li><a href="/b/154580/64165.html" title="贫僧不想当影帝 第四百三十八章 敢不敢打个赌" target="_blank">第四百三十八章 敢不敢打个赌</a></li>
            <li><a href="/b/154580/64115.html" title="贫僧不想当影帝 第四百三十七章 《绣春刀》的前期宣传" target="_blank">第四百三十七章 《绣春刀》的前期宣传</a></li>
            <li><a href="/b/154580/64114.html" title="贫僧不想当影帝 第四百三十六章 许总的用人标准" target="_blank">第四百三十六章 许总的用人标准</a></li>
            <li><a href="/b/154580/64007.html" title="贫僧不想当影帝 第四百三十五章 许老师演技小课堂" target="_blank">第四百三十五章 许老师演技小课堂</a></li>
            <li><a href="/b/154580/63944.html" title="贫僧不想当影帝 第四百三十四章 凤南小分队" target="_blank">第四百三十四章 凤南小分队</a></li>
            <li><a href="/b/154580/63892.html" title="贫僧不想当影帝 第四百三十三章 风萧萧兮易水寒" target="_blank">第四百三十三章 风萧萧兮易水寒</a></li>
            <li><a href="/b/154580/63845.html" title="贫僧不想当影帝 第四百三十二章 莫比乌斯环" target="_blank">第四百三十二章 莫比乌斯环</a></li>
            <li><a href="/b/154580/63774.html" title="贫僧不想当影帝 第四百三十一章 想见你" target="_blank">第四百三十一章 想见你</a></li>
            <li><a href="/b/154580/63726.html" title="贫僧不想当影帝 第四百三十章 许臻影响力的扩散" target="_blank">第四百三十章 许臻影响力的扩散</a></li>
            <li><a href="/b/154580/63674.html" title="贫僧不想当影帝 第四百二十九章 蒸蒸日上的琅琊阁" target="_blank">第四百二十九章 蒸蒸日上的琅琊阁</a></li>
            <li><a href="/b/154580/63591.html" title="贫僧不想当影帝 第四百二十八章 火热的国庆档" target="_blank">第四百二十八章 火热的国庆档</a></li>
            <li><a href="/b/154580/63540.html" title="贫僧不想当影帝 第四百二十七章 敲定角色" target="_blank">第四百二十七章 敲定角色</a></li>
            <li><a href="/b/154580/63469.html" title="贫僧不想当影帝 第四百二十六章 智商低是硬伤" target="_blank">第四百二十六章 智商低是硬伤</a></li>
            <li><a href="/b/154580/63428.html" title="贫僧不想当影帝 第四百二十五章 随机应变" target="_blank">第四百二十五章 随机应变</a></li>
            <li><a href="/b/154580/63369.html" title="贫僧不想当影帝 第四百二十四章 影帝们的战争" target="_blank">第四百二十四章 影帝们的战争</a></li>
            <li><a href="/b/154580/63308.html" title="贫僧不想当影帝 第四百二十三章 天王盖地虎" target="_blank">第四百二十三章 天王盖地虎</a></li>
            <li><a href="/b/154580/63247.html" title="贫僧不想当影帝 第四百二十二章 许臻的路人缘（感谢曦玺的2尊盟主！！）" target="_blank">第四百二十二章 许臻的路人缘（感谢曦玺的2尊盟主！！…</a></li>
            <li><a href="/b/154580/63178.html" title="贫僧不想当影帝 第四百二十一章 《10月围城》预告片出炉" target="_blank">第四百二十一章 《10月围城》预告片出炉</a></li>
            <li><a href="/b/154580/63132.html" title="贫僧不想当影帝 第四百二十章 海浪" target="_blank">第四百二十章 海浪</a></li>
            <li><a href="/b/154580/63064.html" title="贫僧不想当影帝 第四百一十九章 第3次合作" target="_blank">第四百一十九章 第3次合作</a></li>
            <li><a href="/b/154580/63008.html" title="贫僧不想当影帝 第四百一十八章 战长沙" target="_blank">第四百一十八章 战长沙</a></li>
            <li><a href="/b/154580/62938.html" title="贫僧不想当影帝 第四百一十七章 矮矮的蔡总有大大的梦" target="_blank">第四百一十七章 矮矮的蔡总有大大的梦</a></li>
            <li><a href="/b/154580/62883.html" title="贫僧不想当影帝 第四百一十六章 勺勺自危" target="_blank">第四百一十六章 勺勺自危</a></li>
            <li><a href="/b/154580/62838.html" title="贫僧不想当影帝 第四百一十五章 2次回头" target="_blank">第四百一十五章 2次回头</a></li>
            <li><a href="/b/154580/62801.html" title="贫僧不想当影帝 第四百一十四章 视帝的实力" target="_blank">第四百一十四章 视帝的实力</a></li>
            <li><a href="/b/154580/62740.html" title="贫僧不想当影帝 第四百一十三章 缔造传奇" target="_blank">第四百一十三章 缔造传奇</a></li>
            <li><a href="/b/154580/62683.html" title="贫僧不想当影帝 第四百一十二章 大丰收" target="_blank">第四百一十二章 大丰收</a></li>
            <li><a href="/b/154580/62660.html" title="贫僧不想当影帝 第四百一十一章? 雏凤清声（感谢风雨燕单飞的盟主！）" target="_blank">第四百一十一章? 雏凤清声（感谢风雨燕单飞的盟主！）</a></li>
            <li><a href="/b/154580/62620.html" title="贫僧不想当影帝 第四百一十章 厚积薄发" target="_blank">第四百一十章 厚积薄发</a></li>
            <li><a href="/b/154580/62558.html" title="贫僧不想当影帝 第四百零九章 许臻的年度工作总结" target="_blank">第四百零九章 许臻的年度工作总结</a></li>
            <li><a href="/b/154580/62532.html" title="贫僧不想当影帝 第四百零八章 谁是大赢家（感谢藏经老祖的盟主打赏！！）" target="_blank">第四百零八章 谁是大赢家（感谢藏经老祖的盟主打赏！！…</a></li>
            <li><a href="/b/154580/62474.html" title="贫僧不想当影帝 第四百零七章 长江后浪" target="_blank">第四百零七章 长江后浪</a></li>
            <li><a href="/b/154580/62424.html" title="贫僧不想当影帝 第四百零六章 怎么哪儿都有他" target="_blank">第四百零六章 怎么哪儿都有他</a></li>
            <li><a href="/b/154580/62404.html" title="贫僧不想当影帝 第四百零五章 见得到吗" target="_blank">第四百零五章 见得到吗</a></li>
            <li><a href="/b/154580/62336.html" title="贫僧不想当影帝 第四百零四章 打脸不过夜" target="_blank">第四百零四章 打脸不过夜</a></li>
            <li><a href="/b/154580/62292.html" title="贫僧不想当影帝 第四百零三章 信仰的崩塌" target="_blank">第四百零三章 信仰的崩塌</a></li>
            <li><a href="/b/154580/62271.html" title="贫僧不想当影帝 第四百零二章 2顿饭（感谢盟主喝了假酒的纯揆！！）" target="_blank">第四百零二章 2顿饭（感谢盟主喝了假酒的纯揆！！）</a></li>
            <li><a href="/b/154580/62191.html" title="贫僧不想当影帝 第四百零一章 ?玉兰视帝的角逐" target="_blank">第四百零一章 ?玉兰视帝的角逐</a></li>
            <li><a href="/b/154580/62131.html" title="贫僧不想当影帝 第四百章 效率至上" target="_blank">第四百章 效率至上</a></li>
            <li><a href="/b/154580/62070.html" title="贫僧不想当影帝 第三百九十九章 顶级特工的实力" target="_blank">第三百九十九章 顶级特工的实力</a></li>
            <li><a href="/b/154580/62060.html" title="贫僧不想当影帝 请1个小时的假" target="_blank">请1个小时的假</a></li>
            <li><a href="/b/154580/62000.html" title="贫僧不想当影帝 第三百九十八章 这真真是个狠人" target="_blank">第三百九十八章 这真真是个狠人</a></li>
            <li><a href="/b/154580/61993.html" title="贫僧不想当影帝 第三百九十七章 抢进度" target="_blank">第三百九十七章 抢进度</a></li>
            <li><a href="/b/154580/61925.html" title="贫僧不想当影帝 第三百九十六章 对于演戏的执着" target="_blank">第三百九十六章 对于演戏的执着</a></li>
            <li><a href="/b/154580/61919.html" title="贫僧不想当影帝 第三百九十五章 戏比天大" target="_blank">第三百九十五章 戏比天大</a></li>
            <li><a href="/b/154580/61829.html" title="贫僧不想当影帝 第三百九十四章 雪中送炭" target="_blank">第三百九十四章 雪中送炭</a></li>
            <li><a href="/b/154580/61768.html" title="贫僧不想当影帝 第三百九十三章 辣手书生" target="_blank">第三百九十三章 辣手书生</a></li>
            <li><a href="/b/154580/61701.html" title="贫僧不想当影帝 第三百九十二章 救场小能手" target="_blank">第三百九十二章 救场小能手</a></li>
            <li><a href="/b/154580/61639.html" title="贫僧不想当影帝 第三百九十一章 群戏" target="_blank">第三百九十一章 群戏</a></li>
            <li><a href="/b/154580/61589.html" title="贫僧不想当影帝 第三百九十章??? 傲视群雄" target="_blank">第三百九十章??? 傲视群雄</a></li>
            <li><a href="/b/154580/61574.html" title="贫僧不想当影帝 第三百八十九章 新1届的玉兰奖" target="_blank">第三百八十九章 新1届的玉兰奖</a></li>
            <li><a href="/b/154580/61498.html" title="贫僧不想当影帝 第三百八十八章 琅琊阁的许总" target="_blank">第三百八十八章 琅琊阁的许总</a></li>
            <li><a href="/b/154580/61420.html" title="贫僧不想当影帝 第三百八十七章 我不是曾少侠" target="_blank">第三百八十七章 我不是曾少侠</a></li>
            <li><a href="/b/154580/61335.html" title="贫僧不想当影帝 第三百八十六章 光明顶上的纷争" target="_blank">第三百八十六章 光明顶上的纷争</a></li>
            <li><a href="/b/154580/61317.html" title="贫僧不想当影帝 第三百八十五章 此山卧虎藏龙" target="_blank">第三百八十五章 此山卧虎藏龙</a></li>
            <li><a href="/b/154580/61261.html" title="贫僧不想当影帝 第三百八十四章 其实，我是1个演员" target="_blank">第三百八十四章 其实，我是1个演员</a></li>
            <li><a href="/b/154580/61164.html" title="贫僧不想当影帝 第三百八十三章 清源山下许小臻" target="_blank">第三百八十三章 清源山下许小臻</a></li>
            <li><a href="/b/154580/61096.html" title="贫僧不想当影帝 第三百八十二章 技多不压身" target="_blank">第三百八十二章 技多不压身</a></li>
            <li><a href="/b/154580/61025.html" title="贫僧不想当影帝 第三百八十一章 不愧是最佳男配角" target="_blank">第三百八十一章 不愧是最佳男配角</a></li>
            <li><a href="/b/154580/60937.html" title="贫僧不想当影帝 第三百八十章 听说你擅长模仿？" target="_blank">第三百八十章 听说你擅长模仿？</a></li>
            <li><a href="/b/154580/60936.html" title="贫僧不想当影帝 刚加班回家，我现在开始码字" target="_blank">刚加班回家，我现在开始码字</a></li>
            <li><a href="/b/154580/60841.html" title="贫僧不想当影帝 第三百七十九章 1本本人形教材" target="_blank">第三百七十九章 1本本人形教材</a></li>
            <li><a href="/b/154580/60812.html" title="贫僧不想当影帝 第三百七十八章 于无声处听惊雷" target="_blank">第三百七十八章 于无声处听惊雷</a></li>
            <li><a href="/b/154580/60768.html" title="贫僧不想当影帝 第三百七十七章 什么叫压戏啊？" target="_blank">第三百七十七章 什么叫压戏啊？</a></li>
            <li><a href="/b/154580/60698.html" title="贫僧不想当影帝 第三百七十六章 影帝如云" target="_blank">第三百七十六章 影帝如云</a></li>
            <li><a href="/b/154580/60620.html" title="贫僧不想当影帝 第三百七十五章 10月围城" target="_blank">第三百七十五章 10月围城</a></li>
            <li><a href="/b/154580/60520.html" title="贫僧不想当影帝 第三百七十四章 少爷与车夫" target="_blank">第三百七十四章 少爷与车夫</a></li>
            <li><a href="/b/154580/60418.html" title="贫僧不想当影帝 第三百七十三章 禅与摩托车修理艺术" target="_blank">第三百七十三章 禅与摩托车修理艺术</a></li>
            <li><a href="/b/154580/60372.html" title="贫僧不想当影帝 第三百七十二章 失去与孤独" target="_blank">第三百七十二章 失去与孤独</a></li>
            <li><a href="/b/154580/60277.html" title="贫僧不想当影帝 第三百七十一章 公司成立" target="_blank">第三百七十一章 公司成立</a></li>
            <li><a href="/b/154580/60204.html" title="贫僧不想当影帝 第三百七十章 电影界新秀" target="_blank">第三百七十章 电影界新秀</a></li>
            <li><a href="/b/154580/60176.html" title="贫僧不想当影帝 第三百七十章 口碑大爆" target="_blank">第三百七十章 口碑大爆</a></li>
            <li><a href="/b/154580/60148.html" title="贫僧不想当影帝 第三百六十八章 他有1个赵云梦" target="_blank">第三百六十八章 他有1个赵云梦</a></li>
            <li><a href="/b/154580/60092.html" title="贫僧不想当影帝 第三百六十七章 7子去，6子回" target="_blank">第三百六十七章 7子去，6子回</a></li>
            <li><a href="/b/154580/59980.html" title="贫僧不想当影帝 第三百六十六章 《杨家将》上映" target="_blank">第三百六十六章 《杨家将》上映</a></li>
            <li><a href="/b/154580/59920.html" title="贫僧不想当影帝 第三百六十五章 ?杨7郎在电影中的地位" target="_blank">第三百六十五章 ?杨7郎在电影中的地位</a></li>
            <li><a href="/b/154580/59907.html" title="贫僧不想当影帝 第三百六十四章 来自《杨家将》的梦幻联动" target="_blank">第三百六十四章 来自《杨家将》的梦幻联动</a></li>
            <li><a href="/b/154580/59848.html" title="贫僧不想当影帝 第三百六十三章 风起时" target="_blank">第三百六十三章 风起时</a></li>
            <li><a href="/b/154580/59741.html" title="贫僧不想当影帝 第三百六十二章 不务正业的男主角" target="_blank">第三百六十二章 不务正业的男主角</a></li>
            <li><a href="/b/154580/59664.html" title="贫僧不想当影帝 第三百六十一章 史诗级穿帮镜头" target="_blank">第三百六十一章 史诗级穿帮镜头</a></li>
            <li><a href="/b/154580/59663.html" title="贫僧不想当影帝 第三百六十章 《琅琊榜》该怎么黑？" target="_blank">第三百六十章 《琅琊榜》该怎么黑？</a></li>
            <li><a href="/b/154580/59574.html" title="贫僧不想当影帝 第三百五十九章 来自影帝的肯定" target="_blank">第三百五十九章 来自影帝的肯定</a></li>
            <li><a href="/b/154580/59505.html" title="贫僧不想当影帝 第三百五十八章 抽丝剥茧，水落石出" target="_blank">第三百五十八章 抽丝剥茧，水落石出</a></li>
            <li><a href="/b/154580/59478.html" title="贫僧不想当影帝 第三百五十七章 急转直上" target="_blank">第三百五十七章 急转直上</a></li>
            <li><a href="/b/154580/59460.html" title="贫僧不想当影帝 第三百五十六章 画龙点睛的1笔" target="_blank">第三百五十六章 画龙点睛的1笔</a></li>
            <li><a href="/b/154580/59459.html" title="贫僧不想当影帝 第三百五十五章 这个魔幻的世界" target="_blank">第三百五十五章 这个魔幻的世界</a></li>
            <li><a href="/b/154580/59369.html" title="贫僧不想当影帝 第三百五十四章 开播遇冷？" target="_blank">第三百五十四章 开播遇冷？</a></li>
            <li><a href="/b/154580/59348.html" title="贫僧不想当影帝 第三百五十三章 麒麟才子" target="_blank">第三百五十三章 麒麟才子</a></li>
            <li><a href="/b/154580/59272.html" title="贫僧不想当影帝 第三百五十一章 《琅琊榜》的前期宣传" target="_blank">第三百五十一章 《琅琊榜》的前期宣传</a></li>
            <li><a href="/b/154580/59164.html" title="贫僧不想当影帝 第三百五十一章 靳1川在影片中的意义" target="_blank">第三百五十一章 靳1川在影片中的意义</a></li>
            <li><a href="/b/154580/59146.html" title="贫僧不想当影帝 第三百五十章 贼就是贼" target="_blank">第三百五十章 贼就是贼</a></li>
            <li><a href="/b/154580/59073.html" title="贫僧不想当影帝 第三百四十九章 瘆人的即兴表演" target="_blank">第三百四十九章 瘆人的即兴表演</a></li>
            <li><a href="/b/154580/58964.html" title="贫僧不想当影帝 第三百四十八章 不会演戏的锦衣卫不是好裁缝" target="_blank">第三百四十八章 不会演戏的锦衣卫不是好裁缝</a></li>
            <li><a href="/b/154580/58873.html" title="贫僧不想当影帝 第三百四十七章 全剧组演技最差" target="_blank">第三百四十七章 全剧组演技最差</a></li>
            <li><a href="/b/154580/58771.html" title="贫僧不想当影帝 第三百四十六章 细思恐极的靳1川" target="_blank">第三百四十六章 细思恐极的靳1川</a></li>
            <li><a href="/b/154580/58690.html" title="贫僧不想当影帝 第三百四十五章 全员戏疯子" target="_blank">第三百四十五章 全员戏疯子</a></li>
            <li><a href="/b/154580/58568.html" title="贫僧不想当影帝 第三百四十四章 飞鱼服，绣春刀" target="_blank">第三百四十四章 飞鱼服，绣春刀</a></li>
            <li><a href="/b/154580/58531.html" title="贫僧不想当影帝 第三百四十三章 ?选角死循环" target="_blank">第三百四十三章 ?选角死循环</a></li>
            <li><a href="/b/154580/58491.html" title="贫僧不想当影帝 第三百四十二章 电影圈" target="_blank">第三百四十二章 电影圈</a></li>
            <li><a href="/b/154580/58397.html" title="贫僧不想当影帝 第三百四十一章 关于人生的探讨" target="_blank">第三百四十一章 关于人生的探讨</a></li>
            <li><a href="/b/154580/58370.html" title="贫僧不想当影帝 第三百四十章 华影8部" target="_blank">第三百四十章 华影8部</a></li>
            <li><a href="/b/154580/58292.html" title="贫僧不想当影帝 第三百三十九章 史上最硬核的校园剧" target="_blank">第三百三十九章 史上最硬核的校园剧</a></li>
            <li><a href="/b/154580/58277.html" title="贫僧不想当影帝 第三百三十八章 内卷之剧" target="_blank">第三百三十八章 内卷之剧</a></li>
            <li><a href="/b/154580/58180.html" title="贫僧不想当影帝 第三百三十七章 1见直树误终生" target="_blank">第三百三十七章 1见直树误终生</a></li>
            <li><a href="/b/154580/58147.html" title="贫僧不想当影帝 第三百三十六章 惊人的付费率" target="_blank">第三百三十六章 惊人的付费率</a></li>
            <li><a href="/b/154580/58068.html" title="贫僧不想当影帝 第三百三十五章 那时年少" target="_blank">第三百三十五章 那时年少</a></li>
            <li><a href="/b/154580/57971.html" title="贫僧不想当影帝 第三百三十四章 网剧巅峰赛" target="_blank">第三百三十四章 网剧巅峰赛</a></li>
            <li><a href="/b/154580/57855.html" title="贫僧不想当影帝 第三百三十三章 区区校园剧" target="_blank">第三百三十三章 区区校园剧</a></li>
            <li><a href="/b/154580/57840.html" title="贫僧不想当影帝 第三百三十二章 没有面瘫的角色，只有不会演戏的演员" target="_blank">第三百三十二章 没有面瘫的角色，只有不会演戏的演员</a></li>
            <li><a href="/b/154580/57782.html" title="贫僧不想当影帝 单章说明" target="_blank">单章说明</a></li>
            <li><a href="/b/154580/57767.html" title="贫僧不想当影帝 第三百三十一章 顶级规格的偶像剧" target="_blank">第三百三十一章 顶级规格的偶像剧</a></li>
            <li><a href="/b/154580/57657.html" title="贫僧不想当影帝 第三百三十章 秋后算账" target="_blank">第三百三十章 秋后算账</a></li>
            <li><a href="/b/154580/57565.html" title="贫僧不想当影帝 第三百二十九章 嘉嘉的试戏" target="_blank">第三百二十九章 嘉嘉的试戏</a></li>
            <li><a href="/b/154580/57552.html" title="贫僧不想当影帝 第三百二十八章 面试官小许" target="_blank">第三百二十八章 面试官小许</a></li>
            <li><a href="/b/154580/57444.html" title="贫僧不想当影帝 第三百二十七章 校园爱情剧" target="_blank">第三百二十七章 校园爱情剧</a></li>
            <li><a href="/b/154580/57346.html" title="贫僧不想当影帝 第三百二十六章 我那个倔脾气的爹呦" target="_blank">第三百二十六章 我那个倔脾气的爹呦</a></li>
            <li><a href="/b/154580/57250.html" title="贫僧不想当影帝 第三百二十五章 俺会耍大刀" target="_blank">第三百二十五章 俺会耍大刀</a></li>
            <li><a href="/b/154580/57137.html" title="贫僧不想当影帝 第三百二十四章 冰雪早已覆盖我的足迹" target="_blank">第三百二十四章 冰雪早已覆盖我的足迹</a></li>
            <li><a href="/b/154580/57070.html" title="贫僧不想当影帝 第三百二十三章 阿勒锦保卫战" target="_blank">第三百二十三章 阿勒锦保卫战</a></li>
            <li><a href="/b/154580/57005.html" title="贫僧不想当影帝 第三百二十二章 画风清奇的直播间" target="_blank">第三百二十二章 画风清奇的直播间</a></li>
            <li><a href="/b/154580/56906.html" title="贫僧不想当影帝 第三百二十一章 顶级游戏代言的争夺" target="_blank">第三百二十一章 顶级游戏代言的争夺</a></li>
            <li><a href="/b/154580/56863.html" title="贫僧不想当影帝 第三百二十章 《琅琊榜》杀青" target="_blank">第三百二十章 《琅琊榜》杀青</a></li>
            <li><a href="/b/154580/56777.html" title="贫僧不想当影帝 第三百一十九章 全民热播" target="_blank">第三百一十九章 全民热播</a></li>
            <li><a href="/b/154580/56759.html" title="贫僧不想当影帝 第三百一十八章 传武的“武戏”" target="_blank">第三百一十八章 传武的“武戏”</a></li>
            <li><a href="/b/154580/56645.html" title="贫僧不想当影帝 第三百一十七章 改剧本了？" target="_blank">第三百一十七章 改剧本了？</a></li>
            <li><a href="/b/154580/56533.html" title="贫僧不想当影帝 第三百一十六章 上跪天地，下跪爹娘" target="_blank">第三百一十六章 上跪天地，下跪爹娘</a></li>
            <li><a href="/b/154580/56519.html" title="贫僧不想当影帝 第三百一十五章 《闯关东》花絮小剧场" target="_blank">第三百一十五章 《闯关东》花絮小剧场</a></li>
            <li><a href="/b/154580/56421.html" title="贫僧不想当影帝 第三百一十四章 朱传武的原型" target="_blank">第三百一十四章 朱传武的原型</a></li>
            <li><a href="/b/154580/56343.html" title="贫僧不想当影帝 第三百一十三章??? 1部让人停不下来的神剧" target="_blank">第三百一十三章??? 1部让人停不下来的神剧</a></li>
            <li><a href="/b/154580/56314.html" title="贫僧不想当影帝 第三百一十二章 《闯关东》开播" target="_blank">第三百一十二章 《闯关东》开播</a></li>
            <li><a href="/b/154580/56186.html" title="贫僧不想当影帝 第三百一十一章 橄榄枝堆积如山" target="_blank">第三百一十一章 橄榄枝堆积如山</a></li>
            <li><a href="/b/154580/56057.html" title="贫僧不想当影帝 第三百一十章 视帝的感言" target="_blank">第三百一十章 视帝的感言</a></li>
            <li><a href="/b/154580/55967.html" title="贫僧不想当影帝 第三百零九章 创造历史" target="_blank">第三百零九章 创造历史</a></li>
            <li><a href="/b/154580/55953.html" title="贫僧不想当影帝 第三百零八章 得之我幸，失之我命" target="_blank">第三百零八章 得之我幸，失之我命</a></li>
            <li><a href="/b/154580/55826.html" title="贫僧不想当影帝 第三百零七章 5丈原与柴桑口" target="_blank">第三百零七章 5丈原与柴桑口</a></li>
            <li><a href="/b/154580/55710.html" title="贫僧不想当影帝 第三百零六章 玉兰奖花落谁家" target="_blank">第三百零六章 玉兰奖花落谁家</a></li>
            <li><a href="/b/154580/55694.html" title="贫僧不想当影帝 第三百零五章 涨疯了" target="_blank">第三百零五章 涨疯了</a></li>
            <li><a href="/b/154580/55591.html" title="贫僧不想当影帝 第三百零四章 男几号？你再说1遍？" target="_blank">第三百零四章 男几号？你再说1遍？</a></li>
            <li><a href="/b/154580/55447.html" title="贫僧不想当影帝 第三百零三章 《杨家将》先导片" target="_blank">第三百零三章 《杨家将》先导片</a></li>
            <li><a href="/b/154580/55398.html" title="贫僧不想当影帝 第三百零二章??? 待价而沽" target="_blank">第三百零二章??? 待价而沽</a></li>
            <li><a href="/b/154580/55338.html" title="贫僧不想当影帝 第三百零一章 生子当如孙仲谋" target="_blank">第三百零一章 生子当如孙仲谋</a></li>
            <li><a href="/b/154580/55211.html" title="贫僧不想当影帝 第三百章 夜雨石桥" target="_blank">第三百章 夜雨石桥</a></li>
            <li><a href="/b/154580/55183.html" title="贫僧不想当影帝 第二百九十九章 1日3涨价（下）" target="_blank">第二百九十九章 1日3涨价（下）</a></li>
            <li><a href="/b/154580/55164.html" title="贫僧不想当影帝 第二百九十八章 1日3涨价（上）" target="_blank">第二百九十八章 1日3涨价（上）</a></li>
            <li><a href="/b/154580/55019.html" title="贫僧不想当影帝 第二百九十七章 近3年最强龙套" target="_blank">第二百九十七章 近3年最强龙套</a></li>
            <li><a href="/b/154580/54952.html" title="贫僧不想当影帝 第二百九十六章 《猎影》中的半集客串" target="_blank">第二百九十六章 《猎影》中的半集客串</a></li>
            <li><a href="/b/154580/54872.html" title="贫僧不想当影帝 第二百九十五章 《琅琊榜》第1次叫价" target="_blank">第二百九十五章 《琅琊榜》第1次叫价</a></li>
            <li><a href="/b/154580/54800.html" title="贫僧不想当影帝 第二百九十四章 陌路挚友" target="_blank">第二百九十四章 陌路挚友</a></li>
            <li><a href="/b/154580/54701.html" title="贫僧不想当影帝 第二百九十三章 我想选你" target="_blank">第二百九十三章 我想选你</a></li>
            <li><a href="/b/154580/54558.html" title="贫僧不想当影帝 第二百九十二章 且待苏某为殿下筹谋" target="_blank">第二百九十二章 且待苏某为殿下筹谋</a></li>
            <li><a href="/b/154580/54437.html" title="贫僧不想当影帝 第二百九十一章 服众" target="_blank">第二百九十一章 服众</a></li>
            <li><a href="/b/154580/54292.html" title="贫僧不想当影帝 第二百九十章 3年的成长" target="_blank">第二百九十章 3年的成长</a></li>
            <li><a href="/b/154580/54271.html" title="贫僧不想当影帝 第二百八十九章 穿帮镜头" target="_blank">第二百八十九章 穿帮镜头</a></li>
            <li><a href="/b/154580/54165.html" title="贫僧不想当影帝 第二百八十八章 不务正业的梅长苏" target="_blank">第二百八十八章 不务正业的梅长苏</a></li>
            <li><a href="/b/154580/54034.html" title="贫僧不想当影帝 第二百八十七章 静妃娘娘" target="_blank">第二百八十七章 静妃娘娘</a></li>
            <li><a href="/b/154580/53928.html" title="贫僧不想当影帝 第二百八十六章 《琅琊榜》开机发布会（下）" target="_blank">第二百八十六章 《琅琊榜》开机发布会（下）</a></li>
            <li><a href="/b/154580/53882.html" title="贫僧不想当影帝 第二百八十五章 《琅琊榜》开机发布会（上）" target="_blank">第二百八十五章 《琅琊榜》开机发布会（上）</a></li>
            <li><a href="/b/154580/53867.html" title="贫僧不想当影帝 第二百八十五章 大佬乔伊" target="_blank">第二百八十五章 大佬乔伊</a></li>
            <li><a href="/b/154580/53661.html" title="贫僧不想当影帝 第二百八十三章 《琅琊榜》的阵容？" target="_blank">第二百八十三章 《琅琊榜》的阵容？</a></li>
            <li><a href="/b/154580/53633.html" title="贫僧不想当影帝 第二百八十二章 愚者0虑或有1得" target="_blank">第二百八十二章 愚者0虑或有1得</a></li>
            <li><a href="/b/154580/53409.html" title="贫僧不想当影帝 第二百八十一章 臻式表演法" target="_blank">第二百八十一章 臻式表演法</a></li>
            <li><a href="/b/154580/53275.html" title="贫僧不想当影帝 第二百八十章 我感觉我就是个废物" target="_blank">第二百八十章 我感觉我就是个废物</a></li>
            <li><a href="/b/154580/53248.html" title="贫僧不想当影帝 第二百七十九章 我没有这样的儿子" target="_blank">第二百七十九章 我没有这样的儿子</a></li>
            <li><a href="/b/154580/53131.html" title="贫僧不想当影帝 第二百七十八章 最完美的杨延嗣" target="_blank">第二百七十八章 最完美的杨延嗣</a></li>
            <li><a href="/b/154580/53082.html" title="贫僧不想当影帝 第二百七十七章 大佬带带我" target="_blank">第二百七十七章 大佬带带我</a></li>
            <li><a href="/b/154580/52951.html" title="贫僧不想当影帝 第二百七十六章 杨7郎" target="_blank">第二百七十六章 杨7郎</a></li>
            <li><a href="/b/154580/52842.html" title="贫僧不想当影帝 第二百七十五章 梅岭与陈家谷（拜谢沉醉红尘的盟主！！）" target="_blank">第二百七十五章 梅岭与陈家谷（拜谢沉醉红尘的盟主！！…</a></li>
            <li><a href="/b/154580/52815.html" title="贫僧不想当影帝 第二百七十四章 拜年电话" target="_blank">第二百七十四章 拜年电话</a></li>
            <li><a href="/b/154580/52767.html" title="贫僧不想当影帝 刚睡醒……我现在开始码字" target="_blank">刚睡醒……我现在开始码字</a></li>
            <li><a href="/b/154580/52711.html" title="贫僧不想当影帝 第二百七十三章 从根儿上解决问题" target="_blank">第二百七十三章 从根儿上解决问题</a></li>
            <li><a href="/b/154580/52710.html" title="贫僧不想当影帝 第二百七十二章 辟谣" target="_blank">第二百七十二章 辟谣</a></li>
            <li><a href="/b/154580/52709.html" title="贫僧不想当影帝 第二百七十一章 声讨的开始" target="_blank">第二百七十一章 声讨的开始</a></li>
            <li><a href="/b/154580/52480.html" title="贫僧不想当影帝 第二百七十章 你算老几" target="_blank">第二百七十章 你算老几</a></li>
            <li><a href="/b/154580/52464.html" title="贫僧不想当影帝 第二百六十九章 贫僧不想当影帝" target="_blank">第二百六十九章 贫僧不想当影帝</a></li>
            <li><a href="/b/154580/52291.html" title="贫僧不想当影帝 第二百六十八章 今日香客甚多" target="_blank">第二百六十八章 今日香客甚多</a></li>
            <li><a href="/b/154580/52114.html" title="贫僧不想当影帝 第二百六十七章 1卷风云琅琊榜" target="_blank">第二百六十七章 1卷风云琅琊榜</a></li>
            <li><a href="/b/154580/51964.html" title="贫僧不想当影帝 第二百六十六章 演死人有红包" target="_blank">第二百六十六章 演死人有红包</a></li>
            <li><a href="/b/154580/51898.html" title="贫僧不想当影帝 第二百六十五章 ?姐，我想回家" target="_blank">第二百六十五章 ?姐，我想回家</a></li>
            <li><a href="/b/154580/51783.html" title="贫僧不想当影帝 第二百六十四章 热血男儿当保家卫国" target="_blank">第二百六十四章 热血男儿当保家卫国</a></li>
            <li><a href="/b/154580/51738.html" title="贫僧不想当影帝 第二百六十三章 冲击1线" target="_blank">第二百六十三章 冲击1线</a></li>
            <li><a href="/b/154580/51622.html" title="贫僧不想当影帝 第二百六十二章 走到哪儿死到哪儿" target="_blank">第二百六十二章 走到哪儿死到哪儿</a></li>
            <li><a href="/b/154580/51501.html" title="贫僧不想当影帝 第二百六十一章 我愿化身石桥" target="_blank">第二百六十一章 我愿化身石桥</a></li>
            <li><a href="/b/154580/51465.html" title="贫僧不想当影帝 第二百六十章 客串还是砸场子" target="_blank">第二百六十章 客串还是砸场子</a></li>
            <li><a href="/b/154580/51314.html" title="贫僧不想当影帝 第二百五十九章 1身才气半生癫" target="_blank">第二百五十九章 1身才气半生癫</a></li>
            <li><a href="/b/154580/51231.html" title="贫僧不想当影帝 第二百五十八章 来而不往非礼也" target="_blank">第二百五十八章 来而不往非礼也</a></li>
            <li><a href="/b/154580/51099.html" title="贫僧不想当影帝 第二百五十七章 戏骨与流量" target="_blank">第二百五十七章 戏骨与流量</a></li>
            <li><a href="/b/154580/50924.html" title="贫僧不想当影帝 第二百五十六章 传武回家" target="_blank">第二百五十六章 传武回家</a></li>
            <li><a href="/b/154580/50890.html" title="贫僧不想当影帝 第二百五十五章 嘉嘉探班记" target="_blank">第二百五十五章 嘉嘉探班记</a></li>
            <li><a href="/b/154580/50768.html" title="贫僧不想当影帝 第二百五十四章 我那个倔脾气的儿子呦" target="_blank">第二百五十四章 我那个倔脾气的儿子呦</a></li>
            <li><a href="/b/154580/50518.html" title="贫僧不想当影帝 第二百五十三章 你他凉的意大利炮呢" target="_blank">第二百五十三章 你他凉的意大利炮呢</a></li>
            <li><a href="/b/154580/50517.html" title="贫僧不想当影帝 第二百五十二章 自信的你，耀眼得发光" target="_blank">第二百五十二章 自信的你，耀眼得发光</a></li>
            <li><a href="/b/154580/50300.html" title="贫僧不想当影帝 第二百五十一章 衣锦还乡" target="_blank">第二百五十一章 衣锦还乡</a></li>
            <li><a href="/b/154580/50195.html" title="贫僧不想当影帝 第二百五十章 来自陈正豪的指点" target="_blank">第二百五十章 来自陈正豪的指点</a></li>
            <li><a href="/b/154580/50194.html" title="贫僧不想当影帝 下班回家睡过了，正在疯狂码字中" target="_blank">下班回家睡过了，正在疯狂码字中</a></li>
            <li><a href="/b/154580/50047.html" title="贫僧不想当影帝 第二百四十九章 1战成名" target="_blank">第二百四十九章 1战成名</a></li>
            <li><a href="/b/154580/50013.html" title="贫僧不想当影帝 第二百四十八章 世间再无周郎" target="_blank">第二百四十八章 世间再无周郎</a></li>
            <li><a href="/b/154580/49886.html" title="贫僧不想当影帝 第二百四十六章? 黯淡了刀光剑影" target="_blank">第二百四十六章? 黯淡了刀光剑影</a></li>
            <li><a href="/b/154580/49832.html" title="贫僧不想当影帝 第二百四十六章 功高震主" target="_blank">第二百四十六章 功高震主</a></li>
            <li><a href="/b/154580/49692.html" title="贫僧不想当影帝 第二百四十五章 谁是反派？" target="_blank">第二百四十五章 谁是反派？</a></li>
            <li><a href="/b/154580/49655.html" title="贫僧不想当影帝 第二百四十四章 戏里戏外的瑜亮" target="_blank">第二百四十四章 戏里戏外的瑜亮</a></li>
            <li><a href="/b/154580/49507.html" title="贫僧不想当影帝 第二百四十三章 这该死的代入感" target="_blank">第二百四十三章 这该死的代入感</a></li>
            <li><a href="/b/154580/49378.html" title="贫僧不想当影帝 第二百四十二章??? 瑜亮的首次交锋" target="_blank">第二百四十二章??? 瑜亮的首次交锋</a></li>
            <li><a href="/b/154580/49293.html" title="贫僧不想当影帝 第二百四十一章 喧宾夺主？" target="_blank">第二百四十一章 喧宾夺主？</a></li>
            <li><a href="/b/154580/49144.html" title="贫僧不想当影帝 第二百四十章 没想到你竟然是这样的周嘟嘟" target="_blank">第二百四十章 没想到你竟然是这样的周嘟嘟</a></li>
            <li><a href="/b/154580/49090.html" title="贫僧不想当影帝 第二百三十九章 瑜亮之争" target="_blank">第二百三十九章 瑜亮之争</a></li>
            <li><a href="/b/154580/48960.html" title="贫僧不想当影帝 第二百三十八章 破纪录" target="_blank">第二百三十八章 破纪录</a></li>
            <li><a href="/b/154580/48917.html" title="贫僧不想当影帝 第二百三十七章 洛阳纸贵" target="_blank">第二百三十七章 洛阳纸贵</a></li>
            <li><a href="/b/154580/48749.html" title="贫僧不想当影帝 第二百三十六章 江东柱石" target="_blank">第二百三十六章 江东柱石</a></li>
            <li><a href="/b/154580/48736.html" title="贫僧不想当影帝 第二百三十五章 让收视飞1会儿" target="_blank">第二百三十五章 让收视飞1会儿</a></li>
            <li><a href="/b/154580/48458.html" title="贫僧不想当影帝 第二百三十四章 瑜策之交" target="_blank">第二百三十四章 瑜策之交</a></li>
            <li><a href="/b/154580/48388.html" title="贫僧不想当影帝 第二百三十三章 《3国》上映" target="_blank">第二百三十三章 《3国》上映</a></li>
            <li><a href="/b/154580/48239.html" title="贫僧不想当影帝 第二百三十二章 《3国》硬核花絮上线" target="_blank">第二百三十二章 《3国》硬核花絮上线</a></li>
            <li><a href="/b/154580/48046.html" title="贫僧不想当影帝 第二百三十一章 表演的3个层次" target="_blank">第二百三十一章 表演的3个层次</a></li>
            <li><a href="/b/154580/47946.html" title="贫僧不想当影帝 第二百三十章 寄予厚望" target="_blank">第二百三十章 寄予厚望</a></li>
            <li><a href="/b/154580/47917.html" title="贫僧不想当影帝 第二百二十九章 生活化的表演" target="_blank">第二百二十九章 生活化的表演</a></li>
            <li><a href="/b/154580/47825.html" title="贫僧不想当影帝 第二百二十八章 绝妙的选角" target="_blank">第二百二十八章 绝妙的选角</a></li>
            <li><a href="/b/154580/47757.html" title="贫僧不想当影帝 第二百二十七章 那个胖子是谁" target="_blank">第二百二十七章 那个胖子是谁</a></li>
            <li><a href="/b/154580/47642.html" title="贫僧不想当影帝 第二百二十六章 不1样的年代剧" target="_blank">第二百二十六章 不1样的年代剧</a></li>
            <li><a href="/b/154580/47544.html" title="贫僧不想当影帝 第二百二十五章 我恨我自己" target="_blank">第二百二十五章 我恨我自己</a></li>
            <li><a href="/b/154580/47460.html" title="贫僧不想当影帝 第二百二十四章 国家队" target="_blank">第二百二十四章 国家队</a></li>
            <li><a href="/b/154580/47324.html" title="贫僧不想当影帝 第二百二十三章 学霸与学渣" target="_blank">第二百二十三章 学霸与学渣</a></li>
            <li><a href="/b/154580/47201.html" title="贫僧不想当影帝 第二百二十二章???我的父亲" target="_blank">第二百二十二章???我的父亲</a></li>
            <li><a href="/b/154580/47091.html" title="贫僧不想当影帝 第二百二十一章 为生活奔波的人们" target="_blank">第二百二十一章 为生活奔波的人们</a></li>
            <li><a href="/b/154580/46983.html" title="贫僧不想当影帝 第二百二十章 闯关东" target="_blank">第二百二十章 闯关东</a></li>
            <li><a href="/b/154580/46868.html" title="贫僧不想当影帝 第二百一十九章 去东北老林子里拍戏" target="_blank">第二百一十九章 去东北老林子里拍戏</a></li>
            <li><a href="/b/154580/46769.html" title="贫僧不想当影帝 第二百一十八章 好饭不怕晚" target="_blank">第二百一十八章 好饭不怕晚</a></li>
            <li><a href="/b/154580/46697.html" title="贫僧不想当影帝 第二百一十七章 碾压" target="_blank">第二百一十七章 碾压</a></li>
            <li><a href="/b/154580/46557.html" title="贫僧不想当影帝 第二百一十六章 盛赞" target="_blank">第二百一十六章 盛赞</a></li>
            <li><a href="/b/154580/46533.html" title="贫僧不想当影帝 第二百一十五章 怎样的戏才叫好戏" target="_blank">第二百一十五章 怎样的戏才叫好戏</a></li>
            <li><a href="/b/154580/46325.html" title="贫僧不想当影帝 第二百一十四章 小许老师" target="_blank">第二百一十四章 小许老师</a></li>
            <li><a href="/b/154580/46293.html" title="贫僧不想当影帝 第二百一十三章 调整人设" target="_blank">第二百一十三章 调整人设</a></li>
            <li><a href="/b/154580/46111.html" title="贫僧不想当影帝 第二百一十二章 丑是够丑了" target="_blank">第二百一十二章 丑是够丑了</a></li>
            <li><a href="/b/154580/46036.html" title="贫僧不想当影帝 第二百一十一章 意料之外的导师" target="_blank">第二百一十一章 意料之外的导师</a></li>
            <li><a href="/b/154580/45892.html" title="贫僧不想当影帝 第二百一十章 《投名状》组的恩怨情仇" target="_blank">第二百一十章 《投名状》组的恩怨情仇</a></li>
            <li><a href="/b/154580/45834.html" title="贫僧不想当影帝 第二百零九章 来自红点中文网的热销小说" target="_blank">第二百零九章 来自红点中文网的热销小说</a></li>
            <li><a href="/b/154580/45665.html" title="贫僧不想当影帝 第二百零八章 你能做这部小说的男主角吗？" target="_blank">第二百零八章 你能做这部小说的男主角吗？</a></li>
            <li><a href="/b/154580/45644.html" title="贫僧不想当影帝 第二百零七章 这个演员好像阿真" target="_blank">第二百零七章 这个演员好像阿真</a></li>
            <li><a href="/b/154580/45435.html" title="贫僧不想当影帝 第二百零六章 许臻的第1部主角戏" target="_blank">第二百零六章 许臻的第1部主角戏</a></li>
            <li><a href="/b/154580/45396.html" title="贫僧不想当影帝 第二百零五章 玉兰奖最佳男配角提名" target="_blank">第二百零五章 玉兰奖最佳男配角提名</a></li>
            <li><a href="/b/154580/45208.html" title="贫僧不想当影帝 第二百零四章 他们在排《哈姆雷特》" target="_blank">第二百零四章 他们在排《哈姆雷特》</a></li>
            <li><a href="/b/154580/45136.html" title="贫僧不想当影帝 第二百零三章 王者归来" target="_blank">第二百零三章 王者归来</a></li>
            <li><a href="/b/154580/44978.html" title="贫僧不想当影帝 第二百零二章 考察团" target="_blank">第二百零二章 考察团</a></li>
            <li><a href="/b/154580/44905.html" title="贫僧不想当影帝 第二百零一章 我找到了" target="_blank">第二百零一章 我找到了</a></li>
            <li><a href="/b/154580/44740.html" title="贫僧不想当影帝 第二百章 该我上场了" target="_blank">第二百章 该我上场了</a></li>
            <li><a href="/b/154580/44720.html" title="贫僧不想当影帝 第一百九十九章 抛砖引玉" target="_blank">第一百九十九章 抛砖引玉</a></li>
            <li><a href="/b/154580/44572.html" title="贫僧不想当影帝 第一百九十八章 哥只是个传说" target="_blank">第一百九十八章 哥只是个传说</a></li>
            <li><a href="/b/154580/44504.html" title="贫僧不想当影帝 奋笔疾书中，但是有点不在状态，我几点写完几点发了，大家再多睡1会儿吧~" target="_blank">奋笔疾书中，但是有点不在状态，我几点写完几点发了，大…</a></li>
            <li><a href="/b/154580/44442.html" title="贫僧不想当影帝 第一百九十七章 主流演艺圈" target="_blank">第一百九十七章 主流演艺圈</a></li>
            <li><a href="/b/154580/44284.html" title="贫僧不想当影帝 第一百九十六章 爱才之心" target="_blank">第一百九十六章 爱才之心</a></li>
            <li><a href="/b/154580/44133.html" title="贫僧不想当影帝 第一百九十五章?? 扫地僧" target="_blank">第一百九十五章?? 扫地僧</a></li>
            <li><a href="/b/154580/44053.html" title="贫僧不想当影帝 我中午之前把这段写完再发" target="_blank">我中午之前把这段写完再发</a></li>
            <li><a href="/b/154580/44022.html" title="贫僧不想当影帝 第一百九十四章 沈老师的“小灶”" target="_blank">第一百九十四章 沈老师的“小灶”</a></li>
            <li><a href="/b/154580/43829.html" title="贫僧不想当影帝 第一百九十三章 导师们的选择" target="_blank">第一百九十三章 导师们的选择</a></li>
            <li><a href="/b/154580/43790.html" title="贫僧不想当影帝 第一百九十二章 五%的区别" target="_blank">第一百九十二章 五%的区别</a></li>
            <li><a href="/b/154580/43609.html" title="贫僧不想当影帝 第一百九十一章 好人脸" target="_blank">第一百九十一章 好人脸</a></li>
            <li><a href="/b/154580/43608.html" title="贫僧不想当影帝 第一百九十章 雌雄大盗" target="_blank">第一百九十章 雌雄大盗</a></li>
            <li><a href="/b/154580/43357.html" title="贫僧不想当影帝 第一百八十九章 直面A级演员" target="_blank">第一百八十九章 直面A级演员</a></li>
            <li><a href="/b/154580/43304.html" title="贫僧不想当影帝 第一百八十八章 对神剧挑挑拣拣" target="_blank">第一百八十八章 对神剧挑挑拣拣</a></li>
            <li><a href="/b/154580/43133.html" title="贫僧不想当影帝 第一百八十七章 热闹是他们的" target="_blank">第一百八十七章 热闹是他们的</a></li>
            <li><a href="/b/154580/43126.html" title="贫僧不想当影帝 8点前1定写完！！" target="_blank">8点前1定写完！！</a></li>
            <li><a href="/b/154580/43088.html" title="贫僧不想当影帝 第一百八十六章 “前辈”许臻" target="_blank">第一百八十六章 “前辈”许臻</a></li>
            <li><a href="/b/154580/42930.html" title="贫僧不想当影帝 第一百八十五章 无缺，你怎么看？" target="_blank">第一百八十五章 无缺，你怎么看？</a></li>
            <li><a href="/b/154580/42900.html" title="贫僧不想当影帝 稍等，写得不太满意，待我调整1下再发" target="_blank">稍等，写得不太满意，待我调整1下再发</a></li>
            <li><a href="/b/154580/42854.html" title="贫僧不想当影帝 第一百八十四章 花无缺二.零？" target="_blank">第一百八十四章 花无缺二.零？</a></li>
            <li><a href="/b/154580/42667.html" title="贫僧不想当影帝 第一百八十三章 辈分有点乱" target="_blank">第一百八十三章 辈分有点乱</a></li>
            <li><a href="/b/154580/42588.html" title="贫僧不想当影帝 第一百八十二章 来自东岳的奖励" target="_blank">第一百八十二章 来自东岳的奖励</a></li>
            <li><a href="/b/154580/42426.html" title="贫僧不想当影帝 第一百八十一章 全员接受挑战？" target="_blank">第一百八十一章 全员接受挑战？</a></li>
            <li><a href="/b/154580/42345.html" title="贫僧不想当影帝 第一百八十章 许臻的演技评级" target="_blank">第一百八十章 许臻的演技评级</a></li>
            <li><a href="/b/154580/42172.html" title="贫僧不想当影帝 第一百七十九章 天下风云出我辈" target="_blank">第一百七十九章 天下风云出我辈</a></li>
            <li><a href="/b/154580/42133.html" title="贫僧不想当影帝 第一百七十八章 文无第1，武无第2" target="_blank">第一百七十八章 文无第1，武无第2</a></li>
            <li><a href="/b/154580/41922.html" title="贫僧不想当影帝 第一百七十七章 新锐演技派" target="_blank">第一百七十七章 新锐演技派</a></li>
            <li><a href="/b/154580/41903.html" title="贫僧不想当影帝 第一百七十六章 1部短剧虐哭3国群雄" target="_blank">第一百七十六章 1部短剧虐哭3国群雄</a></li>
            <li><a href="/b/154580/41669.html" title="贫僧不想当影帝 第一百七十五章 跟曹操1起看《老男孩》是怎样的体验" target="_blank">第一百七十五章 跟曹操1起看《老男孩》是怎样的体验</a></li>
            <li><a href="/b/154580/41625.html" title="贫僧不想当影帝 第一百七十四章 粮草齐备，只欠东风" target="_blank">第一百七十四章 粮草齐备，只欠东风</a></li>
            <li><a href="/b/154580/41425.html" title="贫僧不想当影帝 第一百七十三章 酣饮" target="_blank">第一百七十三章 酣饮</a></li>
            <li><a href="/b/154580/41345.html" title="贫僧不想当影帝 第一百七十二章 许臻演周瑜是否合适" target="_blank">第一百七十二章 许臻演周瑜是否合适</a></li>
            <li><a href="/b/154580/41162.html" title="贫僧不想当影帝 第一百七十一章 群英会" target="_blank">第一百七十一章 群英会</a></li>
            <li><a href="/b/154580/41119.html" title="贫僧不想当影帝 第一百七十章 投资过亿的穷剧组" target="_blank">第一百七十章 投资过亿的穷剧组</a></li>
            <li><a href="/b/154580/40867.html" title="贫僧不想当影帝 第一百六十九章 谁笑场谁是小狗" target="_blank">第一百六十九章 谁笑场谁是小狗</a></li>
            <li><a href="/b/154580/40817.html" title="贫僧不想当影帝 第一百六十八章 “人精”周瑜" target="_blank">第一百六十八章 “人精”周瑜</a></li>
            <li><a href="/b/154580/40582.html" title="贫僧不想当影帝 第一百六十七章 资源倾斜" target="_blank">第一百六十七章 资源倾斜</a></li>
            <li><a href="/b/154580/40521.html" title="贫僧不想当影帝 第一百六十六章 1时瑜亮" target="_blank">第一百六十六章 1时瑜亮</a></li>
            <li><a href="/b/154580/40389.html" title="贫僧不想当影帝 第一百六十五章 ?1人挑翻江东" target="_blank">第一百六十五章 ?1人挑翻江东</a></li>
            <li><a href="/b/154580/40294.html" title="贫僧不想当影帝 第一百六十四章 别开生面的“行酒令”" target="_blank">第一百六十四章 别开生面的“行酒令”</a></li>
            <li><a href="/b/154580/40208.html" title="贫僧不想当影帝 第一百六十三章 《3国》进组" target="_blank">第一百六十三章 《3国》进组</a></li>
            <li><a href="/b/154580/40008.html" title="贫僧不想当影帝 第一百六十二章 力排众议" target="_blank">第一百六十二章 力排众议</a></li>
            <li><a href="/b/154580/39950.html" title="贫僧不想当影帝 第一百六十一章 再次亮相" target="_blank">第一百六十一章 再次亮相</a></li>
            <li><a href="/b/154580/39731.html" title="贫僧不想当影帝 第一百六十章 加钱？" target="_blank">第一百六十章 加钱？</a></li>
            <li><a href="/b/154580/39680.html" title="贫僧不想当影帝 第一百五十九章与角色的契合度" target="_blank">第一百五十九章与角色的契合度</a></li>
            <li><a href="/b/154580/39443.html" title="贫僧不想当影帝 第一百五十八章试戏成败的关键" target="_blank">第一百五十八章试戏成败的关键</a></li>
            <li><a href="/b/154580/39393.html" title="贫僧不想当影帝 第一百五十七章闯关东" target="_blank">第一百五十七章闯关东</a></li>
            <li><a href="/b/154580/39100.html" title="贫僧不想当影帝 第一百五十六章缔造经典角色" target="_blank">第一百五十六章缔造经典角色</a></li>
            <li><a href="/b/154580/39021.html" title="贫僧不想当影帝 第一百五十五章许臻的扛收视能力" target="_blank">第一百五十五章许臻的扛收视能力</a></li>
            <li><a href="/b/154580/38766.html" title="贫僧不想当影帝 第一百五十四章 后生可畏" target="_blank">第一百五十四章 后生可畏</a></li>
            <li><a href="/b/154580/38723.html" title="贫僧不想当影帝 第一百五十三章久违的“上电视”" target="_blank">第一百五十三章久违的“上电视”</a></li>
            <li><a href="/b/154580/38422.html" title="贫僧不想当影帝 第一百五十二章 人店合1" target="_blank">第一百五十二章 人店合1</a></li>
            <li><a href="/b/154580/38358.html" title="贫僧不想当影帝 第一百五十一章 油腻与颓废" target="_blank">第一百五十一章 油腻与颓废</a></li>
            <li><a href="/b/154580/38226.html" title="贫僧不想当影帝 第一百五十章 人到中年" target="_blank">第一百五十章 人到中年</a></li>
            <li><a href="/b/154580/38161.html" title="贫僧不想当影帝 第一百四十九章 直面新生代演员的扛把子" target="_blank">第一百四十九章 直面新生代演员的扛把子</a></li>
            <li><a href="/b/154580/37933.html" title="贫僧不想当影帝 第一百四十八章 青春如同奔流的江河" target="_blank">第一百四十八章 青春如同奔流的江河</a></li>
            <li><a href="/b/154580/37903.html" title="贫僧不想当影帝 第一百四十七章 碧血剑与老男孩" target="_blank">第一百四十七章 碧血剑与老男孩</a></li>
            <li><a href="/b/154580/37652.html" title="贫僧不想当影帝 第一百四十六章 学艺先学德，做戏先做人" target="_blank">第一百四十六章 学艺先学德，做戏先做人</a></li>
            <li><a href="/b/154580/37601.html" title="贫僧不想当影帝 第一百四十五章 恕我不能苟同" target="_blank">第一百四十五章 恕我不能苟同</a></li>
            <li><a href="/b/154580/37375.html" title="贫僧不想当影帝 第一百四十四章 是风格问题还是正误问题" target="_blank">第一百四十四章 是风格问题还是正误问题</a></li>
            <li><a href="/b/154580/37299.html" title="贫僧不想当影帝 第一百四十三章 哭戏的层次" target="_blank">第一百四十三章 哭戏的层次</a></li>
            <li><a href="/b/154580/37081.html" title="贫僧不想当影帝 第一百四十二章 丹心话剧社" target="_blank">第一百四十二章 丹心话剧社</a></li>
            <li><a href="/b/154580/37001.html" title="贫僧不想当影帝 第一百四十一章 中戏开学" target="_blank">第一百四十一章 中戏开学</a></li>
            <li><a href="/b/154580/36774.html" title="贫僧不想当影帝 第一百四十章 “反面角色”宋2或" target="_blank">第一百四十章 “反面角色”宋2或</a></li>
            <li><a href="/b/154580/36715.html" title="贫僧不想当影帝 第一百三十九章 前方记者杨立婧发来报道" target="_blank">第一百三十九章 前方记者杨立婧发来报道</a></li>
            <li><a href="/b/154580/36480.html" title="贫僧不想当影帝 第一百三十八章 势均力敌" target="_blank">第一百三十八章 势均力敌</a></li>
            <li><a href="/b/154580/36428.html" title="贫僧不想当影帝 第一百三十七章 高考成绩公布" target="_blank">第一百三十七章 高考成绩公布</a></li>
            <li><a href="/b/154580/36160.html" title="贫僧不想当影帝 第一百三十六章 从青涩到成熟" target="_blank">第一百三十六章 从青涩到成熟</a></li>
            <li><a href="/b/154580/36102.html" title="贫僧不想当影帝 第一百三十五章 你对草台班子的实力1无所知" target="_blank">第一百三十五章 你对草台班子的实力1无所知</a></li>
            <li><a href="/b/154580/35844.html" title="贫僧不想当影帝 第一百三十四章 金牌摄影师" target="_blank">第一百三十四章 金牌摄影师</a></li>
            <li><a href="/b/154580/35797.html" title="贫僧不想当影帝 第一百三十三章 逐鹿影视圈" target="_blank">第一百三十三章 逐鹿影视圈</a></li>
            <li><a href="/b/154580/35546.html" title="贫僧不想当影帝 第一百三十二章 出自金牌编剧之手的武侠剧本" target="_blank">第一百三十二章 出自金牌编剧之手的武侠剧本</a></li>
            <li><a href="/b/154580/35494.html" title="贫僧不想当影帝 第一百三十一章 第1届数字电影节" target="_blank">第一百三十一章 第1届数字电影节</a></li>
            <li><a href="/b/154580/35233.html" title="贫僧不想当影帝 第一百三十章 第2批演员敲定" target="_blank">第一百三十章 第2批演员敲定</a></li>
            <li><a href="/b/154580/35143.html" title="贫僧不想当影帝 第一百二十九章 3国知名老赖" target="_blank">第一百二十九章 3国知名老赖</a></li>
            <li><a href="/b/154580/34922.html" title="贫僧不想当影帝 第一百二十八章 《3国》选角" target="_blank">第一百二十八章 《3国》选角</a></li>
            <li><a href="/b/154580/34883.html" title="贫僧不想当影帝 第一百二十七章 艺考成绩出炉" target="_blank">第一百二十七章 艺考成绩出炉</a></li>
            <li><a href="/b/154580/34561.html" title="贫僧不想当影帝 第一百二十六章 反转" target="_blank">第一百二十六章 反转</a></li>
            <li><a href="/b/154580/34499.html" title="贫僧不想当影帝 第一百二十五章 怪我太优秀" target="_blank">第一百二十五章 怪我太优秀</a></li>
            <li><a href="/b/154580/34237.html" title="贫僧不想当影帝 第一百二十四章 集体小品" target="_blank">第一百二十四章 集体小品</a></li>
            <li><a href="/b/154580/34177.html" title="贫僧不想当影帝 第一百二十三章 偶遇戏精" target="_blank">第一百二十三章 偶遇戏精</a></li>
            <li><a href="/b/154580/33640.html" title="贫僧不想当影帝 第一百二十二章 你若盛开，清风自来" target="_blank">第一百二十二章 你若盛开，清风自来</a></li>
            <li><a href="/b/154580/33596.html" title="贫僧不想当影帝 第一百二十一章 留守儿童" target="_blank">第一百二十一章 留守儿童</a></li>
            <li><a href="/b/154580/33303.html" title="贫僧不想当影帝 第一百二十章 江山如画" target="_blank">第一百二十章 江山如画</a></li>
            <li><a href="/b/154580/33257.html" title="贫僧不想当影帝 第一百一十九章 托儿" target="_blank">第一百一十九章 托儿</a></li>
            <li><a href="/b/154580/32973.html" title="贫僧不想当影帝 第一百一十八章 你的刀呢" target="_blank">第一百一十八章 你的刀呢</a></li>
            <li><a href="/b/154580/32825.html" title="贫僧不想当影帝 第一百一十七章 红毯首秀" target="_blank">第一百一十七章 红毯首秀</a></li>
            <li><a href="/b/154580/32594.html" title="贫僧不想当影帝 第一百一十六章 介绍1下，这位是我同事" target="_blank">第一百一十六章 介绍1下，这位是我同事</a></li>
            <li><a href="/b/154580/32556.html" title="贫僧不想当影帝 第一百一十五章 年度爆款" target="_blank">第一百一十五章 年度爆款</a></li>
            <li><a href="/b/154580/32257.html" title="贫僧不想当影帝 第一百一十四章 逆风翻盘" target="_blank">第一百一十四章 逆风翻盘</a></li>
            <li><a href="/b/154580/32216.html" title="贫僧不想当影帝 第一百一十三章 当红的代价" target="_blank">第一百一十三章 当红的代价</a></li>
            <li><a href="/b/154580/31882.html" title="贫僧不想当影帝 第一百一十二章 寒假档之争" target="_blank">第一百一十二章 寒假档之争</a></li>
            <li><a href="/b/154580/31798.html" title="贫僧不想当影帝 第一百一十一章 同行不同命" target="_blank">第一百一十一章 同行不同命</a></li>
            <li><a href="/b/154580/31528.html" title="贫僧不想当影帝 第一百一十章 病态的恋情" target="_blank">第一百一十章 病态的恋情</a></li>
            <li><a href="/b/154580/31425.html" title="贫僧不想当影帝 第一百零九章 万0星辉慈善晚宴" target="_blank">第一百零九章 万0星辉慈善晚宴</a></li>
            <li><a href="/b/154580/31034.html" title="贫僧不想当影帝 第一百零八章 他是1个演员" target="_blank">第一百零八章 他是1个演员</a></li>
            <li><a href="/b/154580/31033.html" title="贫僧不想当影帝 第一百零七章 这是台庆剧吗？" target="_blank">第一百零七章 这是台庆剧吗？</a></li>
            <li><a href="/b/154580/30716.html" title="贫僧不想当影帝 第一百零六章 夏雪宜的第1场戏" target="_blank">第一百零六章 夏雪宜的第1场戏</a></li>
            <li><a href="/b/154580/30540.html" title="贫僧不想当影帝 第一百零五章 夏雪宜的主观视角（拜谢跑调男低音的盟主！！）" target="_blank">第一百零五章 夏雪宜的主观视角（拜谢跑调男低音的盟主…</a></li>
            <li><a href="/b/154580/30273.html" title="贫僧不想当影帝 第一百零四章 人物小传" target="_blank">第一百零四章 人物小传</a></li>
            <li><a href="/b/154580/30272.html" title="贫僧不想当影帝 第一百零三章 蜕变的契机" target="_blank">第一百零三章 蜕变的契机</a></li>
            <li class="volume">正文卷</li>
            <li><a href="/b/154580/30270.html" title="贫僧不想当影帝 第一百零二章 来自董琦玉的提点（后附上架感言）" target="_blank">第一百零二章 来自董琦玉的提点（后附上架感言）</a></li>
            <li><a href="/b/154580/29840.html" title="贫僧不想当影帝 第一百零一章 神秘的武术指导（下）" target="_blank">第一百零一章 神秘的武术指导（下）</a></li>
            <li><a href="/b/154580/29839.html" title="贫僧不想当影帝 第一百章 神秘的武术指导（上）" target="_blank">第一百章 神秘的武术指导（上）</a></li>
            <li><a href="/b/154580/29431.html" title="贫僧不想当影帝 第九十九章 《碧血剑》开机" target="_blank">第九十九章 《碧血剑》开机</a></li>
            <li><a href="/b/154580/29258.html" title="贫僧不想当影帝 第九十八章 梅花桩上的表演" target="_blank">第九十八章 梅花桩上的表演</a></li>
            <li><a href="/b/154580/28981.html" title="贫僧不想当影帝 第九十七章 来自央视的邀约" target="_blank">第九十七章 来自央视的邀约</a></li>
            <li><a href="/b/154580/28693.html" title="贫僧不想当影帝 第九十六章 ?缘，妙不可言" target="_blank">第九十六章 ?缘，妙不可言</a></li>
            <li><a href="/b/154580/28692.html" title="贫僧不想当影帝 第九十五章 ?参评最佳新人奖" target="_blank">第九十五章 ?参评最佳新人奖</a></li>
            <li><a href="/b/154580/28447.html" title="贫僧不想当影帝 第九十四章 被衰神眷顾的男人" target="_blank">第九十四章 被衰神眷顾的男人</a></li>
            <li><a href="/b/154580/28148.html" title="贫僧不想当影帝 第九十三章 你过年的时候都看什么？" target="_blank">第九十三章 你过年的时候都看什么？</a></li>
            <li><a href="/b/154580/28081.html" title="贫僧不想当影帝 第九十二章 悬崖上的对决" target="_blank">第九十二章 悬崖上的对决</a></li>
            <li><a href="/b/154580/27713.html" title="贫僧不想当影帝 第九十一章 不服老的老陈" target="_blank">第九十一章 不服老的老陈</a></li>
            <li><a href="/b/154580/27595.html" title="贫僧不想当影帝 第九十章 迎风1刀斩" target="_blank">第九十章 迎风1刀斩</a></li>
            <li><a href="/b/154580/27264.html" title="贫僧不想当影帝 第八十九章 时也命也" target="_blank">第八十九章 时也命也</a></li>
            <li><a href="/b/154580/27205.html" title="贫僧不想当影帝 第八十八章 央视大导演" target="_blank">第八十八章 央视大导演</a></li>
            <li><a href="/b/154580/26822.html" title="贫僧不想当影帝 第八十七章 出家人的精髓（后附3江感言）" target="_blank">第八十七章 出家人的精髓（后附3江感言）</a></li>
            <li><a href="/b/154580/26763.html" title="贫僧不想当影帝 睡过了……我马上写" target="_blank">睡过了……我马上写</a></li>
            <li><a href="/b/154580/26641.html" title="贫僧不想当影帝 第八十六章 本色出演" target="_blank">第八十六章 本色出演</a></li>
            <li><a href="/b/154580/26640.html" title="贫僧不想当影帝 稍等，写得慢了，请再给我1个小时~" target="_blank">稍等，写得慢了，请再给我1个小时~</a></li>
            <li><a href="/b/154580/26292.html" title="贫僧不想当影帝 第八十五章 来自陈正豪的压力" target="_blank">第八十五章 来自陈正豪的压力</a></li>
            <li><a href="/b/154580/26222.html" title="贫僧不想当影帝 第八十四章 最美艺考生" target="_blank">第八十四章 最美艺考生</a></li>
            <li><a href="/b/154580/25782.html" title="贫僧不想当影帝 第八十三章 酒局上的酒话" target="_blank">第八十三章 酒局上的酒话</a></li>
            <li><a href="/b/154580/25638.html" title="贫僧不想当影帝 第八十二章 被学习绊住了脚步" target="_blank">第八十二章 被学习绊住了脚步</a></li>
            <li><a href="/b/154580/25206.html" title="贫僧不想当影帝 第八十一章 江南的3伏天太热了" target="_blank">第八十一章 江南的3伏天太热了</a></li>
            <li><a href="/b/154580/25108.html" title="贫僧不想当影帝 第八十章 娘心不似铁" target="_blank">第八十章 娘心不似铁</a></li>
            <li><a href="/b/154580/24749.html" title="贫僧不想当影帝 第七十九章 重新定义网剧" target="_blank">第七十九章 重新定义网剧</a></li>
            <li><a href="/b/154580/24577.html" title="贫僧不想当影帝 第七十八章 观众小许" target="_blank">第七十八章 观众小许</a></li>
            <li><a href="/b/154580/24210.html" title="贫僧不想当影帝 第七十七章 破釜沉舟" target="_blank">第七十七章 破釜沉舟</a></li>
            <li><a href="/b/154580/23991.html" title="贫僧不想当影帝 第七十六章 围剿东岳影视" target="_blank">第七十六章 围剿东岳影视</a></li>
            <li><a href="/b/154580/23620.html" title="贫僧不想当影帝 第七十五章 声名鹊起" target="_blank">第七十五章 声名鹊起</a></li>
            <li><a href="/b/154580/22636.html" title="贫僧不想当影帝 第七十四章 杜0山的选择" target="_blank">第七十四章 杜0山的选择</a></li>
            <li><a href="/b/154580/21635.html" title="贫僧不想当影帝 第七十三章 许臻的秘密武器" target="_blank">第七十三章 许臻的秘密武器</a></li>
            <li><a href="/b/154580/19975.html" title="贫僧不想当影帝 第七十二章 绝非良配" target="_blank">第七十二章 绝非良配</a></li>
            <li><a href="/b/154580/19558.html" title="贫僧不想当影帝 第七十一章 邪气凛然" target="_blank">第七十一章 邪气凛然</a></li>
            <li><a href="/b/154580/18061.html" title="贫僧不想当影帝 第七十章 来自古装男神的降维打击" target="_blank">第七十章 来自古装男神的降维打击</a></li>
            <li><a href="/b/154580/17619.html" title="贫僧不想当影帝 第六十九章 世界你好，我叫许真" target="_blank">第六十九章 世界你好，我叫许真</a></li>
            <li><a href="/b/154580/17074.html" title="贫僧不想当影帝 第六十八章 画中的少年" target="_blank">第六十八章 画中的少年</a></li>
            <li><a href="/b/154580/15775.html" title="贫僧不想当影帝 第六十七章 官方打脸（新年快乐！）" target="_blank">第六十七章 官方打脸（新年快乐！）</a></li>
            <li><a href="/b/154580/15774.html" title="贫僧不想当影帝 第六十六章 正义也许会迟到" target="_blank">第六十六章 正义也许会迟到</a></li>
            <li><a href="/b/154580/15219.html" title="贫僧不想当影帝 第六十五章 佛缘深厚" target="_blank">第六十五章 佛缘深厚</a></li>
            <li><a href="/b/154580/12269.html" title="贫僧不想当影帝 第六十四章 大佬带飞" target="_blank">第六十四章 大佬带飞</a></li>
            <li><a href="/b/154580/11910.html" title="贫僧不想当影帝 第六十三章 论表演的感染力" target="_blank">第六十三章 论表演的感染力</a></li>
            <li><a href="/b/154580/8900.html" title="贫僧不想当影帝 第六十二章 随堂小测" target="_blank">第六十二章 随堂小测</a></li>
            <li><a href="/b/154580/8855.html" title="贫僧不想当影帝 第六十一章 自作多情的俞影后" target="_blank">第六十一章 自作多情的俞影后</a></li>
            <li><a href="/b/154580/5252.html" title="贫僧不想当影帝 第六十章 天下第1刀" target="_blank">第六十章 天下第1刀</a></li>
            <li><a href="/b/154580/2953.html" title="贫僧不想当影帝 第五十九章 0面女王" target="_blank">第五十九章 0面女王</a></li>
            <li><a href="/b/154580/2952.html" title="贫僧不想当影帝 第五十八章 来自太平公主的关注" target="_blank">第五十八章 来自太平公主的关注</a></li>
            <li><a href="/b/154580/2951.html" title="贫僧不想当影帝 第五十七章 摊牌了，我叫许臻" target="_blank">第五十七章 摊牌了，我叫许臻</a></li>
            <li><a href="/b/154580/2950.html" title="贫僧不想当影帝 第五十六章 明明是我先的" target="_blank">第五十六章 明明是我先的</a></li>
            <li><a href="/b/154580/2949.html" title="贫僧不想当影帝 第五十五章 许臻的选择" target="_blank">第五十五章 许臻的选择</a></li>
            <li><a href="/b/154580/2948.html" title="贫僧不想当影帝 第五十四章 忽然成了香饽饽" target="_blank">第五十四章 忽然成了香饽饽</a></li>
            <li><a href="/b/154580/2947.html" title="贫僧不想当影帝 第五十三章 我替你转告她" target="_blank">第五十三章 我替你转告她</a></li>
            <li><a href="/b/154580/2946.html" title="贫僧不想当影帝 第五十二章 1戏双杀" target="_blank">第五十二章 1戏双杀</a></li>
            <li><a href="/b/154580/2945.html" title="贫僧不想当影帝 第五十一章 救场" target="_blank">第五十一章 救场</a></li>
            <li><a href="/b/154580/2944.html" title="贫僧不想当影帝 第五十章 论吸睛的正确姿势" target="_blank">第五十章 论吸睛的正确姿势</a></li>
            <li><a href="/b/154580/2943.html" title="贫僧不想当影帝 第四十九章 吾家少年初长成" target="_blank">第四十九章 吾家少年初长成</a></li>
            <li><a href="/b/154580/2942.html" title="贫僧不想当影帝 第四十八章 贫僧不喜欢虐菜" target="_blank">第四十八章 贫僧不喜欢虐菜</a></li>
            <li><a href="/b/154580/2941.html" title="贫僧不想当影帝 第四十七章 人间赫玛" target="_blank">第四十七章 人间赫玛</a></li>
            <li><a href="/b/154580/2940.html" title="贫僧不想当影帝 第四十六章 我是演技派" target="_blank">第四十六章 我是演技派</a></li>
            <li><a href="/b/154580/2939.html" title="贫僧不想当影帝 第四十五章 东岳影视的培养计划" target="_blank">第四十五章 东岳影视的培养计划</a></li>
            <li><a href="/b/154580/2938.html" title="贫僧不想当影帝 第四十四章 少年不识红尘好" target="_blank">第四十四章 少年不识红尘好</a></li>
            <li><a href="/b/154580/2937.html" title="贫僧不想当影帝 第四十三章 回山" target="_blank">第四十三章 回山</a></li>
            <li><a href="/b/154580/2936.html" title="贫僧不想当影帝 第四十二章 跑得了和尚跑不了庙" target="_blank">第四十二章 跑得了和尚跑不了庙</a></li>
            <li><a href="/b/154580/2935.html" title="贫僧不想当影帝 第四十一章 1败涂地" target="_blank">第四十一章 1败涂地</a></li>
            <li><a href="/b/154580/2934.html" title="贫僧不想当影帝 第四十章 ?真戏精就是要carry全场" target="_blank">第四十章 ?真戏精就是要carry全场</a></li>
            <li><a href="/b/154580/2933.html" title="贫僧不想当影帝 第三十九章 命运不公" target="_blank">第三十九章 命运不公</a></li>
            <li><a href="/b/154580/2932.html" title="贫僧不想当影帝 第三十八章 大佬下场" target="_blank">第三十八章 大佬下场</a></li>
            <li><a href="/b/154580/2931.html" title="贫僧不想当影帝 第三十七章 蹭热度第1名" target="_blank">第三十七章 蹭热度第1名</a></li>
            <li><a href="/b/154580/2930.html" title="贫僧不想当影帝 第三十六章 第1次遭遇网暴" target="_blank">第三十六章 第1次遭遇网暴</a></li>
            <li><a href="/b/154580/2929.html" title="贫僧不想当影帝 第三十五章 定1个小目标：打败丁雪松！" target="_blank">第三十五章 定1个小目标：打败丁雪松！</a></li>
            <li><a href="/b/154580/2928.html" title="贫僧不想当影帝 第三十四章 来自东岳影视的橄榄枝" target="_blank">第三十四章 来自东岳影视的橄榄枝</a></li>
            <li><a href="/b/154580/2927.html" title="贫僧不想当影帝 第三十三章 请给家人多1点的陪伴" target="_blank">第三十三章 请给家人多1点的陪伴</a></li>
            <li><a href="/b/154580/2926.html" title="贫僧不想当影帝 第三十二章 烧鸡" target="_blank">第三十二章 烧鸡</a></li>
            <li><a href="/b/154580/2925.html" title="贫僧不想当影帝 第三十一章 实力全开的宋彧" target="_blank">第三十一章 实力全开的宋彧</a></li>
            <li><a href="/b/154580/2924.html" title="贫僧不想当影帝 第三十章 来1场堂堂正正的对决" target="_blank">第三十章 来1场堂堂正正的对决</a></li>
            <li><a href="/b/154580/2923.html" title="贫僧不想当影帝 第二十九章 分组拍摄" target="_blank">第二十九章 分组拍摄</a></li>
            <li><a href="/b/154580/2922.html" title="贫僧不想当影帝 第二十八章 附体式演技" target="_blank">第二十八章 附体式演技</a></li>
            <li><a href="/b/154580/2921.html" title="贫僧不想当影帝 第二十七章 空手入白刃" target="_blank">第二十七章 空手入白刃</a></li>
            <li><a href="/b/154580/2920.html" title="贫僧不想当影帝 第二十六章 开机大吉" target="_blank">第二十六章 开机大吉</a></li>
            <li><a href="/b/154580/2919.html" title="贫僧不想当影帝 第二十五章 潘多拉的硬盘" target="_blank">第二十五章 潘多拉的硬盘</a></li>
            <li><a href="/b/154580/2918.html" title="贫僧不想当影帝 第二十四章 安排得明明白白" target="_blank">第二十四章 安排得明明白白</a></li>
            <li><a href="/b/154580/2917.html" title="贫僧不想当影帝 第二十三章 0载难逢的机会" target="_blank">第二十三章 0载难逢的机会</a></li>
            <li><a href="/b/154580/2916.html" title="贫僧不想当影帝 第二十二章 老天爷赏饭吃" target="_blank">第二十二章 老天爷赏饭吃</a></li>
            <li><a href="/b/154580/2915.html" title="贫僧不想当影帝 第二十一章 错的不是我！" target="_blank">第二十一章 错的不是我！</a></li>
            <li><a href="/b/154580/2914.html" title="贫僧不想当影帝 第二十章 来自沙雕门的师兄" target="_blank">第二十章 来自沙雕门的师兄</a></li>
            <li><a href="/b/154580/2913.html" title="贫僧不想当影帝 第一十九章 许2狗" target="_blank">第一十九章 许2狗</a></li>
            <li><a href="/b/154580/2912.html" title="贫僧不想当影帝 第一十八章 贺白眼" target="_blank">第一十八章 贺白眼</a></li>
            <li><a href="/b/154580/2911.html" title="贫僧不想当影帝 第一十七章 偶遇大明星" target="_blank">第一十七章 偶遇大明星</a></li>
            <li><a href="/b/154580/2910.html" title="贫僧不想当影帝 第一十六章 颜值即是正义" target="_blank">第一十六章 颜值即是正义</a></li>
            <li><a href="/b/154580/2909.html" title="贫僧不想当影帝 第一十五章 贫僧不想带假发" target="_blank">第一十五章 贫僧不想带假发</a></li>
            <li><a href="/b/154580/2908.html" title="贫僧不想当影帝 第一十四章 介绍工作？" target="_blank">第一十四章 介绍工作？</a></li>
            <li><a href="/b/154580/2907.html" title="贫僧不想当影帝 第一十三章 缔造经典" target="_blank">第一十三章 缔造经典</a></li>
            <li><a href="/b/154580/2906.html" title="贫僧不想当影帝 第一十二章 这世上哪有什么轻功" target="_blank">第一十二章 这世上哪有什么轻功</a></li>
            <li><a href="/b/154580/2905.html" title="贫僧不想当影帝 第一十一章 你在教我拍戏？" target="_blank">第一十一章 你在教我拍戏？</a></li>
            <li><a href="/b/154580/2904.html" title="贫僧不想当影帝 第一十章 杀手夜雨" target="_blank">第一十章 杀手夜雨</a></li>
            <li><a href="/b/154580/2903.html" title="贫僧不想当影帝 第九章 夜雨" target="_blank">第九章 夜雨</a></li>
            <li><a href="/b/154580/2902.html" title="贫僧不想当影帝 第八章 许是真的" target="_blank">第八章 许是真的</a></li>
            <li><a href="/b/154580/2901.html" title="贫僧不想当影帝 第七章 盗版逼死原版系列" target="_blank">第七章 盗版逼死原版系列</a></li>
            <li><a href="/b/154580/2900.html" title="贫僧不想当影帝 第六章 有备而来" target="_blank">第六章 有备而来</a></li>
            <li><a href="/b/154580/2899.html" title="贫僧不想当影帝 第五章 气质巨变的“许致远”" target="_blank">第五章 气质巨变的“许致远”</a></li>
            <li><a href="/b/154580/2898.html" title="贫僧不想当影帝 第四章 童星哪有不长残的" target="_blank">第四章 童星哪有不长残的</a></li>
            <li><a href="/b/154580/2897.html" title="贫僧不想当影帝 第三章 佛门高手" target="_blank">第三章 佛门高手</a></li>
            <li><a href="/b/154580/2896.html" title="贫僧不想当影帝 第二章 你能不能替他把戏拍了" target="_blank">第二章 你能不能替他把戏拍了</a></li>
            <li><a href="/b/154580/2895.html" title="贫僧不想当影帝 第一章 双生子" target="_blank">第一章 双生子</a></li>
            <li class="volume">正文卷</li>
            </ul>
'''

def get_url_title():
    idx_begin = 0
    idx_end = 0

    l = []
    while 1:
        idx_begin = html_temp.find("<li><a href=\"", idx_end)
        if idx_begin < 0:
            break

        idx_end = html_temp.find("</a></li>", idx_begin)
        if idx_end < 0:
            break

        li_node = html_temp[idx_begin:idx_end]
        print(li_node)

        pos1 = li_node.find(".html\"")
        if pos1 < 0:
            print("ERROR")
            continue
        url = "https://www.uukanshu.com" + li_node[13:pos1 + 5]

        pos2 = li_node.find("target=\"_blank\">")
        if pos2 < 0:
            print("ERROR")
            continue

        pos2 += len("target=\"_blank\">")

        title = li_node[pos2:]

        # print(url, title)
        l.append([url, title])

    l.reverse()
    print(l)
    return l


def download_urls(l):
    for url, title in l:
        fname = "贫僧不想当影帝/" + title + ".html"
        fname = fname.replace("?", "")

        if os.path.exists(fname):
            print(title, "已存在")
            continue
        print(title, "下载中")
        html = download_html(url)

        with open(fname, "wb") as fw:
            fw.write(html.encode())


def get_content(l):
    fw = open('贫僧不想当影帝.txt', 'w', encoding='utf-8')

    for url, title in l:
        fname = "贫僧不想当影帝/" + title + ".html"
        print(title)
        fname = fname.replace("?", "")
        fr = open(fname, 'rb')
        html = fr.read()
        fr.close()
        html = html.decode('utf-8')
        print(type(html))

        pos1 = html.find("<!-- 桌面内容顶部 -->")
        pos1 += len("<!-- 桌面内容顶部 -->")

        pos2 = html.find("<div style=\"margin:0px;\">", pos1)

        content = html[pos1:pos2]

        content = content.replace("<p>", "\r\n    ")
        content = content.replace("<br/>", "\r\n")
        content = content.replace("<br />", "\r\n")
        content = content.replace("<br>", "\r\n")
        content = content.replace("&ensp;", " ")
        content = content.replace("&nbsp;", " ")


        while 1:
            s1 = content.find("<script>")
            s2 = content.find("</script>")

            if s1 < 0 or s2 < 0:
                break

            content = content[0:s1] + content[s2 + len("</script>"):]

        while 1:
            s1 = content.find("<")
            s2 = content.find(">")

            if s1 < 0 or s2 < 0:
                break

            content = content[0:s1] + content[s2 + 1:]
        content = content.replace("https://", "")
        content = content.replace("天才一秒记住本站地址：。手机版阅读网址：", "")
        content = content.strip()
        content = "    " + content

        fw.write(title)
        fw.write("\r\n\r\n")
        print(type(content))
        print(content)
        fw.write(content)
        fw.write("\r\n\r\n")

    fw.close()

if __name__ == '__main__':
    print('----------dataDealer----------')

    l = get_url_title()
    #download_urls(l)
    get_content(l)





