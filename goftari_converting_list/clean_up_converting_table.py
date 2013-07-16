#! /usr/bin/python
# -*- coding:utf-8
"""
Description: This script is for clean up Persian colloquial table, and write out cleaned list. Finally this script normalize the output table with virastar module.
Usage: Python clean_up_converting_table.py converting_table_path write_out_path
"""

import sys, codecs, commands;

def insert_dummy(items):
    #itemsとは，リストに格納された状態の単語の集合のこと（１行あたり）
    #この処理は実はlambda式でも書けるけど....
    returing_list=[];
    for item in items:
        dummy_inserted=u'<dummy> '+item+u' </dummy>'
        returing_list.append(dummy_inserted);
    return returing_list;

def tab_split(line):
    items=line.strip(u'\n').split(u'\t');
    items=insert_dummy(items);
    input_persian=items[2]; normal_persian1=items[3]; normal_persian2=items[5];
    normal_persian3=items[7]; normal_persian4=items[9];
    output_format=input_persian+u'\t'+normal_persian1+u'\t'+normal_persian2+u'\t'+normal_persian3+u'\t'+normal_persian4+u'\n';
    return output_format;

def tab_split_get_only_surface(line):
    surface_word=line.strip(u'\n').split(u'\t')[2];
    surface_word=u'<dummy> '+surface_word+u' </dummy>'+u'\n';
    return surface_word;

def make_mapping_dic(output_format, conveting_map):
    map_key=output_format.split(u'\t')[0];
    if not map_key in conveting_map:
        conveting_map.setdefault(map_key, output_format);
    else: pass
    return conveting_map;
def write_out_dic(conveting_map):
    write_out_file=codecs.open('./tmp1', 'w', 'utf-8');
    for key_item in conveting_map:
        write_out_file.write(conveting_map[key_item]);
    write_out_file.close();

def call_virastar(input_path, output_path):
    status_tuple=commands.getstatusoutput('ruby1.8 ../lib/pre_per2.rb {0} > {1}'.format(input_path, output_path))
    if status_tuple[0]!=0:
        sys.exit(status_tuple);

def construct_converting_table(): 
    with codecs.open(sys.argv[1], 'r', 'utf-8') as input_lines:
        for i, line in enumerate(input_lines):
            if i == 0:
                pass
            elif i<4119:
                output_format=tab_split(line);
                conveting_map=make_mapping_dic(output_format, conveting_map);
            elif i==4119:
                print len(conveting_map);
                write_out_dic(conveting_map);
                call_virastar('./tmp1', sys.argv[2]);
                sys.exit('end');

def construct_surface_wordlist():
    #当初の目的は，「この変換表でいくつの単語が変換できるのか？」なので，その数を調べる為に，表層形のみをリストに書き出す
    surface_word_list=[];
    write_out_before_preper=codecs.open('./tmp1', 'w', 'utf-8');
    write_out_after_dummy_delete=codecs.open(sys.argv[3], 'w', 'utf-8');
    with codecs.open(sys.argv[2], 'r', 'utf-8') as input_lines:
        for i, line in enumerate(input_lines):
            if i == 0:
                pass
            elif i<4119:
                surface_word=tab_split_get_only_surface(line);
                surface_word_list.append(surface_word);
            #ここに終了条件．暫定的に今は4119行目で終了
            elif i==4119:
                break;

    surface_word_list=list(set(surface_word_list));
    for item in surface_word_list: write_out_before_preper.write(item);
    write_out_before_preper.close();
    call_virastar('./tmp1', './tmp2');
    #<dummy>を削除する処理
    with codecs.open('./tmp2', 'r', 'utf-8') as after_preper_lines:
        for line in after_preper_lines:
            line=line.strip(u'\n').strip(u'<dummy> ').strip(u' </dummy>');
            write_out_after_dummy_delete.write(line+u'\n');
    write_out_after_dummy_delete.close();


def main():
    if sys.argv[1]=='--list': 
        if len(sys.argv)==4:
            construct_surface_wordlist();
        else:
            sys.exit('usage: Python clean_up_converting_table.py --list input_path output_path');
if __name__=='__main__':
    main();
