import wx


class ShippingFrame(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(500,500))

        self.panel = wx.Panel(self, -1)

        self.nameTextctrl = wx.TextCtrl(self, pos=(30, 30), size=(170, -1))
        self.nameLbl = wx.StaticText(self, label='Name', pos=(210, 30))

        self.addressTextctrl = wx.TextCtrl(self, pos=(30, 60), size=(220, -1))
        self.addressLbl = wx.StaticText(self, label='Address', pos=(260, 60))

        self.locationTextctrl = wx.TextCtrl(self, pos=(30, 90), size=(200, -1))
        self.locationLbl = wx.StaticText(self, label='City, State, and Zip', pos=(240, 90))

        self.weightLbl = wx.StaticText(self, label='Weight', pos=(50, 160))
        self.speedLbl = wx.StaticText(self, label='Speed', pos=(220, 160))
        self.optionsLbl = wx.StaticText(self, label='Options', pos=(360, 160))
        
        # weight Group
        self.weight1 = wx.RadioButton(self, label='0 - 1.9 lbls. $5.00', style=wx.RB_GROUP, pos=(20, 180))
        self.weight2 = wx.RadioButton(self, label='2 - 4.9 lbls. $8.00', pos=(20, 200))
        self.weight3 = wx.RadioButton(self, label='5 - 10 lbls. $12.25', pos=(20, 220))

        # Speed Group
        self.speed1 = wx.RadioButton(self,label='Overland $2.75', style=wx.RB_GROUP, pos=(200, 180))
        self.speed2 = wx.RadioButton(self,label='3-day Air $6.15', pos=(200, 200))
        self.speed3 = wx.RadioButton(self,label='2-day Air $10.70', pos=(200, 220))
        self.speed4 = wx.RadioButton(self,label='Overnight $15.50', pos=(200, 240))

        # Check Boxes
        self.cb1 = wx.CheckBox(self, label='Extra Padding $4.00', pos=(330, 180))
        self.cb2 = wx.CheckBox(self, label='Gift Wrapping $6.00', pos=(330, 200))

        # Buttons 
        self.calcButton = wx.Button(self, label='Calculate Total', pos=(140, 300))
        self.clearButton = wx.Button(self, label='Clear Form', pos=(250, 300))

        # Event Handlers
        self.calcButton.Bind(wx.EVT_BUTTON, self.calc_shipping)
        self.clearButton.Bind(wx.EVT_BUTTON, self.clear_Data)

        # calculate label
        self.shipSum = wx.StaticText(self, label='Shipping Summary', pos=(195, 350))
        self.calc_label = wx.StaticText(self, label='', pos=(210, 370), size=(30, 20))


        # Methods
    def clear_Data(self, event):
        self.nameTextctrl.SetValue('')
        self.addressTextctrl.SetValue('')
        self.locationTextctrl.SetValue('')
        self.calc_label.SetLabel('')
        self.cb1.SetValue(False)
        self.cb2.SetValue(False)
        self.weight1.SetValue(1)
        self.speed1.SetValue(1)


    def calc_shipping(self, event):
        cost = 0
            
        # Get weight total
        if self.weight3.GetValue():
            cost = 12.25
        elif self.weight2.GetValue():
            cost = 8.00
        else:
            cost = 5.00

            
        # Get speed total and add to weight
        if self.speed4.GetValue():
            cost += 15.50
        elif self.speed3.GetValue():
            cost += 10.70
        elif self.speed2.GetValue():
            cost += 6.15
        else:
            cost += 2.75
            
        # Get options and add to cost
        if self.cb1.GetValue():
            cost += 4.00
        if self.cb2.GetValue():
            cost += 6.00

        cost = "$%3.2f" % cost
        str1 = self.nameTextctrl.GetValue() + '\n' + self.addressTextctrl.GetValue() + \
               '\n' + self.locationTextctrl.GetValue() + '\n' + cost
        
        self.calc_label.SetLabel(str1)



if __name__ == "__main__":


    app = wx.App(False)
    frame = ShippingFrame(None, 'Shipping Calculator')
    frame.Show(True)
    app.MainLoop()
