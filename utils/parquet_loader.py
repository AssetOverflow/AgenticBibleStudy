from pyarrow import Table
import pyarrow.parquet as pq
from typing import Any
from .models import Bible, Book, Chapter, Verse
from .utils import ensure_pyarrow_available

def load_bible_from_parquet(file_path: str, translation: str) -> Bible:
    """
    Loads a Bible from a Parquet file and organizes it into structured dataclasses.

    Args:
        file_path (str): Path to the Parquet file.
        translation (str): Name of the Bible translation.

    Returns:
        Bible: A Bible object containing books, chapters, and verses.
    """
    ensure_pyarrow_available()

    # Read the Parquet file
    table: Table = pq.read_table(file_path)
    df = table.to_pandas()

    # Group data into structured objects
    books = {}
    for _, row in df.iterrows():
        book_name = row['book']
        chapter_number = row['chapter']
        verse_number = row['verse']
        verse_text = row['text']

        if book_name not in books:
            books[book_name] = Book(name=book_name)

        book = books[book_name]
        if not book[chapter_number]:
            book.chapters.append(Chapter(number=chapter_number))

        chapter = book[chapter_number]
        chapter.verses.append(Verse(number=verse_number, text=verse_text))

    return Bible(translation=translation, books=list(books.values()))
