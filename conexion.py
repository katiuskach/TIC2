import mysql.connector



class Registro_datos():

    def __init__(self):
        self.conexion = mysql.connector.connect( host="localhost",
                                                 user="cuchini",
                                                 passwd="1234",
                                                 database= "registro")

        mycursor = self.conexion.cursor()
        mycursor.execute("CREATE TABLE Registro (usuario VARCHAR(20), contrasena VARCHAR(10), personID int PRIMARY KEY)")


