#April Fuentes
#1/20
#quotable quotes

import random

def quote():
    quotes = ("you can be like me lighting mcqueen kachow- Garion Cox",\
          "good born- Chloe Spilker",\
          "why does your church people want to eat children that seems like an unholy thing to do - anonymous",\
          "School is soup and I am fork- April Fuentes")

    numQuotes = len(quotes)
    index = random.randrange(0, numQuotes)
    print(quotes[index])
    return

quote()


          
