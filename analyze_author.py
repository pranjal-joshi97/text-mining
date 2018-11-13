import random
import string

def process_file(filename, skip_header):
    """Makes a histogram that contains the words from a file.
    filename: string
    skip_header: boolean, whether to skip the header
    returns: map from each word to the number of times it appears.
    """
    hist = {}
    fp = open(filename, encoding="utf8")

    if skip_header:
        skip_the_header(fp)

    for line in fp:
        if line.startswith('*** END OF THIS PROJECT'):
            break

        strippable = string.punctuation + string.whitespace

        for word in line.split():
                word = word.strip(strippable)
                word = word.lower()

                hist[word] = hist.get(word, 0) + 1

    return hist


def skip_the_header(fp):
    """Reads from fp until it finds the line that ends the header.
    fp: open file object
    """
    for line in fp:
        if line.startswith('*** START OF THIS PROJECT'):
            break


def most_common_words_in_book(hist, excluding_stopwords=True):
    """Makes a list of word-freq pairs in descending order of frequency.
    hist: map from word to frequency
    returns: list of (frequency, word) pairs
    """
    wordList = []

    stopwords = process_file('stopwords.txt', False)
    stopwords = list(stopwords.keys())

    for word, freq in hist.items():
        if excluding_stopwords:
            if word in stopwords:
                continue
        wordList.append((freq, word))

    wordList.sort(reverse=True)

    return wordList


def print_most_common_words_in_book(wordList, num=10):
    """Prints the most commons words in a wordList and their frequencies.
    wordList: list of words and frequencies
    num: number of words to print
    """
    for pair in wordList[0:num]:
        print(pair)


def appearIn(d1, d2):
    """Returns a dictionary with all keys in d1 that appear in d2.
    d1, d2: dictionaries
    """
    sameWords = {}
    for words in d1:
        if words in d2:
            sameWords[words] = d1[words]

    for key in sameWords.keys():
            print(key + ",", end =" ")


def main():
    maas = process_file('The_Mysterious_Affair_At_Styles.txt', skip_header=True)
    tsa = process_file('The_Secret_Adversary.txt', skip_header=True)
    # print(maas)
    # print(tsa)

    m = most_common_words_in_book(maas)
    t = most_common_words_in_book(tsa)

    print("The most common words in The Mysterious Affair At Styles are: ")
    str(print_most_common_words_in_book(m,10))
    print("\nThe most common words in The Secret Adversary are: ")
    str(print_most_common_words_in_book(t))

    print('\nThe following words appear in both books: ')
    appearIn(maas,tsa)

if __name__ == '__main__':
    main()
