class CarroPS5():
    def __init__(self,request):
        self.request=request
        self.session=request.session
        carroPS5=self.sessionPS5.get("carroPS5")

        if not carroPS5: 
            carroPS5=self.session["carroPS5"]={}
        #else:
        self.carroPS5=carroPS5
    
    def agregarPS5(self, productoPS5):
        if(str(productoPS5.id) not in self.carroPS5.keys()):
            self.carroPS5[productoPS5.id]={
                "productoPS5_id":productoPS5.id, 
                "nombrePS5":productoPS5.nombrePS5,
                "precioPS5":str(productoPS5.precioPS5),
                "cantidadPS5":1,
                "imagenPS5":productoPS5.imagenPS5.url

            }
        else:
            for key, value in self.carroPS5.items():
                if key==str(productoPS5.id):
                    value["cantidadPS5"]=value["cantidadPS5"]+1
                    value["precioPS5"]=float(value["precioPS5"])+productoPS5.precioPS5
                    break
        self.guardar_carroPS5()
    
    def guardar_carroPS5(self):
        self.session["carroPS5"]=self.carroPS5
        self.session.modified=True
        
    def eliminarPS5(self,productoPS5):
        productoPS5.id=str(productoPS5.id)
        if productoPS5.id in self.carroPS5:
            del self.carroPS5[productoPS5.id]
            self.guardar_carroPS5()

    def restar_productoPS5(self,productoPS5):
        for key, value in self.carroPS5.items():
            if key==str(productoPS5.id):
                value["cantidadPS5"]=value["cantidadPS5"]-1
                value["precioPS5"]=float(value["precioPS5"])-productoPS5.precioPS5
                if value["cantidadPS5"]<1:
                    self.eliminarPS5(productoPS5)
                break
        self.guardar_carroPS5()
    
    def limpiar_carroPS5(self):
        self.session["carroPS5"]={}
        self.session.modified=True

        
        

