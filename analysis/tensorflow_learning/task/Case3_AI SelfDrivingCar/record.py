# -*- coding: UTF-8 -*-

"""
此为样例代码，之后第三个案例录制时会完全重制代码，跟这个代码基本没什么关系
"""

import numpy as np
import os
import shutil
import wx
import matplotlib
matplotlib.use('WXAgg')
from datetime import datetime
from matplotlib.figure import Figure
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigCanvas

from utils import Screenshot, XboxController

IDLE_SAMPLE_RATE = 1500
SAMPLE_RATE = 200

class MainWindow(wx.Frame):
    """ Main frame of the application
    """
    title = 'Data Acquisition'


    def __init__(self):
        wx.Frame.__init__(self, None, title=self.title, size=(660,330))

        self.controller = XboxController()

        self.create_main_panel()

        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.on_timer, self.timer)
        self.rate = SAMPLE_RATE
        self.idle_rate = IDLE_SAMPLE_RATE
        self.timer.Start(self.idle_rate)

        self.recording = False
        self.t = 0

    def create_main_panel(self):
        self.img_panel = wx.Panel(self)
        self.joy_panel = wx.Panel(self)
        self.record_panel = wx.Panel(self)

        img = wx.Image(320,240)
        self.image_widget = wx.StaticBitmap(self.img_panel, wx.ID_ANY, wx.Bitmap(img))

        self.init_plot()
        self.PlotCanvas = FigCanvas(self.joy_panel, wx.ID_ANY, self.fig)

        self.txt_outputDir = wx.TextCtrl(self.record_panel, wx.ID_ANY, pos=(5,0), size=(320,30))
        uid = datetime.now().strftime('%Y-%m-%d_%H:%M:%S')
        self.txt_outputDir.ChangeValue("samples/" + uid)

        self.btn_record = wx.Button(self.record_panel, wx.ID_ANY, label="Record", pos=(335,0), size=(100,30))
        self.Bind(wx.EVT_BUTTON, self.on_btn_record, self.btn_record)
        self.Bind(wx.EVT_UPDATE_UI, self.on_update_btn_record, self.btn_record)

        sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.Add(self.img_panel, 0, wx.ALL, 5)
        sizer.Add(self.joy_panel, 0, wx.ALL, 5)

        mainSizer_v = wx.BoxSizer(wx.VERTICAL)
        mainSizer_v.Add(sizer, 0 , wx.ALL, 5)
        mainSizer_v.Add(self.record_panel, 0 , wx.ALL, 5)

        self.SetAutoLayout(True)
        self.SetSizer(mainSizer_v)
        self.Layout()


    def init_plot(self):
        self.plotMem = 50
        self.plotData = [[0] * (5)] * self.plotMem

        self.fig = Figure((4,3))
        self.axes = self.fig.add_subplot(111)


    def on_timer(self, event):
        self.poll()

        if self.recording == False:
            self.draw()


    def poll(self):
        self.bmp = self.take_screenshot()
        self.controller_data = self.controller.read()
        self.update_plot()

        if self.recording == True:
            self.save_data()

    def take_screenshot(self):
        screen = wx.ScreenDC()
        bmp = wx.Bitmap(Screenshot.SRC_W, Screenshot.SRC_H)
        mem = wx.MemoryDC(bmp)
        mem.Blit(0, 0, Screenshot.SRC_W, Screenshot.SRC_H, screen, Screenshot.OFFSET_X, Screenshot.OFFSET_Y)
        return bmp

    def update_plot(self):
        self.plotData.append(self.controller_data)
        self.plotData.pop(0)


    def save_data(self):
        image_file = self.outputDir+'/'+'img_'+str(self.t)+'.png'
        self.bmp.SaveFile(image_file, wx.BITMAP_TYPE_PNG)

        outfile = open(self.outputDir+'/'+'data.csv', 'a')

        outfile.write( image_file + ',' + ','.join(map(str, self.controller_data)) + '\n' )
        outfile.close()

        self.t += 1


    def draw(self):
        img = self.bmp.ConvertToImage()
        img = img.Rescale(320,240)
        self.image_widget.SetBitmap( img.ConvertToBitmap() )

        x = np.asarray(self.plotData)
        self.axes.plot(range(0,self.plotMem), x[:,0], 'r')
        self.axes.hold(True)
        self.axes.plot(range(0,self.plotMem), x[:,1], 'b')
        self.axes.plot(range(0,self.plotMem), x[:,2], 'g')
        self.axes.plot(range(0,self.plotMem), x[:,3], 'k')
        self.axes.plot(range(0,self.plotMem), x[:,4], 'y')
        self.axes.hold(False)
        self.PlotCanvas.draw()


    def on_update_btn_record(self, event):
        label = "Stop" if self.recording else "Record"
        self.btn_record.SetLabel(label)


    def on_btn_record(self, event):
        self.timer.Stop()

        self.recording = not self.recording

        if self.recording:
            self.start_recording()

        if self.recording:
            self.timer.Start(self.rate)
        else:
            self.timer.Start(self.idle_rate)


    def start_recording(self):
        if self.txt_outputDir.IsEmpty():

            msg = wx.MessageDialog(self, 'Specify the Output Directory', 'Error', wx.OK | wx.ICON_ERROR)
            msg.ShowModal() == wx.ID_YES
            msg.Destroy()

            self.recording = False

        else:
            self.outputDir = self.txt_outputDir.GetValue()
            self.t = 0

            if os.path.exists(self.outputDir):
                msg = wx.MessageDialog(self, 'Output Directory Exists - Overwrite Data?', 'Yes or No', wx.YES_NO | wx.ICON_QUESTION)
                result = msg.ShowModal() == wx.ID_YES
                msg.Destroy()

                if result == True:
                    shutil.rmtree(self.outputDir)
                    os.mkdir(self.outputDir)
                else:
                    self.recording = False
                    self.txt_outputDir.SetFocus()
            else:
                os.mkdir(self.outputDir)


    def on_exit(self, event):
        self.Destroy()


if __name__ == '__main__':
    app = wx.App()
    app.frame = MainWindow()
    app.frame.Show()
    app.MainLoop()
