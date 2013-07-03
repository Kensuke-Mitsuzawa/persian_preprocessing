#! /usr/bin/python
# -*- coding:utf-8 -*-

import sys, codecs;
import post_processing_of_preper as post_preper;

def exception_of_splited_num_is_3(splited_bijankhan_line):
    semispace_concatenated=(splited_bijankhan_line[0]+u'\u200C'+splited_bijankhan_line[1]);
    return semispace_concatenated;
def exception_of_splited_num_is_4(splited_bijankhan_line):
    semispace_concatenated=(splited_bijankhan_line[0]+u'\u200C'+splited_bijankhan_line[1]+u'\u200C'+splited_bijankhan_line[2]);
    return semispace_concatenated;
def split_bijankhan_and_add_to_list(bijankhan_lines, bijankhan_wordset):
    """
    OUTLINE:this function constructs wordset from bijankhan corpus
    DESCRIPTION:In the bijankhan corpus, each data is tab separated cf."word\tPOS". Thus, this function split each line by '\t'. Sometimes the number of elements in the splited list is more than 2. This is because words in bijankhan corpus is concatenated by normal space. In that case, this code copes with other functions 'exception_of_aplited_num_is_*'. These functions concatenate prefix and stem and suffix by semi-space(ZWNJ).
    """
    for bijankhan_line in bijankhan_lines:
        bijankhan_line=post_preper.normalize_line_by_regularexp(bijankhan_line);
        if len(bijankhan_line.split())==3:
            bijankhan_word=exception_of_splited_num_is_3(bijankhan_line.split());
        elif len(bijankhan_line.split())==4:
            bijankhan_word=exception_of_splited_num_is_4(bijankhan_line.split());
        else:
            bijankhan_word, bijankhan_pos=bijankhan_line.split();
        if not bijankhan_word in bijankhan_wordset:
            bijankhan_wordset.append(bijankhan_word);
        else: pass
    return bijankhan_wordset;
def split_folklore_and_add_to_list(folklore_lines, folklore_wordset):
    for folklore_line in folklore_lines:
        items=(folklore_line.strip(u'\n').rstrip(u'.')).split()
        for folklore_word in items:
            folklore_wordset.append(folklore_word);
    return folklore_wordset;
def compare_wordset_of_bijankhan_and_folklore(bijankhan_wordset, folklore_wordset):
    for bijankhan_word in bijankhan_wordset:
        if bijankhan_word in folklore_wordset:
            folklore_wordset.remove(bijankhan_word);
        else: pass#print '{0} is not in the list\n'.format(bijankhan_word.encode('utf-8'));
    return folklore_wordset;
def main():
    bijankhan_wordset=[];
    folklore_wordset=[];
    bijankhan_lines=codecs.open(sys.argv[1], 'r', 'utf-8').readlines();
    #folklore_lines=codecs.open(sys.argv[2], 'r', 'utf-8').readlines();
    bijankhan_wordset=split_bijankhan_and_add_to_list(bijankhan_lines, bijankhan_wordset);
    #folklore_wordset=split_folklore_and_add_to_list(folklore_lines, folklore_wordset);
    #for folklore_word in folklore_wordset:
    #    print folklore_word;
    #compare_wordset_of_bijankhan_and_folklore(bijankhan_wordset, folklore_wordset);

if __name__=='__main__':
    main();



