import sys
import link_grab
import analyzer

SEEN = []

def find_route(source, dest):
    """ Find path from source to dest via Wikipedia links """
    curr = "https://en.wikipedia.org/wiki/" + source
    order = [source]        # links traversed
    print(curr)

    while True:
        unseen_links = []

        # Grab all links in page
        page_links = link_grab.get_links(curr)
        for link in page_links:
            # Ensures no cycles
            if link not in SEEN:
                # only store links that have not been visited
                unseen_links.append(link)
        # Ensures the program does not get stuck
        if not unseen_links:    # all links on page have been visited
            if curr.lower() == source.lower():  # have tracked back to source
                print("Impossible to get there")    # no source to dest path
                sys.exit()
            if curr in order:
                order.remove(curr)
            curr = order[-1]        # this link was a bad choice, move back
            continue
        best_links = analyzer.analyze(list(unseen_links), dest)
        step = best_links[0]
        SEEN.append(step)
        order.append(step)
        curr = "https://en.wikipedia.org/wiki/" + step
        print(curr)
        if step.lower() == dest.lower():    # destination reached
            print(order)
            break

if __name__ == "__main__":
    find_route(sys.argv[1], sys.argv[2])
    
    # Allow users to play continuously
    while (True):
        SEEN = []
        source_dest = (input("Enter next source and destination (space separated) or CTRL+D to exit: ")).split(" ")
        find_route(source_dest[0], source_dest[1])

