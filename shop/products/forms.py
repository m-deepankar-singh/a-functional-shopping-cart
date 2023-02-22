from wtforms import Form,IntegerField, StringField,BooleanField, TextAreaField, validators, DecimalField

class Addproducts(Form):
    name = StringField('Name',[validators.DataRequired()])
    price = IntegerField('Price',[validators.DataRequired()])
    discount = IntegerField('Discount',default=0) 
    stock = IntegerField('Stock',[validators.DataRequired()])
    description= TextAreaField('Description',[validators.DataRequired()])
