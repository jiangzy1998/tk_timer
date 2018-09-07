from storage import storage
import tkinter as tk
from USBTool import MainUSBTool
import datetime as d

# 分，秒，毫秒
min1 = sec1 = ms1 = 0
min2 = sec2 = ms2 = 0
min3 = sec3 = ms3 = 0
pun1 = 0
pun2 = 0
pun3 = 0
startMs1 = startMs2 = startMs3 = 0

#鼠标长按时间
btnPressTime = 0

# 判断3定时器是否正在运行
isT1Start = isT2Start = isT3Start = False

isAllStart = False
isBtnPress = False
isUsbOpen = False
isLongClick = False

window = tk.Tk()
screenwidth = window.winfo_screenwidth()
screenheight = window.winfo_screenheight()
window.geometry("%dx%d" % (screenwidth, screenheight))
window.attributes("-fullscreen", True)

frm = tk.Frame(window)
frm.pack()

frm_top_each_width = int(screenheight / 5 * 4)
frm_top = tk.Frame(frm, height=frm_top_each_width, width=screenwidth)
frm_top.pack()
frm_top.pack_propagate(0)

frm_top_1 = tk.Frame(frm_top,
                     height=frm_top_each_width,
                     width=screenwidth / 3,
                     bg='#4db6ac')

frm_top_2 = tk.Frame(frm_top,
                     height=frm_top_each_width,
                     width=screenwidth / 3,
                     bg='#4dd0e1')

frm_top_3 = tk.Frame(frm_top,
                     height=frm_top_each_width,
                     width=screenwidth / 3,
                     bg='#4fc3f7')

frm_top_1.pack_propagate(0)
frm_top_2.pack_propagate(0)
frm_top_3.pack_propagate(0)
frm_top_1.pack(side='left')
frm_top_2.pack(side='left')
frm_top_3.pack(side='left')


def btnTop1_click():
    global isT1Start
    if isT1Start == True:
        isT1Start = False
    else:
        isT1Start = True
    #isT1Start = ~isT1Start
    check_top_btn_state()

def btnTop2_click():
    global isT2Start
    if isT2Start == True:
        isT2Start = False
    else:
        isT2Start = True
    check_top_btn_state()

def btnTop3_click():
    global isT3Start
    if isT3Start == True:
        isT3Start = False
    else:
        isT3Start = True
    check_top_btn_state()

def punish_1():
    global pun1
    pun1 += 30
    btn_punish_1['text']='已罚时 %d 秒'%(pun1)

def punish_2():
    global pun2
    pun2 += 30
    btn_punish_2['text']='已罚时 %d 秒'%(pun2)

def punish_3():
    global pun3
    pun3 += 30
    btn_punish_3['text']='已罚时 %d 秒'%(pun3)

lab_team1 = tk.Label(frm_top_1,
                     font=('微软雅黑', 68),
                     bg='#4db6ac',
                     fg='white',
                     text='第一组')
lab_team1.pack(pady=70) 
lab1 = tk.Label(frm_top_1,
                font=('Arial', 92),
                bg='#4db6ac',
                fg='white')
lab1.pack(pady=20)

btn_punish_1=tk.Button(frm_top_1,
                       text='已罚时 0 秒',
                       font=('微软雅黑', 22),
                       width=12, height=1,
                       bg='#ec407a',
                       activebackground='#ec407a',
                       fg='white',
                       command=punish_1,
                       state='active')
btn_punish_1.pack(pady=1)

btn_top_1 = tk.Button(frm_top_1,
                      text='暂停',
                      font=('微软雅黑', 40),
                      width=10, height=1,
                      bg='#4db6ac',
                      activebackground='#4db6ac',
                      fg='white',
                      command=btnTop1_click,
                      state='disable')
btn_top_1.pack(side=tk.BOTTOM, pady=int(frm_top_1['height'])* 0.12)


lab_team2 = tk.Label(frm_top_2,
                     font=('微软雅黑', 68),
                     bg='#4dd0e1',
                     fg='white',
                     text='第二组')
lab_team2.pack(pady=70) 
lab2 = tk.Label(frm_top_2,
                font=('Arial', 92),
                bg='#4dd0e1',
                fg='white')
lab2.pack(pady=20)

btn_punish_2=tk.Button(frm_top_2,
                       text='已罚时 0 秒',
                       font=('微软雅黑', 22),
                       width=12, height=1,
                       bg='#ec407a',
                       activebackground='#ec407a',
                       fg='white',
                       command=punish_2,
                       state='active')
