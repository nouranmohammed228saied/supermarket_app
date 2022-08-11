from sqlite3 import connect
from unicodedata import name
import db
from flask import Flask,redirect,request,url_for
from flask import render_template


app = Flask(__name__)
@app.route("/")
def base():
    return render_template('base.html')

@app.route('/register',methods=['GET','POST'])
def register():
    if request.method=='POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        connect= db.get_db()
        connect.execute(f"""INSERT INTO user(name ,email, password)
                           VALUES('{name}','{email}','{password}');""")
        connect.commit()
        db.close_db(connect)
        return redirect(url_for('base'))

    return render_template('register.html')

@app.route("/admin")
def admin_page():
    connect=db.get_db().cursor()
    connect.execute("SELECT * FROM user;") 
    data = connect.fetchall()
    print(data)
    return render_template('admin.html',data = data)

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method=='POST':
        email = request.form['email']
        password= request.form['password']

        connect=db.get_db().cursor()
        connect.execute(f"""SELECT email,password FROM user 
                        WHERE email='{email}' AND password = '{password}';""") 
        data = connect.fetchall()
        if email=='mariam@gmail.com' or email=='habiba@gmail.com' or email=='nouran@gmail.com' and password=='136' or password=='102' or password=='239' :
            return redirect(url_for('admin_page'))
        if len(data)== 1:
            return redirect(url_for('base'))
        else:
            return redirect(url_for('login'))    
       
    return render_template('login.html')

@app.route("/electronics")
def electronics():
    connect=db.get_db().cursor()
    connect.execute("SELECT * FROM electronics;") 
    data = connect.fetchall()
    return render_template('electronics.html',rows = data)


@app.route("/cosmetics")
def cosmetics():
    connect=db.get_db().cursor()
    connect.execute("SELECT * FROM cosmetics;") 
    data = connect.fetchall()
    return render_template('cosmetics.html',rows = data)


@app.route("/grocery")
def grocery():
    connect=db.get_db().cursor()
    connect.execute("SELECT * FROM grocery;") 
    data = connect.fetchall()
    return render_template('grocery.html',rows = data)


@app.route('/search' ,methods =['POST'])
def search_product():
    if request.method =="POST":
        name = request.form['product_name']
        connect=db.get_db().cursor()
        connect.execute(f"""SELECT id , product_name, price, details, photo  FROM product 
                            WHERE product_name  LIKE '%{ name }%' ;""")
        data = connect.fetchall()
    return render_template('search.html',data =data)


@app.route("/product")
def product():
    connect=db.get_db().cursor()
    connect.execute("SELECT * FROM product;") 
    data = connect.fetchall()
    print(data)
    return render_template('product.html',data = data)


@app.route('/update/<int:id>' ,methods =['GET','POST'])
def update_product(id=None):
    if request.method =='POST':
        product_name = request.form['product_name']
        price= request.form['price']
        connect=db.get_db()
        connect.execute(f"""UPDATE product
                       SET product_name ='{product_name}',
                       price='{price}'
                       WHERE id ={id};""")
        connect.commit()
        db.close_db(connect)
        return redirect(url_for('product'))
    cur=db.get_db().cursor()
    cur.execute(f"""SELECT id, product_name, price ,details  FROM product 
                 WHERE id = {id} """)
    row = cur.fetchone()
    return render_template('update.html', row=row)

@app.route('/cart/<int:id>')
def cart(id=None):
    connect=db.get_db()
    connect.execute(f"""INSERT INTO mycart(id)VALUES({id});""")
    connect.commit()
    db.close_db(connect)
    cur =db.get_db().cursor()
    cur.execute(f"""SELECT * FROM product  INNER JOIN mycart ON mycart.id = product.id """)
    rows = cur.fetchall()
    for r in rows:
         print(r)
    return render_template('cart.html', row=rows)

@app.route('/cart/')
def delete_cart(id=None):
    connect=db.get_db().cursor()
    connect.execute("DELETE FROM mycart;") 
    return render_template('cart.html')

@app.route('/order/')
def order():
    return render_template('order.html')