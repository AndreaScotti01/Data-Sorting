from PIL import Image
import numpy as np
import os
from prettytable import PrettyTable

def add_to_text_table(table_name,file_name,pic_height,pic_width,grayscale,red,green,blue,alpha):
       table_name.add_row([file_name,pic_height,pic_width,grayscale,red,green,blue,alpha])

def main():
    myTable = PrettyTable(["name","height","width","grayscale","R","G","B","ALPHA"])
    path = "./files/images"
    for images in os.listdir(path):    
        img = Image.open(str(path) + "/" + str(images))
        img_array = np.array(img)
        width = img_array.shape[0]
        height = img_array.shape[1]
        mean_rgb = 0
        gray_scale = 0  
        if len(img_array.shape) == 2:
            gray_scale = np.round_(np.mean(img_array),decimals=2)
            add_to_text_table(myTable,images.split(".")[0],height,width,gray_scale,mean_rgb,mean_rgb,mean_rgb,mean_rgb)
    
        elif  len(img_array.shape) == 3 and img_array.shape[2] == 3:
            mean_rgb = np.round_(np.mean(np.mean(img_array,axis=0),axis=0),decimals=2)   
            add_to_text_table(myTable,images.split(".")[0],height,width,gray_scale,mean_rgb[0],mean_rgb[1],mean_rgb[2],"0")    
            
        elif  len(img_array.shape) == 3 and img_array.shape[2] == 4:
            mean_rgb = np.round_(np.mean(np.mean(img_array,axis=0),axis=0),decimals=2)     
            add_to_text_table(myTable,images.split(".")[0],height,width,gray_scale,mean_rgb[0],mean_rgb[1],mean_rgb[2],mean_rgb[3])    
    print(myTable)
       
if __name__ == "__main__":
    main()