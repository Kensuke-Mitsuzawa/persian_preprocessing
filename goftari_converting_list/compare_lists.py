#! /usr/bin/python
# -*- coding:utf-8 -*-

import sys, codecs;
"""
先生からもらった変換表でどれだけの単語が変換できるのか？を調べるためだけに書いたスクリプト．
usage: python compare_two_sets.py folklore_corpusのtoken集合リスト もらった変換表のtoken集合のリスト
"""
def add_to_list(line, wordlist):
    word=line.strip(u'\n');
    wordlist.append(word);
    return wordlist;

def make_wordset(wordlist):
    wordset=list(set(wordlist));
    return wordset;

def compare_two_sets(wordset_1, wordset_2):
#wordset_1がもらってきたリスト，wordset_2がBijankhanでフィルタリングしたリストを想定
    for element_1 in wordset_1:
        if element_1 in wordset_2:
            #print '{} is matched'.format(element_1.encode('utf-8'));
            wordset_2.remove(element_1)
    return wordset_2;

def main():
    wordlist_from_bijankhan_filtered_list=[];
    with codecs.open(sys.argv[1], 'r', 'utf-8') as bijankhan_filtered_list:
        for line in bijankhan_filtered_list:
            wordlist_from_bijankhan_filtered_list=add_to_list(line, wordlist_from_bijankhan_filtered_list);
    wordset_from_bijankhan_filtered_list=make_wordset(wordlist_from_bijankhan_filtered_list);
    wordlist_from_converting_table=[];
    with codecs.open(sys.argv[2], 'r', 'utf-8') as entrylist_from_converting_table:
        for line in entrylist_from_converting_table:
            wordlist_from_converting_table=add_to_list(line, wordlist_from_converting_table);
    wordset_from_converting_table=make_wordset(wordlist_from_converting_table);
    print 'A size of converting table is {}'.format(len(wordset_from_converting_table));
    print 'Before filtering, the size of wordset folklore_corpus is {}'.format(len(wordset_from_bijankhan_filtered_list))
    wordset_from_bijankhan_filtered_list=compare_two_sets(wordset_from_converting_table, wordset_from_bijankhan_filtered_list);
    print 'After filtering, the size of wordset folklore_corpus is {}'.format(len(wordset_from_bijankhan_filtered_list))

    write_out=codecs.open(sys.argv[3], 'w', 'utf-8');
    for element in wordset_from_bijankhan_filtered_list:
        write_out.write(element+u'\n');
    write_out.close();
if __name__=='__main__':
    main();
