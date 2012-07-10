'''
Created on 9/07/2012

@author: josuechaqui
'''
import wx
class Hipoteca(wx.Frame):

    def __init__(self,parent,title):
        #Hipoteca Real
        wx.Frame.__init__(self, parent, title="Credito"+" "+title, size=(800, 400))
        self.pos=0
        self.size=20
        self.stCredito=wx.StaticText(self,label="Credito"+" "+title,pos=(5,self.pos+10),size=(200,self.size))
        self.pos=5
        #---------------Datos Del Cliente----------------s
        self.PCLiente=wx.Panel(self,pos=(0,30),size=(800,100))
        self.stCliente=wx.StaticText(self.PCLiente,label="Datos del Cliente:",pos=(5,self.pos),size=(150,self.size))
        self.stNombreCliente=wx.StaticText(self.PCLiente,label="(Primer Nombre)",pos=(131,self.pos),size=(125,self.size))
        self.stNombre2Cliente=wx.StaticText(self.PCLiente,label="(Segundo Nombre)",pos=(266,self.pos),size=(130,self.size))
        self.stApellidoCliente=wx.StaticText(self.PCLiente,label="(Primer Apellido)",pos=(406,self.pos),size=(125,self.size))
        self.stApellido2Cliente=wx.StaticText(self.PCLiente,label="(Segundo Apellido)",pos=(531,self.pos),size=(130,self.size))
        self.pos=self.pos+self.size
        self.stNombreCliente=wx.StaticText(self.PCLiente,label="Nombre:",pos=(61,self.pos),size=(60,self.size))
        self.txtPNombreCliente=wx.TextCtrl(self.PCLiente,pos=(131,self.pos),size=(125,self.size),name="TxtPNombre",id=0)
        self.txtSNombreCliente=wx.TextCtrl(self.PCLiente,pos=(266,self.pos),size=(130,self.size),name="TxtSNombre",id=1)
        self.txtPApellidoCliente=wx.TextCtrl(self.PCLiente,pos=(406,self.pos),size=(125,self.size),name="TxtPApellido",id=2)
        self.txtSApellidoCliente=wx.TextCtrl(self.PCLiente,pos=(531,self.pos),size=(130,self.size),name="TxtSApellido",id=3)
        self.pos=self.pos+self.size
        self.stDirreccionCliente=wx.StaticText(self.PCLiente,label="Dirreccion:",pos=(46,self.pos),size=(75,self.size))
        self.txtDirreccionCliente=wx.TextCtrl(self.PCLiente,pos=(131,self.pos),size=(530,self.size),name="TxtPNombre",id=0)
        self.pos=self.pos+self.size
        self.stTelefonoCliente=wx.StaticText(self.PCLiente,label="Telefono:",pos=(56,self.pos),size=(64,self.size))
        self.txtTelefonoCliente=wx.TextCtrl(self.PCLiente,pos=(131,self.pos),size=(150,self.size),name="TxtTelefono",id=0)
        self.pos2=131+150+10
        self.stCorreoCliente=wx.StaticText(self.PCLiente,label="Correo:",pos=(self.pos2,self.pos),size=(64,self.size))
        self.pos2=self.pos2+64+10
        self.x=295
        self.txtCorreoCliente=wx.TextCtrl(self.PCLiente,pos=(self.pos2,self.pos),size=(self.x,self.size),name="TxtCorreo",id=0)
        self.pos=5
        #-----Credito------
        self.PanelCredito=wx.Panel(self,pos=(0,140),size=(800,50))
        self.stCredito=wx.StaticText(self.PanelCredito,label="Datos del Credito:",pos=(5,self.pos),size=(150,self.size))
        self.pos=self.pos+self.size
        self.stMonto=wx.StaticText(self.PanelCredito,label="Monto:",pos=(56,self.pos),size=(64,self.size))
        self.txtMonto=wx.TextCtrl(self.PanelCredito,pos=(131,self.pos),size=(150,self.size),name="TxtMonto",id=0)
        self.pos2=131+150+10
        #Cuotas
        self.stCuotas=wx.StaticText(self.PanelCredito,label="Cuotas:",pos=(self.pos2,self.pos),size=(64,self.size))
        self.x=100
        self.pos2=self.pos2+74
        self.txtCuotas=wx.TextCtrl(self.PanelCredito,pos=(self.pos2,self.pos),size=(self.x,self.size),name="TxtCorreo",id=0)
        #Cuota
        self.pos2=131+150+10+64+self.x+20
        self.stCuota=wx.StaticText(self.PanelCredito,label="Cuota:",pos=(self.pos2,self.pos),size=(64,self.size))
        self.x=130
        self.pos2=self.pos2+54
        self.txtCuota=wx.TextCtrl(self.PanelCredito,pos=(self.pos2,self.pos),size=(self.x,self.size),name="TxtCorreo",id=0)
        #-----Libro------
        self.PLibro=wx.Panel(self,pos=(0,200), size=(800,150))
        self.pos=5
        self.stCredito=wx.StaticText(self.PLibro,label="Datos del Libro:",pos=(5,self.pos),size=(150,self.size))
        self.pos=self.pos+self.size
        #Libro:
        self.stLibro=wx.StaticText(self.PLibro,label="Libro:",pos=(56,self.pos),size=(64,self.size))
        self.pos2=56+64+10
        self.txtLibro=wx.TextCtrl(self.PLibro,pos=(self.pos2,self.pos),size=(150,self.size),name="TxtLibro",id=0)
        self.pos2=131+150+10
        #Finca
        self.stFinca=wx.StaticText(self.PLibro,label="Finca:",pos=(self.pos2,self.pos),size=(64,self.size))
        self.x=100
        self.pos2=self.pos2+74
        self.txtFinca=wx.TextCtrl(self.PLibro,pos=(self.pos2,self.pos),size=(self.x,self.size),name="txtFinca",id=0)
        #Folio
        self.pos2=131+150+10+64+self.x+20
        self.stFolio=wx.StaticText(self.PLibro,label="Folio:",pos=(self.pos2,self.pos),size=(64,self.size))
        self.x=130
        self.pos2=self.pos2+54
        self.txtFolio=wx.TextCtrl(self.PLibro,pos=(self.pos2,self.pos),size=(self.x,self.size),name="Folio",id=0)
        self.pos=self.pos+self.size
        #Registro de Inscripcion:
        self.stLibro=wx.StaticText(self.PLibro,label="Registro de Inscripcion:",pos=(56,self.pos),size=(175,self.size))
        self.txtLibro=wx.TextCtrl(self.PLibro,pos=(226,self.pos),size=(130,self.size),name="TxtRegistro",id=0)
        self.pos2=131+300+10
        #---Botones...
        self.PBotones=wx.Panel(self,pos=(0,360), size=(800,50))
        #Valorar
        self.pos=5
        self.size=30
        self.BtValorar=wx.Button(self.PBotones,pos=(self.pos,self.pos),size=(self.x,self.size),label="Valorar")
        #Guardar
        self.pos2=self.pos
        self.pos=self.x+self.pos+10
        self.BtGuardar=wx.Button(self.PBotones,pos=(self.pos,self.pos2),size=(self.x,self.size),label="Guardar")
        #Salir
        self.pos=self.x+self.pos+10
        self.BtSalir=wx.Button(self.PBotones,pos=(self.pos,self.pos2),size=(self.x,self.size),label="Salir")
        self.Bind(wx.EVT_BUTTON, self.Salir,self.BtSalir)
        self.Bind(wx.EVT_BUTTON, self.Guardar,self.BtGuardar)
        self.Bind(wx.EVT_BUTTON, self.Valorar,self.BtValorar)
        self.Centre(True)  # Centrar la ventana en pantalla
        self.Show(True)
    def Salir(self,evento):
        self.Close()
    def Guardar(self,evento):
        pass
    def Valorar(self,evento):
        pass
app = wx.App(False)
APP_TITLE="FIduciario"
frame = Hipoteca(None,APP_TITLE)
app.MainLoop()