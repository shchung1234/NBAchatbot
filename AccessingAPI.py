import requests
import json

official = requests.get("http://api.espn.com/v1/sports/basketball/nba/news/headlines")
news = requests.get("http://site.api.espn.com/apis/site/v2/sports/basketball/nba/news")
inj = requests.get("http://site.api.espn.com/apis/site/v2/sports/basketball/nba/injuries")


if __name__ == "__main__":
  print(official.status_code) #this is the official espn api keys but this doesn't work because we don't have api key
  print(news.status_code) #200 means it went okay
  print(inj.status_code) #this is okay too
  print(json.dumps(news.json(), sort_keys=True, indent=4))