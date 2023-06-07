import random
from http.cookies import SimpleCookie

URL = 'https://www.zillow.com/search/GetSearchPageState.htm?searchQueryState=%7B%22pagination%22%3A%7B%22currentPage%22%3A4%7D%2C%22usersSearchTerm%22%3A%22Miami%2C%20FL%22%2C%22mapBounds%22%3A%7B%22west%22%3A-80.58081920019531%2C%22east%22%3A-80.10703379980468%2C%22south%22%3A25.508587084877135%2C%22north%22%3A25.89713312722698%7D%2C%22mapZoom%22%3A11%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A12700%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Afalse%2C%22filterState%22%3A%7B%22isForSaleForeclosure%22%3A%7B%22value%22%3Afalse%7D%2C%22isAllHomes%22%3A%7B%22value%22%3Atrue%7D%2C%22isAuction%22%3A%7B%22value%22%3Afalse%7D%2C%22isNewConstruction%22%3A%7B%22value%22%3Afalse%7D%2C%22isForRent%22%3A%7B%22value%22%3Atrue%7D%2C%22isForSaleByOwner%22%3A%7B%22value%22%3Afalse%7D%2C%22isComingSoon%22%3A%7B%22value%22%3Afalse%7D%2C%22isForSaleByAgent%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D&wants={%22cat1%22:[%22listResults%22]}'

user_agent_list = [
    # Chrome
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (Windows NT 5.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'
    # Firefox
    'Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1)',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)',
    'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 6.2; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/5.0)',
    'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)',
    'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)',
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)',
    'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:59.0) Gecko/20100101 Firefox/59.0'
]


def get_random_agent():
    return random.choice(user_agent_list)

def cookie_parser():
    cookie_string = 'zguid=24|%2426fda719-f9f3-41aa-b116-8b40eb84b351; zgsession=1|886ced83-a8c3-46e4-95b1-71e11b464767; _ga=GA1.2.1270271591.1686090834; _gid=GA1.2.1149577032.1686090834; _gcl_au=1.1.1498208370.1686090835; DoubleClickSession=true; zjs_anonymous_id=%2226fda719-f9f3-41aa-b116-8b40eb84b351%22; zjs_user_id=null; zg_anonymous_id=%22c45fc7ff-00ca-4933-b8f3-58d5b8f494ef%22; pxcts=381e7a0b-04ba-11ee-a308-4b50624a5362; _pxvid=381e67a1-04ba-11ee-a308-ee002c5c549b; tfpsi=46d8e0c4-c8d0-46fe-95f8-6ff602be30b3; __pdst=51c5e52a116044869421dd5d6cccda11; _clck=1w6svn5|2|fc8|0|1252; _pin_unauth=dWlkPU9XRmhZekV6WlRrdFl6Z3lOUzAwT0dSaExXRm1NRGd0TXpFME9URXhZbVEwTXpWaw; _fbp=fb.1.1686090838272.1078555541; JSESSIONID=4CAF0AD87BEE08246E8E72A4E7323B6C; FSsampler=59270056; _hp2_id.1215457233=%7B%22userId%22%3A%224311108766307703%22%2C%22pageviewId%22%3A%22204608929926680%22%2C%22sessionId%22%3A%223427725601255684%22%2C%22identity%22%3Anull%2C%22trackerVersion%22%3A%224.0%22%7D; __gads=ID=e9befc4a0ff3ae5d:T=1686090861:RT=1686093686:S=ALNI_MZ3W6qkze41vtgMZEg8swQiK49mIQ; __gpi=UID=000009f4eeeff802:T=1686090861:RT=1686093686:S=ALNI_MYkfa9hf_62dEPnhWwoCrwXRhs5PA; _pxff_cc=U2FtZVNpdGU9TGF4Ow==; _pxff_cfp=1; _pxff_bsco=1; _px3=f57cc55a8fdafda0e954c46160f47282f8925effdb676ec370e654fe8ac14df0:RYac8Myy85YyiIPGP+h2QONreOT4UjgsgyE+jlqN6Xsd8oEOXkw6c/7wWsc1xO5ZSk9D0jq+C3rjC/rpBRDv7Q==:1000:EJ8FAyvfkpTpu7lkOGHdc9RbM9zFwFRdvyJKi+71jri3vL7ghL2e8Eh5OaePNoXLg7wRWv6Ewtge/9TgnJSudBZwNUotARmTxSghifGBaPmONK/kAd8IXb+ENltiRq0EpTeelS69kolJgxA9Nv0q3MRp3DsXgIat+FtTVr56Z6JNqRKcsNLL3Y2FWkM7BAY6anf/IxYFyuGuSesFfXK/yw==; _uetsid=39a9f0b004ba11eeb7f6cff521211507; _uetvid=39a9fb2004ba11eea4f09f1e0cc3a659; AWSALB=cr9LmezI15wT5+oZNZIrvDpA9nSs6yPQvt9jQouveYYCZ/YAjjHB/3gpGmGFlu6+H94vSHicDYX7D6QG0bgRQNHbwpdB/HJOKEl6eW3mCJuBigVYKIWjsg6mliCG; AWSALBCORS=cr9LmezI15wT5+oZNZIrvDpA9nSs6yPQvt9jQouveYYCZ/YAjjHB/3gpGmGFlu6+H94vSHicDYX7D6QG0bgRQNHbwpdB/HJOKEl6eW3mCJuBigVYKIWjsg6mliCG; search=6|1688685893965%7Crect%3D25.89713312722698%252C-80.10703379980468%252C25.508587084877135%252C-80.58081920019531%26rid%3D12700%26disp%3Dmap%26mdm%3Dauto%26p%3D2%26z%3D1%26listPriceActive%3D1%26fs%3D0%26fr%3D1%26mmm%3D0%26rs%3D0%26ah%3D0%26singlestory%3D0%26housing-connector%3D0%26abo%3D0%26garage%3D0%26pool%3D0%26ac%3D0%26waterfront%3D0%26finished%3D0%26unfinished%3D0%26cityview%3D0%26mountainview%3D0%26parkview%3D0%26waterview%3D0%26hoadata%3D1%26zillow-owned%3D0%263dhome%3D0%26featuredMultiFamilyBuilding%3D0%26excludeNullAvailabilityDates%3D0%26commuteMode%3Ddriving%26commuteTimeOfDay%3Dnow%09%0912700%09%09%09%09%09%09'
    cookie = SimpleCookie()
    cookie.load(cookie_string)

    cookies = {}
    for key, morsel in cookie.items():
        cookies[key] = morsel.value

    return cookies