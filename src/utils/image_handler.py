from pathlib import Path
from flask import current_app # information for my app
from uuid import uuid4



class ImageHandler:

    @staticmethod
    def save_image(image):
        if not image.filename: return None
        suffix = Path(image.filename).suffix
        image_name = str(uuid4()) + suffix
        image_path = Path(current_app.root_path) / "static/images/vacations" / image_name
        image.save(image_path) #saving the image to disk
        return image_name # return only the image name..
    
    @staticmethod
    def update_image(old_image_name, image):
        if not image.filename: return old_image_name
        image_name = ImageHandler.save_image(image)
        ImageHandler.delete_image(old_image_name)
        return image_name

    @staticmethod
    def delete_image(image_name):
        if not image_name: return
        image_path = Path(current_app.root_path) / "static/images/vacations" / image_name
        image_path.unlink(missing_ok = True)    

    
    @staticmethod
    def get_image_path(image_name):
        image_path = Path(current_app.root_path) / "static/images/vacations" / image_name
        if not image_path.exists():
            image_path = Path(current_app.root_path) / "static/images/not_image.jpg"
        return image_path