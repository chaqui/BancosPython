commit 0f200016069cdbabde2ee955c2e22e3bfdacb03f
Author: chaqui <josuechaqui@ubuchaqui.(none)>
Date:   Sun Jul 8 14:06:37 2012 -0600

    aggegamos el primcipal y creamos el objeto para busqueda

diff --git a/Clase_Convencional.py b/Clase_Convencional.py
index c71baf4..9d10434 100644
--- a/Clase_Convencional.py
+++ b/Clase_Convencional.py
@@ -33,7 +33,6 @@ class Convencional(GarantiaPrendaria):
                          tipo=self.producto.tipo,
                          cantidad=self.producto.cantidad,
                          costo=self.producto.costo,
-                         numero=self.nocredito,
                          monto=self.monto,
                          cuotas=self.cuotas,
                          cuota=self.cuota,
diff --git a/Clase_Convencional.pyc b/Clase_Convencional.pyc
index 7c0f3fc..67ffb38 100644
Binary files a/Clase_Convencional.pyc and b/Clase_Convencional.pyc differ
diff --git a/Clase_No_Convencional.pyc b/Clase_No_Convencional.pyc
index 09841a6..2498cfc 100644
Binary files a/Clase_No_Convencional.pyc and b/Clase_No_Convencional.pyc differ
diff --git a/Credito.pyc b/Credito.pyc
index 228bffc..e61fcea 100644
Binary files a/Credito.pyc and b/Credito.pyc differ
diff --git a/Fiduciario_Privado.py b/Fiduciario_Privado.py
index ad37a22..aa7df49 100644
--- a/Fiduciario_Privado.py
+++ b/Fiduciario_Privado.py
@@ -34,7 +34,6 @@ class Fiduciario_Privado(CreditoFiduciario):
                          telefonofid=self.cliente.segundoapellido,
                          correofid=self.cliente.correo,
                          dirreccionfid=self.cliente.dirreccion,
-                         numero=self.nocredito,
                          monto=self.monto,
                          cuotas=self.cuotas,
                          cuota=self.cuota,
diff --git a/Fiduciario_Privado.pyc b/Fiduciario_Privado.pyc
index 0516e78..5c12628 100644
Binary files a/Fiduciario_Privado.pyc and b/Fiduciario_Privado.pyc differ
diff --git a/Fiduciario_Publico.pyc b/Fiduciario_Publico.pyc
index 2dc0ab1..d95ff20 100644
Binary files a/Fiduciario_Publico.pyc and b/Fiduciario_Publico.pyc differ
diff --git a/HipotecaPosesoria.pyc b/HipotecaPosesoria.pyc
index ffef24e..063777d 100644
Binary files a/HipotecaPosesoria.pyc and b/HipotecaPosesoria.pyc differ
diff --git a/HipotecarioReal.pyc b/HipotecarioReal.pyc
index 8bf2d3e..b8cd7a6 100644
Binary files a/HipotecarioReal.pyc and b/HipotecarioReal.pyc differ
diff --git a/Main.py b/Main.py
index 072bb10..6d80055 100644
--- a/Main.py
+++ b/Main.py
@@ -6,6 +6,7 @@ from Fiduciario_Publico import FiduciarioPublico
 from Vehiculos_Y_Maquinaria import VehiculosYMaquinaria
 from HipotecaPosesoria import HipotecaPosesoria
 from HipotecarioReal import HipotecaReal    
+from buscar import Buscar
 class Principal(object):
     def principal(self):
         self.res=0
@@ -15,6 +16,7 @@ class Principal(object):
             print"buscar cliente.........1"
             print"salir..................2"
             self.respuesta=int(raw_input("Ingrese su respuesta:"))
+            self.res=self.respuesta
             if self.respuesta==0 :
                 self.ingresar()
                 self.res=raw_input("¿desea regresar al menu? (1=si,2=no)")
@@ -73,7 +75,7 @@ class Principal(object):
             noconvencional.guardar()
             noconvencional.imprimir()
     def buscar(self):
-        pass
+        self.serch=Buscar()
 principal=Principal()
 principal.principal()
 
diff --git a/Main.pyc b/Main.pyc
new file mode 100644
index 0000000..d5b2184
Binary files /dev/null and b/Main.pyc differ
diff --git a/Vehiculos_Y_Maquinaria.pyc b/Vehiculos_Y_Maquinaria.pyc
index 20bca68..9407b1b 100644
Binary files a/Vehiculos_Y_Maquinaria.pyc and b/Vehiculos_Y_Maquinaria.pyc differ
diff --git a/buscar.pyc b/buscar.pyc
new file mode 100644
index 0000000..17b4f9a
Binary files /dev/null and b/buscar.pyc differ
diff --git a/principal.py b/principal.py
new file mode 100644
index 0000000..36b54ec
--- /dev/null
+++ b/principal.py
@@ -0,0 +1,9 @@
+'''
+Created on 8/07/2012
+
+@author: josuechaqui
+'''
+from Main import Principal
+if __name__ == '__main__':
+    princioal =Principal()
+    princioal.principal()
\ No newline at end of file
