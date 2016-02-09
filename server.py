from bottle import route, run, template
import requests
from bs4 import BeautifulSoup
import os 

URL = "http://public.mig.kz";
def forks():
    resp = requests.get(URL);
    bs4 = BeautifulSoup(resp.content, "html.parser");
    res="{";
    for tag in bs4.find_all("table"):
	for tag1 in BeautifulSoup(tag.prettify(), "html.parser").find_all("tr"):
	    r1=tag1.find("td","buy delta-neutral");
	    r2=tag1.find("td","currency");
	    res=res+"\""+r2.string+"\":  "+r1.string+", ";
	break;
    return res[0:len(res)-2]+"}";

@route('/')
def index():
    return forks();

run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))

