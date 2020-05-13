import os
from PIL import Image
from flask import url_for,current_app

def add_profile_pic(pic_upload,username):
    filename = pic_upload.filename
    # filename : 'mypicture.jpg '  
    # ext_type: jpg
    ext_type = filename.split('.')[-1]
    storage_filename = filename.split('.')[0]+'.'+ext_type

    filepath = os.path.join(current_app.root_path,'static\profile_pics',storage_filename)

    output_size = (300,300)

    pic = Image.open(pic_upload)
    pic.thumbnail(output_size)
    pic.save(filepath)

    return storage_filename