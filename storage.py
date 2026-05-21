import json
import os
from models import Book

FILE_NAME = "books.json"

def load_books() -> list[Book]:
    if not os.path.exists(FILE_NAME):
        return []
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as f:
            data = json.load(f)
            return [Book.from_dict(book) for book in data]
    except Exception:
        return []


def save_books(books: list[Book]):
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump([book.to_dict() for book in books], f, ensure_ascii=False, indent=2)


def add_book(book: Book) -> bool:
    """Возвращает False, если книга уже существует (дубликат по автор + название)"""
    books = load_books()
    
    books.append(book)
    save_books(books)
    return True


def get_all_books() -> list[Book]:
    return load_books()


def delete_book(title: str) -> bool:
    books = load_books()
    original_len = len(books)
    
    books = [b for b in books if b.title.lower() != title.lower()]
    
    if len(books) < original_len:
        save_books(books)
        return True
    return False
