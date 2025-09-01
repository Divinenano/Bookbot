from stats import get_num_words, total_counter, chars_dict_to_sorted_list

path = "books/frankenstein.txt"

counts = total_counter(path)
sorted_list = chars_dict_to_sorted_list(counts)
count = get_num_words(path)

print("============ BOOKBOT ============")
print("Analyzing book found at books/frankenstein.txt...")
print("----------- Word Count ----------")
print(f"Found {count} total words")
print("--------- Character Count -------")
for item in sorted_list:
    print(f"{item['char']}: {item['num']}")
print("============= END ===============")

