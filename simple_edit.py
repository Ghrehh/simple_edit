import wx, os, atexit



class MainWindow(wx.Frame):
    def __init__(self, parent, title):
        self.dirname=''
        self.title = None

        # A "-1" in the size parameter instructs wxWidgets to use the default size.
        # In this case, we select 200px width and the default height.
        wx.Frame.__init__(self, parent, title=title, size=(500,400))
        self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        self.CreateStatusBar() # A Statusbar in the bottom of the window

        # Setting up the menu.
        filemenu= wx.Menu()
        menuOpen = filemenu.Append(wx.ID_OPEN, "&Open"," Open a file to edit")
        menuSave= filemenu.Append(wx.ID_ABOUT, "&Save"," Save your file")
        menuSaveAs= filemenu.Append(wx.ID_ABOUT, "Save As"," Save your file")
        menuExit = filemenu.Append(wx.ID_EXIT,"E&xit"," Terminate the program")

        # Creating the menubar.
        menuBar = wx.MenuBar()
        menuBar.Append(filemenu,"&File") # Adding the "filemenu" to the MenuBar
        self.SetMenuBar(menuBar)  # Adding the MenuBar to the Frame content.

        # Events.
        self.Bind(wx.EVT_MENU, self.OnOpen, menuOpen)
        self.Bind(wx.EVT_MENU, self.OnExit, menuExit)
        self.Bind(wx.EVT_MENU, self.OnSave, menuSave)
        self.Bind(wx.EVT_MENU, self.OnSaveAs, menuSaveAs)


        self.Show()

    def OnSave(self,e):
        dlg = wx.FileDialog(self, "Choose a Location to Save", self.dirname, "", "*.*", wx.SAVE|wx.FD_OVERWRITE_PROMPT)
        if dlg.ShowModal() == wx.ID_OK:
            self.filename = dlg.GetFilename()
            self.dirname = dlg.GetDirectory()
            self.title = self.filename
            f = open(os.path.join(self.dirname, self.filename), 'w')
            f.write(self.control.Value)
            f.close()
        dlg.Destroy()
        frame.SetTitle(self.title)

    def OnExit(self,e):
        self.YesNo()
        self.Close(True)  # Close the frame.


    def OnOpen(self,e):
        """ Open a file"""
        dlg = wx.FileDialog(self, "Choose a file", self.dirname, "", "*.*", wx.OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            self.filename = dlg.GetFilename()
            self.dirname = dlg.GetDirectory()
            self.title = self.filename
            f = open(os.path.join(self.dirname, self.filename), 'r')
            self.control.SetValue(f.read())
            f.close()
        dlg.Destroy()
        frame.SetTitle(self.title)

    def OnSaveAs(self, e):
        if self.title == None:
            self.OnSave(e)
        else:
            f = open(self.title, 'w')
            f.write(self.control.Value)
            f.close()

    def YesNo(self):
        dlg = wx.MessageDialog(self, "Save you work?", "Save Prompt", wx.YES_NO | wx.ICON_QUESTION)
        result = dlg.ShowModal() == wx.ID_YES
        dlg.Destroy()
        if result:
            self.OnSaveAs("")




app = wx.App(False)
frame = MainWindow(None, "Simple Edit")
app.MainLoop()
