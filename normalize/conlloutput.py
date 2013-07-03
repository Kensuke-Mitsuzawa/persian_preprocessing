#! /usr/bin/python
# coding=utf8

#In the name of Allah
#   Copyright: © 2012 Supreme Council of Information and Communication Technology (SCICT) 

__author__="Mohammad Sadegh Rasooli <rasooli.ms@gmail.com>"
__date__ ="Nov, 2012"

import sys
import os
import codecs

sys.stdout = codecs.getwriter('utf8')(sys.stdout)


BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE = range(8)

#following from Python cookbook, #475186
def has_colours(stream):
    if not hasattr(stream, "isatty"):
        return False
    if not stream.isatty():
        return False # auto color only on TTYs
    try:
        import curses
        curses.setupterm()
        return curses.tigetnum("colors") > 2
    except:
        # guess false in case of error
        return False
has_colours = has_colours(sys.stdout)


def printout(text, colour=WHITE):
        if has_colours:
                seq = "\x1b[1;%dm" % (30+colour) + text + "\x1b[0m"
                sys.stdout.write(seq)
        else:
                sys.stdout.write(text)

if len(sys.argv)<2 or sys.argv[1]=='--help':
	printout( 'Copyright\n2012 Supreme Council of Information and Communication Technology (SCICT)\n',GREEN)
	print '___________________________________'
	printout('How to use: ',BLUE)
	printout('python conlloutput.py inputFile > outputfile\n',RED)
	print '___________________________________'

else:
	inputAddress=os.path.abspath(sys.argv[1])
	outputOpen=codecs.open(inputAddress, 'r',encoding='utf-8')

	readline=outputOpen.readline()

	while readline:
		readline=readline.strip()
		splitedText=readline.split('\t')
		outLine=''
		for i in range(0,len(splitedText)):
			splitedText[i]=splitedText[i].strip()
			if ' ' in splitedText[i]:
				splitedText[i]=splitedText[i].replace(' ','_')
			outLine+=splitedText[i]+'\t'
		outLine=outLine.strip()
		#.replace(' ','_')
		print outLine
		readline=outputOpen.readline()