# encoding:utf-8

"""
Author: liutongyang
Date: 2020-12-24 10:25:21
LastEditTime: 2020-12-24 11:14:25
Description: FAQ data loader
FilePath: /search_engines/FAQ-system-master/s.py
                               |~~~~~~~|
                               |       |
                               |       |
                               |       |
                               |       |
                               |       |
    |~.\\\_\~~~~~~~~~~~~~~xx~~~         ~~~~~~~~~~~~~~~~~~~~~/_//;~|
    |  \  o \_         ,XXXXX),                         _..-~ o /  |
    |    ~~\  ~-.     XXXXX`)))),                 _.--~~   .-~~~   |
     ~~~~~~~`\   ~\~~~XXX' _/ ';))     |~~~~~~..-~     _.-~ ~~~~~~~
              `\   ~~--`_\~\, ;;;\)__.---.~~~      _.-~
                ~-.       `:;;/;; \          _..-~~
                   ~-._      `''        /-~-~
                       `\              /  /
                         |         ,   | |
                          |  '        /  |
                           \/;          |
                            ;;          |
                            `;   .       |
                            |~~~-----.....|
                           | \             \
                          | /\~~--...__    |
                          (|  `\       __-\|
                          ||    \_   /~    |
                          |)     \~-'      |
                           |      | \      '
                           |      |  \    :
                            \     |  |    |
                             |    )  (    )
                              \  /;  /\  |
                              |    |/   |
                              |    |   |
                               \  .'  ||
                               |  |  | |
                               (  | |  |
                               |   \ \ |
                               || o `.)|
                               |`\\) |
                               |       |
                               |       |
"""

import re
import jieba


def filter_out_category(input):
    """
    clean data using regular expressions
    """
    new_input = re.sub('[\u4e00-\u9fa5]{2,5}\\/', '', input)
    return new_input


def filter_out_punctuation(input):
    """
    clean data using regular expressions
    """
    new_input = re.sub('([a-zA-Z0-9])', '', input)
    new_input = ''.join(e for e in new_input if e.isalnum())
    return new_input


def word_segmentation(input):
    """
    word segmentation using jieba
    """
    new_input = ','.join(jieba.cut(input))
    return new_input


class QueryData(object):
    """
    store query data
    """
    def __init__(self, file_path):
        """
        init function
        """
        self.query_list = list()
        self.read_corpus(file_path)
        self.query_data = self.main(self.query_list)

    def read_corpus(self, file_path):
        """
        load data
        """
        with open(file_path, 'r', encoding='utf8', errors='ignore') as f:
            lines = f.readlines()
            for i in lines:
                self.query_list.append(i)

    def main(self, data):
        """
        main function
        """
        pure_data = []
        for q in data:
            q = filter_out_category(q)
            q = filter_out_punctuation(q)
            q = word_segmentation(q)
            pure_data.append(q)
        return pure_data


class AnwserData(object):
    """
    store anwser data
    """
    def __init__(self, file_path):
        """
        init function
        """
        self.anwser_data = list()
        self.read_corpus(file_path)

    def read_corpus(self, file_path):
        """
        load data
        """
        with open(file_path, 'r', encoding='utf8', errors='ignore') as f:
            lines = f.readlines()
            for i in lines:
                self.anwser_data.append(i)


if __name__ == "__main__":
    query = QueryData('./query.txt')
    query_list = query.query_data

    anwser = AnwserData('./anwser.txt')
    anwser_list = anwser.anwser_data

    print('Example:')
    print('Question', query_list[1])
    print('Answer', anwser_list[1])