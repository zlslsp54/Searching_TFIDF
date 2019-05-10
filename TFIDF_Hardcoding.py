import nltk
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
import math
# nltk.download('punkt')

text1 = '''
If you like tuna and tomato sauce- try combinaning the two.
It's really not as bad as it sounds.
If the Easter Bunny and the Tooth Fairy had babies would they take
your teeth and leave chocolate for you?
'''

# preprocessing
def remove_string_special_characters(s):
    '''
    This function removes special characters from within a string

    parameters:
        s(str): single input string.

    return:
        stripped(str): A string with special characters removed
    '''

    # Replace special character with ' '
    stripped = re.sub('[^\w\s]', '', s)
    stripped = re.sub('_', '', stripped) # ??

    # Change any withespace to one space
    stripped = re.sub('\s+', ' ', stripped)

    # Remove start and end's white space
    stripped = stripped.strip()

    return stripped

def count_words(sent):
    '''
    This function returns the
    total number of words in the input text.
    '''
    count = 0
    words = word_tokenize(sent)
    for word in words:
        count += 1
    return count

def get_doc(sents):
    '''
    this function splits the text into sentences and
    considering each sentence as a document,
    calculates the total word count of each
    '''
    doc_info = []
    i = 0
    for sent in sents:
        i += 1
        count = count_words(sent)
        temp = {'doc_id' : i, 'doc_length' : count}
        doc_info.append(temp)
    return doc_info

def create_freq_dict(sents):
    '''
    This function creates a frequency dictionary
    for each word in each document.
    '''
    i = 0
    freqDict_list = []
    for sent in sents:
        i += 1
        freq_dict = {}
        words = word_tokenize(sent)
        for word in words:
            word = word.lower()
            if word in freq_dict:
                freq_dict[word] += 1
            else:
                freq_dict[word] = 1
            temp = {'doc_id' : i, 'freq_dict' : freq_dict}
        freqDict_list.append(temp)
    return freqDict_list

def computeIDF(doc_info, freqDict_list):
    '''
    idf = ln(total number of docs / number of docs with term in it)
    '''
    IDF_scores = []
    counter = 0
    for dict in freqDict_list:
        counter += 1
        for k in dict['freq_dict'].keys():
            count = sum([k in tempDict['freq_dict'] for tempDict in freqDict_list])
            temp = {'doc_id' : counter, 'IDF_score' : math.log(len(doc_info)/count), 'key' : k}

            IDF_scores.append(temp)

    return IDF_scores

def computeTFIDF(TF_socres, IDF_scores):
    TFIDF_scores = []
    for j in IDF_scores:
        for i in TF_scores:
            if j['Key'] == i['key'] and j['doc_id'] == i['doc_id']:
                temp = {'doc_id' : j['doc_id'],
                       'TFIDF_scores' : j['IDF_score'] * i['TF_score'],
                       'key' : i['key']}
        TFIDF_scores.append(temp)
    return TFIDF_scores
