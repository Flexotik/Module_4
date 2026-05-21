from models import Book
from storage import get_all_books
from collections import defaultdict


def average_rating() -> float:
    books = get_all_books()
    if not books:
        return 0.0
    return round(sum(b.rating for b in books) / len(books), 2)


def author_statistics() -> dict:
    books = get_all_books()
    stats = defaultdict(lambda: {"count": 0, "total_rating": 0})
    
    for book in books:
        stats[book.author]["count"] += 1
        stats[book.author]["total_rating"] += book.rating
    
    result = {}
    for author, data in stats.items():
        result[author] = {
            "books": data["count"],
            "avg_rating": round(data["total_rating"] / data["count"], 2)
        }
    return result
