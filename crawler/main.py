from urllib.request import Request, urlopen, URLError, urljoin
from urllib.parse import urlparse
import time
import threading
import queue
from bs4 import BeautifulSoup
import ssl

"""A classmethod that is use for crawling website

"""
class Crawler(threading.Thread):
  def __init__(self, base_url, links_to_crawl, have_visited, error_links, url_lock):
    threading.Thread.__init__(self)
    print("Web Crawler worker" + str(threading.current_thread()) + "has Started")
    self.base_url = base_url
    self.links_to_crawl = links_to_crawl
    self.have_visited = have_visited
    self.error_links = error_links
    self.url_lock = url_lock

  def run(self):
    """Create a ssl context
      allow https handshake
      create with default settings
    """
    my_ssl = ssl.create_default_context()
    """Default ssl is used for handshaking
      no check hostname is required
      in this case any certificate is acceptable
    """
    my_ssl.check_hostname = False
    my_ssl.verify_mode = ssl.CERT_NONE

    """Defining an while 1 so that all links
      will be processed
    """
    while True:
      
      # at most one mode with global lock
      self.url_lock.acquire()
      print("Queue Size" + str(self.links_to_crawl.qsize()))
      link = self.links_to_crawl.get()
      self.url_lock.release()

      if link is None:
        break

      if link in self.have_visited:
        print("link {link} is already existed")
        break

      try:
        link = urljoin(self.base_url, link)
        req = Request(link, headers={'User-Agent': 'Mozilla/5.0'})
        response = urlopen(req, context=my_ssl)
        print("URL:" + str(response))

        soup = BeautifulSoup(response.read(), "html.parser")

        for a_tag in soup.find_all('a'):
          if (a_tag.get('href') not in self.have_visited) and (urlparse(link).netloc == "www.python.org"):
            self.links_to_crawl.put(a_tag.get("href"))
          else:
            print("The link" + str(a_tag.get('href')) + "is already visited or is not part of the website")
      except URLError as e:
        print("Error Reason: ", e.reason)
        self.error_links.append(link)
      finally:
        self.links_to_crawl.task_done()

print("The Crawler is started")
base_url = input("Please Enter Website to Crawl > ")
number_of_threads = input("Please Enter number of Threads > ")

links_to_crawl = queue.Queue()
url_lock = threading.Lock()
links_to_crawl.put(base_url)

have_visited = set()
crawler_threads = []
error_links = []

for i in range(int(number_of_threads)):
  crawler = Crawler(base_url=base_url, links_to_crawl=links_to_crawl, have_visited=have_visited, error_links=error_links, url_lock=url_lock)
  crawler.start()
  crawler_threads.append(crawler)

for crawler in crawler_threads:
  crawler.join()
  
print("Total Number of pages visited are" + str(len(have_visited)))
print("Error Number of pages visited are" + str(len(error_links)))
