#!/usr/bin/python3
# -*- coding: utf-8 -*-

import asyncio
import aiohttp

async def get_api( api_url, key ):
    async with aiohttp.ClientSession() as session:

        #api_url = 
        async with session.get(api_url) as resp:
            result = await resp.json()
            print(result[ key ])

asyncio.run( get_api( 'http://127.0.0.1:5000/multiply?v1=3&v2=4', "result" ) )

