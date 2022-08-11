import db
import sqlite3
from msilib.schema import tables
from db import get_db, close_db 

def create_user():
    connect_db = get_db()
    try: 
        #Create Table
        connect_db.execute("""CREATE TABLE user (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            password TEXT NOT NULL
            );""")
    except Exception as err:
        print("user_Table is Created Before", str(err))

    connect_db.commit()
    close_db(connect_db) 
create_user()   


def create_product():
    connect_db = get_db()

    try: 
        cursor = connect_db.cursor()

        #Create Table
        cursor.execute("""CREATE TABLE product (
            id INTEGER ,
            product_name TEXT NOT NULL,
            price NUMBER NOT NULL,
            details TEXT,
            photo BLOB NOT NULL
            );""")

    except Exception as err:
        print("product_Table is Created Before", str(err))

    connect_db.commit()
    close_db(connect_db) 
create_product() 


def insertIntoDB(id,product_name, price, details, photo):
    connect_db = get_db()

    try: 
        #Create Table
        cursor =  connect_db.cursor()
        sqlite_insert_blob_query = """ INSERT INTO product
                                  (id,product_name, price, details, photo) VALUES (?, ?, ?, ?,?)"""
        
        data_tuple = (id,product_name, price, details,photo)
        cursor.execute(sqlite_insert_blob_query, data_tuple)
        connect_db.commit()
        print("Image and file inserted successfully as a BLOB into a table")

        close_db(cursor) 

    except Exception as err:
        print("Failed to insert blob data into sqlite table", str(err))
    


insertIntoDB(1,"Sharp", 18425 , "Silver,Cooling only", "sharp.jpg")
insertIntoDB(2,"Samsung washer", 10590, " 9 KG, Silver","washer.jpg")
insertIntoDB(3,"Zanossi", 12499, "432 Liters, Silver ","zanossi.jpg")
insertIntoDB(4,"Keriazi", 10000, "370 Liters, Black","keriazi.jpg")
insertIntoDB(5,"Lenovo2",  31000, "512GB SSD, 16GB RAM","lenovo2.jpg")
insertIntoDB(6,"Realme GT Master Edition", 10000, "Dual Sim, 256GB, 8GB RAM, 5G - Daybreak Blue","realme.jpg")
insertIntoDB(7,"Samsung Galaxy Note 20 Ultra ", 20000, "Dual Sim, 256GB, 4G LTE - Mystic Black","samsung_galaxy_note_20.jpg")
insertIntoDB(8,"Samsung Galaxy Z Flip3", 29000, ", 256GB, 8GB RAM, 5G - Phantom Black","samsung_galaxy.jpg")
insertIntoDB(9,"Huawei_matebook", 10000, "256GB SSD, 8GB RAM","huawei_matebook.jpg")

insertIntoDB(10,"Disaar Face Care Vitamin C ", 100 , "Hyaluronic Acid Whitening Cream 50ml", "disaar.jpg")
insertIntoDB(11,"THE ORDINARY serum , 30 ml ", 300 , "Hyaluronic Acid 2% + B5 Hydrator", "ordinary.jpg")
insertIntoDB(13,"Ever Beauty Dream Matte ", 80 , "Soft Matte Hydrating Foundation - 40, Golden Beige - 60 ml", "everbeauty.jpg")
insertIntoDB(14,"Neutrogena Face Wash", 200 , "Visibly Clear, Pink Grapefruit, 200ml", "neutrogena.jpg")
insertIntoDB(15,"Dove Beauty", 70 , " Moisturizing Body Cream - 150 ml", "dove.jpg")
insertIntoDB(16,"L'Oreal Paris Air Volume Mega Mascara, 01 Black ", 300 , "Mega volume light as airOur 1st whipped texture", "mascara.jpg")
insertIntoDB(17,"Hyaluronic Acid Serum for Skin from Real Beauty",140,"Hyaluronic acid works to tighten the skin","realbeauty.jpg")
insertIntoDB(18,"La Roche-Posay Effaclar Duo+ 40 ml", 250 , "Specifically formulated for oily, blemish and acne-prone skin in adults and teenagers", "possay.jpg")
insertIntoDB(19,"CeraVe Foaming ", 250 , "Cleanser for Normal to Oily Skin 236ml", "cerave.jpg")


