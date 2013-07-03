#! /usr/bin/python

import sys, re;

def normalize_line_by_regularexp(input_line):
        if re.findall(r'!\s.+!', input_line):
                input_line=input_line.rstrip(u'!').replace(u'!', '');
        
	return input_line;

