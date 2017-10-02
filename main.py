import threading
from queue import Queue
from spider import Spider
from domain import *
from general import *

PROJECT_NAME = 'enter_your_project_name_here'
HOMEPAGE = 'enter_your_website_homepage_to_crawl'
DOMAIN_NAME = get_domain_name(HOMEPAGE)
QUEUE_FILE = PROJECT_NAME + '/queue.txt'
CRAWLED_FILE = PROJECT_NAME + '/crawled.txt'
NUMBER_OF_THREADS = 8
queue = Queue()
Spider(PROJECT_NAME, HOMEPAGE, DOMAIN_NAME)


# create workers (will die when main terminates)
def create_workers():
    for _ in range(NUMBER_OF_THREADS):
        t = threading.Thread(target=work)
        t.daemon = True
        t.start()


# do the next job in the queue
def work():
    while True:
        url = queue.get()
        if url is None:
            break
        Spider.crawl_page(threading.current_thread().name, url)
        queue.task_done()


# each queue link is a new job
def create_jobs():
    for link in file_to_set(QUEUE_FILE):
        queue.put(link)
    queue.join()
    crawl()


# if there are items in the queue go and crawl them
def crawl():
    queue_links = file_to_set(QUEUE_FILE)
    if len(queue_links) > 0:
        print(str(len(queue_links)) + ' links in the queue')
        create_jobs()


create_workers()
crawl()
