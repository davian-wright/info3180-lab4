from flask_uploads import UploadSet, images
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired


class UploadForm(FlaskForm):
    upload = FileField('image', validators=[FileRequired(),FileAllowed(images, 'Images only!')])