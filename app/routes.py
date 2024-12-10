from flask import render_template, request, redirect, url_for, flash


def init_routes(app):
    from . import db
    from .models import Book

    @app.route("/")
    def index():
        books = Book.query.all()
        return render_template("index.html", books=books)
    
    @app.route("/add", methods=["GET", "POST"])
    def add_book():
        if request.method == "POST":
            title = request.form.get("title")
            author = request.form.get("author")
            published_date = request.form.get("published_date")
            genre = request.form.get("genre")

            new_book = Book(title=title, author=author, 
                        published_date=published_date,
                        genre=genre)
            db.session.add(new_book)
            db.session.commit()
            flash("Book added successfully", "success")
            return redirect(url_for("index"))
        
        return render_template("add_book.html")

    @app.route("/delete/<int:book_id>")
    def delete_book(book_id):
        book = Book.query.get_or_404(book_id)
        db.session.delete(book)
        db.session.commit()
        flash("Book deleted successfully", "danger")
        return redirect(url_for("index"))

