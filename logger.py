import os
import sys
from datetime import datetime
import time
import random

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import math
from time import sleep
from scipy.signal import savgol_filter

# Threading for plotss
# import threading

file_array = []
plt.figure(figsize=(15,6), dpi = 85,facecolor = 'black')

plt.get_current_fig_manager().set_window_title('LIVE Telemetry- AT_Mine')
# plt.gcf().text(0, 0, 'text',fontsize=14)
# plt.text(2000, 2000, 'wewe', fontsize=14)


# plt.manager.set_window_title('LIVE Telemetry')
# plt.gcf().set_window_title('LIVE Telemetry')
# Maximized screen
mng = plt.get_current_fig_manager()
mng.window.state('zoomed') #works fine on Windows!

plt.rcParams['axes.facecolor'] = 'black'
plt.rcParams['text.color'] = 'white'
plt.rcParams['axes.edgecolor'] = 'white'
plt.rcParams['axes.titlecolor'] = 'white'
plt.rcParams['xtick.color'] = 'white'
plt.rcParams['ytick.color'] = 'white'
plt.rcParams['xtick.labelcolor'] = 'white'
plt.rcParams['ytick.labelcolor'] = 'white'
plt.rcParams['axes.labelcolor'] = 'white'

# plt.rcParams['figure.facecolor'] = 'grey'
# plt.rcParams['figure.edgecolor'] = 'grey'
# plt.patch.set_facecolor('xkcd:mint green')


scale = 100
mine_tri = 80

# plt.set_title('P-T Graph')
x = [l for l in range(scale)]
y = [0 for l in range(scale)]
trigger_line = [mine_tri for l in range(scale)]



bar_x = ['Trig_point', 'Pressure_max', 'Pressure_current' ]
bar_y = [mine_tri, 3, 4]


def x_axis():
    x.pop(0)
    x.append(x[len(x)-1]+1)

def animate():
    x_axis()
    # # plt.text(0, 0,'Skunk_works_v2',ha='center', va='bottom', rotation=0, fontsize = 20)
    # # plt.text(0, 0, 'text', bbox=dict(facecolor='red', alpha=0.5))
    # # yhat = savgol_filter(y, 55, 4)
    # plt.plot(x,y, '.',color = 'red')
    # # plt.plot(x,yhat, color = 'blue')
    # plt.draw()
    # plt.pause(0.0001)
    # plt.clf()

# Show 2 sub plots/////////////////////////////////////////////////////////////////////
    # y_lastelem = y[len(y)-1]
    # yhat = savgol_filter(y, 55, 4)
    # plt.subplot(2,1,1)
    # plt.title('P-T Graph')
    # plt.grid(True, linestyle ='dashed', linewidth = 0.3)
    # plt.ylabel('Weight')
    # plt.xlabel('Time')
    # plt.plot(x,y , '3' ,label='REC', color = 'cyan', linestyle= 'dashed', linewidth=0.8)
    # # plt.scatter(x,y ,color = 'cyan')
    # # plt.ylim(-10,200)
    # if(y_lastelem>mine_tri):
    #     plt.plot(x,y ,'3',label = 'Detonation', color = 'red', linestyle= 'dashed', linewidth=0.8)
    # plt.plot(x,yhat,label = 'Prediction', color = 'y')
    # plt.plot(x, trigger_line, label = 'Trigger_lim', color='red', linestyle='dashed', linewidth=1, markersize=12)
    # plt.legend(loc='upper right', bbox_to_anchor=(1.1, 1))
    #
    # # plt.plot(x,trigger_line, color = 'blu')
    # # plt.xlim(0,200)
    #
    # # plt.plot(x,yhat, color = 'blue')
    # # print(bar_y[1])
    # # bar_y.pop(1)
    # # print(bar_y)
    # plt.subplot(2,1,2)
    # bar_y[2] = y_lastelem
    # adj = bar_y[1]/10
    # if (bar_y[2] > bar_y[1]):
    #     bar_y[1] = bar_y[2]
    # plt.bar(bar_x[0], bar_y[0], color = 'b')
    # plt.ylabel('Weight')
    # plt.text(0, bar_y[0]-adj,str(bar_y[0]),ha='center', va='bottom', rotation=0, fontsize = 15)
    # plt.grid(True, linestyle ='dashed', linewidth = 0.3)
    # if(bar_y[2] > mine_tri):
    #     plt.bar(bar_x[1], bar_y[1], color = 'r')
    #     plt.bar(bar_x[2], bar_y[2], color = 'r')
    #     plt.text(1, bar_y[1]-adj,str(bar_y[1]),ha='center', va='bottom', rotation=0, fontsize = 15)
    #     plt.text(2, bar_y[2]-adj,str(bar_y[2]),ha='center', va='bottom', rotation=0, fontsize = 15)
    # else:
    #     plt.bar(bar_x[1], bar_y[1], color = 'g')
    #     plt.bar(bar_x[2], bar_y[2], color = 'g')
    #     plt.text(1, bar_y[1]-adj,str(bar_y[1]),ha='center', va='bottom', rotation=0, fontsize = 15)
    #     plt.text(2, bar_y[2]-adj,str(bar_y[2]),ha='center', va='bottom', rotation=0, fontsize = 15)
    #
    # plt.draw()
    # plt.pause(0.00001)
    # plt.clf()


