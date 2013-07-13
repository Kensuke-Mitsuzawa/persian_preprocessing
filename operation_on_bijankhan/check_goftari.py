#! /usr/bin/python
# -*- coding:utf-8 -*-


import sys, codecs, commands, os;
import post_processing_of_preper as post_preper;
sys.path.append('../preproc_of_folklore_corpus');
sys.path.append('../preproc_of_bijankhan_posdataset');
import preproc_of_bijankhan, preproc_folklore_corpus;

#覚え書き　３と４の例外は時々呼ばれているようなので，必要
def exception_of_splited_num_is_3(splited_bijankhan_line):
    semispace_concatenated=(splited_bijankhan_line[0]+u'\u200C'+splited_bijankhan_line[1]);
    return semispace_concatenated;
def exception_of_splited_num_is_4(splited_bijankhan_line):
    semispace_concatenated=(splited_bijankhan_line[0]+u'\u200C'+splited_bijankhan_line[1]+u'\u200C'+splited_bijankhan_line[2]);
    return semispace_concatenated;

def exception_of_splited_num_is_more_than(splited_bijankhan_line):
    semispace_concatenated=u'';
    del splited_bijankhan_line[-1];
    for item in splited_bijankhan_line: semispace_concatenated=semispace_concatenated+item+u'\u200C';
    semispace_concatenated=semispace_concatenated.strip(u'\u200C');
    return semispace_concatenated;

def split_bijankhan_and_add_to_list(normalized_bijankhan_path, bijankhan_wordset):
    """
    OUTLINE:this function constructs wordset from bijankhan corpus
    DESCRIPTION:In the bijankhan corpus, each data is tab separated cf."word\tPOS". Thus, this function split each line by '\t'. Sometimes the number of elements in the splited list is more than 2. This is because words in bijankhan corpus is concatenated by normal space. In that case, this code copes with other functions 'exception_of_aplited_num_is_*'. These functions concatenate prefix and stem and suffix by semi-space(ZWNJ).
    """
    with codecs.open(normalized_bijankhan_path, 'r', 'utf-8') as normalized_bijankhan_file:
       for bijankhan_line in normalized_bijankhan_file:
            bijankhan_line=bijankhan_line.strip(u'\n');
            bijankhan_line=post_preper.normalize_line_by_regularexp(bijankhan_line);
            try:
                """
                elif len(bijankhan_line.split())==3:
                bijankhan_word=exception_of_splited_num_is_3(bijankhan_line.split());
                elif len(bijankhan_line.split())==4:
                bijankhan_word=exception_of_splited_num_is_4(bijankhan_line.split());
                """
                if len(bijankhan_line.split(u'\t')) > 2:
                    bijankhan_word=exception_of_splited_num_is_more_than(bijankhan_line);
                elif len(bijankhan_line.split(u'\t'))==1 :pass
                else:
                    bijankhan_word, bijankhan_pos=bijankhan_line.split(u'\t');
            except:
                print [bijankhan_line];

            if not bijankhan_word in bijankhan_wordset:
                bijankhan_wordset.append(bijankhan_word);
            else: pass
    return bijankhan_wordset;

def split_folklore_and_add_to_list(folklore_path, folklore_wordset):
        with codecs.open(folklore_path, 'r', 'utf-8') as lines:
                for line in lines:
                        items=(line.strip(u'\n').strip(u'.')).split();
                        for folklore_word in items:
                            folklore_wordset.append(folklore_word);
        return folklore_wordset;

def compare_wordset_of_bijankhan_and_folklore(bijankhan_wordset, folklore_wordset):
        for bijankhan_word in bijankhan_wordset:
                if bijankhan_word in folklore_wordset:
                        folklore_wordset.remove(bijankhan_word);
                else: pass#print '{0} is not in the list\n'.format(bijankhan_word.encode('utf-8'));
        return folklore_wordset;
def get_recursive_list(directory_path):
    if directory_path[-1]!='/':
        directory_path=directory_path+'/';
    recursive_list=[];
    for root, dir_name, files in os.walk(directory_path):
        for _file_ in files:
            recursive_list.append(root+','+_file_);
    return recursive_list;
