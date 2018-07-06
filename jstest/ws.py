#!/usr/bin/env python

# WS server that sends messages at random intervals

import asyncio
import datetime
import random
import websockets

color = 'blue'

async def time(websocket, path):

    while True:
        color = input("Enter the color: ")

        await websocket.send(color)
        print("Sent " + color)

start_server = websockets.serve(time, '127.0.0.1', 5678)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
