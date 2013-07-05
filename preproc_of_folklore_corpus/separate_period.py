#! /usr/bin/python
# -*- coding:utf-8 -*-
__author__=="Kensuke Mitsuzawa"
__version__=="2013/7/6"

import sys, codecs;

def separate_period(sentence):
        """
        This function separates period(dot) from sentence that its period is adhere to last word.The character format of input sentece must be unicode.
        """
	sentence=sentence.replace(u'.', u' .');
	return sentence;

if __name__=='__main__':
        if len(sys.argv)==3:
                input_lines=codecs.open(sys.argv[1], 'r', 'utf8').readlines();
		output_lines=codecs.open(sys.argv[2], 'w', 'utf8');
		for line in input_lines:
			separated_line=separate_period(line);
			output_lines.write(separated_line);
		output_lines.close();	
	else:
		sys.exit('usage: python separate_period.py input_file output_file');	