def main():
    if len(sys.argv)!=5 and len(sys.argv)!=6:
        sys.exit('usage: python check_goftari.py [-r] bijankhan_corpus_path folklore_corpus_path[folklore_directory_path] path_to_save_compared_goftari_wordset path_to_save_bijankhan_wordset');
    else:
        #----------common process----------
        bijankhan_wordset=[];       
        folklore_wordset=[];
        normalized_bijankhan='./normalized_bijankhan';
        normalized_folklore='./normalized_folklore';
        #----------single mode----------
        if len(sys.argv)==5:
            writeout_compared=codecs.open(sys.argv[3], 'w', 'utf-8');
            writeout_bijankhan_set=codecs.open(sys.argv[4], 'w', 'utf-8');
            bijankhan_normalize_commands=\
                commands.getstatusoutput('python ../preproc_of_bijankhan_posdataset/preproc_of_bijankhan.py {0} {1}'.format(sys.argv[1], normalized_bijankhan));
            if bijankhan_normalize_commands[0]!=0:
                sys.exit(bijankhan_normalize_commands[1])
            bijankhan_wordset=split_bijankhan_and_add_to_list(normalized_bijankhan, bijankhan_wordset);
            folklore_normalization_commands=\
                commands.getstatusoutput('python ../preproc_of_folklore_corpus/preproc_folklore_corpus.py {0} {1}'.format(sys.argv[2], normalized_folklore));
            if folklore_normalization_commands[0]!=0:
                sys.exit(folklore_normalization_commands[1]);
            folklore_wordset=split_folklore_and_add_to_list(normalized_folklore, folklore_wordset);
            print 'the num. of words in folklore corpus',len(folklore_wordset);
            compared_wordset=compare_wordset_of_bijankhan_and_folklore(bijankhan_wordset, folklore_wordset);
            print 'the num. of words filterd out by Bijankhan wordset', len(compared_wordset);
            for compared_items in compared_wordset: writeout_compared.write(compared_items+u'\n');
            for bijankhan_items in bijankhan_wordset: writeout_bijankhan_set.write(bijankhan_items+u'\n');
            writeout_compared.close();
            writeout_bijankhan_set.close();
            commands.getstatusoutput('rm ./normalized_bijankhan ./normalized_folklore');
        #----------recursive mode----------
        elif len(sys.argv)==6:
            if sys.argv[1]=='-r':
                recursive_list=get_recursive_list(sys.argv[3]);
            #TODO ここからさき，再帰モードの続きを書いていく．主な流れはリストからitemをとって，集合を生成してでっかいbijankhan listを構築する．で，それをfolkloreコーパスと比較する
            writeout_compared=codecs.open(sys.argv[4], 'w', 'utf-8');
            writeout_bijankhan_set=codecs.open(sys.argv[5], 'w', 'utf-8');
            bijankhan_normalize_commands=\
                commands.getstatusoutput('python ../preproc_of_bijankhan_posdataset/preproc_of_bijankhan.py {0} {1}'.format(sys.argv[2], normalized_bijankhan));
            if bijankhan_normalize_commands[0]!=0: sys.exit(bijankhan_normalize_commands[1])
            bijankhan_wordset=split_bijankhan_and_add_to_list(normalized_bijankhan, bijankhan_wordset);
            for path_to_one_folklore_file in recursive_list:
                root, file_=path_to_one_folklore_file.split(',');
                path_to_one_folklore_file=root+file_;
                folklore_normalization_commands=\
                    commands.getstatusoutput('python ../preproc_of_folklore_corpus/preproc_folklore_corpus.py {0} {1}'.format(path_to_one_folklore_file, normalized_folklore));
                if folklore_normalization_commands[0]!=0: sys.exit(folklore_normalization_commands[1]);
                folklore_wordset=split_folklore_and_add_to_list(normalized_folklore, folklore_wordset);
                
            print 'the num. of words in folklore corpus',len(folklore_wordset);
            compared_wordset=compare_wordset_of_bijankhan_and_folklore(bijankhan_wordset, folklore_wordset);
            print 'the num. of words filterd out by Bijankhan wordset', len(compared_wordset);
            for compared_items in compared_wordset: writeout_compared.write(compared_items+u'\n');
            for bijankhan_items in bijankhan_wordset: writeout_bijankhan_set.write(bijankhan_items+u'\n');
            writeout_compared.close();
            writeout_bijankhan_set.close();
            commands.getstatusoutput('rm ./normalized_bijankhan ./normalized_folklore');
        
if __name__=='__main__':
    main();