btn_punish_2.pack(pady=1)

btn_top_2 = tk.Button(frm_top_2,
                      text='暂停',
                      font=('微软雅黑', 40),
                      width=10, height=1,
                      bg='#4dd0e1',
                      fg='white',
                      activebackground='#4dd0e1',
                      command=btnTop2_click,
                      state='disable')
btn_top_2.pack(side=tk.BOTTOM, pady=int(frm_top_2['height'])* 0.12)


lab_team3 = tk.Label(frm_top_3,
                     font=('微软雅黑', 68),
                     bg='#4fc3f7',
                     fg='white',
                     text='第三组')
lab_team3.pack(pady=70) 
lab3 = tk.Label(frm_top_3,
                font=('Arial', 92),
                bg='#4fc3f7',
                fg='white')
lab3.pack(pady=20)

btn_punish_3=tk.Button(frm_top_3,
                       text='已罚时 0 秒',
                       font=('微软雅黑', 22),
                       width=12, height=1,
                       bg='#ec407a',
                       activebackground='#ec407a',
                       fg='white',
                       command=punish_3,
                       state='active')
btn_punish_3.pack(pady=1)
btn_top_3 = tk.Button(frm_top_3,
                      text='暂停',
                      font=('微软雅黑', 40),
                      width=10, height=1,
                      bg='#64b5f6',
                      fg='white',
                      activebackground='#64b5f6',
                      command=btnTop3_click,
                      state='disable')
btn_top_3.pack(side=tk.BOTTOM, pady=int(frm_top_3['height'])* 0.12)

frm_bottom = tk.Frame(frm,
                      height=screenheight / 5,
                      width=screenwidth,
                      bg='#f06292')
frm_bottom.pack()
frm_bottom.pack_propagate(0)



def btn_press(event):
    global isBtnPress
    if isAllStart:
        isBtnPress = True
        check_top_btn_state()


def btn_Release(event):
    global isAllStart, isT1Start, isT2Start, isT3Start, isBtnPress, btnPressTime
    isBtnPress = False
    if isAllStart == False and btnPressTime < 50:
        isT1Start = isT2Start = isT3Start = isAllStart = True
        btn_bottom['text'] = '长按清零'
    check_top_btn_state()
    btnPressTime = 0


btn_bottom = tk.Button(frm_bottom,
                       text='开始',
                       state='active',
                       font=('微软雅黑', 60),
                       width=screenwidth, height=4,
                       activebackground='#ec407a',
                       fg='white',
                       bg='#ec407a')
btn_bottom.bind("<ButtonPress-1>", btn_press)
btn_bottom.bind("<ButtonRelease-1>", btn_Release)
btn_bottom.pack()


def init_clear():
    global sec1, min1, ms1
    global sec2, min2, ms2
    global sec3, min3, ms3
    global pun1, pun2, pun3
    global isAllStart, isT1Start, isT2Start, isT3Start
    isT1Start = isT2Start = isT3Start = isAllStart = False
    check_top_btn_state()
    lab1['text'] = '00:00.0'
    lab2['text'] = '00:00.0'
    lab3['text'] = '00:00.0'
    btn_bottom['text'] = '开始'
    min1 = sec1 = ms1 = 0
    min2 = sec2 = ms2 = 0
    min3 = sec3 = ms3 = 0
    pun1 = pun2 = pun3 =0
    btn_punish_1['text']='已罚时 0 秒'
    btn_punish_2['text']='已罚时 0 秒'
    btn_punish_3['text']='已罚时 0 秒'


def check_top_btn_state():
    if isUsbOpen:
        btn_top_1['state'] = 'disable'
        btn_top_2['state'] = 'disable'
        btn_top_3['state'] = 'disable'
    else:
        if isAllStart:
            btn_top_1['state'] = 'active'
            btn_top_2['state'] = 'active'
            btn_top_3['state'] = 'active'
        else:
            btn_top_1['state'] = 'disable'
            btn_top_2['state'] = 'disable'
            btn_top_3['state'] = 'disable'

        if isT1Start:
            btn_top_1['text'] = '暂停'
        else:
            btn_top_1['text'] = '继续'

        if isT2Start:
            btn_top_2['text'] = '暂停'
        else:
            btn_top_2['text'] = '继续'

        if isT3Start:
            btn_top_3['text'] = '暂停'
        else:
            btn_top_3['text'] = '继续'



