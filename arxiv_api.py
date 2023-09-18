import requests
import xml.etree.ElementTree as ET

class arxiv_clinical_api:
    def __init__(self, search_query, max_results):
        self.search_query = search_query
        self.max_results = max_results
        self.url = 'http://export.arxiv.org/api/query?search_query={}&start=0&max_results={}&sortBy=lastUpdatedDate&sortOrder=descending'.format(self.search_query, self.max_results)
        self.response = requests.get(self.url)
        self.root = ET.fromstring(self.response.content)
        self.entries = self.root.findall('{http://www.w3.org/2005/Atom}entry')
        self.results = []
        for entry in self.entries:
            result = {}
            result['title'] = entry.find('{http://www.w3.org/2005/Atom}title').text
            result['summary'] = entry.find('{http://www.w3.org/2005/Atom}summary').text
            result['link'] = entry.find('{http://www.w3.org/2005/Atom}link').attrib['href']
            self.results.append(result)
        self.results = self.results[:self.max_results]
    def get_results(self):
        return self.results

