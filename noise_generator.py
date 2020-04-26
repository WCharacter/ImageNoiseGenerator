from PIL import Image
import random
import os
from multiprocessing import Pool, freeze_support
from config import dest, image_resolution, images_amount, img_format, dest

def get_random_pixel(p):
    return (random.randint(0, 255),random.randint(0, 255),random.randint(0, 255))


if(not os.path.isdir(dest)):
    os.mkdir(dest)

if __name__ == '__main__':
    for i in range(0, images_amount):
        freeze_support()    # for multiprocessing      
        pool = Pool(6)      # 6 threads

        img = Image.new('RGB', image_resolution)
        pixels = list(img.getdata())
        new_pixels = pool.map(get_random_pixel, pixels)
        pool.close()
        pool.join()
        
        img.putdata(new_pixels)
        path = f'{dest}\\{i}{img_format}'
        img.save(path)
        print(path)