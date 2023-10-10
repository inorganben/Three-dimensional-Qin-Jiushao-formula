import functions

"""
所需参数：
输入的基础参数：abcdef（做为列表使用）
其他参数（此处应作为函数使用）：
i,底面三角形BDC的高DM
h,三棱锥的高
j,前侧面三角形ABC的高AP
k,过高和AP的三角形与地面的交线
p、q,被M所分成的左右两部分
m、n,被P点所分成的左右两部分
r,过高和AP的三角形和左后面的三角形相交的线，用以计算h
"""


# 主思路：求h
def main():
    # 引入abcdef做为列表使用
    list_v = list(map(float, input("三棱锥的边长以空格隔开").split()))
    # 构造所需的三角形的列表
    list_bdc = [list_v[3], list_v[4], list_v[5]]  # d e f
    list_abc = [list_v[3], list_v[2], list_v[0]]  # d c a
    list_acd = [list_v[4], list_v[1], list_v[2]]  # e b c
    list_adb = [list_v[5], list_v[1], list_v[0]]  # f b a

    # 求底面面积
    s_bdc = s_def = functions.qin(list_bdc)
    # 求dac为边的面积
    s_dac = functions.qin(list_abc)
    # m,q的处理
    m_lst = [list_v[3], list_v[0], list_v[2]]
    q_lst = [list_v[3], list_v[4], list_v[5]]
    m = def_m(m_lst)
    q = def_m(q_lst)

    # 前三角形和底三角形的高：i、j
    i = def_i(s_def, list_v[3])  # key = s_bdc, d
    j = def_j(s_dac, list_v[3])  # key = s_dac, d

    # 过高和AP的三角形与地面的交线：K
    k = def_k(m, i, list_v[3], q)  # key = i, d, m, q,
    # 计算r！
    list_r = [list_v[0], list_v[1], list_v[5]]
    k_k = functions.kmn(list_v)
    r = functions.hx(k_k, list_r)

    # 计算高h！！！
    list_h = [j, r, k]
    s_jrk = functions.qin(list_h)
    h = def_h(s_jrk, k)

    # 最后，得出体积：！！！！！！！
    v = (s_bdc * h) / 3
    print(v)


# 定义i函数生成数据i
def def_i(s_s, dd):
    ii = s_s / (0.5 * dd)  # 面积除以底
    return ii


def def_m(lst):
    m = functions.fen(lst)
    return m


def def_h(s_s, dd):
    hh = s_s / (0.5 * dd)
    return hh


def def_j(s_s, dd):
    jj = s_s / (0.5 * dd)
    return jj


def def_k(m, i, d, q):
    kk = (m * i) / (d - q)
    return kk


main()
