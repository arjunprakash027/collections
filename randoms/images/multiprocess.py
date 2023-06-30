import timeit
import requests
import threading
import multiprocessing

image_urls = []
for i in range(100,500):
    image_urls.append(f'https://picsum.photos/{i}')

def download_image(image_url):
    response = requests.get(image_url)
    if response.status_code == 200:
        with open(f"images/{image_url.split('/')[-1]}.png", 'wb') as f:
            f.write(response.content)
    else:
        print(f'Error downloading image {image_url}')

def pool_handler():
    with multiprocessing.Pool(4) as pool:
        pool.map(download_image, image_urls)

pool_handler()

