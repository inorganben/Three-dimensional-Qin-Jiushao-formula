# 定义秦九韶’公式
def qin(lst):
    a = float(lst[0])
    b = float(lst[1])
    c = float(lst[2])
    s = ((2 * ((a ** 2 * b ** 2) + (a ** 2 * c ** 2) + (b ** 2 * c ** 2)) - (a ** 4 + b ** 4 + c ** 4)) ** 0.5) / 4
    return s


# 三角形垂线分割底后的两段长度
def fen(lst):
    a = float(lst[0])  # 设第一个为底边
    b = float(lst[1])  # 设第二个为临边
    c = float(lst[2])  # 设第三个为对边
    l = (a ** 2 + b ** 2 - c ** 2) / (2 * a)
    return l


"""
引申问题：
对于三角形abc，已知abc的长度，底边c上存在一点将c平分为左右m、n两段，已知m、n的长度，求该点和顶点的连线的长度
"""


# 设要求的长度为hx,
# 可定义函数如下,需要引入的参数有：mn的比例k，三角形三边长组成的列表
def hx(k, lst):
    a = lst[0]
    b = lst[1]
    c = lst[2]
    w = (k*((a**2 + b**2 - c**2) / (2 * b) - b) + b)**2
    w_1 = (2 * ((a ** 2 * b ** 2) + (a ** 2 * c ** 2) + (b ** 2 * c ** 2)) - (a ** 4 + b ** 4 + c ** 4))
    ww = (k**2 * w_1) / (4 * b**2)
    answer = (w + ww)**0.5
    return answer


# 上个问题的比例仍需补充一个公式
def kmn(lst):
    a = lst[0]
    c = lst[2]
    d = lst[3]
    e = lst[4]
    f = lst[5]
    k = (f**2 + c**2 - e**2 - a**2) / (d**2 + f**2 - e**2)
    return k


if __name__ == "__main__":
    list_test = list(map(float, input().split()))
    print(qin(list_test))
    print(fen(list_test))


    def gao(ss, d):
        g = ss / (0.5 * d)
        return g


    dd = 2
    q = qin(list_test)
    print(gao(q, dd))
