from crawler import Crawler
import util,log

def start():
    url = input("Enter the starting url:")
    if util.validateUrl(url):

        pageLimit = input("Enter the number of urls to inspect: ")

        cr = Crawler(url, int(pageLimit))
        # source must be in simplified chinese
        cr.start()
    else:
        start()

start()
