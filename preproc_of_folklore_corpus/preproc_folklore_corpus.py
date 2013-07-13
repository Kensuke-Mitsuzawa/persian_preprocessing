#! /usr/bin/python
# -*- coding:utf-8 -*-

import sys, codecs, commands, subprocess;
from subprocess import PIPE, Popen;
import separate_period;

def call_pre_per2(input_path, out_path):
        status_tuple=commands.getstatusoutput('ruby1.8 ../lib/pre_per2.rb {0} > {1}'.format(input_path, out_path));
        if status_tuple[0]!=0:
                sys.exit(status_tuple);
def main():
        if len(sys.argv)==3:
                tmp_1=codecs.open('./tmp1', 'w', 'utf-8');
                with codecs.open(sys.argv[1], 'r' , 'utf-8') as folklore:
                        for folklore_line in folklore:   
                                folklore_dot_separated=separate_period.separate_period(folklore_line);
                                tmp_1.write(folklore_dot_separated);

                        tmp_1.close();
                call_pre_per2('./tmp1', sys.argv[2]);
                commands.getstatusoutput('rm ./tmp1');
        else:
                sys.exit('usage: python preproc_folklore.2py input_file output_file');

if __name__=='__main__':
        main();

