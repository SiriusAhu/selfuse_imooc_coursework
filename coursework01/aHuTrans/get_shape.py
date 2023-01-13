import numpy as np
from .Shape import *


def rectangle(startPos: tuple, width: float, height: float) -> Shape:
    '''
    返回围成一个矩形的tuple形式的`Shape`

    *注意：为了包围整个图形，实际返回的坐标有5个点
    
    Parameters
    ----------
    `startPos` : tuple 起始点，位于图形左下角
    `width` : float 矩形的长
    `height` : float 矩形的宽
    '''
    return Shape([(startPos[0], startPos[1]),
                  (startPos[0], startPos[1] + height),
                  (startPos[0] + width, startPos[1] + height),
                  (startPos[0] + width, startPos[1]),
                  (startPos[0], startPos[1])])


def triangle_3p(startPos: tuple, pos1: tuple, pos2: tuple) -> Shape:
    '''
    根据`三点坐标`，返回围成一个三角形的`Shape`

    *注意：为了包围整个图形，实际返回的坐标有4个点
    
    Parameters
    ----------
    `startPos` : tuple 起始点，位于图形左下角
    `pos1` : tuple 另一个角的坐标
    `pos2` : tuple 另一个角的坐标
    '''
    return Shape([(startPos[0], startPos[1]), (pos1[0], pos1[1]),
                  (pos2[0], pos2[1]), (startPos[0], startPos[1])])


def circle(center: tuple, radius: float) -> Shape:
    '''
    根据`圆心坐标`和`半径`，返回围成一个圆形的`Shape`
    
    Parameters
    ----------
    `center` : tuple 圆心
    `radius` : float 半径
    '''
    thetas = np.arange(0, 2 * np.pi, 0.01 * np.pi)
    x = [radius * np.sin(t) + center[0] for t in thetas]
    y = [radius * np.cos(t) + center[1] for t in thetas]
    pointList = []
    for i in range(len(x)):
        pointList.append((x[i], y[i]))
    return Shape((pointList))