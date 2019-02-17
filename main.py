import sys
import linkGrab
import analyzer

source = "https://en.wikipedia.org/wiki/Penis"

seen = []

def findRoute(source, dest):
    curr = "https://en.wikipedia.org/wiki/"+ source
    order = []
    while (True):
        print(curr)
        pageLinks = linkGrab.get_links(curr)
        bestLinks = analyzer.analyze(list(pageLinks), source)
        #step = list(set(bestLinks) - set(seen))[0]
        step = bestLinks[0]
        seen.append(step)
        order.append(step)
        curr = "https://en.wikipedia.org/wiki/" + step
        print(curr)
        if step == source:
            print(order)
            exit(0)


if __name__ == "__main__":
    findRoute(sys.argv[1], sys.argv[2])
