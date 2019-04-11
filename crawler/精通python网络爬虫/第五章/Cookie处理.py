import http.cookiejar
import urllib.request
import urllib.parse



req = ''


cjar = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cjar))
urllib.request.install_opener(opener)
file=opener.open(req)