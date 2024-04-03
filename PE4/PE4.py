import wikipedia
import time
from concurrent.futures import ThreadPoolExecutor

# Part A: Sequentially download wikipedia content

# Use the wikipedia.search method to return a list of topics 
# related to 'generative artificial intelligence'.
topics = wikipedia.search("generative artificial intelligence")

start_time = time.perf_counter()

for topic in topics:
    ## assign the page contents to a variable named page using the wikipedia.page method. 
    ## Be sure to use auto_suggest=False when using this method
    page = wikipedia.page(topic, auto_suggest=False)

    ## assign the page title to a variable (using page.title)
    title = page.title

    ## retrieve the references for that page (using page.references)
    references = page.references

    ## write references to a txt file
    ## ['http://www.fastcompany.com/3042430/most-creative-people/using-toytalk-technology-new-hello-barbie-will-have-real-conversations-', 
    ## 'https://twit.tv/shows/triangulation/episodes/179/', 
    ## 'https://venturebeat.com/2015/02/23/elementals-smart-connected-toy-cognitoys-taps-ibms-watson-supercomputer-for-its-brains/',....]
    filename = title + ".txt"
    with open(filename, 'w', encoding='utf-8') as file:
        for reference in references:
            file.write(reference + "\n") # each link is in its own line

end_time = time.perf_counter()
print(f"By running the code subsequentially, it took {end_time - start_time} seconds")

# Part B: Concurrently download wikipedia content

# Use the wikipedia.search method to return a list of topics 
# related to 'generative artificial intelligence'.
topics = wikipedia.search("generative artificial intelligence")

# Create a function def wiki_dl_and_save(topic): t
def wiki_dl_and_save(topic):
    page = wikipedia.page(topic, auto_suggest=False)
    title = page.title
    references = page.references

    filename = title + ".txt"
    with open(filename, 'w', encoding='utf-8') as file:
        for reference in references:
            file.write(reference + "\n")


start_time = time.perf_counter()
with ThreadPoolExecutor() as executor:
    executor.map(wiki_dl_and_save, topics)
end_time = time.perf_counter()
print(f"By running the code concurrently, it took {end_time - start_time} seconds")
