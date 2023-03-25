from serpapi import GoogleSearch
import urllib.request
import os, json
import time
import socket 

socket.setdefaulttimeout(15)

query = ["Human face","Human without helmet", "bike rider without helmet", "Desi bike rider"]
image_results = []
for index,item in enumerate(query):
    for i in range(2):
        params = {
            "q": item,
            "tbm": "isch",
            "ijn": str(i),
            "api_key": "1de6c81396a7fabf3da1c3100234e561e6f4225a22fc6d6974d278e262ba8ff9"
        }
        search = GoogleSearch(params)
        results = search.get_dict()

        if "error" not in results:
            for image in results["images_results"]:
                if image["original"] not in image_results:
                    image_results.append(image["original"])

for index, image in enumerate(image_results, start=1):
    try:
        print(f"Downloading {index} image...")        
        start_time = time.time()
        opener=urllib.request.build_opener()
        opener.addheaders=[("User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36")]
        urllib.request.install_opener(opener)
        urllib.request.urlretrieve(image, f"SerpApi_Images/original_size_img_{index}.jpg")
    except Exception as inst:
        continue

print(json.dumps(image_results, indent=2))
print(len(image_results))
