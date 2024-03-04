#!/usr/bin/python3
# -*- coding: utf-8 -*-

import asyncio
import aiohttp
import random

async def guess_secret_number(api_url, guess):
    async with aiohttp.ClientSession() as session:
        async with session.post(api_url, json={"guess": guess}) as resp:
            result = await resp.json()
            print(f"Devine {guess} -> Réponse: {result['response']} | Nombre secret: {result['secret_number']}")

async def main():
    api_url = 'http://127.0.0.1:5000/guess'
    guesses = [random.randint(1, 100) for _ in range(10)]  # Générer 10 nombres aléatoires à deviner
    tasks = [guess_secret_number(api_url, guess) for guess in guesses]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
