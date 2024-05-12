import click

@click.group()
def comamdos():
    pass

import app



@click.command()
@click.option("--prueba_corta",prompt= "Ingrese cuanto saco en la prueba corta",type=int, help="el valor de la prueba corta tiene que ser numerico")
def pruebacorta(prueba_corta): #recibe los argumentos de la linea 4
    resultado = app.pruebacorta(prueba_corta)
    print(resultado)

@click.command()
@click.option("--prueba_parcial",prompt= "Ingrese cuanto saco en la prueba parcial",type=int, help="el valor de la prueba parcial tiene que ser numerico")
def pruebaparcial(prueba_parcial): 
    resultado = app.pruebaparcial(prueba_parcial)
    print(resultado)


comamdos.add_command(pruebacorta)
comamdos.add_command(pruebaparcial)

if __name__ == "__main__":
    comamdos()