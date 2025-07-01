from utils.bible_processor import read_parquet_bible

# Example usage of the Parquet reader
if __name__ == "__main__":
    # Path to a sample Parquet file
    sample_file_path = "bible_data/parquet_bible_translations/English_Standard_Version_2001_ESV.parquet"

    # Query for a specific book
    print("Querying for the book of Genesis:")
    genesis_data = read_parquet_bible(sample_file_path, book="Genesis")
    print(genesis_data[:5])  # Print the first 5 results

    # Query for a specific chapter
    print("\nQuerying for Genesis chapter 1:")
    genesis_chapter_1 = read_parquet_bible(sample_file_path, book="Genesis", chapter=1)
    print(genesis_chapter_1[:5])  # Print the first 5 results

    # Query for a specific verse
    print("\nQuerying for Genesis chapter 1, verse 1:")
    genesis_verse_1 = read_parquet_bible(sample_file_path, book="Genesis", chapter=1, verse=1)
    print(genesis_verse_1)
