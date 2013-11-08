#! /usr/bin/python
#-*- coding:utf-8 -*-

import codecs, sys;

lines_list=[];
file_out=codecs.open('goftari_converting_table_no_duplication', 'w', 'utf-8');
with codecs.open('folklore_goftari_converting_table_roman.tsv', 'r', 'utf-8') as input_lines:
    for i, line in enumerate(input_lines):
        line=line.strip(u'\n').strip(u'\t');
        items=line.split(u'\t');
        #4120行目からはゴミファイルなので
        if i==4119:
            break;
        else:
            items=items[2:];
            goftari_neveshtari=u'\t'.join(items);
            lines_list.append(goftari_neveshtari);
lines_set=list(set(lines_list));

for line in lines_set:
    file_out.write(line+u'\n');
file_out.close();

