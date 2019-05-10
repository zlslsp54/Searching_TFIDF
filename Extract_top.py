from sklearn.metrics.pairwise import cosine_similarity
from operator import itemgetter

# extract top 5

def extract_top5(captions, clean_captions, tfidf_matrix):
    checked_similarity = []

    for i in range(len(clean_captions)):

        if cosine_similarity(tfidf_matrix[-1], tfidf_matrix[i]) != 0: # 이부분 없애고 나중에 다 저장 한 뒤에 제일 첫번째 즉 자신의 문장을 없애주자.(알고리즘 낭비) ?? 이부분 다시 한번 해보기.

            checked_similarity.append([captions[i], cosine_similarity(tfidf_matrix[-1], tfidf_matrix[i])])

    checked_similarity = sorted(checked_similarity, key=itemgetter(1), reverse=True)
    top_5 = checked_similarity[1:6]
    return top_5
