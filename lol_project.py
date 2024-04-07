from lcu_driver import Connector

client = Connector()

print("looking for match")
@client.ws.register('/lol-matchmaking/v1/ready-check',event_types=("UPDATE",))
async def auto_accept_match(connection,event):
    if event.data['playerResponse'] == "None":
        await connection.request('post','/lol-matchmaking/v1/ready-check/accept')
        print("match accept")

client.start()