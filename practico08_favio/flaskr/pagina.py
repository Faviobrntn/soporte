import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from flaskr.db import get_db
import json, requests
from tmdbv3api import TMDb, TV, Movie, Season, Discover

bp = Blueprint('pagina', __name__)
apikey="e00b72174e4ae097af808f34a8f220fc"
tmdb= TMDb()
# tmdb.api_key="e00b72174e4ae097af808f34a8f220fc"
tmdb.api_key=apikey
tmdb.language='es-ES'


@bp.route('/')
def index():
    # discover = 'https://api.themoviedb.org/3/discover/movie'
    # '''
    #     Allowed Values: , popularity.asc, popularity.desc, release_date.asc, release_date.desc, revenue.asc, revenue.desc, primary_release_date.asc, primary_release_date.desc, original_title.asc, original_title.desc, vote_average.asc, vote_average.desc, vote_count.asc, vote_count.desc
    #     default: popularity.desc
    # '''
    # parameters = dict(
    #     api_key=apikey,
    #     language='es-ES'
    #     # sort_by='release_date.desc'
    # )
    # resp = requests.get(url=discover, params=parameters)
    # data = json.loads(resp.text)

    # print(data['page'])
    # print(data['total_results'])
    # print(data['total_pages'])

    discover = Discover()
    movie = discover.discover_movies({
        'sort_by': 'popularity.desc',
        'language': 'es-ES'
    })

    # return render_template('pagina/index.html', posts=data['results'])
    return render_template('pagina/index.html', peliculas=movie)



@bp.route('/buscar', methods=('GET', 'POST'))
def buscar():
    try:
        if request.method == 'POST':
            titulo = request.form['titulo']
            tipo = request.form['tipo']

            if not titulo:
                raise Exception('El Titulo es requerido.')

            if tipo == "peliculas":
                entidad = Movie()
            elif tipo == "series":
                entidad = Season()
            elif tipo == "tv":
                entidad = TV()

            show=entidad.search(titulo)
        
    except Exception as e:
        flash(str(e))
        return redirect(url_for('pagina.index'))
        
    return render_template('pagina/buscar.html', resultados=show)




def get_detalles(id, tipo=''):
    try:
        if id == '':
            abort(404, "Post id {0} doesn't exist.".format(id))
        if tipo == '':
            abort(403)
        detalles = ""
        if tipo == "peliculas":
            movie = Movie()
            detalles = movie.details(id)
        elif tipo == "series":
            season = Season()
            detalles = season.details(id)
        elif tipo == "tv":
            tv = TV()
            detalles = tv.details(id)

        return detalles

    except Exception as e:
        raise e



@bp.route('/<int:id>/detalles', methods=('GET', 'POST'))
def detalles(id):

#Comprobamos si viene el parametro por GET
    try:
        if request.method == 'GET':

            tipo = request.args.get('tipo')

            if (tipo != ''):
                detalles = get_detalles(id, tipo)
            else:
                raise Exception('Parametro vacio.')
    except Exception as e:
        flash(str(e))
        return redirect(url_for('pagina.index'))
    
    return render_template('pagina/detalles.html', resultado=detalles)




@bp.route('/favorito', methods=('GET', 'POST'))
def favorito():
    resp = {'status':False, 'msg':''}
    try:
        if request.method == 'POST':
            pelicula_id = request.form['id']

            if (pelicula_id):
                fav = get_db().execute(
                    'SELECT * FROM favoritos f WHERE f.user_id = ? AND f.pelicula_id = ?', (g.user['id'], pelicula_id)
                    ).fetchone()
                #Significa que no existe, por ende, guardo el FAV
                if fav is None: 
                    db = get_db()
                    db.execute(
                        'INSERT INTO favoritos (user_id, pelicula_id) VALUES (?, ?)', (g.user['id'], pelicula_id ))
                    db.commit()
                    resp['status'] = True
                    resp['fav'] = True
                else:
                    db = get_db()
                    db.execute('DELETE FROM favoritos WHERE id = ?', (fav['id'],))
                    db.commit()
                    resp['status'] = True
                    resp['fav'] = False
            else:
                raise Exception('Parametro vacio.')
    except Exception as e:
        resp['msg'] = str(e)
        return json.dumps(resp)

    return json.dumps(resp)