# all intergrated ////////////////////////////////////////////////////////////////
    y_lastelem = y[len(y)-1]
    plt.gcf().text(0, 0.97,'Skunk_works_v2', fontsize=13)

    yhat = savgol_filter(y, 55, 4)
    plt.title('P-T Graph')
    plt.grid(True, linestyle ='dashed', linewidth = 0.3)
    plt.ylabel('Weight')
    plt.xlabel('Time')

    if(y_lastelem>mine_tri):
        plt.plot(x, y,'3',label = 'Detonation', color = 'red', linestyle= 'dashed', linewidth=0.8)
    else:
        plt.plot(x,y , '3' ,label='Safe-level', color = 'cyan', linestyle= 'dashed', linewidth=0.8)
    plt.plot(x,yhat,label = 'Prediction', color = 'y')
    plt.plot(x, trigger_line, label = 'Trigger_lim', color='red', linestyle='dashed', linewidth=1, markersize=12)
    plt.legend(loc='upper right', bbox_to_anchor=(1.1, 1))
    bar_y[2] = y_lastelem

    if (bar_y[2] > bar_y[1]):
        bar_y[1] = bar_y[2]
    plt.bar(x[0], bar_y[0],width=scale/40, color = 'b')
    plt.ylabel('Weight')
    plt.text(x[0], bar_y[0],str(bar_y[0]),ha='center',va='bottom', rotation=0, fontsize = 15)
    plt.text(x[0], 0,bar_x[0],ha='center', va='bottom', rotation=90, fontsize = 12)
    plt.grid(True, linestyle ='dashed', linewidth = 0.3)

    if(bar_y[2] > mine_tri):
        plt.bar(x[1] + (scale/40)+ scale/80, bar_y[1],width=scale/40, color = 'r')
        plt.text(x[1] + (scale/40)+ scale/80, 0,bar_x[1],ha='center', va='bottom', rotation=90, fontsize = 12)
        plt.text(x[1] + (scale/40)+ scale/80, bar_y[1],str(bar_y[1]),ha='center', va='bottom', rotation=0, fontsize = 15)
        plt.bar(x[2]+ 2*((scale/40)+ scale/80), bar_y[2],width=scale/40, color = 'r')
        plt.text(x[2]+ 2*((scale/40)+ scale/80), 0,bar_x[2],ha='center', va='bottom', rotation=90, fontsize = 12)
        plt.text(x[2]+ 2*((scale/40)+ scale/80), bar_y[2],str(bar_y[2]),ha='center', va='bottom', rotation=0, fontsize = 15)
        plt.gcf().text(0.45, 0.91,'Detonation!!!!', color = 'r',fontsize=25)
        # plt.bar(x[scale-1], bar_y[2],width=scale/40, color = 'r')
        # plt.text(x[scale-1], 0,bar_x[2],ha='center', va='bottom', rotation=90, fontsize = 12)
        # plt.text(x[scale-1], bar_y[2],str(bar_y[2]),ha='center', va='bottom', rotation=0, fontsize = 15)
    else:
        plt.bar(x[1] + (scale/40)+ scale/80, bar_y[1],width=scale/40, color = 'g')
        plt.text(x[1] + (scale/40)+ scale/80, 0,bar_x[1],ha='center', va='bottom', rotation=90, fontsize = 12)
        plt.text(x[1] + (scale/40)+ scale/80, bar_y[1],str(bar_y[1]),ha='center', va='bottom', rotation=0, fontsize = 15)
        plt.bar(x[2]+ 2*((scale/40)+ scale/80), bar_y[2],width=scale/40, color = 'g')
        plt.text(x[2]+ 2*((scale/40)+ scale/80), 0,bar_x[2],ha='center', va='bottom', rotation=90, fontsize = 12)
        plt.text(x[2]+ 2*((scale/40)+ scale/80), bar_y[2],str(bar_y[2]),ha='center', va='bottom', rotation=0, fontsize = 15)
        # plt.bar(x[scale-1], bar_y[2],width=scale/40, color = 'g')
        # plt.text(x[scale-1], 0,bar_x[2],ha='center', va='bottom', rotation=90, fontsize = 12)
        # plt.text(x[scale-1], bar_y[2],str(bar_y[2]),ha='center', va='bottom', rotation=0, fontsize = 15)

    plt.draw()
    plt.pause(0.00001)
    plt.clf()



