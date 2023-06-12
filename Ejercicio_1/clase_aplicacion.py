
import tkinter as tk




class Aplication(tk.Tk):
    def __init__(self):
        
        self.__variables = []
        
        super().__init__()
        
        # Atributos ventana
        self.geometry("300x200")
        self.title("Calculadora IPC")
        
        # Atributos texto

        opts = {"padx": 5, "pady": 5,"ipadx":10, "ipady": 10}
        
        # Columnas
        item = tk.Label(self, text = "Item")
        cantidad = tk.Label(self, text = "Cantidad")
        precio_base = tk.Label(self, text = "Precio Año Base")
        precio_actual = tk.Label(self, text = "Precio Año Actual")
        
        item.grid(row = 0, column = 0, **opts)
        cantidad.grid(row = 0, column = 1, **opts)
        precio_base.grid(row = 0, column = 2, **opts)
        precio_actual.grid(row = 0, column = 3, **opts)
        
        #Filas
        
        vestimenta = tk.Label(self, text = "Vestimenta")
        alimentos = tk.Label(self, text = "Alimentos")
        educacion = tk.Label(self, text ="Educación")
        
        
        vestimenta.grid(row = 1, column = 0, **opts)
        alimentos.grid(row = 2, column = 0, **opts)
        educacion.grid(row = 3, column = 0, **opts)
        
        
        #Entrys
        
        for i in range(0,3):
            variables_fila = []
            for j in range(0,3):
                dato = tk.DoubleVar()
                ingreso = tk.Entry(textvariable = dato)
                ingreso.grid(row = i + 1, column = j + 1, **opts)
                variables_fila.append(dato)
            self.__variables.append(variables_fila)
                
        #Atributos Botones 
        
        buttonAttributes = {"width":9, "height":1}
        
        #Botones
        
        
        calculaIPC = tk.Button(self, text = "Calcular IPC", **buttonAttributes, command = self.calcula)
        calculaIPC.grid(row = 4, column = 1)
        
        
        salir = tk.Button(self, text = "Salir", **buttonAttributes, command = self.salir)
        salir.grid(row = 4, column = 2)
        
        

        self.mainloop()

    def salir(self):
        self.destroy()
        
    def calcula(self):
        attributes = {"padx": 5, "pady": 5,"ipadx":10, "ipady": 10}
        datoActual = 0
        datoBase = 0
        band = True
        for variables_fila in self.__variables:
            for dato in variables_fila:
                if band:
                    multiplicador = dato.get()
                    band = False
                elif variables_fila.index(dato) == 1:
                    datoBase += dato.get() * multiplicador
                else:
                    datoActual += dato.get() * multiplicador
            band = True
        resultado = tk.Label(self, text = "IPC " + str(int(datoBase)*100) + " % " + str(int(datoActual)*100) + " % ")
        resultado.grid(row = 7, column = 1, **attributes)
        
        
