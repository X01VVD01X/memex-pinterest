#This class provide APIs for interfaces applications
#to communicate with seed crawler
#
#03/11/2015

# from subprocess import call
# from subprocess import Popen
# from subprocess import PIPE
# import os
# from os.path import isfile, join, exists
# import download
# import rank

class SeedCrawlerModel:
    #Note: we should estimate the latency of each operation so that the application could adapt smoothly

    def __init__(self):
        #Intermediate data will being handled here: urls, extracted text, terms, clusters, etc.

        #list of urls and their labels, ranking scores
        #e.g: urls = [["nature.com", 1, 0.9], ["sport.com", 0, 0.01]
        self.urls = []

        #list of terms and their labels, ranking scores
        #e.g: terms = [["science", 1, 0.9], ["sport", 0, 0.02]]
        self.terms = []
        # self.memex_home = os.environ['MEMEX_HOME']


    def submit_query_terms(self, term_list):
    #Perform queries to Search Engine APIs
    #This function only operates when there is no information associated with the terms,
    #usually before running extract_terms()
    #
    #Args:
    #   term_list: list of search terms that are submited by user
    #Returns:
    #   urls: list of urls that are returned by Search Engine
    #     os.chdir(self.memex_home + '/seed_crawler/seeds_generator')
    #
    #     with open('conf/queries.txt','w') as f:
    #         for term in term_list:
    #             f.write(term)
    #
    #     p=Popen("java -cp .:class:libs/commons-codec-1.9.jar BingSearch -t 15",shell=True,stdout=PIPE)
    #     output, errors = p.communicate()
    #     print output
    #     print errors
    #     call(["rm", "-rf", "html"])
    #     call(["mkdir", "-p", "html"])
    #     download.download("results.txt","html")
    #
    #     if exists(self.memex_home + "/seed_crawler/ranking/exclude.txt"):
    #         call(["rm", self.memex_home + "/seed_crawler/ranking/exclude.txt"])
    #
    #     urls = []
    #     with open("results.txt",'r') as f:
    #         urls = [self.validate_url(line.strip()) for line in f.readlines()]
    #
    #     return urls #Results from Search Engine

        # mock implementation for dev purposes
        # urls = []
        # urls[0] = "https://www.dartlang.org/"
        # urls[1] = "www.dublin.ie/transport/dart.htm/"
        # urls[2] = "googledart.es/"

        return ["https://www.dartlang.org/", "www.dublin.ie/transport/dart.htm/", "googledart.es/"]

    def submit_selected_urls(self, positive, negative):
    #Perform ranking and diversifing on all urls with regard to the positive urls
    #
    #Args:
    #   labeled_urls: a list of pair <url, label>. Label 1 means positive and 0 means negative.
    #Returns:
    #   urls: list of urls with ranking scores

        # Test new positive and negative examples with exisitng classifier
        # If accuracy above threshold classify pages
        # Ranking
        # Diversification
        '''
        os.chdir(self.memex_home + '/seed_crawler/lda_pipeline')
        call(["mkdir", "-p", "data"])
        p=Popen("java -cp .:class/:lib/boilerpipe-1.2.0.jar:lib/nekohtml-1.9.13.jar:lib/xerces-2.9.1.jar Extract ../seeds_generator/html/  | python concat_nltk.py data/lda_input.csv",shell=True,stdout=PIPE)
        output, errors = p.communicate()
        print output
        print errors

        os.chdir(self.memex_home + '/seed_crawler/ranking')
        ranker = rank.rank()

        [ranked_urls,scores] = ranker.results(self.memex_home + '/seed_crawler/lda_pipeline/data/lda_input.csv',positive, negative)
        return [ranked_urls, scores] # classified, ranked, diversified
        '''

        # mock implementation for dev purposes
        return [["https://www.dartlang.org/", "www.dublin.ie/transport/dart.htm/", "googledart.es/"], [90, 60, 30]]


    def extract_terms(self):
    #Extract salient terms from positive urls
    #
    #Returns:
    #   terms: list of extracted salient terms and their ranking scores

        terms = [] #if there is no positive url
        return terms

    def submit_selected_terms(self, labeled_terms):
    #Rerank the terms based on the labeled terms
    #
    #Args:
    #   labeled_terms: list of pair of term and label: <term, label>. Label 1 means postive, 0 means negative.
    #Returns:
    #   terms: list of newly ranked terms and their ranking scores

        terms = []
        return terms # ranked

    def validate_url(self, url):
        s = url[:4]
        if s == "http":
            return url
        else:
            url = "http://" + url
        return url


if __name__=="__main__":
    scm = SeedCrawlerModel()
    #Create a test that mimick user process here to test
    #1. User starts with some terms
    #2. (Repeat) User labels the urls and submits the labeled urls
    #3. User requests for extracting terms from labeled urls
    #4. (Repeat) User labels the terms and submits the labeled terms for reranking