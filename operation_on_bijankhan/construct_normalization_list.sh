suffix_normalized=".normalized"
suffix_result=".training"
ruby pre_per2.rb $1 > $1$suffix_normalized
python check_normalize_error_in_preper.py -t $1$suffix_normalized $1$suffix_result
