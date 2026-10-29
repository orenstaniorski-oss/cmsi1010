# ----------------------------------------------------------------------
# This is the file mad_libs.py
#
# The intent is to give you practice writing a complete, interactive
# Python program using a lot of Python data types, especially lists,
# sets, and dictionaries.
#
# Remove ALL of the existing comments in this file prior to submission.
# You can, and should, add your own comments, but please remove all the
# comments that are here now.
#
# Things to do:
#
# Define a bunch of templates in which some of the words begin with a colon (:).
# The words that begin with a colon are the words that you will ask the user
# to fill in. An example of a template is:
#
#     "The :color :animal :action over the :adjective :plant."
#
# You should define a list of at least 10 templates. Be creative!
#
# Your app should begin by selecting a random template. Then, for each word
# that begins with a colon in the template, prompt the user for a word
# that fits the description. Make sure that their input is between 1 and 30
# characters long, to prevent them from making too much of a mess of things.
#
# After the user has filled in all of the words, print the completed
# template with the user's words filled in. Then after a blank line, print
# a line crediting the author of the template. Then, print a couple of blank
# lines and ask them if they want to play again. If they say "yes" (or "sí"
# or "oui") or any acceptable version of an affirmative answer, start over
# with a new random template. Otherwise, say "no", print "Thanks for playing!"
# and exit the program.
#
# Here are some constraints:
#
#   1. The templates should be a list of dictionaries, in which each entry
#      has a "text" fields and an "author" field. The "text" field should
#      contain the template string, and the "author" field should contain
#      the name of the person who wrote the template.
#
#   2. The possible "yes" answers should be stored in a set.
# ----------------------------------------------------------------------
import random 

templates = [
   { "text":"A :adjective ghost is behind you!",
     "author":"class"
    },
   {"text":"Some :adjective :creature with a :weapon is eating :dessert",
    "author":"class"
    },
    {"text" : "Look! There is a :adverb :adjective :verb a :noun in :place",
     "author" : "class"
     },
    {"text":"Run! There is a :adjective :creature :verb :adverb",
     "author":"oren"  
    },
    {"text":"Avoid the :place there is a :creature inside",
      "author":"oren" 
    },
    {"text":"You need to :verb or :creature will :verb you",
     "author":"oren"    
    },
    {"text":"A :creature eats its :food at :place",
     "author":"oren"     
    },
    {"text":"Don't :verb the :creature it will :verb you :adverb",
     "author":"oren"    
    },
    {"text":"If :creature comes in here, :verb it with a :weapon",
     "author":"oren"  
    },
    {"text":"Run towards :place there is a :weapon there",
     "author":"oren"    
    } 
    
]

yes_answers = {"yes","oui","si","yup","bet","yeah"}
playing=True

while playing:
    current_template = random.choice(templates)
    string=current_template["text"]
    string=string.split()
    output=[]
    for word in string:
      if ":" in word:
        choice=input(f"Pick a {word[1:]}: ")
        if len(choice)>30:
           raise ValueError("Please input a 30 character or less word")
        output.append(choice)
      else:
        output.append(word)
    sentence= " ".join(output)
    print("""
    
     """)
    print(sentence)
    print(""" 

    """)
    print("Ad-lib written by " + current_template["author"])
    print("""

    """)
    still_playing = input("Would you like to play another round? ").lower().strip()
    while True:
      if still_playing in yes_answers:
          break
      elif still_playing.lower()=='no':
          playing=False
          print("thank you for playing")
          break 
      else:
        still_playing=input("Please say either yes or no: ")
        continue 
  
    
          







