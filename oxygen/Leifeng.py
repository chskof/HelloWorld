"""
谁是雷锋
"""


def main():
    f = 1   # 用1234分别表示甲乙丙丁 首先假设甲是雷锋
    while f <= 4:
        p1 = f != 3     # 不是丙做的
        p2 = f == 4     # 是丁做的
        p3 = f == 2     # 是乙做的
        p4 = f != 4     # 不是丁做的

        if p1 + p2 + p3 + p4 == 1:      # 只有一人说了真话
            print(f)    # 打印假设的人
            break
        else:
            f += 1      # 假设是下一个人


if __name__ == '__main__':
    main()


