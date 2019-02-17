from queue import PriorityQueue
from similar_words import SimilarWords
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from p_item import PrioritizedItem

def analyze(links, source):
    pq = PriorityQueue()

    #clean up words to only use important ones, and tokenize them
    similar_word_calc = SimilarWords()
    stop_words = set(stopwords.words('english'))
    source_spaces = source.replace("_", " ")
    source_tokens = word_tokenize(source_spaces)
    filtered_source = [w for w in source_tokens if not w in stop_words]

    #for every link in the page we haven't seen, find the distance between every word in the link to every word in dest.
    for link in links:
        link_spaces = link.replace("_", " ")
        link_tokens = word_tokenize(link_spaces)
        filtered_link = [w for w in link_tokens if not w in stop_words]
        minNum = 9999999999.0
        outer_sum = 0
        inner_sum = 0
        innerAvgs = []
        #get the average of the distances between every word in link to every other word desired dest., order in priority queue
        for s in filtered_source:
            inner_sum = 0
            for l in filtered_link:
                inner_sum += similar_word_calc.get_distance(s.lower(), l.lower())
            outer_sum += inner_sum/len(filtered_link)
        temp_p_item = PrioritizedItem(outer_sum/len(filtered_source),link)
        pq.put(temp_p_item)
    l = []
    while not pq.empty():
        l.append(pq.get().item)


    return l
