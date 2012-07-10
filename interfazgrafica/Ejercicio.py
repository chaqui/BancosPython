import wx
from VentanaCredito import Credito
App=wx.App()
win=wx.Frame(None,title="Primera Ventana",size=(410,200))
button=wx.Button(win, label="Abrir")
button=wx.Button(win, label="Guardar")
win.Show()
App.MainLoop()