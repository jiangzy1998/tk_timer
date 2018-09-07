import time
import tkinter as tk
import threading
import datetime
import platform
import operator


import pywinusb.hid as hid
from COM import hidHelper
from COM import usbHelper


class MainUSBTool():

    def __init__(self, master=None,vid = None,pid =None,command = None):
        self.list_box_pyusb = list()
        self.receive_count = 0
        self.usbDev = None
        self.vidStr = vid
        self.pidStr = pid
        self.vidX = int(vid, 16)
        self.pidX = int(pid, 16)
        self.command = command
        self.find_all_devices()
        

    def find_all_devices(self):
        '''
        线程检测USB的连接状态
        '''
        try:
            self.temp_pyusb = list()
            if platform.system() == "Windows":
                usb_dev = hid.find_all_hid_devices()
                for dev in usb_dev:
                    vid = hex(dev.vendor_id)[2:].rjust(4, "0")
                    pid = self.fill_zero(hex(dev.product_id)[2:])
                    dev_info = "VID:{0} PID:{1}".format(vid, pid)
                    self.temp_pyusb.append(dev_info)
                    if operator.eq(vid,self.vidStr) and operator.eq(pid,self.pidStr):
                        if self.Check() == False:
                            self.Open()
                        
                        
            
            # 检测到usb设备被拔出时，关闭usb设备
            if self.pidX and self.vidX:
                _vid = self.fill_zero(hex(self.vidX)[2:])
                _pid = self.fill_zero(hex(self.pidX)[2:])
                dev_info = "VID:{0} PID:{1}".format(_vid, _pid)
                if dev_info not in self.temp_pyusb:
                    self.Close()
            self.list_box_pyusb = self.temp_pyusb
            self.thread_find_all_devices = threading.Timer(
                1, self.find_all_devices)
            self.thread_find_all_devices.setDaemon(True)
            self.thread_find_all_devices.start()
        except Exception as e:
            print(e)

    def fill_zero(self, strHex, strLen=4):
        '''
        为了美观，将不足位用0填充
        '''
        if len(strHex) > strLen:
            strHex = strHex[0:strLen]
        elif len(strHex) < strLen:
            strHex = (strLen-len(strHex))*"0" + strHex
        return strHex.upper()


    def Open(self):
        '''
        打开/关闭 usb设备
        '''
        self.usbDev = hidHelper.hidHelper(self.vidX, self.pidX)
        self.usbDev.start()
        if self.usbDev.device:
            self.usbDev.device.set_raw_data_handler(self.command)

    def Close(self):
        try:
            if hasattr(self.usbDev, "stop"):
                self.usbDev.stop()
                self.usbDev.device = None
        except Exception as e:
            print(e)

    def Check(self):
        try:
            return self.usbDev.device != None
        except:
            return False
