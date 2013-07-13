#! /usr/bin/python
# -*- coding:utf-8 -*-

import sys, codecs, commands, subprocess;
from subprocess import Popen, PIPE;
import dummy, delete_dummy;

def main():
        out_of_dummy='./tmp_out_01';
        out_of_preper='./tmp_out_02';
        if len(sys.argv)!=3:
                sys.exit('Usage: preproc_of_bijankhan.py input_file output_file');
        else:
                write_out=codecs.open(out_of_dummy, 'w', 'utf-8');
                with codecs.open(sys.argv[1], 'r', 'utf-8') as input_document:
                        for index_num, line in enumerate(input_document):
                                write_out_format=dummy.insert_dummy(line);
                                write_out.write(write_out_format);
                write_out.close();
                status_tuple=commands.getstatusoutput('ruby1.8 ../lib/pre_per2.rb {0} > {1}'.format(out_of_dummy, out_of_preper));
                if status_tuple[0]!=0:
                        sys.exit(status_tuple);
                """
                file_of_out_of_preper=codecs.open(out_of_preper, 'w', 'utf-8');
                normalize_sequence=subprocess.Popen( ['ruby1.9', '../lib/pre_per2.rb', out_of_dummy], stdout=PIPE);
                for line in normalize_sequence.stdout: file_of_out_of_preper.write(line.decode('utf-8'));
                """
                system_out=codecs.open(sys.argv[2], 'w', 'utf-8');
                with codecs.open(out_of_preper, 'r', 'utf-8') as after_preper:
                        for line in after_preper:
                                write_out_format=delete_dummy.delete_dummy(line);
                                system_out.write(write_out_format);
                system_out.close();
                commands.getoutput('rm {0} {1}'.format(out_of_dummy, out_of_preper));
if __name__=='__main__':
        main();
