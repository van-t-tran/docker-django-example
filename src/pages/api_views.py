from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Book


@api_view(["GET"])
def api_home(request):
    author_name = request.query_params.get("author", "")
    query = "SELECT * FROM pages_book WHERE author like %s"
    books = Book.objects.raw(query, [author_name])

    # Convert raw query results to a list of dictionaries
    books_list = [
        {"id": book.id, "title": book.title, "author": book.author, "published_date": book.published_date}
        for book in books
    ]
    return Response({"books": books_list})