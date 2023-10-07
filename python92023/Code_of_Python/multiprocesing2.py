# import multiprocessing
import concurrent.futures

import requests

def downloadimage(url, name):
    print(f"{name} starting  downloading")
    response = requests.get(url)
    with open(f"{name}.jpg", "wb") as f:
        f.write(response.content)
    print(f"{name} downloaded")

if __name__ == "__main__":
    url = "https://picsum.photos/200/300"
#     processes = []
#     for i in range(4):
#         p = multiprocessing.Process(target=downloadimage, args=(url, i + 2))
#         p.start()
#         processes.append(p)

#     for p in processes:
#         p.join()

    with concurrent.futures.ProcessPoolExecutor() as executor:
        l1=[url for i in range(5)]
        l2=[i for i in range(5)]
        result=executor.map(downloadimage,l1,l2)
    
        for r in result:
            print(r)

    
