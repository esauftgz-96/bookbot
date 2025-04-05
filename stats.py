def count_words(rawtext):
    x = rawtext.split()
    return len(x)

def get_book_characters(filepath):
    with open(filepath) as f:
        file_contents=f.read()
    step1 = file_contents.lower()
    step2 = {}
    for chr in step1:
        if chr.isalpha():
            if chr not in step2:
                step2[chr] = 1
            else:
                step2[chr] += 1
    return step2

def sort_dict(dict):
    sorted_d = {k: v for k, v in sorted(dict.items(), key=lambda x: x[1],reverse=True)}
    sorted_d_a = ""
    for chr in sorted_d:
        sorted_d_a += f"{chr}"+": "+f"{sorted_d.get(chr)}"+"\n"
    return sorted_d_a

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents=f.read()
    return file_contents