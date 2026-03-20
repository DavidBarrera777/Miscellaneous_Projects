from PIL import Image
from PIL.ExifTags import TAGS

#this is the path to the photo that needs to analyzed
#and the output to the photo with no exif data
image = 'analyze_photos/WIN_20260319_23_04_21_Pro.jpg'
output_image = 'analyze_photos/clean_image.jpg'


#this function is responsible for extracting the exif data from a photo if there is some
#and converting it to readable content for the user to view
def get_metadata(image_path):
    image = Image.open(image_path)
    exif_data = image._getexif()

    if not exif_data:
        print("No metadata found")
        return
    
    for tag, value in exif_data.items():
        #tage_name = dictionary.get(key, default_value)
        #This takes two arguments, if the tag is not in dictionary
        #return the tag untranslated
        tag_name = TAGS.get(tag,tag)

        #checks if value is raw binary data
        if isinstance(value, bytes):
            continue
        print(f'{tag_name}: {value}')


#This function is taking the image and extracting only the pixel data
#Creating a blank image with no metadata and copying the pixel data to this 
#blank image and saving it as a new file
def delete_metadata(image_path, output_path):
    image = Image.open(image_path)

    data = list(image.getdata())
    clean_image = Image.new(image.mode, image.size)
    clean_image.putdata(data)

    clean_image.save(output_path)

    return None


#This is the main function that displays the meta data from an image then asks the user 
#if they wanna delete the meta data
def main():
    get_metadata(image)

    ask_user = input('Do you want to delete this meta data y/n: ')

    if ask_user == 'y':
        delete_metadata(image, output_image)
        print("\n--- Cleaned Image Metadata ---")
        get_metadata(output_image)
    else:
        return None

    return None




if __name__ == "__main__":
    main()