# C:\Azhaar_Data\IM_proc\Data_logger\Data_text
def create_file(fname):
    name = "C:\Azhaar_Data\IM_proc\Data_logger\Data_text"+ "\\" + str(fname) + ".txt"
    # print(name)
    file1 = open(name, 'w+')
    print('file created')
    file1.close()

def read_text(fname, l_data):
    global file_array
    if (len(file_array)==0):
        print(len(file_array))
        name= "C:\Azhaar_Data\IM_proc\Data_logger\Data_text"+ "\\" + str(fname) + ".txt"
        l = open(name, encoding="utf-8")
        file_array = l.read().split('\n')
        file_array.append(l_data)
        file_array.remove('')
    write_text_file(fname, file_array)
    # print(file_array)


def write_text_file(filename, data):
    try:
        name = "C:\Azhaar_Data\IM_proc\Data_logger\Data_text"+ "\\" + str(filename) + ".txt"
        # print(name)
        file1 = open(name, 'a')
        # file1.writelines(data)
        # file1.writelines(" ")
        # file1.writelines("\n")
        # file1.writelines(data)
        file1.writelines(data)
        file1.writelines("\n")

        # for l in range(len(data)):
        #     file1.writelines(data[l])
        #     # file1.writelines(" ")
        #     file1.writelines("\n")
        #     # for ll in range(len(data[l])):

        file1.close()
    except:
        create_file(filename)











def date_time():
    now = datetime.now()
    time_now = now.strftime("%H:%M:%S")
    date_now = now.strftime("%Y/%m/%d")
    sec = int(now.strftime("%S"))
    # print(time_now)
    # print(date_now)
    return time_now, date_now, sec





def draw():
    ani = FuncAnimation(plt.gcf(),animate,interval = 2)
    plt.show()


fps = 0
s1 = 0


def plt_telemetry(logger_data):
    global fps
    global s1
    plt.xticks(rotation = 90)
    t, d, s = date_time()
    # T = random.randint(-10, 20)
    fps = fps+1

    T = logger_data
    t  = t + ' T: ' + str(T)
    if(s-s1>=1):
        print(fps)
        fps=0
        s1 = s

    # s = datetime.now().strftime("%H.%M.%S")
    # print(t)
    # write_text_file("Telemetrylogs", t)
    # read_text("Telemetrylogs", t)

    write_text_file("Telemetrylogs", t)

    y.pop(0)
    y.append(T)
    animate()
    # pause()
    # time.sleep(0.01)


if __name__ == "__main__":
    print('hello')
    # threading.Thread(target=draw).start()
    for _ in range(1000):

        plt.xticks(rotation = 90)
        t, d = date_time()
        T = random.randint(-10, 20)
        t  = t + ' T: ' + str(T)
        # s = datetime.now().strftime("%H.%M.%S")
        print(t)
        # write_text_file("Telemetrylogs", t)
        read_text("Telemetrylogs", t)
        y.pop(0)
        y.append(T)
        animate()
        # pause()
        time.sleep(0.01)
    # threading.Thread(target=draw).join()
        # resume()
