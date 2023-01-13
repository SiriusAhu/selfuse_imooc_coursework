# aHu的小型图形变换库
## 简介
本库是用于imooc线性代数课程的自用微型图形变换库，仅为个人练习用。

包含了一个Shape类以及一系列内置方法来更方便得对以点围成的封闭图形进行图形变换上的操作。
## 引用的库：
- matplotlib
- numpy
## 实现的功能：
参考example_code（md或jupyter）
### get_shape.py中的一系列方法
- rectangle(startPos: tuple, width: float, height: float)
  - 给出`起始点`，`长`和`宽`，获得用于绘制矩形的Shape类
- triangle_3p(startPos: tuple, pos1: tuple, pos2: tuple)
  - 给出`三个点`，获得用于绘制三角形的Shape类
- circle(center: tuple, radius: float)
  - 给出`圆心`和`半径，获得用于绘制圆的Shape类

### draw_shape.py中的一系列方法
- default_canvas()
  - 规定了画布的默认大小
- draw(shape: Shape, useDefaultCanvas=True, isNewFig=False, newFigSize=(5, 5))
  - 直接传入Shape类进行绘制
  - （可选择）创建新的画布
  - （可选择）使用默认/自定义的画布大小
### 图形（Shape）类
- zoom(self, zoomout: tuple or float) -> 'Shape'
  - 规则缩放
  - 不规则缩放（指定x，y方向的缩放倍数）
- rotate(self, radian: float) -> 'Shape'
  - 按弧度旋转
- flip(self, axis='y') -> 'Shape'
  - 沿`原点`或`y轴`或`x轴`翻转