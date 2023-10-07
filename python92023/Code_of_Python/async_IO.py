import requests
import time
import asyncio
'''urls= [
    "https://unsplash.com/photos/78A265wPiO4/download?ixid=M3wxMjA3fDB8MXxhbGx8fHx8fHx8fHwxNjk1MTAwNTUzfA&force=true",
    "https://images.unsplash.com/photo-1473496169904-658ba7c44d8a?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxleHBsb3JlLWZlZWR8MjF8fHxlbnwwfHx8fHw%3D&auto=format&fit=crop&w=400&q=60",
    "https://images.unsplash.com/photo-1503642551022-c011aafb3c88?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxleHBsb3JlLWZlZWR8MjN8fHxlbnwwfHx8fHw%3D&auto=format&fit=crop&w=400&q=60"]


def download_wallpaper(url,filename):
    response=requests.get(url)
    if response.status_code==200:
        with open (filename,"wb") as f:
            f.write(response.content)
            print(f"{filename} is downloaded successfully")

def main():
    for i,url in enumerate(urls):
        filename=f"file{i+4}.jpg"
        download_wallpaper(url,filename)

if __name__=="__main__":
    main()'''
'''---- NOTE  THAT  THIS CODE IS CONTAIN ERROR----
async def function1():
    # await asyncio.sleep(2)
    url="https://unsplash.com/photos/a-man-sitting-on-top-of-a-white-sand-dune-yXXhJZ7SPfk    response=requests.get(url)"
    response=requests.get(url)
    if response.status_code==200:
        with open ("ajay1.jpg","wb") as f:
                f.write(response.content)
                print(f"ajay1.jpg is downloaded successfully")
async def function2():
    url="https://unsplash.com/photos/an-escalator-with-two-people-walking-down-it-gu8WJiEUYz4"
    
    response=requests.get(url)
    if response.status_code==200:
        with open ("ajay2.jpg","wb") as f:
                f.write(response.content)
                print(f"ajay2.jpg is downloaded successfully")
    
async def function3():
    url="https://unsplash.com/photos/nJupV3AOP-U"
    response=requests.get(url)
    if response.status_code==200:
        with open ("ajay3.jpg","wb") as f:
                f.write(response.content)
                print(f"ajay3.jpg is downloaded successfully")
   

async def main():
        # task=asyncio.create_task(function1())
        # # await function1()
        # await function2()
        # await function3()
        await asyncio.gather(
            function1(),
            function2(),
            function3(),
        )
    
if __name__=="__main__":
    asyncio.run(main())   '''

import httpx

async def download_image(url, filename):
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        if response.status_code == 200:
            with open(filename, "wb") as f:
                f.write(response.content)
                print(f"{filename} is downloaded successfully")
        else:
            print(f"Failed to download {filename} (Status Code: {response.status_code})")

async def main():
    urls = [
        ("https://unsplash.com/photos/a-man-sitting-on-top-of-a-white-sand-dune-yXXhJZ7SPfk", "ajay1.jpg"),
        ("https://unsplash.com/photos/an-escalator-with-two-people-walking-down-it-gu8WJiEUYz4", "ajay2.jpg"),
        ("https://unsplash.com/photos/nJupV3AOP-U", "ajay3.jpg"),
    ]

    # Use asyncio.gather to download images concurrently
    await asyncio.gather(*[download_image(url, filename) for url, filename in urls])

if __name__ == "__main__":
    asyncio.run(main())

