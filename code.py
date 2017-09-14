#Matthew Mantese

import urllib
from collections import deque

def getLinks(url,baseurl="http://secon.utulsa.edu/cs2123/webtraverse/"):
    """
    Input: url to visit, Boolean absolute indicates whether URLs should include absolute path (default) or not
    Output: list of pairs of URLs and associated text
    """
    #import the HTML parser package 
    try:
        from BeautifulSoup import BeautifulSoup
    except:
        print 'You must first install the BeautifulSoup package for this code to work'
        raise
    #fetch the URL and load it into the HTML parser
    soup = BeautifulSoup(urllib.urlopen(url).read())
    #pull out the links from the HTML and return
    return [baseurl+a["href"].encode('ascii','ignore') for a in soup.findAll('a')]

def print_dfs(url):
    G = getDictionary(url)
    dfsLs = recurs_dfs(G, url)
    for link in dfsLs:
        print link

def recurs_dfs(G, url, S = set()):
    S.add(url)
    for u in G[url]:
        if u in S: 
            continue
        recurs_dfs(G, u, S)
    return S

def print_bfs(url):
    S, Q = set(), deque()
    G = getDictionary(url)
    Q.append(url)
    while Q:
        u = Q.popleft()
        if u in S:
            continue
        S.add(u)
        Q.extend(G[u])
    for link in S:
        print link

def get_parent_bfs(url1, url2):
    G = getDictionary(url1)
    P, Q = {url1 : None}, deque([url1])
    while Q:
        u = Q.popleft()
        for v in G[u]:
            if v in P: continue
            P[v] = u
            Q.append(v)
        if(u == url2):
            return P
    return None

    
def find_shortest_path(url1,url2):
    """
    Find and return the shortest path
    from **url1** to **url2** if one exists.
    If no such path exists, say so.
    """
    #
    P = get_parent_bfs(url1, url2)
    ls = []
    if P != None:
        u = url2
        while u != url1:
            ls.append(u)
            u = P[u]
        ls.append(u)
        for i in xrange(len(ls)):
            print ls.pop()
    else:
        print "There is no path."



def find_max_depth(start_url):
    """
    Find and return the URL that is the greatest distance from start_url, along with the sequence of links that must be followed to reach the page.
    For this problem, distance is defined as the minimum number of links that must be followed from start_url to reach the page.
    """
    #
    G = getDictionary()
    for links in G:
        

def getDictionary (start, G = {}):
    G[start] = getLinks(start)
    for link in G[start]:
        if link not in G:
            getDictionary(link, G)
    return G

if __name__=="__main__":
    starturl = "http://secon.utulsa.edu/cs2123/webtraverse/index.html"
    print "*********** (a) Depth-first search   **********"
    print_dfs(starturl)
    print "*********** (b) Breadth-first search **********"
    print_bfs(starturl)
    print "*********** (c) Find shortest path between two URLs ********"
    find_shortest_path("http://secon.utulsa.edu/cs2123/webtraverse/index.html","http://secon.utulsa.edu/cs2123/webtraverse/wainwright.html")
    find_shortest_path("http://secon.utulsa.edu/cs2123/webtraverse/turing.html","http://secon.utulsa.edu/cs2123/webtraverse/dijkstra.html")
    print "*********** (d) Find the longest shortest path from a starting URL *****"
    find_max_depth(starturl)