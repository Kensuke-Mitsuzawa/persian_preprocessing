#! /usr/bin/python
# -*- coding:utf-8 -*-
__author__='Kensuke Mitsuzawa'
__version__='2013/7/6'
import sys, codecs, re;

def insert_dummy(line):
        """
        This function inserts dummy tag prefix and suffix position of word column. This process is done because of the work of preper2.rb. The preper2.rb needs white spaces before and after words to regulalize word style.
        """
        after_splitted=re.split('\s{2,}', line);
        surface_word=after_splitted[0];POS=after_splitted[1];
        prefix_dummy_tag=u'<dummy>  ';
        suffix_dummy_tag=u'  </dummy>';
        dummied_word=prefix_dummy_tag+u''.join(surface_word)+suffix_dummy_tag;
        write_out_format=dummied_word+u'\t'+u''.join(POS);
        return write_out_format;
def main():
        if len(sys.argv)==3:
                write_out=codecs.open(sys.argv[2], 'w', 'utf-8');
                with codecs.open(sys.argv[1], 'r', 'utf-8') as input_document:
                        for index_num, line in enumerate(input_document): 
                                write_out_format=insert_dummy(line);
                                write_out.write(write_out_format);
                write_out.close();
        else:
                sys.exit('Usage: python dummy.py input_file output_file');
if __name__=='__main__':
        main();

