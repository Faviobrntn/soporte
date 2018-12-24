from Negocio import ABMPersona, ABMUsuario, ShowAPI,ABMPersonaShow,ABMShow
from DBase import Tablas


def altaPer():
    persona=Tablas.Persona()
    usuario=Tablas.Usuario()
    def alta():
        persona.nombre=input("nombre: ")
        persona.apellido=input("apellido: ")
        persona.dni=input("dni: ")
        usuario.nombreUsuario=input("usuario: ")
        usuario.contrasena=input("contrasena: ")
    alta()
    usuario.persona=persona
    abm=ABMPersona.ABMPersona()
    abm.altaPersona(persona,usuario)

def mostrarPer():
    abmu=ABMUsuario.ABMUsuario()
    us=abmu.listarUsuarios()
    abm=ABMPersona.ABMPersona()
    pers=abm.listarPersonas()
    for i in pers:
        print(i.nombre)
        print(i.apellido)
        print(i.dni)
    for i in us:
        print(i.nombreUsuario)
        print(i.contrasena)
        print(i.idpersona)

def buscarUSU():
    usu=Tablas.Usuario()
    usu.nombreUsuario=input("usuario: ")
    usu.contrasena=input("contra: ")
    abmu = ABMUsuario.ABMUsuario()
    usEnc = abmu.buscarUsuario(usu)
    print(usEnc)

def buscarSerie():
    api=ShowAPI.ShowAPI()
    nombre=input("ingrese nombre: ")
    resultados=api.buscarSerie(nombre)
    for i in resultados:
        print(i.idShow)

def buscarPelicula():
    api=ShowAPI.ShowAPI()
    nombre=input("ingrese nombre: ")
    resultados=api.buscarPelicula(nombre)
    for i in resultados:
        print(i.idShow)

def buscarpeliporID():
    api=ShowAPI.ShowAPI()
    id=71446
    resultado=api.buscarPeliculaPorId(id)
    print(resultado.nombre)

def buscarserieporid():
    api=ShowAPI.ShowAPI()
    id=71446
    nombre="la casa de papel"
    resultado=api.buscarSeriePorId(id)
    return resultado


def listarShows():
    ambs=ABMShow.ABMShow()
    resul=ambs.listarShows()
    for i in resul:
        print(i.idShow)
        print(i.tipo)


def pershow():
    abmshow=ABMShow.ABMShow()
    showEncontrado =Tablas.Show
    showEncontrado.idShow=71446
    showEncontrado = abmshow.buscarShow(showEncontrado)
    abmPer=ABMPersona.ABMPersona()
    pershow = Tablas.PersonaShow()
    pershow.idshow=showEncontrado.idShow
    pershow.idpersona=1
    pershow.estado = 1
    pershow.puntuado= 0
    abmshoper = ABMPersonaShow.ABMPersonaShow()
    agregado2=abmshoper.altaPersonaShow(pershow)
    print(agregado2)

def listarPershow():
    abmpershow=ABMPersonaShow.ABMPersonaShow()
    lista=abmpershow.listarPersonaShow()
    for i in lista:
        print(i.idpersona)
        print(i.idshow)
        print(i.tipo)
def shows():
    listarShows()
    abm=ABMPersonaShow.ABMPersonaShow()
    showPer=abm.buscarPerShowPorIdPersona(1)
    for i in showPer:
        print(i.idshow)
    abms=ABMShow.ABMShow()
    shows=abms.listarShowsPorID(showPer)
    for i in shows:
        print(i.nombre)



