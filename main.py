from datetime import datetime
from models import Book
from storage import add_book, get_all_books, delete_book
from stats import average_rating, author_statistics


def print_menu():
    print("\n" + "="*40)
    print("   ТРЕКЕР ПРОЧИТАННЫХ КНИГ")
    print("="*40)
    print("1. Добавить книгу")
    print("2. Показать все книги")
    print("3. Показать среднюю оценку")
    print("4. Статистика по авторам")
    print("5. Удалить книгу")
    print("6. Выход")
    print("="*40)


def add_book_handler():
    print("\nДобавление новой книги:")
    author = input("Автор: ").strip()
    title = input("Название: ").strip()
    
    while True:
        try:
            rating = int(input("Оценка (1-5): "))
            if 1 <= rating <= 5:
                break
            print("Оценка должна быть от 1 до 5!")
        except ValueError:
            print("Введите число!")
    
    read_date = input("Дата прочтения (YYYY-MM-DD) или Enter для сегодня: ").strip()
    if not read_date:
        read_date = datetime.now().strftime("%Y-%m-%d")
    
    book = Book(author=author, title=title, rating=rating, read_date=read_date)
    
    if add_book(book):
        print("Книга успешно добавлена!")
    else:
        print("Такая книга уже существует!")


def show_all_books():
    books = get_all_books()
    if not books:
        print("Библиотека пока пуста.")
        return
    
    print(f"\nВаша библиотека ({len(books)} книг):")
    for i, book in enumerate(books, 1):
        print(f"{i}. {book.title} — {book.author} ({book.rating}/5, {book.read_date})")


def show_average():
    avg = average_rating()
    print(f"\nСредняя оценка всех книг: {avg}")


def show_author_stats():
    stats = author_statistics()
    if not stats:
        print("Нет данных для статистики.")
        return
    
    print("\nСтатистика по авторам:")
    for author, data in sorted(stats.items()):
        print(f"• {author}: {data['books']} книг, средняя оценка {data['avg_rating']}")


def delete_book_handler():
    title = input("\nВведите название книги для удаления: ").strip()
    if delete_book(title):
        print("Книга удалена.")
    else:
        print("Книга с таким названием не найдена.")


def main():
    while True:
        print_menu()
        choice = input("Выберите действие (1-6): ").strip()
        
        if choice == "1":
            add_book_handler()
        elif choice == "2":
            show_all_books()
        elif choice == "3":
            show_average()
        elif choice == "4":
            show_author_stats()
        elif choice == "5":
            delete_book_handler()
        elif choice == "6":
            print("До свидания! 👋")
            break
        else:
            print("Неверный выбор. Попробуйте ещё раз.")


if __name__ == "__main__":
    main()
