import logger as lg
import time
import serial.tools.list_ports
import random
import keyboard

ser = "null"
d = 0

def Connect():
    # global l
    global ser
    # global status
    # global running
    port_sel = 'COM8'
    print("Connecting")
    ser = serial.Serial(port = port_sel, baudrate =  9600, timeout=1)
    time.sleep(2)

def con(m = 0):
    # global is_reading_serial
    line = str(ser.readline()).replace('r','').replace('n','').replace('\\','').replace('b','').replace('\'','')
    # print(line)
    try:
        lg.plt_telemetry(int(line))
    except:
        print('TLM - N/A')
    # time.sleep(0.0001)
    # while(is_alive == 1):
    #     if (status == 1):
    #         try:
    #             is_reading_serial = True
    #             # time.sleep(2)
    #             # m = m+1
    #             # print_term(str(m))
    #             # print(m)
    #             # line = str(ser.readline()).replace('r','').replace('n','').replace('\\','').replace('b','').replace('\'','')
    #             # print("Recieved: " + line)
    #             if (line == '' ):
    #                 time.sleep(0.1)
    #                 line = str(ser.readline()).replace('r','').replace('n','').replace('\\','').replace('b','').replace('\'','')
    #             if (line != ''):
    #                 pr = "Alert: " + line
    #                 print_term(str(pr))
    #                 if(line == '60'):
    #                     messagebox.showwarning('Warning', 'Malfunction Warning!!!!')
    #             term="READ <-" + line
    #             print(term)
    #         except:
    #             print("Port Closed")
    #     else:
    #         time.sleep(0.2)
    #     is_reading_serial = False
    #     time.sleep(0.1)

    # try:
    #     if (running == 0):
    #         running = 1
    #     print("Connecting")
    #     ser = serial.Serial(port = port_sel, baudrate =  9600, timeout=1)
    #     l = l+1
    #     term = "Connected to: " + str(port_sel)
    #     print_term(term)
    #     time.sleep(2)
    #     Connect_result = send_data(3)
    #     status = 1
    #     if Connect_result == "3":
    #         print("Connected Successfully")
    #         Button_Open.config(text ='Connected', bg='#00FF00')
    #     else:
    #         print("Connection Failed")
    #         threading.Thread(target=Open_B_Blink).start()
    #         # Button_Open.confi(bg='#FF0000')
    # except:
    #     threading.Thread(target=Open_B_Blink).start()
    #     print_term("Failed to open port")

def ran():
    global d
    d = d+random.randint(-2,3)
    if (d>=350 or d<-350):
        d = 0
    lg.plt_telemetry(d)
    # time.sleep(0.0001)

if __name__ == '__main__':
    Connect()

    while(1):
        con()
        # ran()
        if keyboard.is_pressed('q'):  # if key 'q' is pressed
            print('Program Exit')
            break  # finishing the loop
