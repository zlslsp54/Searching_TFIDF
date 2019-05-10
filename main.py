# from nltk.corpus import stopwords
# from nltk.tokenize import word_tokenize, sent_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from PreProcessing import preprocessing
from Get_data import get_data
from Extract_top import extract_top5

input_sentence = input('Input sentence: ') # 입력값 소문자로.

captions = get_data('localhost', 'root', '111111', db='youtube')
captions.append(input_sentence)

clean_captions = preprocessing(captions)

tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform(clean_captions)

# extract top 5

top_5 = extract_top5(captions, clean_captions, tfidf_matrix)

for i in range(len(top_5)):
    print("\n" + str(i+1) + ". " + top_5[i][0] + " | similarity: " + str(top_5[i][1][0][0]))
