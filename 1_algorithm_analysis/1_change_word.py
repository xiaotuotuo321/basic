"""
变位词
问题记录,如果一个字符串为“python”,还有一个字符串“pyonth”,则说它们互为'变位词'
"""


def judge_change_word(str1, str2):
    """
    判断变位词
    :param str1: 第一个字符串
    :param str2: 第二个字符串
    :return: bool
    """

    new_str1 = list(str1)
    new_str2 = list(str2)

    if sorted(new_str1) == sorted(new_str2):
        print(sorted(new_str1))
        print(sorted(new_str2))
        return True
    else:
        return False


if __name__ == '__main__':
    a = "python"
    b = "pyonth"
    c = ""
    print(judge_change_word(a, b))
    print(judge_change_word(a, c))


