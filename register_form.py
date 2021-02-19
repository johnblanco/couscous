from wtforms import Form, StringField, PasswordField, validators


class RegisterForm(Form):
    username = StringField(u'Usuario', validators=[validators.input_required()], render_kw={"placeholder": "Ingresar usuario"})
    password = PasswordField(u'Contraseña', validators=[validators.input_required(),
                                                        validators.EqualTo('repeat_password', message='Las contraseñas deben coincidir')], render_kw={"placeholder": "Ingresar contraseña"})
    repeat_password = PasswordField(u'Repetir contraseña', validators=[validators.input_required()], render_kw={"placeholder": "Repetir contraseña"})

