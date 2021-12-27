from os import replace
from data_scraping import DataScrape
from data_transfer import DataTransfer
data_scrape = DataScrape()
all = data_scrape.run()
print("*"*150)
print(all)

data_transfer = DataTransfer(all)

data_transfer.write_google_datasheet()