# Using twint library to scrape data
import twint

class twitterScraper:

    def __init__(self):
        pass

    def gatherDataAbout(self, searchTerm, dataLimit, startDate, endDate, fileName):
        
        twintObject = twint.Config()

        twintObject.Search = searchTerm

        twintObject.Limit = dataLimit

        twintObject.Since = startDate

        twintObject.Until = endDate

        twintObject.Store_csv = True

        twintObject.Output = fileName

        return twintObject


twintObject = twitterScraper()

newObject = twintObject.gatherDataAbout('Tesla', 10, '2020-02-15', '2022-01-15', './test.csv')

twint.run.Search(newObject)
