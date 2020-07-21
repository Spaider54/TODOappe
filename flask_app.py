"""

@auteur :  walid.menghour
@Date  : 07/07/2020

"""

#Python Project
from flask import Flask, render_template, request, redirect
import time
import os

# Defining Object
datatodo = []

# Definig class
class Todoo:
    def __init__(self, title, img, discription):
        self.title = title
        self.img = img
        self.discription = discription
        self.timenow = time.asctime(time.localtime(time.time()))

    def gettitle(self):
        return self.title

    def getimg(self):
        return self.img

    def getdiscription(self):
        return self.discription

    def gettime(self):
        return self.timenow

    def valide(self):
        return ((self.discription) and (self.img) and (self.title))




#Creating instance
app =Flask(__name__)


#Make Configuration
app.config["IMAGE_UPLOADS"] = "static/images/"
app.config["ALLOWED_IMAGE_EXTENSIONS"] = ["JPEG", "JPG", "PNG", "GIF"]


@ app.route('/')
def Home():

    return render_template("Home.html", title="HOME", TODOliste=datatodo)


@ app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "GET":

        return render_template("login.html")
    else:
        if request.form["user"] == "admin" and request.form["pass"] == "admin":

            return redirect("/add")
        return render_template("login.html", custom_css="signin")


@ app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == "GET":

        return render_template("Add.html", title="ADD TODO")

    else:
        # Here add appe
        try:
            image = request.files['iimg']
            image.save(os.path.join(
                app.config["IMAGE_UPLOADS"], image.filename))
            itemtodo = Todoo(request.form["ititle"],
                             image.filename, request.form["idis"])
            if itemtodo.valide():
                datatodo.append(itemtodo)
        except Exception as e:
            print(e)
        return redirect("/")


if __name__ == '__main__':
# Run the appe
    app.run(debug=True, port=9001)
