#! /usr/bin/python

# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="kensuke-mi"
__date__ ="$2013/07/04 20:39:25$"
import sys, codecs;

def construct_map(exception_list_lines):
    pass
    

def main():
    unnormalized_document_lines=codecs.open(sys.argv[1], 'r', 'utf-8').readlines();
    exception_list_lines=codecs.open(sys.argv[2], 'r', 'utf-8').readlines();
    write_out=codecs.open(sys.argv[3], 'r', 'utf-8').readlines();
    

if __name__ == "__main__":
    print "Hello World";
