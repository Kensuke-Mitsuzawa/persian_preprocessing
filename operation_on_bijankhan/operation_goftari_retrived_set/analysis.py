#! /usr/bin/python
# -*- coding:utf-8 -*-

__author__='Kensuke Mitsuzawa'
__version__='2013/7/14'

import sys, codecs, string;

def remove_marks(word):
    word=word.translate({
        ord(u',') : None,
        ord(u'.') : None,
        ord(u'(') : None,
        ord(u')') : None,
        ord(u'[') : None,
        ord(u']') : None,
        ord(u'،') : None
    })
    return word;
def main():
    if len(sys.argv)==3:
        filtered_out_set=[];
        num_of_original_element=0;
        input_lines=codecs.open(sys.argv[1], 'r', 'utf-8').readlines();
        write_out=codecs.open(sys.argv[2], 'w', 'utf-8');
        print 'The number of original element is', len(input_lines);
        for line in input_lines:
            line=remove_marks(line);
            if not line in input_lines:
                filtered_out_set.append(line);
        print 'Before converting to set', len(filtered_out_set);
        filtered_out_set=list(set(filtered_out_set));
        print 'After filtering out', len(filtered_out_set);
        for item in filtered_out_set: write_out.write(item);
    else:
        sys.exit('usage: ')

if __name__=='__main__':
    main();
