# dataframe2.py 
 
import wx 
import sqlite3 as db 
 
 
 
class DataFrame(wx.Frame): 
 
    def __init__(self): 
        super().__init__(None, id=-1, title='read data', size=(480, 270)) 
        panel = wx.Panel(self, -1) 
 
        self.table_name = wx.StaticText(panel, -1, 'Contacts', pos=(50, 5)) 

        self.list = wx.ListCtrl(panel, -1, style=wx.LC_REPORT, pos=(20, 30), size=(370, -1)) 

        # set up columns 
        self.list.InsertColumn(0, 'id', width=30) 
        self.list.InsertColumn(1, 'name', width=90) 
        self.list.InsertColumn(2, 'phone', width=90) 
        self.list.InsertColumn(3, 'email', wx.LIST_FORMAT_RIGHT, 140) 
 
        # setup buttons 
        display = wx.Button(panel, -1, 'Display', size=(-1, 30), pos=(100, 190)) 
        cancel = wx.Button(panel, -1, 'Cancel', size=(-1, 30), pos=(250, 190)) 
 
        display.Bind(wx.EVT_BUTTON, self.OnDisplay )  # bind buttons 2 event handlers 
        cancel.Bind(wx.EVT_BUTTON, self.OnCancel) 
 
        self.Centre()     # center the window
 
 
    def OnDisplay(self, event): 
        try: 
            self.table_name.SetLabel("Table: Contacts") 
            con = db.connect('people.sqlite')  # connect to db 
            cur = con.cursor() 
 
            cur.execute('SELECT * FROM contacts') 
            results = cur.fetchall() 
            for row in results: 
               self.list.Append(row)  # add record to list control 
 
            cur.close() 
            con.close() 
 
        except db.Error as err: 
            dlg = wx.MessageDialog(self, str(err), 'Error occured') 
            dlg.ShowModal()   # display error message 

 
    def OnCancel(self, event): 
        self.Close()  # exit program
        
 
app = wx.App() 
df = DataFrame() 
df.Show() 
app.MainLoop() 
