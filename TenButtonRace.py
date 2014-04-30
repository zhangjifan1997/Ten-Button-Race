#! /usr/bin/evn python

import wx
import time
import random
class TenButtonFrame(wx.Frame):
        buttonNumber=1
        btn=[]
	def __init__(self, parent):
		wx.Frame.__init__(self, parent, wx.ID_ANY, "Ten Button Race",size=(890,620))

		self.panel = wx.Panel(self)

		self.btnClickFirst = wx.Button(self.panel, label="Start", pos=(200, 100))
		for btnNumber in range(0,11):
                        self.btnClickLater = wx.Button(self.panel, label="Button "+str(btnNumber), pos=(random.randint(0,800), random.randint(0,593)))
                        self.btnClickLater.Show(False)
                        self.btn.append(self.btnClickLater)
                        self.btn[-1].Bind(wx.EVT_BUTTON, self.OnClickLater)

		self.btnClickFirst.Bind(wx.EVT_BUTTON, self.OnClickFirst)

        def TheEnd(self):
                self.endTime = time.time()
                wx.MessageBox("You used "+str(self.endTime-self.startTime)+" seconds","You Win!")

	def OnClickFirst(self, e):
		self.btnClickFirst.Show(False)
		self.startTime = time.time()
		self.btn[self.buttonNumber].Show(True)

	def OnClickLater(self, e):
                self.btn[self.buttonNumber].Show(False)
                self.buttonNumber=self.buttonNumber+1
                if self.buttonNumber==11:
                        self.TheEnd()
                else:
                        self.btn[self.buttonNumber].Show(True)


# -------- Main Program Below ------------

app = wx.App(False)
frame = TenButtonFrame(None)
frame.Show()
app.MainLoop()