def show_t1_time():
    global ms1, sec1, min1
    global startMs1
    if isT1Start:
        nowMs = int(d.datetime.now().microsecond / 100000) 
        if nowMs != startMs1:
            startMs1 = nowMs
            ms1 += 1
            if ms1 % 10 == 0:
                ms1 = 0
                sec1 += 1
                if sec1 % 60 == 0:
                    sec1 = 0
                    min1 += 1
            if min1 < 100:
                lab1.configure(text='%02d:%02d.%d' % (min1, sec1, ms1))
            else:
                lab1.configure(text='%03d:%02d.%d' % (min1, sec1, ms1))


def show_t2_time():
    global ms2, sec2, min2
    global startMs2
    if isT2Start:
        nowMs = int(d.datetime.now().microsecond / 100000) 
        if nowMs != startMs2:
            startMs2 = nowMs
            ms2 += 1
            if ms2 % 10 == 0:
                ms2 = 0
                sec2 += 1
                if sec2 % 60 == 0:
                    sec2 = 0
                    min2 += 1
            if min2 < 100:
                lab2.configure(text='%02d:%02d.%d' % (min2, sec2, ms2))
            else:
                lab2.configure(text='%03d:%02d.%d' % (min2, sec2, ms2))


def show_t3_time():
    global ms3, sec3, min3
    global startMs3
    if isT3Start:
        nowMs = int(d.datetime.now().microsecond / 100000) 
        if nowMs != startMs3:
            startMs3 = nowMs
            ms3 += 1
            if ms3 % 10 == 0:
                ms3 = 0
                sec3 += 1
                if sec3 % 60 == 0:
                    sec3 = 0
                    min3 += 1
            if min3 < 100:
                lab3.configure(text='%02d:%02d.%d' % (min3, sec3, ms3))
            else:
                lab3.configure(text='%03d:%02d.%d' % (min3, sec3, ms3))



# 更新本地存储时间
def update_srotage():
    storage.write(window,min1,sec1,ms1
                        ,min2,sec2,ms2
                        ,min3,sec3,ms3
                        ,pun1,pun2,pun3)


# 定时函数
def update_timeText():
    global btnPressTime, isUsbOpen
    window.after(45, update_timeText)
    if isBtnPress :
        btnPressTime += 1
        if btnPressTime >= 50:
            init_clear()
    show_t1_time()
    show_t2_time()
    show_t3_time()
    update_srotage()
    if usbTool.Check() == False:
        isUsbOpen = False
        check_top_btn_state()


# 显示存储时间
def update_lable_time():
    global sec1, min1, ms1
    global sec2, min2, ms2
    global sec3, min3, ms3
    global pun1, pun2, pun3
    min1,sec1,ms1,min2,sec2,ms2,min3,sec3,ms3,pun1,pun2,pun3 = storage.read(window)
    show_t1_time()
    show_t2_time()
    show_t3_time()
    if min1 < 100:
        lab1.configure(text='%02d:%02d.%d' % (min1, sec1, ms1))
    else:
        lab1.configure(text='%03d:%02d.%d' % (min1, sec1, ms1))
    if min2 < 100:
        lab2.configure(text='%02d:%02d.%d' % (min2, sec2, ms2))
    else:
        lab2.configure(text='%03d:%02d.%d' % (min2, sec2, ms2))
    if min3 < 100:
        lab3.configure(text='%02d:%02d.%d' % (min3, sec3, ms3))
    else:
        lab3.configure(text='%03d:%02d.%d' % (min3, sec3, ms3))
    
    btn_punish_1['text']='已罚时 %d 秒'%(pun1)
    btn_punish_2['text']='已罚时 %d 秒'%(pun1)
    btn_punish_3['text']='已罚时 %d 秒'%(pun1)
    print('update_lable_time')



def HidUsbRead(data):
    '''
    回调事件，接收数据
    '''
    global isT1Start, isT2Start, isT3Start, isUsbOpen
    try:
        temp_list = data[1:]
        if usbTool.Check():
            isUsbOpen = True
            if isAllStart == True and temp_list[0] == 170:
                if temp_list[1] == 1:
                    isT1Start = False
                else:
                    isT1Start = True
                
                if temp_list[2] == 1:
                    isT2Start = False
                else:
                    isT2Start = True

                if temp_list[3] == 1:
                    isT3Start = False
                else:
                    isT3Start = True
                check_top_btn_state()
        print(temp_list)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    # 显示本地存储时间
    update_lable_time() 

    usbTool = MainUSBTool(master=window, vid = '0483',pid = '5750',command = HidUsbRead)
    # 开启定时
    update_timeText()
    window.mainloop()
