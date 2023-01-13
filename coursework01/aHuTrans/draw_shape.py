import matplotlib.pyplot as plt
from .Shape import *


def defalt_canvas():
    """Ruled the default size of canvas (-10, 10) x (-10, 10)"""
    plt.xlim(-10, 10)
    plt.ylim(-10, 10)


def draw(shape: Shape,
         useDefaultCanvas=True,
         isNewFig=False,
         newFigSize=(5, 5)):
    """
    绘制图形
    
    可选择是否创建新图像
    
    可选择图像大小
    """
    if isNewFig:
        plt.figure(figsize=newFigSize)
    if useDefaultCanvas:
        defalt_canvas()
    plt.plot(shape._xyList[0], shape._xyList[1])