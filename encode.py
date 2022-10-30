# list1 = ['零', '一', '二', '三', '四', '五', '六', '七', '八', '九']
list1 = ['零', '壹', '贰', '叁', '肆', '伍', '陆', '柒', '捌', '玖']


# 阿拉伯数字转大写数字/数字
def encrypt(enter1):
    enter = str(int(enter1))
    go = ''
    for i in range(0, len(enter)):
        go += list1[int(enter[i])]

    return go


# 大写数字/数字转阿拉伯数字
def decrypt(enter1):
    enter = str(enter1)
    go = ''
    for i in range(0, len(enter)):
        go += str(list1.index(enter[i]))

    return go
