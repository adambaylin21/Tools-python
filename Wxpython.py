import wx

class bucky(wx.Frame):

    def __init__(self,parent,id):
        wx.Frame.__init__(self,parent,id,'Post T-shirt', size = (1054,450))
        panel=wx.Panel(self)


        # make Box Message

        box=wx.MessageDialog(None,'Program make by Vip.phamquangthinh \nCopyright 2017','About',wx.OK)
        answer=box.ShowModal()
        box.Destroy()

        # make Box Input

        box2=wx.TextEntryDialog(None,'What is your name?','Welcome','Adam Baylin')
        if box2.ShowModal()==wx.ID_OK:
            answer=box2.GetValue()

        # make Box choice

        box3=wx.SingleChoiceDialog(None,'You are ?','Choice your sex',['Male','Woman','Gay','Les'])
        if box3.ShowModal()==wx.ID_OK:
            answer=box3.GetStringSelection()


        # make Menu & Statusbar

        status=self.CreateStatusBar()
        menubar=wx.MenuBar()
        first=wx.Menu()
        second=wx.Menu()
        first.Append(wx.NewId(),'About Post T-shirt','See Information about program')
        first.Append(wx.NewId(),'Website','Go to website')
        second.Append(wx.NewId(),'Comming','I\'m developing')
        menubar.Append(first,'About')
        menubar.Append(second,'Tool')
        self.SetMenuBar(menubar)


        # Make button

        button=wx.Button(panel,label='Post',pos=(895,315),size=(120,45))
        self.Bind(wx.EVT_BUTTON,self.closebutton, button)
        self.Bind(wx.EVT_CLOSE,self.closewindow)

    def closebutton (self,event):
        self.Close(True)
    def closewindow(self,event):
        self.Destroy()

        # End Make button


if __name__=='__main__':
    app=wx.PySimpleApp()
    frame=bucky(parent=None,id=-1)
    frame.Show()
    app.MainLoop()

