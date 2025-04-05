from stats import count_words
from stats import get_book_characters
from stats import sort_dict
from stats import get_book_text
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book=sys.argv[1]
        a = get_book_text(book)
        b = count_words(a)
        c = get_book_characters(book)
        d = sort_dict(c)
        #print (f"Found {b} total words")
        #print (d)
        print(f"""============ BOOKBOT ============
Analyzing book found at {book}...
----------- Word Count ----------
Found {b} total words
--------- Character Count -------
{d}""")

main()