MAIN_URL = "https://www.markastok.com"
NUMBER_OF_PAGE_URL = "?ps="
url_file_name = "url.xlsx"
PAGE_CHUNK = 12
KATALOG_ID = "katalog"
PRODUCT_NAME_ID = "product-name"
PRODUCT_PRICE_ID = "product-price"
ALL_PRODUCT_REGEX = {"class": "p-total fl"}
HREF_TYPE = "a"
DIV_TYPE = "div"
SPAN_TYPE = "span"
PRODUCT_HREF = {'class': "product-item-inner fl col-12"}
product_config = {
    "product_name": {
        'type': 'h1',
        'attrs': {"class", "product-name"}
    },
    "offer": {
        'type': 'div',
        'attrs': {"class", "detay-indirim"}
    },
    "product_price": {
        'type': 'span',
        'attrs': {"class", "currencyPrice discountedPrice"}
    },
    "sale_price": {
        'type': 'span',
        'attrs': {"class", "product-price"}
    },
    "new-size-variant fl col-12 ease variantList": {
        'type': 'div',
        'attrs': {"class", "new-size-variant fl col-12 ease variantList"}
    },
}