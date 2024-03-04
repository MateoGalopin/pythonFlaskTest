#!/usr/bin/python3
# -*- coding: utf-8 -*-

import asyncio
import aiohttp

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.json(), response.status

async def main():
    async with aiohttp.ClientSession() as session:
        # Adresse de l'application Flask
        test_url = "http://localhost:5000/test/"
        init_url = "http://localhost:5000/init"

        # Faire une première requête pour voir le nombre de visites
        print("Récupération du nombre de visites...")
        response, status = await fetch(session, init_url)
        print(f"Réponse: {response}, Statut: {status}")

        val_high    = 100
        val_low     = 0
        
        while( 1 ):
            val_test = (val_low + val_high) // 2
            resultat, status = await fetch(session, test_url+str(val_test))
            resultat = resultat[ 'resultat']
            print( resultat)
            if resultat == '-' :
                val_high = val_test - 1
            elif resultat == '+' :
                val_low = val_test + 1
            else :
                print( 'BRAVO !!!' )
                exit( 0 )

if __name__ == '__main__':
    asyncio.run(main())
