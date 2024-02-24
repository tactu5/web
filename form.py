from wtforms import TextAreaField, Form
from wtforms import validators

class CommentForm(Form):
    datos = TextAreaField('Datos',
                        [
                            validators.input_required(message='Los datos son requeridos'),
                            validators.regexp(regex=r'^[0-9, .]*$', message="Solo números, puntos, espacios o comas son permitidos.")
                        ]
                        )
    punto = TextAreaField('Digitos después del decimal',
                        [
                            validators.input_required(message='favor de ingresar los datos'),
                            validators.regexp(regex=r'^\d+$', message="Solo números son permitidos.")
                        ]
                        )