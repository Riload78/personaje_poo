class Personaje:
    name = "Default"
    fuerza = 0
    inteligencia = 0
    defensa = 0
    vida = 0
    
    def __init__(self,name,fuerza,inteligencia,defensa,vida):
        self._name = name
        self._fuerza = fuerza
        self._inteligencia = inteligencia
        self._defensa = defensa
        self._vida = vida
        
    def __str__(self):
        return print(f"{self._name} tiene {self._fuerza} fuerza, {self._inteligencia} inteligencia, {self._defensa} defensa y {self._vida} de vida")
    
    def atributos(self):
        return (print(f'{self._name}: \nFuerza:{self._fuerza}\nIntelifencia{self._inteligencia}\nDefensa:{self._defensa}\nVida:{self._vida}'))
    
    def get_fuerza(self):
        return self._fuerza
    
    def set_fuerza(self,fuerza):
        if fuerza < 0 :
            print('La fuerza no puede ser negativa')
        else:
            self._fuerza = fuerza
    
    def subir_nivel(self,fuerza,inteligencia,defensa):
        self._fuerza += fuerza
        self._inteligencia += inteligencia
        self._defensa += defensa
        
    def esta_vivo(self):
        return self._vida > 0
    
    def __morir(self):
        self._vida = 0
        return(f'{self._name} ha muerto!!')
        
    def daño(self, enemigo):
        return self._fuerza - enemigo._defensa
    
    def atacar(self, enemigo):
        daño = self.daño(enemigo)
        enemigo.vida = enemigo._vida - daño
        print(f'{self._name} ha realizado {daño} puntos de daño a {enemigo._name}')
        if enemigo.esta_vivo() :
            print(f'La vida de {enemigo._name} es {enemigo._vida}')
        else:
            enemigo.morir()
            
class Guerrero(Personaje):
    
    def __init__(self,name,fuerza,inteligencia,defensa,vida,espada):
       # hereda los atributos de la clase padre(personaje)
       super().__init__(name,fuerza,inteligencia,defensa,vida)  
       self.espada = espada
       
    # Añadir espada a los atributos de la super clase (padre)   
    def atributos(self):
        super().atributos()
        print(f'Espada: {self.espada}')
        
    def cambiar_arma(self):
        opcion = int(input('Elige un arma: (1) Acero Valyrio, daño 8. (2) Matadragones, daño 10'))
        if opcion == 1:
            self.espada = 8
        elif opcion == 2:
            self.espada = 10
        else:
            print('Opcion incorrecta')
        
    def daño(self, enemigo):
        return self._fuerza * self.espada - enemigo.defensa
    
class Mago(Personaje):
    def __init__(self, name, fuerza, inteligencia, defensa, vida,libro):
        super().__init__(name, fuerza, inteligencia, defensa, vida)
        self.libro = libro
    
    def atributos(self):
        super().atributos()
        print('Libro',self.libro)
        
    def daño(self,enemigo):
        return self.inteligencia * self.libro - enemigo.defensa 
        
    
        
        
    
player1 = Personaje("Toni",20,15,10,100)
guerrero = Guerrero('Mariano',20,15,10,100,5)
mago = Mago('Guths', 20,15,10,100,5)
player1.atributos()
guerrero.atributos()
mago.atributos()
print('------------------------')
player1.atacar(guerrero)
guerrero.atacar(mago)
mago.atacar(player1)
print('------------------------')
player1.atributos()
guerrero.atributos()
mago.atributos()

