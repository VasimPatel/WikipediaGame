import sys
import linkGrab
import analyzer

source = "https://en.wikipedia.org/wiki/Penis"

seen = []

def findRoute(source, dest):
    curr = "https://en.wikipedia.org/wiki/"+ source
    order = [source]
    print(curr)
    while (True):
        unseen_links = []

        #grab all links in page, and save the ones we have not been to already
        pageLinks = linkGrab.get_links(curr)
        for link in pageLinks:
            if link not in seen:
                unseen_links.append(link)
        if not unseen_links:
            if curr.lower() == source.lower():
                print("Impossible to get there")
                sys.exit()
            if curr in order:
                order.remove(curr)
            curr = order[-1]
            continue
        bestLinks = analyzer.analyze(list(unseen_links), dest)
        step = bestLinks[0]
        seen.append(step)
        order.append(step)
        curr = "https://en.wikipedia.org/wiki/" + step
        print(curr)
        if step.lower() == dest.lower():
            print(order)
            sys.exit()


if __name__ == "__main__":
    findRoute(sys.argv[1], sys.argv[2])
