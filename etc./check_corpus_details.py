#! /usr/bin/python
# -*- coding:utf-8 -*-

import sys, codecs, os;

def split_sentence(sentence_number, document):
    lines=document.split(u'.');
    sentence_number=sentence_number+len(lines);
    return sentence_number, lines;

def count_up_words(sentence, word_number):
    for line in sentence:
        words=line.split();
        word_number=word_number+len(words);
    return word_number;

def get_recursive_list(directory_path):
    if directory_path[-1]!='/':
        directory_path=directory_path+'/';
    recursive_list=[];
    for root, dir_name, files in os.walk(directory_path):
        for _file_ in files:
            recursive_list.append(root+'/'+_file_);
    return recursive_list;

def main():
    sentence_number=0;
    word_number=0;
    recursive_list=get_recursive_list(sys.argv[1]);
    for path_to_file in recursive_list:
        file_lines=codecs.open(path_to_file, 'r', 'utf-8').read();
        sentence_number, lines=split_sentence(sentence_number, file_lines);
        word_number=count_up_words(lines, word_number);
    document_number=len(recursive_list);
    print 'The number of documents is {}'.format(document_number);
    print 'The number of sentences is {}'.format(sentence_number);
    print 'The number of words(Not token number) is {}'.format(word_number);

if __name__=='__main__':
    main();



