#! /usr/bin/python
# -*- coding:utf-8 -*-

import sys, codecs;
import post_processing_of_preper as post_preper;

def exception_of_splited_num_is_more_than(splited_bijankhan_line):
    semispace_concatenated=u'';
    del splited_bijankhan_line[-1];
    for item in splited_bijankhan_line: semispace_concatenated=semispace_concatenated+item+u'\u200C';
    semispace_concatenated=semispace_concatenated.strip(u'\u200C');
    return semispace_concatenated;
def split_bijankhan_and_add_to_list(bijankhan_lines, bijankhan_exception_list):
    """
    OUTLINE:this function checks normalization errors of preper.rb
    DESCRIPTION:preper.rb normalizes the un-defined persian writing style. But some exceptions occure in normalization. This function checks such normalization errors. After process of preper.rb, Bijankhan dataset is following dataformat "word POS". Thus this function tries to split by white space. If preper.rb fails to normalize, a separation by white space is invalid. Thus, this function caches such exceptions. 
    """
    for bijankhan_line in bijankhan_lines:
        bijankhan_line=bijankhan_line.strip(u'\n');
        bijankhan_line=post_preper.normalize_line_by_regularexp(bijankhan_line);
        try:
            bijankhan_word, bijankhan_pos=bijankhan_line.split();
        except ValueError:
            if len(bijankhan_line.split())>2:
                correct_bijankhan_line=exception_of_splited_num_is_more_than(bijankhan_line.split());
            elif len(bijankhan_line.split())==1:
                pass
            else:
                sys.exit('[Error] exception not expected happends\n{0}\n{1}'.format(bijankhan_line.encode('utf-8'), bijankhan_line.split() ));
            items=bijankhan_line.split()
            del items[-1]
            bijankhan_line_without_POS=''.join(items);
            write_out_format='{0}\t{1}'.format(bijankhan_line_without_POS.encode('utf-8'), correct_bijankhan_line.encode('utf-8'))
            if not write_out_format in bijankhan_exception_list: bijankhan_exception_list.append(write_out_format);
            else: pass
    return bijankhan_exception_list;
def construct_POS_tarining(bijankhan_lines, bijankhan_POS_set):
    """
    Construct POS training file.
    This function constructs tarining file that word and POS is separated by tab. An original bijankhan corpus format is that word is concatenated by white space. Thus, this function converts from white space concatenation to semi-space(ZWNJ) concatenation.
    """
    for bijankhan_line in bijankhan_lines:
        bijankhan_line=bijankhan_line.strip(u'\n');
        bijankhan_line=post_preper.normalize_line_by_regularexp(bijankhan_line);
        try:
            bijankhan_word, bijankhan_pos=bijankhan_line.split();
            write_out_format='{0}\t{1}'.format(bijankhan_word.encode('utf-8'), bijankhan_pos.encode('utf-8'));
            bijankhan_POS_set.append(write_out_format);
        except ValueError:
            if len(bijankhan_line.split())>2:
                correct_bijankhan_line=exception_of_splited_num_is_more_than(bijankhan_line.split());
            elif len(bijankhan_line.split())==1:
                #なんか，DELMだけの行があったような気がするので，要チェック
                print bijankhan_line
            else:
                sys.exit('[Error] exception not expected happends\n{0}\n{1}'.format(bijankhan_line.encode('utf-8'), bijankhan_line.split() ));
            items=bijankhan_line.split()
            POS_element=items.pop(-1)
            bijankhan_line_without_POS=''.join(items);
            write_out_format='{0}\t{1}'.format(bijankhan_line_without_POS.encode('utf-8'), POS_element.encode('utf-8'));
            bijankhan_POS_set.append(write_out_format);
    return bijankhan_POS_set;
def main():
    if len(sys.argv)<2 or sys.argv[1]=='--help':
        print 'How to use:';
        print 'python check_normalize_error_in_preper.py inputFile outputfile';
        print 'To make training file';
        print 'python check_normalize_error_in_preper.py -t inputFile outpath';
    elif sys.argv[1]=='-t':
        bijankhan_lines=codecs.open(sys.argv[2], 'r', 'utf-8').readlines();
        write_out=codecs.open(sys.argv[3], 'w', 'utf-8');
        bijankhan_POS_set=[];
        bijankhan_POS_set=construct_POS_tarining(bijankhan_lines, bijankhan_POS_set);
        for item in bijankhan_POS_set:
            write_out.write(item.decode('utf-8')+'\n');
        write_out.close()
    else:
        bijankhan_exception_list=[];
        bijankhan_lines=codecs.open(sys.argv[1], 'r', 'utf-8').readlines();
        write_out_path=codecs.open(sys.argv[2], 'w', 'utf-8');
        bijankhan_exception_list=split_bijankhan_and_add_to_list(bijankhan_lines, bijankhan_exception_list);
        for item in bijankhan_exception_list:
            write_out_path.write(item.decode('utf-8')+'\n');
        write_out_path.close()
if __name__=='__main__':
    main();
