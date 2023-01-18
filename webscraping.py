from bs4 import BeautifulSoup
import requests

url = "https://wuzzuf.net/search/jobs/?q=python&a=navbg"
result = requests.get(url)

#print(result.text)
doc = BeautifulSoup(result.text,"html.parser")

job_title = doc.find_all(class_="css-o171kl")[0]
job_title_text = job_title.find_all("/a")
print(job_title_text)