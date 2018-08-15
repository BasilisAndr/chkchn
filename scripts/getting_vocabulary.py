import os
from lxml import etree

def open_file(name):
    with open(name) as f:
        text = f.read()
    return text

def turn_into_tree(text):
    root = etree.fromstring(text)
    return root


def handle_blocks(blocks):
    words = {block.xpath('item[@type="cf"]')[0].text: \
                block.xpath('item[@type="gls"]')[0].text for block in blocks}
    return words



def main():
    root = turn_into_tree(open_file('/Users/Basilis/Downloads/corpus.xml'))
    blocks = root.xpath('//morph[@type="stem"]')
    words = handle_blocks(blocks)
    wds = sorted(words, key=lambda x:words[x][-1])
    with open('new_words.txt', 'w') as f:
        for wd in wds:
            f.write('{0}\t!\t{1}\n'.format(' '.join(wd), words[wd]))



if __name__ == '__main__':
    main()
