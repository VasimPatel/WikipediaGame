from queue import PriorityQueue
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from p_item import PrioritizedItem
from similar_words import SimilarWords

STOP_WORDS = set(stopwords.words('english'))
SIMILAR_WORD_CALC = SimilarWords()

def analyze(links, dest):
    """ Returns a list of links to explore sorted by similarity to the dest """

    p_queue = PriorityQueue()

    # Remove stop words and tokenize
    dest_tokens = word_tokenize(dest.replace("_", " "))
    filtered_dest = [w for w in dest_tokens if not w in STOP_WORDS]

    # for every link in the page, find the distance between every word in the
    # link to every word in dest
    for link in links:
        link_tokens = word_tokenize(link.replace("_", " "))
        filtered_link = [w for w in link_tokens if not w in STOP_WORDS]

        outer_sum = 0
        inner_sum = 0
        # Average of the distances between every word in link to every word in
        # desired dest - order in priority queue
        for dest_word in filtered_dest:
            inner_sum = 0
            for link_word in filtered_link:
                inner_sum += SIMILAR_WORD_CALC.get_distance(dest_word.lower(),
                                                            link_word.lower())
            outer_sum += inner_sum/len(filtered_link)
        temp_p_item = PrioritizedItem(outer_sum/len(filtered_dest), link)
        p_queue.put(temp_p_item)
    result_list = []
    while not p_queue.empty():
        result_list.append(p_queue.get().item)
    return result_list
