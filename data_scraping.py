from bs4 import BeautifulSoup
import requests
import pandas as pd
import constants as const

class DataScrape:
    def __init__(self):
        self.product_config = const.product_config
        self.urls_df = self.read_url_file()
    def run(self):
        all_product_info = []
        for index, url in self.urls_df.iloc[950:1000].iterrows():
            print(index)
            page_url = const.MAIN_URL + url.name
            page_result = requests.get(page_url)
            soup = BeautifulSoup(page_result.content, 'html.parser')
            print(url.name, page_result.status_code)
            if page_result.status_code != 200:
                print("SAYFA BULUNAMADI..")
                continue
            if soup.find(id=const.KATALOG_ID):
                print("Bu bir katalogtur.")
                try:
                    product_count_info = soup.find_all(const.DIV_TYPE, const.ALL_PRODUCT_REGEX)
                    product_count = [int(span.get_text().split(" ")[1]) for span in product_count_info]
                    page_count = (int(product_count[0] / const.PAGE_CHUNK)) + 1
                except:
                    print("Eksik content type tespit edilmiştir.")
                    continue
                print(page_url[:-1] + const.NUMBER_OF_PAGE_URL + str(page_count))
                all_product_result = requests.get(page_url[:-1] + const.NUMBER_OF_PAGE_URL + str(page_count))
                catalog_soup = BeautifulSoup(all_product_result.content, 'html.parser')
                product_detailed = catalog_soup.find_all(const.HREF_TYPE, attrs=const.PRODUCT_HREF)
                for product in product_detailed:
                    try:
                        offer = product.parent.find_all(const.DIV_TYPE, "product-item-discount")[0].get_text().replace("\n", " ")
                        product_price = product.parent.find_all(const.SPAN_TYPE, "discountedPrice")[0].get_text().replace("\n", " ")
                        sale_price = product.parent.find_all(const.SPAN_TYPE, "currentPrice")[0].get_text().replace("\n", " ")
                        product_name = product.parent.find_all("a", "fl col-12 product-description")[0].get("title")
                        product_size = product.parent.find_all("a", "fl col-12 product-description")[0].findAll('ul')[0].get_text().replace("\n", " ")
                        all_product_info.append([product_name, offer, product_price, sale_price, product_size])
                    except Exception as err:
                        print("Farklı content type tespit edilmiştir.")
                continue
                

            if soup.find(id=const.KATALOG_ID) is None and soup.find(id=const.PRODUCT_NAME_ID) is None:
                print("Bu sayfada ürün bulunmamaktadır")
                continue

            if soup.find_all("span", {"class": "product-price"}):
                product_info = self.parse_product(page_url)
                print(product_info)
                all_product_info.append(product_info)
            else:
                print("Ürün stokta yoktur.")
                continue

        return all_product_info

    def read_url_file(self):
        urls_df = pd.read_excel(const.url_file_name, index_col=0, usecols='A')
        return urls_df

    def parse_product(self, url):
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        product_data = []
        for key, value in self.product_config.items():
            spans = soup.find_all(value["type"], attrs=value["attrs"])
            for span in spans: 
                product_data.append(span.get_text().replace("\n"," "))



        return product_data