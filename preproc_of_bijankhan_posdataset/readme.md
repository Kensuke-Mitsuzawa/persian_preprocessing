# Preprocess module of Bijankhan POS dataset
___

## outline
The characters in Bijankhan POS tagset is not regularized. Cf. Arabic character for ye and kaf, intermixed spaces etc.  
This system make them regular format with pre_per2.rb and virastar module.  

[Bijankhan POS dataset](http://ece.ut.ac.ir/dbrg/bijankhan/) this is suit for *new* bijankhan corpus.

The pre_per2.rb is [pre_per2.rb](http://stp.lingfil.uu.se/~mojgan/preper.html)
The virastar module is [virastar github page](https://github.com/aziz/virastar)

I improved both of pre_per2.rb and virastar to fit my purpose. 

## usage

`python preproc_of_bijankhan.py input_file output_file`  

## files

preproc_of_bijankhan.py:main script  
dummy.py:insert dummy tag before pre_per2.rb  
delete_dummy.py:remove dummy tag after pre_per2.rb  