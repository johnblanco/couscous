from wtforms import Form, StringField, PasswordField, validators, SubmitField


class LoginForm(Form):
    username = StringField(u'Usuario', validators=[validators.input_required()], render_kw={"placeholder": "Ingresar usuario"})
    password = PasswordField(u'Contraseña', validators=[validators.input_required()], render_kw={"placeholder": "Ingresar contraseña"})
