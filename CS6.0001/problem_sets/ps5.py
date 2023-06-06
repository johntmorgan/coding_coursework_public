# 6.0001/6.00 Problem Set 5 - RSS Feed Filter
# Name:
# Collaborators:
# Time:

import feedparser
import string
import time
import threading
from project_util import translate_html
from mtTkinter import *
from datetime import datetime
import pytz


#-----------------------------------------------------------------------

#======================
# Code for retrieving and parsing
# Google and Yahoo News feeds
# Do not change this code
#======================

def process(url):
    """
    Fetches news items from the rss url and parses them.
    Returns a list of NewsStory-s.
    """
    feed = feedparser.parse(url)
    entries = feed.entries
    ret = []
    for entry in entries:
        guid = entry.guid
        title = translate_html(entry.title)
        link = entry.link
        description = translate_html(entry.description)
        pubdate = translate_html(entry.published)

        try:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %Z")
            pubdate.replace(tzinfo=pytz.timezone("GMT"))
          #  pubdate = pubdate.astimezone(pytz.timezone('EST'))
          #  pubdate.replace(tzinfo=None)
        except ValueError:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %z")

        newsStory = NewsStory(guid, title, description, link, pubdate)
        ret.append(newsStory)
    return ret

#======================
# Data structure design
#======================

class NewsStory(object):
    def __init__(self, guid, title, description, link, pubdate):
        self.guid = guid
        self.title = title
        self.description = description
        self.link = link
        self.pubdate = pubdate
    
    def get_guid(self):
        return self.guid

    def get_title(self):
        return self.title
    
    def get_description(self):
        return self.description
    
    def get_link(self):
        return self.link
    
    def get_pubdate(self):
        return self.pubdate


#======================
# Triggers
#======================

class Trigger(object):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        # DO NOT CHANGE THIS!
        raise NotImplementedError

class PhraseTrigger(Trigger):
    def __init__(self, phrase):
        self.phrase = phrase
    
    def is_phrase_in(self, text):
        lower_phrase = self.phrase.lower().split(' ')
        lower_text = text.lower()
        depunct_text = lower_text
        for char in string.punctuation:
            depunct_text = depunct_text.replace(char, ' ')
        split_text = depunct_text.split(" ")
        spaceless_list = [value for value in split_text if value != ""]
        phrase_present = False
        for list_word in spaceless_list:
            potential_phrase = spaceless_list[spaceless_list.index(list_word)\
                :spaceless_list.index(list_word) + len(lower_phrase)]
            if potential_phrase == lower_phrase:
                phrase_present = True
        return phrase_present

class TitleTrigger(PhraseTrigger):
    def __init__(self, phrase):
        PhraseTrigger.__init__(self, phrase)
        
    def evaluate(self, story):
        return self.is_phrase_in(story.get_title())

class DescriptionTrigger(PhraseTrigger):
    def __init__(self, phrase):
        PhraseTrigger.__init__(self, phrase)
        
    def evaluate(self, story):
        return self.is_phrase_in(story.get_description())

# TIME TRIGGERS

class TimeTrigger(Trigger):
    def __init__(self, string_time):
        self.time = datetime.strptime(string_time.strip(), \
            "%d %b %Y %H:%M:%S").replace(tzinfo=pytz.timezone("EST"))
    
    def get_time(self):
        return self.time
    
class BeforeTrigger(TimeTrigger):
    def __init__(self, string_time):
        TimeTrigger.__init__(self, string_time)
    
    def evaluate(self, story):
        time_convert = story.get_pubdate().replace(tzinfo=pytz.timezone("EST"))
        return time_convert < self.get_time()

class AfterTrigger(TimeTrigger):
    def __init__(self, string_time):
        TimeTrigger.__init__(self, string_time)
    
    def evaluate(self, story):
        time_convert = story.get_pubdate().replace(tzinfo=pytz.timezone("EST"))
        return time_convert > self.get_time()

class NotTrigger(Trigger):
    def __init__(self, trigger):
        self.trigger = trigger
    
    def evaluate(self, story):
        return not self.trigger.evaluate(story)

class AndTrigger(Trigger):
    def __init__(self, trigger1, trigger2):
        self.trigger1 = trigger1
        self.trigger2 = trigger2
        
    def evaluate(self, story):
        return self.trigger1.evaluate(story) and self.trigger2.evaluate(story)

class OrTrigger(Trigger):
    def __init__(self, trigger1, trigger2):
        self.trigger1 = trigger1
        self.trigger2 = trigger2

    def evaluate(self, story):
        return self.trigger1.evaluate(story) or self.trigger2.evaluate(story)

#======================
# Filtering
#======================

