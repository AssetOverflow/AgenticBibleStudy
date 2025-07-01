from utils.models import Bible
from utils.parquet_loader import load_bible_from_parquet

# Example script to load and test Bible data from Parquet files
def main():
    # Paths to sample Parquet files
    translations = {
        "ESV": "bible_data/parquet_bible_translations/English_Standard_Version_2001_ESV.parquet",
        "KJV": "bible_data/parquet_bible_translations/King_James_Version_1611_1769_KJV.parquet",
    }

    bibles = {}

    # Load each translation into a Bible object
    for translation, file_path in translations.items():
        print(f"Loading {translation} Bible from {file_path}...")
        bibles[translation] = load_bible_from_parquet(file_path, translation)

    # Test capabilities
    for translation, bible in bibles.items():
        print(f"\nTesting {translation} Bible:")
        print(bible)

        # Get a specific book
        genesis = bible.get_book("Genesis")
        if genesis:
            print(f"\nBook: {genesis}")

            # Get a specific chapter
            chapter_1 = genesis[1]
            if chapter_1:
                print(f"\n{chapter_1}")

                # Get a specific verse
                verse_1 = chapter_1[1]
                if verse_1:
                    print(f"\nVerse 1: {verse_1}")

    # Directly test Bible object methods
    for translation, bible in bibles.items():
        print(f"\nDirectly testing {translation} Bible object:")

        # List all books in the Bible
        print(f"Books in {translation} Bible:")
        for book in bible.books:
            print(f"- {book.name}")

        # Access a specific book and its chapters
        genesis = bible.get_book("Genesis")
        if genesis:
            print(f"\nAccessing Genesis in {translation} Bible:")
            print(genesis)

            # Access chapters in Genesis
            for chapter in genesis.chapters[:3]:  # Limit to first 3 chapters for brevity
                print(f"\n{chapter}")

                # Access verses in the chapter
                for verse in chapter.verses[:5]:  # Limit to first 5 verses for brevity
                    print(verse)

if __name__ == "__main__":
    main()