insertIntoDB(20,"flour", 20, "Al Doha Egyptian Flour-1kg","flour.jpg")
insertIntoDB(21,"jam", 24,"Vitrac Date Jam - 430 gm ","vitrac.jpg")
insertIntoDB(22,"maxtella", 35, "Maxtella Jar - 500 g","maxtella.jpg")
insertIntoDB(23,"caramel_galaxy", 20,"Mars Galaxy Caramel Chocolate Bar","galaxy.jpg")
insertIntoDB(24,"snikers", 10 ,"snickers-single-chocolate bar", "snikers.jpg")
insertIntoDB(25,"ice_cream", 30, " Great Value Vanilla Bean Ice Cream","ice_cream.jpg")
insertIntoDB(26,"dina_milk", 23, "Dina Farms Full Cream Milk","dina_milk.jpg")
insertIntoDB(27,"mashroom", 21, "kenana mushroom 400 g","mashroom.jpg")
insertIntoDB(28,"pink_noodles", 35, "Hot Chicken Carbonara Ramen ","pink_noodles.jpg")



def create_cosmetics():
    connect_db = get_db()

    try: 
        cursor = connect_db.cursor()

        #Create Table
        cursor.execute("""CREATE TABLE cosmetics (
            id INTEGER,
            product_name TEXT NOT NULL,
            price NUMBER NOT NULL,
            details TEXT,
            photo BLOB NOT NULL
            );""")

    except Exception as err:
        print("product_Table is Created Before", str(err))

    connect_db.commit()
    close_db(connect_db) 

create_cosmetics() 

def insertIntoDB(id,product_name, price, details, photo):
    connect_db = get_db()

    try: 
        #Create Table
        cursor =  connect_db.cursor()
        sqlite_insert_blob_query = """ INSERT INTO cosmetics
                                  (id,product_name, price, details, photo) VALUES (?, ?, ?, ?,?)"""
        
        data_tuple = (id,product_name, price, details,photo)
        cursor.execute(sqlite_insert_blob_query, data_tuple)
        connect_db.commit()
        print("Image and file inserted successfully as a BLOB into a table")

        close_db(cursor) 

    except Exception as err:
        print("Failed to insert blob data into sqlite table", str(err))

insertIntoDB(10,"Disaar Face Care Vitamin C ", 100 , "Hyaluronic Acid Whitening Cream 50ml", "disaar.jpg")
insertIntoDB(11,"THE ORDINARY serum , 30 ml ", 300 , "Hyaluronic Acid 2% + B5 Hydrator", "ordinary.jpg")
insertIntoDB(13,"Ever Beauty Dream Matte ", 80 , "Soft Matte Hydrating Foundation - 40, Golden Beige - 60 ml", "everbeauty.jpg")
insertIntoDB(14,"Neutrogena Face Wash", 200 , "Visibly Clear, Pink Grapefruit, 200ml", "neutrogena.jpg")
insertIntoDB(15,"Dove Beauty", 70 , " Moisturizing Body Cream - 150 ml", "dove.jpg")
insertIntoDB(16,"L'Oreal Paris Air Volume Mega Mascara, 01 Black ", 300 , "Mega volume light as airOur 1st whipped texture", "mascara.jpg")
insertIntoDB(17,"Hyaluronic Acid Serum for Skin from Real Beauty",140,"Hyaluronic acid works to tighten the skin","realbeauty.jpg")
insertIntoDB(18,"La Roche-Posay Effaclar Duo+ 40 ml", 250 , "Specifically formulated for oily, blemish and acne-prone skin in adults and teenagers", "possay.jpg")
insertIntoDB(19,"CeraVe Foaming ", 250 , "Cleanser for Normal to Oily Skin 236ml", "cerave.jpg")


def create_electronics():
    connect_db = get_db()

    try: 
        cursor = connect_db.cursor()

        #Create Table
        cursor.execute("""CREATE TABLE electronics(
            id INTEGER NOT NULL,
            product_name TEXT NOT NULL,
            price NUMBER NOT NULL,
            details TEXT,
            photo BLOB NOT NULL
            );""")

    except Exception as err:
        print("product_Table is Created Before", str(err))

    connect_db.commit()
    close_db(connect_db) 

create_electronics()

