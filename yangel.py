import serial
import sys
from tkinter import *
import binascii

global x
global y
x=0
y=0
dic = {
    '0': 0, '1': 1, '2': 2,
    '3': 3, '4': 4, '5': 5,
    '6': 6, '7': 7, '8': 8,
    '9': 9, 'a': 10, 'b': 11,
    'c': 12, 'd': 13, 'e': 14,
    'f': 15,
}
def setChars( OData):
    # 将字符串转换为字符组格式，并还原每一行
    asd = []
    i = 0
    TLong = len(OData)
    while OData[i + 1] is not None:
        asd.append(OData[i:i + 2])
        i = i + 2
        if i >= TLong:
            break
    return asd


def byte16ToInt(byte16):
    # 补码转换为原码
    if (byte16 & 0x80) == 0:
        r = byte16
    else:
        byte16 = byte16 ^ 0xff
        byte16 = byte16 + 1
        r = -byte16
    return r


def NumChange2(OData):
    TLong = len(OData)
    i = 0
    asd = []
    while TRUE:
        a = 0x00 + 16 * dic[OData[i][0]] + dic[OData[i][1]]
        b = byte16ToInt(a)
        asd.append(b)
        i = i + 1
        if i == TLong:
            break
    return asd


def searchFF1(OData):
    global x
    global y
    # 检索角度数据并反馈数据流
    for i in range(len(OData) - 12):
        if OData[i:i + 3] == ["55", "55", "01"] and i + 11 <= len(OData):
            Slop = OData[i + 4:i + 10]
            for m in range(len(Slop)):
                Slop[m] = byte16ToInt(0x00 + 16 * dic[Slop[m][0]] + dic[Slop[m][1]])
            setSloop(Slop)
            x = float(setSloop(Slop)[0])
            y = float(setSloop(Slop)[1])
            OData[:i] = []


def setSloop(OData):
    # 角度算法，数组有三个模块，分别为x,y,z方向的角度
    return [round((byte16ToInt(OData[1]) << 8 | byte16ToInt(OData[0])) / 32768 * 180, 3),
            round((byte16ToInt(OData[3]) << 8 | byte16ToInt(OData[2])) / 32768 * 180, 3),
            round((byte16ToInt(OData[5]) << 8 | byte16ToInt(OData[4])) / 32768 * 180, 3)]