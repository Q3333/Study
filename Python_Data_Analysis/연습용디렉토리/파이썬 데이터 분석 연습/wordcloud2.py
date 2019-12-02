from wordcloud import WordCloud, STOPWORDS
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import platform
import random

text = open('../data/09. a_new_hope.txt').read()

text = text.replace('HAN', 'Han')
text = text.replace("LUKE`S", 'Luke')

mask = np.array(Image.open('../data/09. stormtrooper_mask.png'))

stopwords = set(STOPWORDS)
stopwords.add("int")
stopwords.add("ext")

wc = WordCloud(max_words=1000, mask=mask, stopwords=stopwords, margin=10,
random_state=1).generate(text)

default_colors = wc.to_array()

def grey_color_func(word, font_size, position, orientation,
                    random_state=None, **kwargs):
                    return 'hsl(0, 0%%, %d%%)' % random.randint(60,100)

plt.figure(figsize=(12,12))
plt.imshow(wc.recolor(color_func=grey_color_func,random_state=3),
            interpolation='bilinear')
plt.axis('off')        
plt.show()
