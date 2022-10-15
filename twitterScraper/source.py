# Using twint library to scrape data
import twint

# Putting the main functionality for the scraper in a class allows for better organization
class twitterScraper:

    def __init__(self):
        pass

    # This function creates a twint object based on the given paremeters
    def gatherDataAbout(self, searchTerm, dataLimit, startDate, endDate, fileName):
        
        twintObject = twint.Config()

        twintObject.Limit = dataLimit

        twintObject.Search = searchTerm

        twintObject.Since = startDate

        twintObject.Until = endDate

        twintObject.Store_csv = True

        twintObject.Output = fileName

        return twintObject

    # Uses gatherDataAbout function and user inputs to return a twint object
    def userInterface(self):

        searchTerm = input("Enter search term:\n")

        dataLimit = input("Enter number of tweets:\n")

        startDate = input("Enter start date (year-month-day as numbers):\n")

        endDate = input("Enter end date:\n")

        fileName = input("Enter directory and or filename (recommended: ./twitterData/fileName.csv):\n")

        return self.gatherDataAbout(searchTerm, int(dataLimit), startDate, endDate, fileName)


userInterface = input("Would you like to use the user interface? Enter 1 for yes or 0 for no: ")

while (userInterface != str(0) and userInterface != str(1)):
    userInterface = input("Please enter 1 for yes or 0 for no ")

if (userInterface == str(1)):

    twintObject = twitterScraper().userInterface()

    # Twint searches based off the returned object, but only if the user chooses to do so
    twint.run.Search(twintObject)

    print("Thankyou for using the twitter scraper!")





# Test Code
#twintObject = twitterScraper()

#newObject = twintObject.gatherDataAbout('Tesla', 20, '2020-02-15', '2021-01-15', './twitterData/test3.csv')

#twint.run.Search(newObject)

