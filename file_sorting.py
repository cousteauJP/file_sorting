import os
import glob
import re

path = './'
 
filelist = []
 
#フォルダーごとに処理
for f in os.listdir(path):
    
    #フォルダー内のpngを検索するための正規表現
    pngregexp = './' + f  + '/*.png'

    #pngの画像ごとに処理
    for png_dir in glob.glob(pngregexp):
        #日付を抽出するための正規表現
        if not re.match(r'\d\d\d\d-\d\d-\d\d', png_dir):
            s = re.findall(r'\d\d\d\d-\d\d-\d\d', png_dir)
            os.renames(s,s[:8]+"\\"+s)
