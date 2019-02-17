from queue import PriorityQueue
from similar_words import SimilarWords
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

def analyze(links, source):
    pq = PriorityQueue()
    similar_word_calc = SimilarWords()
    stop_words = set(stopwords.words('english'))
    source_spaces = source.replace("_", " ")
    source_tokens = word_tokenize(source_spaces)
    filtered_source = [w for w in source_tokens if not w in stop_words]
    for link in links:
        link_spaces = link.replace("_", " ")
        link_tokens = word_tokenize(link_spaces)
        filtered_link = [w for w in link_tokens if not w in stop_words]
        outer_sum = 0
        inner_sum = 0
        for s in filtered_source:
            inner_sum = 0
            for l in filtered_link:
                inner_sum = 0
                inner_sum += similar_word_calc.get_distance(s, l)
            outer_sum += inner_sum/len(filtered_link)
        pq.put(link, outer_sum/len(filtered_source))
    
    return list(pq)
