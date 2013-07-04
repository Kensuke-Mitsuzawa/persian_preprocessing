#! /usr/bin/python

# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="kensuke-mi"
__date__ ="$2013/07/04 20:39:25$"
#! /usr/bin/python
# -*- coding:utf-8 -*-


import sys, codecs;

def construct_convertion_map_from_bijankhan_list(bijankhan_normalization_list, original_normalized_map):
    for line in bijankhan_normalization_list:
        if line[0]==u'#': pass
        else:
            original_word, normalized_word=line.split(u'\t');
            original_normalized_map.setdefault(original_word, normalized_word);
    return original_normalized_map;
def main():
    if len(sys.argv)<3 or sys.argv[1]=='--help':
        print 'usage: python normalize_by_bijhankhan_list.py un-normalized-document bijankhan-normalization-list outpath-of-normalized-document\n';
    else:
        un_normalized_document=codecs.open(sys.argv[1], 'r', 'utf-8').readlines();
        bijankhan_normalization_list=codecs.open(sys.argv[2], 'r', 'utf-8').readlines();
        normalized_document=codecs.open(sys.sys.argv[3], 'w', 'utf-8');
    original_normalized_map={};
    original_normalized_map=construct_convertion_map_from_bijankhan_list(bijankhan_normalization_list, original_normalized_map);

if __name__=='__main__':
    main()
