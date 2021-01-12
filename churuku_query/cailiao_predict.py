
from matplotlib import pyplot

def cailiao_pre():


    #横坐标
    year=[2010,2012,2014,2016]
    #纵坐标
    count=[20,40,60,100]
    #生成折线图：函数polt
    pyplot.plot(year,count)
    #设置横坐标说明
    pyplot.xlabel('year')
    #设置纵坐标说明
    pyplot.ylabel('count')
    #添加标题
    pyplot.title('count year correspondence')
    #设置纵坐标刻度
    pyplot.yticks([0, 25, 50, 75, 90])
    # 显示网格
    pyplot.grid(False)
    #显示图表
    pyplot.show()