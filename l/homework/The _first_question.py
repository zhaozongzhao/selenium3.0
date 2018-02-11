#有一篇英文文章保存在 a.txt 中，请用python实现统计这篇文章内每个单词的出现频率，
# 并返回出现频率最高的前10个单词及其出现次数（只考虑空格，标点符号可忽略）

import re
from collections import Counter
c = Counter()
def Word_counts():
  '''单次排序'''
  with open('a.txt','r',encoding='utf-8') as f:
       for line in f:
          words =re.findall(r'\w+', line)
          c1 = Counter(words)
          c.update(c1)
  return sorted(c.items(),key=lambda x:x[1],reverse=True)



if __name__ == '__main__':
    print(Word_counts()[0:10])
