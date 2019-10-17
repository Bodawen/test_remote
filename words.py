import re,collections
def get_words(file,outputfile ="text.txt"):
    with open(outputfile) as of:
        with open (file) as f:
            words_box=[]
            for line in f:
                string = re.sub("[\s+\.\!\/,$%^*(+\"\']+".encode('utf-8').decode('utf-8')," " ,line)
                print(string)
                words_box.extend(string.strip().split())
    return collections.Counter(words_box)

a = get_words ('text.txt')
for key in a:
    print(key)