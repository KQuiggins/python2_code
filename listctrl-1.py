from numpy import size
import wx

data = [
    ('smith, joe', '555-1111', 'jsmith@xyz.com'),
    ('jones, moe', '555-2222', 'mjones@xyz.com'),
    ('allen, sue', '555-3333', 'sallen@xyz.com'),
    ('green, zoe', '555-4444', 'zgreen@xyz.com')
] # list of tuples to be inserted in list control

class DataFrame(wx.Frame):

    def __init__(self):
        super().__init__(None, -1, title='Insert Into List Control', size=(480, 270)) # parent, id, title, size
        panel = wx.Panel(self, -1)

        self.table_name = wx.StaticText(panel, -1, 'Contacts', pos=(50, 5))

        self.list = wx.ListCtrl(panel, -1, style=wx.LC_REPORT, pos=(20, 30), size=(370, -1))

        # set up columns
        self.list.InsertColumn(0, 'name', width=100)
        self.list.InsertColumn(1, 'phone', width=90)
        self.list.InsertColumn(2, 'email', wx.LIST_FORMAT_RIGHT, 140)

        for row in data:
            self.list.Append(row)  # add tuple items left to right

        self.Centre()

app = wx.App()
df = DataFrame()
df.Show()
app.MainLoop()