def main():
    path_to_file = 'books/frankenstein.txt'
    
    for line in create_char_report(path_to_file):
        print(line)


def count_letters(path):
    letters = {}
    with open(path) as f:
        text = f.read()
        words = text.split()
    for word in words:
        for w in word:
            if w.lower() in letters:
                letters[w.lower()] += 1
            else:
                letters[w.lower()] = 1
    return letters

def create_char_report(path):
    letter_count_list = count_letters(path)
    report = []
    report.append(f"--- Begin report of {path} ---")
    report.append(f"{get_num_words(path)} words found in the document")
    report. append("")
    for letter in letter_count_list:
        report.append(f"The '{letter}' character was found {letter_count_list[letter]} times")
    return report

def get_book_text(path):
    with open(path) as f:
        return f.read()
def get_num_words(path):
    with open(path) as f:
        text = f.read()
        words = text.split()
    return len(words)

main()