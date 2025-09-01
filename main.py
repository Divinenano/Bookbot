import sys

from stats import get_num_words, total_counter, chars_dict_to_sorted_list
if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    path = sys.argv[1]

counts = total_counter(path)
sorted_list = chars_dict_to_sorted_list(counts)
count = get_num_words(path)

print("============ BOOKBOT ============")
print(f"Analyzing book found at {path}...")
print("----------- Word Count ----------")
print(f"Found {count} total words")
print("--------- Character Count -------")
for item in sorted_list:
    print(f"{item['char']}: {item['num']}")
print("============= END ===============")
