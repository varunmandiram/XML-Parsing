# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 19:42:57 2019

@author: varun_mandiram
"""
import xml.etree.ElementTree as ET
import pandas as pd
import sys

def parse_xml(filename):

    tree = ET.parse(filename)
    root = tree.getroot()

    word_attributes=[]
    word_text=[]

    #print(root.tag)

    for words in root.iter('W'):
        word_attributes.append(words.attrib)
        word_text.append(words.text)

    word_attributes_df=pd.DataFrame(word_attributes)
    #print(list(word_attributes_df))
    word_text_df=pd.DataFrame(word_text)

    words = pd.concat([word_attributes_df, word_text_df], axis=1,ignore_index=True)
    words.columns = ['bottom', 'left', 'right', 'top', 'x', 'y','text']

    
    return words
    
if __name__ == "__main__":
    filename= sys.argv[1]
    
    ##Input a pdf here
    parse_xml(filename)






            