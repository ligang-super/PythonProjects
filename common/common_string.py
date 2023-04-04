# -*- coding:utf-8 -*-
# __author__='ligang'


#检验是否含有中文字符
def is_contains_chinese(strs):
    for _char in strs:
        if '\u4e00' <= _char <= '\u9fa5':
            return True
    return False


def is_chinese(uchar):
    """判断一个unicode是否是汉字"""
    if uchar >= u'\u4e00' and uchar <= u'\u9fa5':
        #print(uchar, True)
        return True
    else:
        #print(uchar, False)
        return False


def is_alphabet(uchar):
    """判断一个unicode是否是英文字母"""
    if (uchar >= u'\u0041' and uchar <= u'\u005a') or (uchar >= u'\u0061' and uchar <= u'\u007a'):
        return True
    else:
        return False


def count_str(content):
    space_count = 0
    digit_count = 0
    alphabet_count = 0
    chinese_count = 0
    other_count = 0

    for i in content:
        # 判断是否为空格
        if i.isspace():
            #print(i, "isspace")
            space_count += 1
        # 判断是否为数字
        elif i.isdigit():
            #print(i, "isdigit")
            digit_count += 1
        # 判断是否为英文字符
        elif is_alphabet(i):
            #print(i, "is_alphabet")
            alphabet_count += 1
        # 判断是否为中文字符
        elif is_chinese(i):
            #print(i, "is_chinese")
            chinese_count += 1
        # 判断是否为其他字符
        else:
            #print(i, "is either")
            other_count += 1

    return {
        "space_count": space_count,
        "digit_count": digit_count,
        "alphabet_count": alphabet_count,
        "chinese_count": chinese_count,
        "other_count": other_count,
    }