def insertIntoDB(id,product_name, price, details, photo):
    connect_db = get_db()

    try: 
        #Create Table
        cursor =  connect_db.cursor()
        sqlite_insert_blob_query = """ INSERT INTO electronics
                                  (id,product_name, price, details, photo) VALUES (?, ?, ?, ?,?)"""
        
        data_tuple = (id,product_name, price, details,photo)
        cursor.execute(sqlite_insert_blob_query, data_tuple)
        connect_db.commit()
        print("Image and file inserted successfully as a BLOB into a table")

        close_db(cursor) 

    except Exception as err:
        print("Failed to insert blob data into sqlite table", str(err))

insertIntoDB(1,"Sharp", 18425 , "Silver,Cooling only", "sharp.jpg")
insertIntoDB(2,"Samsung washer", 10590, " 9 KG, Silver","washer.jpg")
insertIntoDB(3,"Zanossi", 12499, "432 Liters, Silver ","zanossi.jpg")
insertIntoDB(4,"Keriazi", 10000, "370 Liters, Black","keriazi.jpg")
insertIntoDB(5,"Lenovo2",  31000, "512GB SSD, 16GB RAM","lenovo2.jpg")
insertIntoDB(6,"Realme GT Master Edition", 10000, "Dual Sim, 256GB, 8GB RAM, 5G - Daybreak Blue","realme.jpg")
insertIntoDB(7,"Samsung Galaxy Note 20 Ultra ", 20000, "Dual Sim, 256GB, 4G LTE - Mystic Black","samsung_galaxy_note_20.jpg")
insertIntoDB(8,"Samsung Galaxy Z Flip3", 29000, ", 256GB, 8GB RAM, 5G - Phantom Black","samsung_galaxy.jpg")
insertIntoDB(9,"Huawei_matebook", 10000, "256GB SSD, 8GB RAM","huawei_matebook.jpg")




def create_grocery():
    connect_db = get_db()

    try: 
        cursor = connect_db.cursor()

        #Create Table
        cursor.execute("""CREATE TABLE grocery(
            id INTEGER NOT NULL,
            product_name TEXT NOT NULL,
            price NUMBER NOT NULL,
            details TEXT,
            photo BLOB NOT NULL
            );""")

    except Exception as err:
        print("product_Table is Created Before", str(err))

    connect_db.commit()
    close_db(connect_db) 

create_grocery()

def insertIntoDB(id,product_name, price, details, photo):
    connect_db = get_db()

    try: 
        #Create Table
        cursor =  connect_db.cursor()
        sqlite_insert_blob_query = """ INSERT INTO grocery
                                  (id,product_name, price, details, photo) VALUES (?, ?, ?, ?,?)"""
        
        data_tuple = (id,product_name, price, details,photo)
        cursor.execute(sqlite_insert_blob_query, data_tuple)
        connect_db.commit()
        print("Image and file inserted successfully as a BLOB into a table")

        close_db(cursor) 

    except Exception as err:
        print("Failed to insert blob data into sqlite table", str(err))


insertIntoDB(20,"flour", 20, "Al Doha Egyptian Flour-1kg","flour.jpg")
insertIntoDB(21,"jam", 24,"Vitrac Date Jam - 430 gm ","vitrac.jpg")
insertIntoDB(22,"maxtella", 35, "Maxtella Jar - 500 g","maxtella.jpg")
insertIntoDB(23,"caramel_galaxy", 20,"Mars Galaxy Caramel Chocolate Bar","galaxy.jpg")
insertIntoDB(24,"snikers", 10 ,"snickers-single-chocolate bar", "snikers.jpg")
insertIntoDB(25,"ice_cream", 30, " Great Value Vanilla Bean Ice Cream","ice_cream.jpg")
insertIntoDB(26,"dina_milk", 23, "Dina Farms Full Cream Milk","dina_milk.jpg")
insertIntoDB(27,"mashroom", 21, "kenana mushroom 400 g","mashroom.jpg")
insertIntoDB(28,"pink_noodles", 35, "Hot Chicken Carbonara Ramen ","pink_noodles.jpg")

def create_mycart():
    connect_db = get_db()

    try: 
        cursor = connect_db.cursor()

        #Create Table
        cursor.execute("""CREATE TABLE mycart(
            id INTEGER NOT NULL
            );""")

    except Exception as err:
        print("product_Table is Created Before", str(err))

    connect_db.commit()
    close_db(connect_db) 

create_mycart()