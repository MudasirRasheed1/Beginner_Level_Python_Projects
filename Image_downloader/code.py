import os 
import requests


def get_extension(url):
    """Returns the extension of the image from the url"""
    extensions = ['.jpg', '.png', '.gif', '.jpeg', '.svg']
    for extension in extensions:
        if extension in url:
            return extension
        
def download_image(url, f_name, folder_name = None):
    """downloas an image from the url and saves it in the folder_name with the name f_name"""
    if ext := get_extension(url):  # walrus operator , in c expression takes a value and returns it but to achieve it in python we use walrus operator
        if folder_name :
            image_name = f"{folder_name}/{f_name}{ext}" 
        else:
            image_name = f"{f_name}{ext}"
    else :
        raise Exception("Image extension not found")
    
    if os.path.isfile(image_name):  # isfile returns True if the file exists , os.path is module
        raise Exception("Image already exists") # raise is used to raise an exception manually
    
    try:
        image_content = requests.get(url).content #get is function of requests module which returns the object containing the content of the url in content attribute
        with open(image_name, 'wb') as handler: 
            handler.write(image_content)
            print(f"Image {image_name} downloaded")
    except Exception as e:
        print(f"Error while downloading image {image_name} : \n{e}")


if __name__ == "__main__":
    url = "https://www.python.org/static/community_logos/python-logo-master-v3-TM.png"
    download_image(url, "python_logo1", "images")


        


    