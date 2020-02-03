# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 17:01:37 2019

@author: cyuan
"""

import os
import csv
 
TRAIN_IMG_DIR = r'C:\Users\cyuan\Desktop\ML_summary\autokeras自动生成最佳网络\train'
TRAIN_CSV_DIR = r'C:\Users\cyuan\Desktop\ML_summary\autokeras自动生成最佳网络\train_labels.csv'
TEST_IMG_DIR = r'C:\Users\cyuan\Desktop\ML_summary\autokeras自动生成最佳网络\test'
TEST_CSV_DIR = r'C:\Users\cyuan\Desktop\ML_summary\autokeras自动生成最佳网络\test_labels.csv'
 
def mkcsv(img_dir, csv_dir):
    list = []
    list.append(['File Name','Label'])
    for file_name in os.listdir(img_dir):
        if file_name[0] == '3':   #bus
            item = [file_name, 0]
        elif file_name[0] == '4': #dinosaur
            item = [file_name, 1]
        elif file_name[0] == '5': #elephant
            item = [file_name, 2]
        elif file_name[0] == '6': #flower
            item = [file_name, 3]
        else:
            item = [file_name, 4] #horse
        list.append(item)
 
    print('\n' ,list)
    f = open(csv_dir, 'w', newline='')
    writer = csv.writer(f)
    writer.writerows(list)#生成csv文件
 
mkcsv(TRAIN_IMG_DIR, TRAIN_CSV_DIR)#生成
mkcsv(TEST_IMG_DIR, TEST_CSV_DIR)