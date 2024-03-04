#!/usr/bin/python3
# -*- coding: utf-8 -*-

import asyncio
import aiohttp
import random


api_url = 'http://127.0.0.1:5000/'

async def call_api( url, guess):
    async with aiohttp.ClientSession() as session:
        async with session.get( url ) as resp:
            result = await resp.json()
            return result[ guess ] 

asyncio.run( call_api( api_url+'init', 'result' ) )

resultat = ''
val_test = 50

while( 1 ):
    resultat = asyncio.run(call_api( api_url+'test/'+str(val_test), 'resultat' ))
   
    if resultat == '-' :
        val_test = val_test//2
    elif resultat == '+' :
        val_test = val_test + (val_test//2)+1 
    else :
        print( 'BRAVO !!!' )
        exit( 0 )

