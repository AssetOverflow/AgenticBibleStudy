from dataclasses import dataclass, field
from typing import List, Optional

@dataclass
class Verse:
    number: int
    text: str

    def __str__(self):
        return f"{self.number}: {self.text}"

@dataclass
class Chapter:
    number: int
    verses: List[Verse] = field(default_factory=list)

    def __getitem__(self, verse_number: int) -> Optional[Verse]:
        for verse in self.verses:
            if verse.number == verse_number:
                return verse
        return None

    def __str__(self):
        return f"Chapter {self.number} with {len(self.verses)} verses"

@dataclass
class Book:
    name: str
    chapters: List[Chapter] = field(default_factory=list)

    def __getitem__(self, chapter_number: int) -> Optional[Chapter]:
        for chapter in self.chapters:
            if chapter.number == chapter_number:
                return chapter
        return None

    def __str__(self):
        return f"Book of {self.name} with {len(self.chapters)} chapters"

@dataclass
class Bible:
    translation: str
    books: List[Book] = field(default_factory=list)

    def get_book(self, book_name: str) -> Optional[Book]:
        for book in self.books:
            if book.name == book_name:
                return book
        return None

    def __str__(self):
        return f"{self.translation} Bible with {len(self.books)} books"
