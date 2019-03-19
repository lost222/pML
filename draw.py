import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np

import os


def list_dat(dir):
    list = os.listdir(dir)#列出目录下的所有文件和目录
    data_list = []
    for line in list:
        filepath = os.path.join(dir, line)
        if not os.path.isdir(filepath):
            if line[-3:] == "dat":
                data_list.append(line)
    return data_list


data_file = list_dat("./")
formlist = ['o', 'd', 's', "*", "^"]
for name in data_file:
    file = open(name)
    nameSplited = str(name).split("_")
    fs_label = nameSplited[1]
    if nameSplited[2] == "no":
        fs_label = fs_label + "_" + nameSplited[2] + "_" +nameSplited[3]
    x = []
    y = []
    line = file.readline()
    line = file.readline()
    while line:
        x.append(int(line.split()[0]))
        y.append(float(line.split()[1]))
        line = file.readline()
    plt.plot(x, y, marker=formlist[-1], label=fs_label)
    formlist.pop()

t = data_file[0].split("_")
t.pop(1)
title = ""
for i in t:
    title = title + " " + str(i)

title = title.rstrip(".dat")
plt.title(title)
plt.legend(loc='best')
plt.xlabel("cores")
plt.ylabel("M ops/s")

plt.savefig(title + ".png")
