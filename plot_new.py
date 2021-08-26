import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import math
from time import sleep
from datetime import datetime
import random
from scipy.signal import savgol_filter
# x = [i for i in range(-100,100)]
# y = [i**3 for i in x]
# plt.plot(x,y)
# plt.show()
# x = []
# y = []

# ***************************************************************
plt.figure(figsize=(15,7))
x = [l for l in range(100)]
y = [0 for l in range(100)]
lst = 0
data = 45
fps = 0
s1 = 0

# for l in range(100):
#     m = lst + (random.randint(-3,3)/random.randint(1,5))
#     # m = lst + (random.randint(-3,3))
#     # m = lst + (random.uniform(float(-1.5),float(1.5)))
#     y.append(m)
#     lst = m

def date_time():
    now = datetime.now()
    time_now = now.strftime("%H:%M:%S")
    date_now = now.strftime("%Y/%m/%d")
    sec = int(now.strftime("%S"))
    # print(time_now)
    # print(date_now)
    return time_now, date_now, sec

def x_axis():
    x.pop(0)
    x.append(x[98]+1)

def animate(i):
    global lst
    global fps
    global s1
    x_axis()
    y.pop(0)


    # m = lst + (random.uniform(float(-1.5),float(1.5)))
    m = (random.randint(-4,4))

    # m = data
    # m = (math.sin(math.radians(i)))
    # m = lst + (math.sin(math.radians(i)))
    y.append(m)
    lst = m
    # print(m)
        # m = lst + (random.randint(-3,3)/random.randint(1,5))

    # for m in range(len(x)):
    #     # print("x: " + str(m))
    #     # print("y: " + str(y[m]))
    #     y.append(random.randint(-2,2))
    # yhat = savgol_filter(y, 51, 3)
    plt.cla()
    plt.plot(x,y, color = 'red')
    t, d, s = date_time()
    # T = random.randint(-10, 20)
    fps = fps+1
    if(s-s1>=1):
        print(fps)
        fps=0
        s1 = s
    # plt.plot(x,yhat, color = 'blue')

ani = FuncAnimation(plt.gcf(),animate, interval = 2)
plt.show()

# x = [i for i in range(1001)]
# y = []
# def ran():
#     for l in x:
#         y.append(random.randint(-100, 100))
#     plt.cla()
#     plt.plot(x,y)
#     plt.show()
#     sleep(1)
#
# ran()
# ****************************************************
