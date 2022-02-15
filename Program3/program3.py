import wx
import sqlite3 as db
from myDial import *

class DataList(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size=(700, 600))
        panel = wx.Panel(self, -1)
        panel.SetBackgroundColour('#add8e6')

        self.table_name = wx.StaticText(panel, -1, 'citation data', pos=(50, 5))
        self.list = wx.ListCtrl(panel, -1, style=wx.LC_REPORT, pos=(20, 30), size=(650, 400))

        # set up columns
        self.list.InsertColumn(0, 'tid', width=50)
        self.list.InsertColumn(1, 'stop_date', width=70)
        self.list.InsertColumn(2, 'stop_time', width=70)
        self.list.InsertColumn(3, 'actual_speed', width=80)
        self.list.InsertColumn(4, 'posted_speed', width=85)
        self.list.InsertColumn(5, 'mph_over', width=70)
        self.list.InsertColumn(6, 'age', width=70)
        self.list.InsertColumn(7, 'violator_sex', wx.LIST_FORMAT_RIGHT, 85)

        # set up buttons
        display = wx.Button(panel, -1, 'Display', size=(-1, 30), pos=(95, 450))
        insert = wx.Button(panel, -1, 'Insert Citation', size=(-1, 30), pos=(300, 450))
        cancel = wx.Button(panel, -1, 'Cancel', size=(-1, 30), pos=(500, 450))

        # Bind Buttons
        display.Bind(wx.EVT_BUTTON, self.OnDisplay)
        insert.Bind(wx.EVT_BUTTON, self.OnInsert)
        cancel.Bind(wx.EVT_BUTTON, self.OnClose)

        self.Centre()

    
    def getAllData(self):
        self.list.DeleteAllItems() # empty the list control
        con = db.connect('speeding_tickets.db') # connect to database
        cur = con.cursor() # create a cursor

        cur.execute('SELECT * FROM tickets')
        results = cur.fetchall()
        
        for row in results:
            self.list.Append(row) # add record to list control

        cur.close()
        con.close() 
    
    
    def OnDisplay(self, event):
        
        try:
            self.getAllData() # display whole table

        except db.Error as error:
            dlg = wx.MessageDialog(self, str(error), 'Error occured')
            dlg.ShowModal()

    def OnInsert(self, event):
        dlg = MyDialog()  # create a instance of MyDialog
        btnID = dlg.ShowModal()
        if btnID == wx.ID_OK:
            ticket_id = dlg.ticket_id.GetValue() # get data from controls on dialog box
            time = dlg.time.GetValue()
            post_speed = dlg.post_speed.GetValue()
            age = dlg.age.GetValue()
            date = dlg.date.GetValue()
            actual_speed = dlg.actual_speed.GetValue()
            mph_over = dlg.mph_over.GetValue()
            off_sex = dlg.off_sex.GetValue()

        if ticket_id != "" and time != "" and post_speed != "" and age != "" and\
            date != "" and actual_speed != "" and mph_over != "" and off_sex != "":  # only if no blank values

            try:
                con = db.connect('speeding_tickets.db')
                cur = con.cursor()

                sql = "INSERT INTO tickets VALUES (?, ?, ?, ?, ?, ?, ?, ?)"

                cur.execute(sql, (ticket_id, date, time, actual_speed, post_speed, 
                                 mph_over, age, off_sex))

                con.commit() # complete the transaction

                self.getAllData()  # display all the data

            except db.Error as error:
                dlg =wx.MessageDialog(self, str(error), 'Error occurred')
                dlg.ShowModal()    # display error message

        dlg.Destroy()



    def OnClose(self, event):
        self.Close() # exit the program


        
app = wx.App()
dl = DataList(None, -1, 'traffic tickets')
dl.Show()
app.MainLoop()