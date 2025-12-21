# Write a function that when given a URL as a string, parses out just the domain name and returns it as a string. For example:

# * url = "http://github.com/carbonfive/raygun" -> domain name = "github"
# * url = "http://www.zombie-bites.com"         -> domain name = "zombie-bites"
# * url = "https://www.cnet.com"                -> domain name = cnet"


def domain_name(url):
    if "//" not in url and "www" not in url:
        return url.split(".")[0]
    if url[0:4] == "www.":
        return url.split(".")[1]
    elif url.split("//")[1].split(".")[0] == "www":
        return url.split("//")[1].split(".")[1]
    else:
        return url.split("//")[1].split(".")[0]



print(domain_name("www.xakep.ru"))
