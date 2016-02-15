import requests

text = """
Its awesome being able to sit together with all of your friends for X event, but you can really only interact with people in your immediate vicinity. The people on the ends cant really talk to each other without shouting over 5 people.\n\nSplitting up your group into 2 rows would make for a better experience. Not always possible if you are late to get tickets though. Then you get what you can.
"""

payload = {'q': "select * from contentanalysis.analyze where text='{text}'".format(text=text)}
r = requests.post("http://query.yahooapis.com/v1/public/yql", data=payload)
print(r.text)
