#! /usr/bin/python
# -*- coding:utf-8 -*-
__author__='Kensuke Mitsuzawa'
__version__='2013/7/6'
import sys, codecs, re;

def delete_dummy(line):
        """
        This function deletes dummy tag and clean up disused white spaces. This function is assumed to use after a processe of pre_per2.rb script.
        Input format is string in unicode.
        Output format is string in unicode.
        """
        write_out_format=u'';
	try:
		line=line.strip(u'\n');
       		surface_word, POS=line.split(u'\t');
        	prefix_deleted=re.sub(ur'<dummy>\s?', ur'', surface_word);
        	suffix_deleted=prefix_deleted.replace(u'</dummy>', u'').strip();
        	write_out_format=suffix_deleted+u'\t'+POS+u'\n';
        	return write_out_format;
	except:
		print [line];
def main():
        if len(sys.argv)==3:
                write_out=codecs.open(sys.argv[2], 'w', 'utf-8');
                with codecs.open(sys.argv[1], 'r', 'utf-8') as input_document:
                        for index_num, line in enumerate(input_document): 
                                write_out_format=delete_dummy(line);
                                write_out.write(write_out_format);
                write_out.close();
        else:
                sys.exit('Usage: python delete_dummy.py input_file output_file');       

if __name__=='__main__':
        main();
