import sys
from io import BytesIO
from PIL import Image
from django.core.files.uploadedfile import InMemoryUploadedFile

BACKGROUND_TRANSPARENT = (255, 255, 255, 0)


def get_file_name(image_data):
    return image_data.name


def get_image_extension(image):
    return image.format


def optimize_image(uploaded_image):
    image_temp = Image.open(uploaded_image)
    output_stream = BytesIO()
    image_temp.save(output_stream, format='PNG', dpi=[300, 300])
    output_stream.seek(0)
    uploaded_image = InMemoryUploadedFile(output_stream, 'ImageField', "%s.png" % uploaded_image.name.split('.')[0], 'image/png', sys.getsizeof(output_stream), None)
    return uploaded_image


def optimize_media(uploaded_file):
    content_type = uploaded_file.content_type.split('/')[0]
    if content_type == 'image':
        return optimize_image(uploaded_file)
    else:
        return uploaded_file
