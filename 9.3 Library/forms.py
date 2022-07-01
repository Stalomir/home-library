from turtle import title
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, SubmitField 
from wtforms.validators import DataRequired

class BookForm(FlaskForm):
    title = StringField('Tytuł', validators=[DataRequired()])
    author = StringField('Autor', validators=[DataRequired()])
    year = IntegerField('Rok wydania', validators=[DataRequired()])
    genre = SelectField('Gatunek', choices=['Fantastyka','Sci-Fi','Romans','Powieść','Horror',
    'Kryminał','Dokument','Biografia','Inne','Nieznany'], coerce=str, validators=[DataRequired()])
    pages = IntegerField('Liczba stron', validators=[DataRequired()])
    


