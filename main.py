'''
Author: liutongyang
Date: 2020-12-24 15:36:19
LastEditTime: 2020-12-29 10:09:23
Description: Retrieval Q & A System main function
FilePath: /search_engines/FAQ-system-master/main.py

　　┏┓　　　┏┓+ +
　┏┛┻━━━┛┻┓ + +
　┃　　　　　　　┃ 　
　┃　　　━　　　┃ ++ + + +
 ████━████ ┃+
　┃　　　　　　　┃ +
　┃　　　┻　　　┃
　┃　　　　　　　┃ + + 
　┗━┓　　　┏━┛
　　　┃　　　┃　　　　　　　　　　　
　　　┃　　　┃ + + + +
　　　┃　　　┃
　　　┃　　　┃ +  神兽保佑
　　　┃　　　┃    代码无bug　　
　　　┃　　　┃　　+　　　　　　　　　
　　　┃　 　　┗━━━┓ + +
　　　┃ 　　　　　　　┣┓
　　　┃ 　　　　　　　┏┛
　　　┗┓┓┏━┳┓┏┛ + + + +
　　　　┃┫┫　┃┫┫
　　　　┗┻┛　┗┻┛+ + + +

'''

import sys

from query_feature import conver2BOW
from query_feature import conver2tfidf
from similarity import idx_for_largest_cosine_sim
from data_layer.data_loader import QueryData
from data_layer.data_loader import AnwserData
from data_layer.data_loader import word_segmentation
from data_layer.data_loader import filter_out_category
from data_layer.data_loader import filter_out_punctuation


def answer_bow(input, bow_vectorizer, bow_X, answers):
    """
    bow model's anwser
    """
    input = filter_out_punctuation(input)
    input = word_segmentation(input)
    bow = bow_vectorizer.transform([input])
    best_idx = idx_for_largest_cosine_sim(bow, bow_X)
    return answers[best_idx]

def answer_tfidf(input, tfidf_vectorizer, tfidf_X, answers, questions):
    """
    tfidf model's anwser
    """
    input = filter_out_punctuation(input)
    input = word_segmentation(input)
    bow = tfidf_vectorizer.transform([input])
    best_idx = idx_for_largest_cosine_sim(bow, tfidf_X)
    return questions[best_idx], answers[best_idx]

if __name__ == "__main__":
    # loads questions data
    query = QueryData('./data_layer/query.txt')
    question_list = query.query_data

    # loads anwsers data
    anwser = AnwserData('./data_layer/anwser.txt')
    anwser_list = anwser.anwser_data
    
    pure_question = AnwserData('./data_layer/query.txt')
    pure_question_list = pure_question.anwser_data
    # extract bow feature
    bow_vectorizer, bow_X = conver2BOW(question_list)

    # extract tfidf feature
    tfidf_vectorizer, tfidf_X = conver2tfidf(question_list)
    
    print('请输入您的问题：')
    
    for input in sys.stdin:
        # BOW_result = answer_bow(input, bow_vectorizer, bow_X, anwser_list)
        tfidf_result_question, tfidf_result_anwser = answer_tfidf(input, tfidf_vectorizer, tfidf_X, anwser_list, pure_question_list)

        # print(BOW_result)
        print('最佳匹配问题：', tfidf_result_question.strip())
        print('最佳匹配回答：', tfidf_result_anwser.strip())
        print('\n')