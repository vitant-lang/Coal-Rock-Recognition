import cv2
import numpy as np
import pyqtgraph as pg

app = pg.mkQApp("Gradiant Layout Example")
view = pg.GraphicsView()
l = pg.GraphicsLayout(border=(100,100,100))
view.setCentralItem(l)
#view.show()
view.setWindowTitle('识别数据分析')
view.resize(800,600)

## Title at top
text = """图像识别"""
l.addLabel(text, col=1, colspan=4)
l.nextRow()

## Put vertical label on left side
l.addLabel('参数分析', angle=-90, rowspan=3)

## Add 3 plots into the first row (automatic position)
p1 = l.addPlot(title="精准度")
p2 = l.addPlot(title="图片噪声")
vb = l.addViewBox(lockAspect=True)

img = cv2.imread('demo.jpg')
image_arr = np.array(img)
img = pg.ImageItem(image_arr)
vb.addItem(img)
vb.autoRange()


## Add a sub-layout into the second row (automatic position)
## The added item should avoid the first column, which is already filled
l.nextRow()
l2 = l.addLayout(colspan=3, border=(50,0,0))
l2.setContentsMargins(10, 10, 10, 10)
l2.addLabel("---------------------------", colspan=3)
l2.nextRow()
l2.addLabel('竖直分析', angle=-90, rowspan=2)
p21 = l2.addPlot(row=3, col=1)
p22 = l2.addPlot(row=3, col=1)
l2.nextRow()
p23 = l2.addPlot()
p24 = l2.addPlot()
l2.nextRow()
l2.addLabel("水平分析", col=1, colspan=2)

## hide axes on some plots
p21.hideAxis('bottom')
p22.hideAxis('bottom')
p22.hideAxis('left')
p24.hideAxis('left')
p21.hideButtons()
p22.hideButtons()
p23.hideButtons()
p24.hideButtons()


## Add 2 more plots into the third row (manual position)
p4 = l.addPlot(row=3, col=1)
p5 = l.addPlot(row=3, col=2, colspan=2)

## show some content in the plots
p1.plot([1,3,2,4,3,5])
p2.plot([3,5,1,3,2,4])
p4.plot([2,5,3,2,1,4])
p5.plot([1,3,2,4,3,5])

