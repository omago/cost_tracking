import urllib
import urllib2
import cookielib
from lxml import html

cj = cookielib.CookieJar()

opener = urllib2.build_opener(
    urllib2.HTTPCookieProcessor(cj),
    urllib2.HTTPHandler(debuglevel=1)
)

login_url = "http://10.70.52.56:8000/account/login/"

login_form = opener.open(login_url).read()
csrf_token = html.fromstring(login_form).xpath(
    '//input[@name="csrfmiddlewaretoken"]/@value'
)[0]

# make values dict
values = {
    "username": "admin",
    "password": "fba82mka",
    "csrfmiddlewaretoken": csrf_token,
}

# Convert to params
params = urllib.urlencode(values)

login_page = opener.open(login_url, params)

# run sync
sync_page = opener.open("http://10.70.52.56:8000/sync-tables/")