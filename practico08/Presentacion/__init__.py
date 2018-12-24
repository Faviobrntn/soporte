import functools

from flask import (
    Flask, Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from Negocio import ABMPersona,ABMUsuario,ShowAPI,ABMShow,ABMPersonaShow
from DBase import Tablas

bp = Blueprint('Presentacion', __name__, url_prefix='/')

app = Flask(__name__)
app.secret_key ="sebastian"
app.register_blueprint(bp)
# app.add_url_rule('/', endpoint='index')

@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('idpersona')
    if user_id is None:
        g.user = None
    else:
        abmu = ABMUsuario.ABMUsuario()
        usr = abmu.buscarUsuarioPorID(user_id)
        g.user = usr

@app.route('/',methods=["GET","POST"])
def index():
    if("idpersona" in session):
        load_logged_in_user()
        return render_template('bienvenido.html')
    else:
        return render_template('loguin.html')

@app.route('/index',methods=["GET","POST"])
def loguin():
    if request.method=='POST':
        usuario=Tablas.Usuario()
        usuario.nombreUsuario = request.form['usuario']
        usuario.contrasena = request.form['contraseña']
        abm=ABMUsuario.ABMUsuario()
        usuEncontrado = abm.buscarUsuario(usuario)
        if (usuEncontrado!=None):
            session["idpersona"] = usuEncontrado.idpersona
            load_logged_in_user()
            return render_template('bienvenido.html')
        else:
            return render_template('loguin.html',var=True)
    return render_template('loguin.html')


@app.route('/altaPersonaForm')
def altaPersonaForm():
    return render_template('AltaPersona.html')

@app.route('/altaPersona',methods=["GET","POST"])
def altaPersona():
    per=Tablas.Persona()
    usu=Tablas.Usuario()
    if request.method=='POST':
        per.nombre=request.form['nombre']
        per.apellido=request.form['apellido']
        per.dni=request.form['dni']
        usu.nombreUsuario = request.form['usuario']
        usu.contrasena = request.form['contraseña']
        usu.persona = per
        abm=ABMPersona.ABMPersona()
        guardado=abm.altaPersona(per,usu)
        if (guardado):
            abm=ABMUsuario.ABMUsuario()
            usuEncontrado = abm.buscarUsuario(usu)
            session["idpersona"]=usuEncontrado.idpersona
            load_logged_in_user()
            return render_template('bienvenido.html',var1=True)
        else:
            return render_template('loguin.html', var1=True)

@app.route('/resultados', methods=['GET','POST'])
def buscarShow():
    if request.method=='POST':
        nombre = request.form['titulo']
        opcion = request.form['show']
        load_logged_in_user()
        if (opcion =='serie'):
            show=ShowAPI.ShowAPI()
            shows=show.buscarSerie(nombre)
            return render_template('resultados.html',shows=shows, cantidad=len(shows))
        elif(opcion=='pelicula'):
            show=ShowAPI.ShowAPI()
            shows=show.buscarPelicula(nombre)
            return render_template('resultados.html',shows=shows, cantidad=len(shows))
    return render_template('bienvenido.html')



@app.route('/<int:id>/detalles', methods=('GET', 'POST'))
def detalles(id):
    #Comprobamos si viene el parametro por GET
    try:
        load_logged_in_user()
        if request.method == 'GET':

            tipo = request.args.get('tipo')
            detalles = None

            if (tipo != ''):
                show=ShowAPI.ShowAPI()
                if (tipo == '1'):
                    detalles=show.buscarSeriePorId(id)
                elif(tipo == '0'):
                    detalles=show.buscarPeliculaPorId(id)
            else:
                raise Exception('Parametro vacio.')
    except Exception as e:
        flash(str(e))
        return redirect(url_for('index'))

    return render_template('detalles.html', resultado=detalles)





@app.route('/logout')
def logout():
    session.pop('idpersona', None)
    return render_template('loguin.html')


@app.route('/modificarUsuarioForm')
def modificarUsuario():
    load_logged_in_user()
    if("idpersona" in session):
        abmp=ABMPersona.ABMPersona()
        per=abmp.buscarPersonaPorID(session['idpersona'])
        abmu=ABMUsuario.ABMUsuario()
        usu=abmu.buscarUsuarioPorID(session['idpersona'])
        if(per!=None and usu!=None):
            return render_template('modificarUsuario.html', persona=per,usuario=usu)
    return render_template('loguin.html')


@app.route('/usuarioModificado',methods=['GET','POST'])
def usuarioModificado():
    per=Tablas.Persona()
    # usu=Tablas.Usuario()
    if request.method=='POST':
        per.idpersona=request.form['idpersona']
        per.nombre=request.form['nombre']
        per.apellido=request.form['apellido']
        per.dni=request.form['dni']
        # usu.idpersona=request.form['idpersona']
        # usu.nombreUsuario = request.form['usuario']
        # usu.contrasena = request.form['contrasena']
        abm=ABMPersona.ABMPersona()
        guardado=abm.actualizarPersona(per)
        print(guardado)
        # abmu=ABMUsuario.ABMUsuario()
        # guardado1= abmu.actualizarUsuario(usu)
        if (guardado):
            load_logged_in_user()
            flash("Sus datos se actualizaron con éxito.")
            return render_template('bienvenido.html',var=guardado)
        else:
            session.clear()
            flash("No se pudo guardar.")
            return render_template('loguin.html', var1=True)



@app.route('/formAgregarShow',methods=['GET','POST'])
def formAgregarResultado():
    load_logged_in_user()
    if request.method=='POST':
        show=ShowAPI.ShowAPI()
        if (request.form['tipo']=="0"):
            showEncontrado = show.buscarPeliculaPorId(request.form['idShow'])
            abmshow = ABMShow.ABMShow()
            agregado1 = abmshow.altaShow(showEncontrado)
            if (agregado1):
                return render_template('formAgregarShow.html',show=showEncontrado)
        elif(request.form['tipo']=="1"):
            showEncontrado = show.buscarSeriePorId(request.form['idShow'])
            abmshow = ABMShow.ABMShow()
            agregado1 = abmshow.altaShow(showEncontrado)
            if (agregado1):
                return render_template('formAgregarShow.html',show=showEncontrado)
    return render_template('loguin.html', var1=True)



@app.route('/agregarShow',methods=['GET','POST'])
def agregarShow():
    load_logged_in_user()
    if request.method=='POST':
        persho=Tablas.PersonaShow()
        persho.tipo=int(request.form['tipo'])
        persho.idpersona=session['idpersona']
        persho.estado=int(request.form['estado'])
        persho.idshow=int(request.form['idShow'])
        persho.puntuado=0
        tipo=int(request.form['tipo'])
        abm=ABMPersonaShow.ABMPersonaShow()
        final=abm.altaPersonaShow(persho)
        if (final):
            # return render_template('bienvenido.html',var3=True)
            flash("Se agrego con éxito.")
            if tipo == 0:
                return redirect(url_for('misPeliculas'))
            elif tipo == 1:
                return redirect(url_for('misSeries'))
            else:
                return redirect(url_for('descubrir'))
    return render_template('loguin.html', var1=True)



@app.route('/misPeliculas')
def misPeliculas():
    load_logged_in_user()
    if("idpersona" in session):
        abm=ABMPersonaShow.ABMPersonaShow()
        showPer=abm.buscarPerShowPorIdPersona(session['idpersona'])
        if(len(showPer)>0):
            abms=ABMShow.ABMShow()
            shows=abms.listarShowsPorID(showPer)
            peliculas=[]
            for i in shows:
                if (i.tipo==0):
                    peliculas.append(i)
            return render_template('misShows.html',cantidad=len(peliculas),shows=peliculas,tipo=0)
        return render_template('misShows.html',cantidad=0)
    return render_template('loguin.html')

@app.route('/misSeries')
def misSeries():
    load_logged_in_user()
    if("idpersona" in session):
        abm=ABMPersonaShow.ABMPersonaShow()
        showPer=abm.buscarPerShowPorIdPersona(session['idpersona'])
        if(len(showPer)>0):
            abms=ABMShow.ABMShow()
            shows=abms.listarShowsPorID(showPer)
            series=[]
            for i in shows:
                if (i.tipo==1):
                    series.append(i)
            return render_template('misShows.html',cantidad=len(series),shows=series,tipo=1)
        return render_template('misShows.html',cantidad=0)
    return render_template('loguin.html',var1=True)

@app.route('/descubrir')
def descubrir():
    load_logged_in_user()
    if('idpersona' in session):
        abm=ShowAPI.ShowAPI()
        shows=abm.descubrir()
        return render_template('descubrir.html',shows=shows,cantidad=len(shows))
    return render_template('loguin.html',var1=True)

@app.route('/modificarPerShowForm',methods=['GET','POST'])
def modificarPerShow():
    load_logged_in_user()
    if request.method=='POST':
        pershow=Tablas.PersonaShow()
        abm=ABMPersonaShow.ABMPersonaShow()
        pershow.idpersona=session["idpersona"]
        pershow.idshow=request.form["idShow"]
        pershow.tipo=request.form["tipo"]
        pershow=abm.buscarPerShow(pershow)
        abms=ABMShow.ABMShow()
        show=Tablas.Show()
        show.idShow=request.form["idShow"]
        show.tipo=request.form['tipo']
        show=abms.buscarShowporIDyTipo(show)
        if(pershow!=None):
            return render_template('modificarShow.html',pershow=pershow,show=show)
    return render_template('loguin.html',var1=True)

@app.route('/modiShow',methods=['GET','POST'])
def modiShow():
    load_logged_in_user()
    if request.method=='POST':
        pershow=Tablas.PersonaShow()
        abm=ABMPersonaShow.ABMPersonaShow()
        pershow.idpersona=int(session["idpersona"])
        pershow.idshow=int(request.form['idShow'])
        pershow.estado=int(request.form['estado'])
        pershow.tipo=int(request.form['tipo'])
        pershow.puntuado=1
        abm.modificarPerShow(pershow)
        show=Tablas.Show()
        show.idShow=int(request.form['idShow'])
        show.tipo=int(request.form['tipo'])
        if("puntuacion" in request.form):
            show.puntuacionUsuariosAcumulada=int(request.form['puntuacion'])
            abms=ABMShow.ABMShow()
            abms.puntuarShow(show)
        return render_template('bienvenido.html')
    return render_template('loguin.html',var1=True)


@app.route('/eliminarShow',methods=['GET','POST'])
def eliminarShow():
    load_logged_in_user()
    if request.method=='POST':
        pershow=Tablas.PersonaShow()

        pershow.idpersona=int(session["idpersona"])
        pershow.idshow=int(request.form['idShow'])
        pershow.tipo=int(request.form['tipo'])
        pershow.puntuado=1

        abm=ABMPersonaShow.ABMPersonaShow()
        result = abm.eliminarPerShow(pershow)

        if result == True:
            flash("Se elimino con éxito.")
        else:
            flash("No se puedo eliminar el registro.")
        # show=Tablas.Show()
        # show.idShow=int(request.form['idShow'])
        # show.tipo=int(request.form['tipo'])
    return redirect(url_for('descubrir'))



@app.route('/filtrar',methods=['GET','POST'])
def filtrar():
    load_logged_in_user()
    if request.method=='POST':
        abm=ABMPersonaShow.ABMPersonaShow()
        showPer=abm.buscarPerShowPorIdPersona(session['idpersona'])
        showsid=[]
        filtro=int(request.form['show'])
        if filtro==0:
            for i in showPer:
                if i.estado==0:
                    showsid.append(i)
        elif filtro==1:
            for i in showPer:
                if i.estado==1:
                    showsid.append(i)
        elif filtro==2:
            for i in showPer:
                if i.estado==2:
                    showsid.append(i)
        if(len(showsid)>0):
            abms=ABMShow.ABMShow()
            shows=abms.listarShowsPorID(showsid)
            if request.form['tipo']=="0":
                peliculas=[]
                for i in shows:
                    if (i.tipo==0):
                        peliculas.append(i)
                return render_template('misShows.html',cantidad=len(peliculas),shows=peliculas,tipo=0)
            elif request.form['tipo']=="1":
                series=[]
                for i in shows:
                    if (i.tipo==1):
                        series.append(i)
                return render_template('misShows.html',cantidad=len(series),shows=series,tipo=1)
        tipo=request.form['tipo']
        return render_template('misShows.html',cantidad=0,tipo=tipo)
    return render_template('loguin.html',var1=True)





def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('loguin'))

        return view(**kwargs)

    return wrapped_view

if __name__=="__main__":
    app.run(debug=True)
