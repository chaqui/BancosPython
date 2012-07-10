import wx

class Editor(wx.Frame):

    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title="Credito"+" "+title, size=(800, 600))
        self.pos=0
        self.size=20
        self.stCredito=wx.StaticText(self,label="Credito"+" "+title,pos=(5,self.pos+10),size=(200,self.size))
        self.pos=self.pos+self.size+10
        self.stCliente=wx.StaticText(self,label="Datos del Cliente:",pos=(5,self.pos),size=(150,self.size))
        self.stNombreCliente=wx.StaticText(self,label="(Primer Nombre)",pos=(131,self.pos),size=(125,self.size))
        self.stNombre2Cliente=wx.StaticText(self,label="(Segundo Nombre)",pos=(266,self.pos),size=(130,self.size))
        self.stApellidoCliente=wx.StaticText(self,label="(Primer Apellido)",pos=(406,self.pos),size=(125,self.size))
        self.stApellido2Cliente=wx.StaticText(self,label="(Segundo Apellido)",pos=(531,self.pos),size=(130,self.size))
        self.pos=self.pos+self.size
        self.stNombreCliente=wx.StaticText(self,label="Nombre:",pos=(61,self.pos),size=(60,self.size))
        self.txtPNombreCliente=wx.TextCtrl(self,pos=(131,self.pos),size=(125,self.size),name="TxtPNombre",id=0)
        self.txtSNombreCliente=wx.TextCtrl(self,pos=(266,self.pos),size=(130,self.size),name="TxtSNombre",id=1)
        self.txtPApellidoCliente=wx.TextCtrl(self,pos=(406,self.pos),size=(125,self.size),name="TxtPApellido",id=2)
        self.txtSApellidoCliente=wx.TextCtrl(self,pos=(531,self.pos),size=(130,self.size),name="TxtSApellido",id=3)
        self.pos=self.pos+self.size
        self.stDirreccionCliente=wx.StaticText(self,label="Dirreccion:",pos=(46,self.pos),size=(75,self.size))
        self.txtDirreccionCliente=wx.TextCtrl(self,pos=(131,self.pos),size=(530,self.size),name="TxtPNombre",id=0)
        self.pos=self.pos+self.size
        self.stTelefonoCliente=wx.StaticText(self,label="Telefono:",pos=(56,self.pos),size=(64,self.size))
        self.txtTelefonoCliente=wx.TextCtrl(self,pos=(131,self.pos),size=(150,self.size),name="TxtTelefono",id=0)
        self.pos2=131+150+10
        self.stCorreoCliente=wx.StaticText(self,label="Correo:",pos=(self.pos2,self.pos),size=(64,self.size))
        self.pos2=self.pos2+64+10
        self.x=295
        self.txtCorreoCliente=wx.TextCtrl(self,pos=(self.pos2,self.pos),size=(self.x,self.size),name="TxtCorreo",id=0)
        self.pos=self.pos+self.size+10
        self.stCredito=wx.StaticText(self,label="Datos del Credito:",pos=(5,self.pos),size=(150,self.size))
        self.pos=self.pos+self.size
        self.stMonto=wx.StaticText(self,label="Monto:",pos=(56,self.pos),size=(64,self.size))
        self.txtMonto=wx.TextCtrl(self,pos=(131,self.pos),size=(150,self.size),name="TxtMonto",id=0)
        self.pos2=131+150+10
        #Cuotas
        self.stCuotas=wx.StaticText(self,label="Cuotas:",pos=(self.pos2,self.pos),size=(64,self.size))
        self.x=100
        self.pos2=self.pos2+74
        self.txtCuotas=wx.TextCtrl(self,pos=(self.pos2,self.pos),size=(self.x,self.size),name="TxtCorreo",id=0)
        #Cuota
        self.pos2=131+150+10+64+self.x+20
        self.stCuota=wx.StaticText(self,label="Cuota:",pos=(self.pos2,self.pos),size=(64,self.size))
        self.x=130
        self.pos2=self.pos2+54
        self.txtCuota=wx.TextCtrl(self,pos=(self.pos2,self.pos),size=(self.x,self.size),name="TxtCorreo",id=0)
        self.Centre(True)  # Centrar la ventana en pantalla
        self.Show(True)
app = wx.App(False)
APP_TITLE="FIduciario"
frame = Editor(None, APP_TITLE)
app.MainLoop()