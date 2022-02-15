import wx

class MyDialog(wx.Dialog):

    def __init__(self):

        wx.Dialog.__init__(self, None, title="Dialog Window", size=(700, 400))
        self.SetBackgroundColour('#add8e6')

        lbl = wx.StaticText(self, label='Ticket Record Entry', pos=(300, 10))

        self.ticket_id = wx.TextCtrl(self, -1, '', pos=(115, 40))
        wx.StaticText(self, -1, 'Ticket ID:', pos=(60, 40))

        self.time = wx.TextCtrl(self, -1, '', (115, 80))
        wx.StaticText(self, -1, 'Time:', (80, 80))

        self.post_speed = wx.TextCtrl(self, -1, '', (115, 120))
        wx.StaticText(self, -1, 'Posted Speed:', (35, 120))

        self.age = wx.TextCtrl(self, -1, '', pos=(115, 160))
        wx.StaticText(self, -1, 'Age:', pos=(80, 160))

        self.date = wx.TextCtrl(self, -1, '', pos=(500, 40))
        wx.StaticText(self, -1, 'Date:', pos=(465, 40))

        self.actual_speed = wx.TextCtrl(self, -1, '', pos=(500, 80))
        wx.StaticText(self, -1, 'Actual Speed:', pos=(420, 80))

        self.mph_over = wx.TextCtrl(self, -1, '', pos=(500, 120))
        wx.StaticText(self, -1, 'MPH Over:', pos=(435, 120))

        self.off_sex = wx.TextCtrl(self, -1, '', pos=(500, 160))
        wx.StaticText(self, -1, 'Sex:', pos=(465, 160))

        okBtn = wx.Button(self, id=wx.ID_OK, pos=(300, 250))  # add wx.OK butt