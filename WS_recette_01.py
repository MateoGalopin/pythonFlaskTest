#!/usr/bin/python3
# -*- coding: utf-8 -*-

from flask import Flask, jsonify, session
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.secret_key = '1234'

#app.config["SESSION_PERMANENT"] = False
#app.config["SESSION_TYPE"] = "filesystem"
#Session(app)

@app.route('/', methods=['GET'])
def init():
    if 'ingredients' not in session :
        ingredients = []
        session[ 'ingredients' ] = ingredients
    page = '''<!DOCTYPE html>
            <html lang="en">               
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Document</title>
                <script>
                    url_add  = 'http://127.0.0.1:5000/add_ingredient';
                    url_list = 'http://127.0.0.1:5000/list_ingredient';
                    url_raz  = 'http://127.0.0.1:5000/raz';

                    function razList()
                    {
                        url = url_raz;
                        fetch( url ).catch(error => console.error('Error:', error));
                    }

                    function addIngredient()
                    {
                        champ_saisie = document.getElementById( 'saisie_ingredient' );
                        ingredient = champ_saisie.value;
                        url = url_add + '/' + ingredient;
                        fetch( url ).catch(error => console.error('Error:', error));
                        //showIngredient();
                    }

                    function showIngredient()
                    {
                        fetch(url_list)
                        .then(response => {
                            // Vérifier si la requête a réussi
                            if (!response.ok) {
                                throw new Error('Network response was not ok');
                            }
                            // Convertir la réponse en JSON
                            return response.json();
                        })
                        .then(data => {
                            affichage = document.getElementById( 'affiche' )
                            list_ingredients = data[ 'ingredients' ]
                            chaine_affiche = ''; 
                            list_ingredients.forEach( (x)=>{ chaine_affiche = chaine_affiche + '<br>' + x  } );
                            affichage.innerHTML = chaine_affiche; 
                            console.log(list_ingredients);
                        })
                        .catch(error => {
                            // Gérer les erreurs éventuelles
                            console.error('There has been a problem with your fetch operation:', error);
                        });
                    }
                </script>
            </head>
                ingrédient: 
                <input type='text' id='saisie_ingredient' >
                <button type='button' onclick="addIngredient()">add</button>  
                <button type='button' onclick="showIngredient()">list</button>  
                <button type='button' onclick="razList()">RAZ</button>  
                <br>
                <div id="affiche"></div>  
            </body>
            </html>'''

    return page, 200


@app.route('/add_ingredient/<string:ingredient>', methods=['GET'])
def add_ingredient( ingredient ):
    print( '>>>', ingredient )
    session[ 'ingredients' ].append(ingredient)
    session.modified = True 
    return jsonify( {'resultat' : 'OK' } ), 200


@app.route('/list_ingredient', methods=['GET'])
def list_ingredient( ):
    ingredients = session[ 'ingredients' ]
    return jsonify( {'ingredients' : ingredients } ), 200

@app.route('/raz', methods=['GET'])
def raz( ):
    ingredients = []
    session[ 'ingredients' ] = ingredients
    session.modified = True 
    return jsonify( {'resultat' : 'OK' } ), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

# Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:123.0) Gecko/20100101 Firefox/123.0'
# Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'
