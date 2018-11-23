import xlrd
import matplotlib.pyplot as plt
from pylab import *
from matplotlib.ticker import MultipleLocator, FormatStrFormatter

path = "D:\\lion_ide\\py_1\\data.xlsx"

data = xlrd.open_workbook(path)
table = data.sheets()[1]

# plt.axis([-100, 100, 0, 10000])

# 这一段很重要 ， 写的是每一个数据来自 excel 文件的哪一列 ，
# 我做的事情是 按照从左到右的顺序复制的， 你得自己看一眼数据和标签对上了吗
X_RH = table.col_values(0)
Y_RH = table.col_values(1)

X_RO = table.col_values(2)
Y_RO = table.col_values(3)

X_RD = table.col_values(4)
Y_RD = table.col_values(5)

X_RL = table.col_values(6)
Y_RL = table.col_values(7)

X_RM = table.col_values(8)
Y_RM = table.col_values(9)

X_RP = table.col_values(10)
Y_RP = table.col_values(11)

X_RS = table.col_values(12)
Y_RS = table.col_values(13)

X_P1670 = table.col_values(14)
Y_P1670 = table.col_values(15)

X_P1570 = table.col_values(16)
Y_P1570 = table.col_values(17)

# 这是可以更改的风格 有一些风格可以选择
# 底下这些随便复制一个代替ggplot应该都可以修改风格
# ['seaborn-dark', 'dark_background', 'seaborn-pastel', 'seaborn-colorblind', 'tableau-colorblind10', 'seaborn-notebook', 'seaborn-dark-palette', 'grayscale', 'seaborn-poster', 'seaborn', 'bmh', 'seaborn-talk', 'seaborn-ticks', '_classic_test', 'ggplot', 'seaborn-white', 'classic', 'Solarize_Light2', 'seaborn-paper', 'fast', 'fivethirtyeight', 'seaborn-muted', 'seaborn-whitegrid', 'seaborn-darkgrid', 'seaborn-bright', 'seaborn-deep']
plt.style.use('seaborn-bright')
# plt.figure(figsize=(10, 5))
plt.xlim(140, 390)
plt.ylim(18, 105)
# plt.xticks() 这条是调整横坐标具体哪几个点上有数字的， 目前是默认的

X_list = [X_RH, X_RO, X_RD, X_RL, X_RM, X_RP, X_RS, X_P1670, X_P1570]
Y_list = [Y_RH, Y_RO, Y_RD, Y_RL, Y_RM, Y_RP, Y_RS, Y_P1670, Y_P1570]

# 这条决定了每一个数据的marker， 具体有一个网页， 决定的方式就是和X_list一样的顺序
Markerlist = ['o', 'v', '^', '<', '>', 's', 'p', 'H', 'D']

L_handler = []

for i in range(len(X_list)):
    # 在这里更改线的粗细和marksize的大小，具体就是修改下面等号后面的小数
    L, = plt.plot(X_list[i], Y_list[i], linewidth=1.0, marker=Markerlist[i], markersize=2.5)
    L_handler.append(L)

Label_list = ["RH", "RO", "RD", "RL", "RM", "RP", "RS", "P1670", "P1570"]
xla = "Temperature (℃)"
plt.xlabel(xla)
yla = "Residual mass(%)"
plt.ylabel(yla)
plt.legend(L_handler, Label_list, loc=0)



xmajorLocator = MultipleLocator(50)  # 将x主刻度标签设置为20的倍数
xmajorFormatter = FormatStrFormatter('%1.1f')  # 设置x轴标签文本的格式
xminorLocator = MultipleLocator(10)  # 将x轴次刻度标签设置为5的倍数

ymajorLocator = MultipleLocator(10)  # 将y轴主刻度标签设置为0.5的倍数
ymajorFormatter = FormatStrFormatter('%1.1f')  # 设置y轴标签文本的格式
yminorLocator = MultipleLocator(2)  # 将此y轴次刻度标签设置为0.1的倍数

# t = arange(0.0, 100.0, 1)
# s = sin(0.1 * pi * t) * exp(-t * 0.01)
#
# ax = subplot(111)  # 注意:一般都在ax中设置,不再plot中设置
# plot(t, s, '--b*')


ax = plt.gca()
# 设置主刻度标签的位置,标签文本的格式
ax.xaxis.set_major_locator(xmajorLocator)
ax.xaxis.set_major_formatter(xmajorFormatter)

ax.yaxis.set_major_locator(ymajorLocator)
ax.yaxis.set_major_formatter(ymajorFormatter)

# 显示次刻度标签的位置,没有标签文本
ax.xaxis.set_minor_locator(xminorLocator)
ax.yaxis.set_minor_locator(yminorLocator)



# plt.savefig("testsave.png")
plt.show()