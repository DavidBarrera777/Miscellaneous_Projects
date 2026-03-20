from PIL import Image
from PIL.ExifTags import TAGS

#this is the path to the photo that needs to analyzed
image = 'analyze_photos/WIN_20260319_23_04_21_Pro.jpg'
output_image = 'analyze_photos/clean_image.jpg'


def get_metadata(image_path):
    image = Image.open(image_path)
    exif_data = image._getexif()

    if not exif_data:
        print("No metadata found")
        return
    
    for tag, value in exif_data.items():
        tag_name = TAGS.get(tag,tag)

        if isinstance(value, bytes):
            continue
        print(f'{tag_name}: {value}')



def delete_metadata(image_path, output_path):
    image = Image.open(image_path)

    data = list(image.getdata())
    clean_image = Image.new(image.mode, image.size)
    clean_image.putdata(data)

    clean_image.save(output_path)

    return None

def main():
    get_metadata(output_image)

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
