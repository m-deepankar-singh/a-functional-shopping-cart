from flask import session,redirect, render_template, url_for,flash, request
from shop import db, app
from .models import Brand, Category, Addproduct
from .forms import Addproducts
import secrets


@app.route('/')
def home():
    products = Addproduct.query.filter(Addproduct.stock > 0)
    return render_template('products/index.html', products=products)


@app.route('/product/<int:id>')
def single_page(id):
    product = Addproduct.query.get_or_404(id)
    return render_template('/products/single_page.html', product=product)

@app.route('/brand/<int:id>')
def get_brand(id):
    brand = Addproduct.query.filter_by(brand_id=id)
    other =  Brand.query.join(Addproduct, (Brand.id == Addproduct.brand_id)).all()
    return render_template('products/index.html', brand=brand, other=other)


@app.route('/addbrand', methods=['GET','POST'])
def addbrand():
    if request.method=="POST":
        getbrand = request.form.get('brand')
        brand = Brand(name=getbrand)
        db.session.add(brand)
        flash(f'The Brand {getbrand} was added to your database','success')
        db.session.commit()
        return redirect(url_for('addbrand'))

    return render_template('products/addbrand.html',brands='brands')


@app.route('/addcat', methods=['GET','POST'])
def addcat():
    if request.method=="POST":
        getbrand = request.form.get('category')
        cat = Category(name=getbrand)
        db.session.add(cat)
        flash(f'The Category {getbrand} was added to your database','success')
        db.session.commit()
        return redirect(url_for('addbrand'))

    return render_template('products/addbrand.html')


@app.route('/addproduct', methods=['POST','GET'])
def addproduct():
    brands = Brand.query.all()
    categories= Category.query.all()
    form = Addproducts(request.form)
    if request.method == "POST":
        name =form.name.data
        price= form.price.data
        discount=form.discount.data
        stock=form.stock.data
        desc=form.description.data
        brand=request.form.get('brand')
        category=request.form.get('category')

        addpro=Addproduct(name=name,price=price,discount=discount,stock=stock,desc=desc,brand_id=brand,category_id=category)
        db.session.add(addpro)

        flash(f'The product {name} has been added to your database', 'success')
        db.session.commit()
        return redirect(url_for('admin'))

    return render_template('products/addproduct.html', title="Add Product", form =form, brands=brands, categories= categories)


'''@app.route('/updateproduct<int:id>', methods=['GET','POST'])
def updateproduct(id):
    brands=Brand.query.all()
    categories=Category.query.all()
    product = Addproduct.query.get_or_404(id)
    brand= request.form.get('brand')
    category= request.form.get('category')
    form = Addproducts(request.form)
    if request.method == "POST":
        product.name = form.name.data
        product.price= form.price.data
        product.discount=form.discount.data
        product.brand_id=brand
        product.stock=form.stock.data
        product.category_id=category
        product.desc=form.description.data
        db.session.commit()
        flash(f'Your product has been updated','success')
        return redirect(url_for('admin'))

        
    form.name.data = product.name
    form.price.data = product.price
    form.discount.data = product.discount
    form.stock.data = product.stock
    form.description.data = product.desc
    return render_template('products/updateproduct.html', form = form, brands=brands, categories=categories,product=product)'''