# Problem 10
def filter_stories(stories, triggerlist):
    """
    Takes in a list of NewsStory instances.

    Returns: a list of only the stories for which a trigger in triggerlist fires.
    """
    good_stories = []
    for story in stories:
        good_story = False
        for trigger in triggerlist:
            if trigger.evaluate(story) == True:
                good_story = True
        if good_story:
            good_stories += [story]
    return good_stories


#======================
# User-Specified Triggers
#======================
# Problem 11
def read_trigger_config(filename):
    """
    filename: the name of a trigger configuration file

    Returns: a list of trigger objects specified by the trigger configuration
        file.
    """
    # We give you the code to read in the file and eliminate blank lines and
    # comments. You don't need to know how it works for now!
    trigger_file = open(filename, 'r')
    lines = []
    for line in trigger_file:
        line = line.rstrip()
        if not (len(line) == 0 or line.startswith('//')):
            lines.append(line)
    triggers = []
    trigger_dict = {}
    for line in lines:
        entries = line.split(',')
        if entries[0] != 'ADD':
            if entries[1] == "TITLE":
                trigger_dict[entries[0]] = TitleTrigger(entries[2])
            elif entries[1] == "DESCRIPTION":
                trigger_dict[entries[0]] = [DescriptionTrigger(entries[2])]
            elif entries[1] == "AFTER":
                trigger_dict[entries[0]] = [AfterTrigger(entries[2])]
            elif entries[1] == "BEFORE":
                trigger_dict[entries[0]] = [BeforeTrigger(entries[2])]
            elif entries[1] == "AND":
                trigger_dict[entries[0]] = [trigger_dict[entries[2]],\
                                            trigger_dict[entries[3]]]
            elif entries[1] == "OR":
                trigger_dict[entries[0]] = [trigger_dict[entries[2]],\
                                            trigger_dict[entries[3]]]
            elif entries[1] == "NOT":
                trigger_dict[entries[0]] = [NotTrigger[entries[2]]]
        else:
            for entry in entries[1:len(entries) + 1]:
                triggers += trigger_dict[entry]
    print(triggers)


SLEEPTIME = 120 #seconds -- how often we poll

def main_thread(master):
    # A sample trigger list - you might need to change the phrases to correspond
    # to what is currently in the news
    try:
        t1 = TitleTrigger("election")
        t2 = DescriptionTrigger("Trump")
        t3 = DescriptionTrigger("Clinton")
        t4 = AndTrigger(t2, t3)
        triggerlist = [t1, t4]

        # Problem 11 
        triggerlist = read_trigger_config('triggers.txt')
        
        # HELPER CODE - you don't need to understand this!
        # Draws the popup window that displays the filtered stories
        # Retrieves and filters the stories from the RSS feeds
        frame = Frame(master)
        frame.pack(side=BOTTOM)
        scrollbar = Scrollbar(master)
        scrollbar.pack(side=RIGHT,fill=Y)

        t = "Google & Yahoo Top News"
        title = StringVar()
        title.set(t)
        ttl = Label(master, textvariable=title, font=("Helvetica", 18))
        ttl.pack(side=TOP)
        cont = Text(master, font=("Helvetica",14), yscrollcommand=scrollbar.set)
        cont.pack(side=BOTTOM)
        cont.tag_config("title", justify='center')
        button = Button(frame, text="Exit", command=root.destroy)
        button.pack(side=BOTTOM)
        guidShown = []
        def get_cont(newstory):
            if newstory.get_guid() not in guidShown:
                cont.insert(END, newstory.get_title()+"\n", "title")
                cont.insert(END, "\n---------------------------------------------------------------\n", "title")
                cont.insert(END, newstory.get_description())
                cont.insert(END, "\n*********************************************************************\n", "title")
                guidShown.append(newstory.get_guid())

        while True:

            print("Polling . . .", end=' ')
            # Get stories from Google's Top Stories RSS news feed
            stories = process("http://news.google.com/news?output=rss")

            # Get stories from Yahoo's Top Stories RSS news feed
            stories.extend(process("http://news.yahoo.com/rss/topstories"))

            stories = filter_stories(stories, triggerlist)

            list(map(get_cont, stories))
            scrollbar.config(command=cont.yview)


            print("Sleeping...")
            time.sleep(SLEEPTIME)

    except Exception as e:
        print(e)


if __name__ == '__main__':
    # TK broken with this version of Python, welp
    # No manual testing to see if this one works
    # But all tests passed!
    
    triggerlist = read_trigger_config('triggers.txt')
    
    # root = Tk()
    # root.title("Some RSS parser")
    # t = threading.Thread(target=main_thread, args=(root,))
    # t.start()
    # root.mainloop()

