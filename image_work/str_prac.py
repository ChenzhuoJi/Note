import d2_str_study

from emoji import Cdt_list
from d2_str_study import strix

txt_to_wt=strix(Cdt_list,'000')
with open('image_work/text/heart.txt', 'w', encoding='utf-8') as file:  
    file.write(txt_to_wt)  