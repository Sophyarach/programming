import re
import os
from collections import Counter

def get_word(line):
    match=re.search(r'</ana>(\w+)',line)
    return match.group(1)

def get_lemma(line):
    match=re.search(r'lex="(\w+)',line)
    return match.group(1)

def remove_tags(line):
    tag_expr=r'<.*?>'
    return re.sub(tag_expr,'',line)

def maketxt_from_file(filename):
    with open(filename, encoding='utf-8') as file:
        title=''
        #for s in file:
            #if '<title>' in s:
             #   title=re.search(r'<title>(.*?)</title>',s).groups()[0]
             #   break
        newname=filename+'.txt'
        with open(newname, 'w', encoding='cp1251') as newfile:
            newfile.write(title+'\n')
            newtext=''
            for s in file:
                if s.startswith('<w>'):
                    word=remove_tags(s)
                    word=re.sub('(`)','', word)
                    newtext=newtext+word.strip('\n')+' '
            newtext=re.sub('  ',' ',newtext)
            newfile.write(newtext)
                    #if '</se>' in s:
                    #    punct=re.search(r'</w>(.*?)</se>',s).groups(1)
                    #else:
                    #    punct=re.search(r'</w>(.*?)\n',s).groups(1)
                    #newfile.write(punct+' ')

def count_to_file(counter,filename):
    with open(filename, 'w', encoding='utf-8') as f:
        for k,v in counter.items():
            f.write('{}\t{}\n'.format(k,v))

def capitalised_lemmas(filename):
    counter=Counter()
    with open(filename, encoding='utf-8') as file:
        for s in file:
            if s.startswith('<w>'):
                lemma=get_lemma(s)
                if lemma[0].isupper():
                    counter[lemma]+=1
    return(counter)

def find_bigrams(filename):
    result=''
    with open(filename, encoding='utf-8') as file:
        for s in file:
            if re.search(r'content="(.*?)" name="docid"></meta>', s):
                docid = re.search(r'content="(.*?)" name="docid"></meta>', s).groups()[0]
            if re.search(r'content="(.*?)" name="topic"></meta>', s):
                topic = re.search(r'content="(.*?)" name="topic"></meta>', s).groups()[0]
        text=file.read()
        sentences=text.split('\n<se>\n')
        for sentence in sentences:
                words=sentence.split('\n')
                for n, word in enumerate(words):
                    if 'gr="NUM' in words[n]:
                        if 'gen' in words[n+1]:
                            bigram=words[n]+words[n+1]
                            bigram=remove_tags(bigram)
                            result=result+docid+';'+bigram+';'+topic+'\n'
    return result

def doeverything(path):
    full_counter=Counter()
    for filename in os.listdir(path):
        maketxt_from_file(filename)
        full_counter=full_counter+capitalised_lemmas(filename)
        fileres='bigrams.csv'
        with open(fileres, 'w', encoding='utf-8') as f:
            f.write(find_bigrams(filename))
    count_to_file(full_counter,'именасобственные.txt')
                                    
                

doeverything('.')
            
