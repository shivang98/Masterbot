from urllib.parse import urlparse


# get the domain name
def get_domain_name(url):
    try:
        results = get_sub_domain(url).split('.')
        return results[-2] + '.' + results[-1]
    except:
        return ''

# get subdomain (name.example.com)
def get_sub_domain(url):
    try:
        return urlparse(url).netloc
    except:
        return ''
