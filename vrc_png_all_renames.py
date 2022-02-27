import os
import glob
import re


#フォルダー内のpngを検索するための正規表現
pngregexp = './*.png'

#pngの画像ごとに処理
for png_dir in glob.glob(pngregexp):
    #日付を抽出するための正規表現
    if re.search(r'\d{4}-\d{2}-\d{2}', png_dir):
        s = re.findall(r'\d{4}-\d{2}-\d{2}', png_dir)
        os.renames(png_dir,s[0]+"\\"+png_dir)
