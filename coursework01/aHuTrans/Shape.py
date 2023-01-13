import numpy as np


class Shape:
    '''
    一个储存形状（Shape）坐标及其变化方法的类

    需要传入围成Shape的点
    '''
    def __init__(self, pointList) -> None:
        self._pointList = pointList
        self._xyList = np.array([[point[0] for point in self._pointList],
                                 [point[1] for point in self._pointList]])

    def _pointList_update(self) -> None:
        """同步`self._pointList`和`self._xyList`的值"""
        self._pointList = [(x, y)
                           for x, y in zip(self._xyList[0], self._xyList[1])]

    # 形状变换的几种方法：
    def zoom(self, zoomout: tuple or float) -> 'Shape':
        '''
        将Shape按`zoomout`倍率进行放大

        *zoomout可以是单个数或者是数组
        
        *若为tuple：(x方向倍数, y方向倍数)
        
        Parameters
        ----------
        `zoomout`: tuple or float 根据传入数值进行规则/不规则放大
        '''
        if isinstance(zoomout, tuple):
            Trans = np.array([[zoomout[0], 0], [0, zoomout[1]]])
        else:
            Trans = np.array([[zoomout, 0], [0, zoomout]])
        self._xyList = Trans.dot(self._xyList)
        self._pointList_update()
        return self

    def rotate(self, radian: float) -> 'Shape':
        '''
        将Shape按`radian`弧度进行旋转

        *注意：`radian`为弧度
        
        Parameters
        ----------
        `radian`: float 根据传入弧度进行旋转
        '''
        Trans = np.array([[np.cos(radian), np.sin(radian)],
                          [-np.sin(radian), np.cos(radian)]])
        self._xyList = Trans.dot(self._xyList)
        self._pointList_update()
        return self

    def flip(self, axis='y') -> 'Shape':
        '''
        沿着原点（o）或者y轴（y）或者x轴（x）方向翻转

        *默认为沿垂直方向翻转

        Parameters
        ----------
        `axis`: str 翻转时参考的轴，应填入('o''y''x')之一，默认为'y'
        '''
        if axis == 'o':
            Trans = np.array([[-1, 0], [0, -1]])
        elif axis == 'y':
            Trans = np.array([[-1, 0], [0, 1]])
        elif axis == 'x':
            Trans = np.array([[1, 0], [0, -1]])

        self._xyList = Trans.dot(self._xyList)
        self._pointList_update()
        return self
