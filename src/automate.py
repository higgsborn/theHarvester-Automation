import subprocess
from tqdm import tqdm
import time

start_time = time.time()

with open("../data/urls_100k.txt", 'r') as f:
    url = f.readlines()
    # print(url)

# remove the trailing new line character
url_cleaned = [u.split('\n')[0] for u in url]
del url

# chunk the urls into 100 url groups
url_chunk = []
url_matrix = []
for i, u in enumerate(url_cleaned):
    url_chunk.append(u)
    if i % 46 == 0:
        url_matrix.append(url_chunk)
        url_chunk = []

del url_cleaned
del url_chunk

for url_batch in tqdm(url_matrix):
    processes = []
    for u in url_batch:
        process = subprocess.Popen(["theHarvester", 
                                    "-d", 
                                    u, 
                                    "-b", 
                                    "bing,baidu,duckduckgo", 
                                    "-f", 
                                    f"../data/results/{u}"])
        processes.append(process)

    for process in processes:
        process.wait()

end_time = time.time()
elapsed_time = (end_time - start_time) / 60.0

print(f"Script execution time: {elapsed_time} in minutes")
