from datetime import datetime
from flask_wtf import Form
from wtforms import StringField, SelectField, SelectMultipleField, DateTimeField, IntegerField 
from wtforms.validators import DataRequired, AnyOf, URL


class VendorForm(Form):
    name = StringField(
        'name', validators=[DataRequired()]
    )
    category = SelectField(
        # TODO implement enum restriction
        'category', validators=[DataRequired()],
        choices=[
            ('Sit-down', 'Sit-down'),
            ('Counter', 'Counter'),
            ('Drive-thru', 'Drive-thru'),
        ]
    )
  
    cost = SelectField(
        'cost', validators=[DataRequired()],
        choices=[
            ('1', '$'),
            ('2', '$$'),
            ('3', '$$$'),
            ('4', '$$$$')
        ]
    )
    cuisine = SelectField(
        'cuisine', validators=[DataRequired()],
        choices=[
            ('Italian', 'Italian'),
            ('American', 'American'),
            ('Mexican', 'Mexican'),
            ('Thai', 'Thai'),
            ('Indian', 'Indian'),
            ('Chinese', 'Chinese'),
            ('Greek', 'Greek'),
            ('Vegetarian', 'Vegetarian')
        ]
    )
    location = StringField('location')
    purchase_to_points = IntegerField('purchase_to_points')


    

class UserForm(Form):
    username = StringField(
        'username', validators=[DataRequired()]
    )
    favorites = StringField(
        'favorites', validators=[DataRequired()]
    )

class DealForm(Form):
    item = StringField(
        'item', validators=[DataRequired()]
    )
    price = StringField(
        'price', validators=[DataRequired()]
    )
    points_required = StringField(
        'points_required', validators=[DataRequired()]
    )
    vendor_id = StringField(
        'vendor_id', validators=[DataRequired()]
    )

class PurchaseForm(Form):
    user = StringField(
        'user', validators=[DataRequired()]
    )

    item = StringField(
        'item', validators=[DataRequired()]
    )

class MenuForm(Form):
    item = StringField(
        'item', validators=[DataRequired()]
    )
    price = IntegerField('price')

