"""
random_pwd_kayotin - 生成随机密码

Author: ahjiang
Date 2023/3/30
"""
import random


def random_password(digits=8):
    """
    生成随机密码
    :param digits:密码位数，默认为8
    :return: 密码字符串
    """
    upper = ["A", "B", "C", "D", "E", "F", "G", "H", "J", "K",
             "M", "N", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    lower = []
    for i in range(len(upper)):
        lower.append(upper[i].lower())
    nums = [num for num in range(2, 10)]
    password = ""
    for dig in range(digits):
        if dig == 0:
            password += upper[random.randrange(0, len(upper))]
        elif dig < 4:
            password += lower[random.randrange(0, len(lower))]
        else:
            password += str(nums[random.randrange(0, len(nums))])
    return password


if __name__ == '__main__':
    print(f"生成的密码是：{random_password()}")
