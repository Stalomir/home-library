from flask import Flask, request, redirect, render_template, url_for
from forms import BookForm
from models import books
app = Flask(__name__)
app.config["SECRET_KEY"] = "nininini"

@app.route("/books/", methods = ["GET", "POST"])
def books_library():
    form = BookForm()
    error = ""
    if request.method == "POST":
        data = request.form
        if form.validate_on_submit() and request.form['action']=='Dodaj':
            books.create(form.data)
            books.save_all()
        if request.form['action']=='Sort':
            label = data.get('label') 
            books.sort(label)
        return redirect(url_for("books_library"))
    return render_template("books.html", form=form, books=books.all(), error=error)

@app.route("/books/<int:book_id>/", methods=["GET","POST"])
def book_details(book_id):
    book = books.get(book_id - 1)
    form = BookForm(data=book)
    
    if request.method == "POST":
        if form.validate_on_submit():  
            books.update(book_id - 1, form.data)
        if request.form['action']=='Remove':
            books.remove(book_id - 1, form.data)
        return redirect(url_for("books_library"))
    return render_template("book.html", form=form, book_id=book_id)

if __name__=="__main__":
    app.run(debug=True)

