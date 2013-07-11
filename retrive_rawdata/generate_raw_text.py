#! /usr/bin/python
# -*- coding:utf-8 -*-

__autohor__='Kensuke Mitsuzawa';
__version__='2013/7/11';
import codecs, sys, os;
from xml.etree import ElementTree;
def parse_and_get_text(file_path):
    extracted_list=[];
    xmltree=ElementTree.parse(file_path);
    persian_sentences=xmltree.findall(u'//ペルシア語文');
    for persian_sent in persian_sentences:
        #print persian_sent.text;
        #TODO なぜだかわからないけど，NONEが返されている．xmlのエラーかもわからないので，ファイルをチェックしてみること   
        if persian_sent.text==None:
            pass;
        else:
            extracted_list.append(persian_sent.text);
    extracted_document=''.join(extracted_list);
    return extracted_document;
def get_recursive_list(directory_path):
    if directory_path[-1]!='/':
        directory_path=directory_path+'/';
    recursive_list=[];
    for root, dir_name, files in os.walk(directory_path):
        for _file_ in files:
            recursive_list.append(root+','+_file_);
    return recursive_list;
def main():
    if len(sys.argv)==4:
        if sys.argv[1]=='-r':
            recursive_list=get_recursive_list(sys.argv[2]);
            #os.mkdir(sys.argv[3]);
            for item_in_list in recursive_list:
                root, file_=item_in_list.split(',');
                file_path=root+file_;
                extracted_document=parse_and_get_text(file_path);
                write_out=codecs.open(sys.argv[3]+file_, 'w', 'utf-8');
                write_out.write(extracted_document);
                write_out.close();
                print '{} is completed'.format(sys.argv[3]+file_);
    elif len(sys.argv)==3: 
            write_out=codecs.open(sys.argv[2], 'w', 'utf-8');
            extracted_document=parse_and_get_text(sys.argv[1]);
            write_out.write(extracted_document);
            write_out.close();
    else:
        sys.exit('usage: python generate_raw_text.py');
    


if __name__=='__main__':
    main();
    """
    #file_path=sys.argv[1];
    file_path='e1998t0001.xml';
    extracted_document=parse_and_get_text(file_path);
    print extracted_document
    """
