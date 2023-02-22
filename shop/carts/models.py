from shop import db,app


class Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    price = db.Column(db.Numeric(10,2),nullable=False)
    discount= db.Column(db.Integer,default=0)
    stock = db.Column(db.Integer,default=0)

    def __repr__(self):
        return '<Cart %r>' % self.title


with app.app_context():
  db.create_all()