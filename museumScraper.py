__author__ = 'kens'
import requests
import bs4
import random
import time

# you'll need to install requests and bs4, I just made a virtual environment for them. Im using python 2.7



# just trying out different pages
root_url = "http://www.walkerart.org"
index_url = root_url + '/collections/browse'
#index_url = root_url + '/collections/browse?type=Drawings+and+Watercolors'
#index_url = root_url + '/collections/browse?order=asc&order_by=Title&type=Drawings+and+Watercolors'

# this was helpful to me
# http://blog.miguelgrinberg.com/post/easy-web-scraping-with-python

# STUPID long data, had to do this because my website only loaded 40 pics at a time, so I whipped this up myself
# using word editors and grep after viewing page source
data = ['/collections/artworks/still-alive-iii', '/collections/artworks/still-alive-ii', '/collections/artworks/still-alive-i', '/collections/artworks/mr-iii', '/collections/artworks/sound-series-5', '/collections/artworks/sound-series-4', '/collections/artworks/sound-series-3', '/collections/artworks/2-dot-2-1861-from-all-your-deeds-shall-in-water-be-writ-but-this-in-marble', '/collections/artworks/rebus', '/collections/artworks/untitled-289', '/collections/artworks/untitled-number-10', '/collections/artworks/untitled-number-2-3', '/collections/artworks/untitled-number-28', '/collections/artworks/untitled-number-11', '/collections/artworks/untitled-number-15', '/collections/artworks/its-a-draw-for-robert-rauschenberg', '/collections/artworks/non-foldings-no-4', '/collections/artworks/search-for-ideas-supporting-the-black-man-as-a-work-of-modern-art-slash-contemporary-painting-a-death-without-end-an-appreciation-of-the-creative-spirit-of-lynch-mobs', '/collections/artworks/untitled-from-the-series-the-israel-diary-8', '/collections/artworks/untitled-from-the-series-the-israel-diary-7', '/collections/artworks/untitled-from-the-series-the-israel-diary-6', '/collections/artworks/untitled-from-the-series-the-israel-diary-5', '/collections/artworks/untitled-from-the-series-the-israel-diary-4', '/collections/artworks/untitled-from-the-series-the-israel-diary-3', '/collections/artworks/untitled-from-the-series-the-israel-diary-2', '/collections/artworks/untitled-from-the-series-the-israel-diary', '/collections/artworks/untitled-from-the-series-the-israel-diary-1', '/collections/artworks/score-for-7th-light', '/collections/artworks/wall-of-letters-necessary-reminders-from-the-past-for-a-future-of-choice-number-23', '/collections/artworks/wall-of-letters-necessary-reminders-from-the-past-for-a-future-of-choice-number-8', '/collections/artworks/wall-of-letters-necessary-reminders-from-the-past-for-a-future-of-choice-number-7', '/collections/artworks/wall-of-letters-necessary-reminders-from-the-past-for-a-future-of-choice-number-2', '/collections/artworks/untitled-48-portraits', '/collections/artworks/new-ulm-state-monument-minnesota', '/collections/artworks/friendly-chippewa-monument-minnesota', '/collections/artworks/long-drawing-for-walker-art-center', '/collections/artworks/fort-ridgely-state-monument-minnesota', '/collections/artworks/wallowing-in-pachuco-threads', '/collections/artworks/snacks-for-a-ventriloquist', '/collections/artworks/untitled-please-do-not-litter-from-paul-mc-meats-series-the-violence-around-us', '/collections/artworks/untitled-my-entrails-playtime-from-paul-mc-meats-series-the-violence-around-us', '/collections/artworks/untitled-essay-one-from-paul-mc-meats-series-the-violence-around-us', '/collections/artworks/untitled-come-as-you-are-from-paul-mc-meats-series-the-violence-around-us', '/collections/artworks/untitled-tocada-por-la-muerte-touched-by-death', '/collections/artworks/untitled-tina-of-broadlands', '/collections/artworks/untitled-prelude-to-summer', '/collections/artworks/untitled-pescando-fishing', '/collections/artworks/untitled-pajaros-birds', '/collections/artworks/untitled-la-muerte-death', '/collections/artworks/untitled-diablito-en-la-espalda-little-devil-on-the-back', '/collections/artworks/olux', '/collections/artworks/untitled-2185', '/collections/artworks/untitled-2184', '/collections/artworks/pictures-of-what-happens-on-each-page-of-thomas-pynchons-novel-gravitys-rainbow', '/collections/artworks/untitled-111', '/collections/artworks/bend-sinister', '/collections/artworks/study-for-gulf-stream', '/collections/artworks/untitled-water-study-for-gulf-stream-2', '/collections/artworks/untitled-water-study-for-gulf-stream-1', '/collections/artworks/untitled-water-study-for-gulf-stream', '/collections/artworks/untitled-figure-study-for-gulf-stream-3', '/collections/artworks/improvised-structure-number-43', '/collections/artworks/improvised-structure-number-38', '/collections/artworks/quartet-forming', '/collections/artworks/mas-4', '/collections/artworks/untitled-230', '/collections/artworks/untitled-figure-study-for-gulf-stream-2', '/collections/artworks/untitled-figure-study-for-gulf-stream-1', '/collections/artworks/untitled-figure-study-for-gulf-stream', '/collections/artworks/improvised-structure-number-9', '/collections/artworks/improvised-structure-number-3', '/collections/artworks/improvised-structure-number-2', '/collections/artworks/improvised-structure-number-1', '/collections/artworks/el-hajj-malik-el-shabazz-malcolm-x-malcolm-little', '/collections/artworks/green-slash-white-drawing-number-2', '/collections/artworks/homunc-04', '/collections/artworks/untitled-from-the-passing-slash-posing-series', '/collections/artworks/up-north-slash-down-south', '/collections/artworks/underground-connections', '/collections/artworks/levels-of-communications', '/collections/artworks/level-flip-slash-high-and-low', '/collections/artworks/leonard-peltier-is-still-in-prison', '/collections/artworks/wishin-all-these-old-things-were-new', '/collections/artworks/the-cold-hard-truth', '/collections/artworks/i-learned-them-sad-songs-early-on', '/collections/artworks/every-day-above-ground-is-a-good-one', '/collections/artworks/hen-house', '/collections/artworks/untitled-first-flower-drawing-done-by-foot', '/collections/artworks/frozen-ghost', '/collections/artworks/untitled-2178', '/collections/artworks/covered-car-missouri-street', '/collections/artworks/covered-car-high-street', '/collections/artworks/20th-and-mississippi-night', '/collections/artworks/untitled-11', '/collections/artworks/untitled-2157', '/collections/artworks/untitled-2154', '/collections/artworks/untitled-2153', '/collections/artworks/endless-conundrum-an-african-anonymous-adventuress', '/collections/artworks/blue-serie-women-against-war', '/collections/artworks/blue-serie-profit-warning', '/collections/artworks/blue-serie-no-society', '/collections/artworks/blue-serie-junior-thesis-senior-thesis', '/collections/artworks/blue-serie-globalization-from-below', '/collections/artworks/blue-serie-engagement', '/collections/artworks/blue-serie-c', '/collections/artworks/blue-serie-body-mass-index-b-dot-m-i-dot', '/collections/artworks/blue-serie-acephale-headless', '/collections/artworks/blue-serie-a-repeat', '/collections/artworks/storyteller', '/collections/artworks/speak', '/collections/artworks/omnipotent', '/collections/artworks/matriarch', '/collections/artworks/futurist', '/collections/artworks/feminine-way', '/collections/artworks/debutante', '/collections/artworks/combined-wisdom', '/collections/artworks/atlas', '/collections/artworks/ein-schloss-in-trummem-a-castle-in-trummem', '/collections/artworks/house-upside-down', '/collections/artworks/bbq-pit', '/collections/artworks/e-t-c', '/collections/artworks/untitled-2175', '/collections/artworks/untitled-2174', '/collections/artworks/untitled-2173', '/collections/artworks/untitled-2172', '/collections/artworks/untitled-2170', '/collections/artworks/untitled-2169', '/collections/artworks/untitled-2167', '/collections/artworks/untitled-2166', '/collections/artworks/untitled-2165', '/collections/artworks/untitled-2163', '/collections/artworks/untitled-2162', '/collections/artworks/untitled-2161', '/collections/artworks/untitled-2160', '/collections/artworks/untitled-2158', '/collections/artworks/untitled-2155', '/collections/artworks/untitled-2151', '/collections/artworks/carta-faminta-starving-letters', '/collections/artworks/portrait-of-emily', '/collections/artworks/within-the-marzipan-confection', '/collections/artworks/under-sweet-dreams', '/collections/artworks/they-drew-first-blood', '/collections/artworks/marzipan-the-hidden-conflict', '/collections/artworks/marzipan-defenders', '/collections/artworks/making-warrior-marzipan', '/collections/artworks/imagine-a-world-without-marzipan', '/collections/artworks/human-slash-marzipan-experiments', '/collections/artworks/heart-of-marzipan', '/collections/artworks/chains-of-marzipan', '/collections/artworks/park-city-grill', '/collections/artworks/bent-guitar', '/collections/artworks/unnecessary-roughness', '/collections/artworks/untitled-ivb', '/collections/artworks/portrait-of-julie-h', '/collections/artworks/untitled-2221', '/collections/artworks/untitled-2218', '/collections/artworks/untitled-2223', '/collections/artworks/untitled-2224', '/collections/artworks/untitled-2214', '/collections/artworks/untitled-2222', '/collections/artworks/untitled-2191', '/collections/artworks/untitled-2190', '/collections/artworks/untitled-2189', '/collections/artworks/the-modernists', '/collections/artworks/untitled-2168', '/collections/artworks/untitled-2164', '/collections/artworks/farnsworth-house', '/collections/artworks/aktiengesellschaft-pavilloneinheiten-austria-1956-corporate-pavilion-unit-austria-1956', '/collections/artworks/untitled-272', '/collections/artworks/battlefield', '/collections/artworks/untitled-2176', '/collections/artworks/untitled-2171', '/collections/artworks/untitled-2159', '/collections/artworks/untitled-2156', '/collections/artworks/untitled-2152', '/collections/artworks/urban-cocktail', '/collections/artworks/untitled-2150', '/collections/artworks/one-minute-sculpture-1', '/collections/artworks/one-minute-sculpture', '/collections/artworks/do-you-like-creme-in-your-coffee-and-chocolate-in-your-milk', '/collections/artworks/red-riding-hood-studies', '/collections/artworks/a-diary-of-flowers-in-love', '/collections/artworks/untitled-110', '/collections/artworks/el-daddio-portrait-of-bruce-t', '/collections/artworks/untitled-109', '/collections/artworks/do-it', '/collections/artworks/john-lennon', '/collections/artworks/total-excitement', '/collections/artworks/wavy-brushstrokes-1', '/collections/artworks/wall-drawing-number-9-a-and-b', '/collections/artworks/untitled-282', '/collections/artworks/untitled-271', '/collections/artworks/wavy-brushstrokes', '/collections/artworks/evolution-number-3', '/collections/artworks/untitled-287', '/collections/artworks/kurt-lilliput', '/collections/artworks/untitled-words-too-heavy-for-my-head', '/collections/artworks/untitled-the-oppressor-slash-oppressed-paradigm', '/collections/artworks/untitled-free-northern-girls', '/collections/artworks/untitled-final-solutions', '/collections/artworks/untitled-emancipation-proclaimation', '/collections/artworks/untitled-destroying-the-terror', '/collections/artworks/untitled-2065', '/collections/artworks/untitled-2200', '/collections/artworks/envelopa-drawing-restraint-7-manual-d', '/collections/artworks/untitled-229', '/collections/artworks/untitled-277', '/collections/artworks/no-title-the-bad-are-swept', '/collections/artworks/no-title-whirrrrr-not-too', '/collections/artworks/irregular-vertical-bands-zig-zag', '/collections/artworks/study-for-bits-and-pieces-put-together-to-present-a-semblance-of-a-whole', '/collections/artworks/rirkrit', '/collections/artworks/no-title-the-directors-ass', '/collections/artworks/form-derived-from-a-cubic-rectangle', '/collections/artworks/no-title-these-indeed-are', '/collections/artworks/rolling-stock-series-no-21-for-jeanne', '/collections/artworks/rolling-stock-series-no-11-for-kyle', '/collections/artworks/rolling-stock-series-no-21-for-jeanne-1', '/collections/artworks/rolling-stock-series-no-22-for-bill', '/collections/artworks/no-title-my-god-was', '/collections/artworks/revival-field', '/collections/artworks/vertical-lines-not-straight-not-touching', '/collections/artworks/revival-field-projection-and-procedure', '/collections/artworks/ohne-titel-untitled-5', '/collections/artworks/untitled-1995', '/collections/artworks/untitled-1994', '/collections/artworks/untitled-213', '/collections/artworks/rolling-stock-series-no-8-for-jane', '/collections/artworks/no-title-we-almost-made-it-out-of-kansas', '/collections/artworks/no-title-the-baby-daughter', '/collections/artworks/a-square-with-two-even-vertical-bands-with-colors-superimposed', '/collections/artworks/laments', '/collections/artworks/layering-of-worlds', '/collections/artworks/drawing-for-round-house', '/collections/artworks/drawing-away-the-national-art-gallery', '/collections/artworks/untitled-hitlers-bedroom-the-reich-chancellery-bunker-berlin-1939', '/collections/artworks/rolling-stock-series-no-5-pool-car', '/collections/artworks/rolling-stock-series-no-2-miner', '/collections/artworks/rolling-stock-series-no-4-for-chuck', '/collections/artworks/no-title-vavoom-the-chord', '/collections/artworks/no-title-why-are-we-killing', '/collections/artworks/view-of-spoonbridge-and-cherry-with-sailboat-and-skater', '/collections/artworks/untitled-study-for-the-sculpture-spoonbridge-and-cherry-2', '/collections/artworks/maquette-for-crosswalk-lines-in-two-directions-between-walker-art-center-and-the-minneapolis-sculpture-garden-6', '/collections/artworks/maquette-for-crosswalk-lines-in-two-directions-between-walker-art-center-and-the-minneapolis-sculpture-garden-5', '/collections/artworks/maquette-for-crosswalk-lines-in-two-directions-between-walker-art-center-and-the-minneapolis-sculpture-garden-4', '/collections/artworks/maquette-for-crosswalk-lines-in-two-directions-between-walker-art-center-and-the-minneapolis-sculpture-garden-3', '/collections/artworks/maquette-for-crosswalk-lines-in-two-directions-between-walker-art-center-and-the-minneapolis-sculpture-garden-schematic-drawing-of-4-1-slash-4-circles', '/collections/artworks/maquette-for-crosswalk-lines-in-two-directions-between-walker-art-center-and-the-minneapolis-sculpture-garden-schematic-drawing-for-four-rectangles', '/collections/artworks/maquette-for-crosswalk-lines-in-two-directions-between-walker-art-center-and-the-minneapolis-sculpture-garden-2', '/collections/artworks/maquette-for-crosswalk-lines-in-two-directions-between-walker-art-center-and-the-minneapolis-sculpture-garden-1', '/collections/artworks/maquette-for-crosswalk-lines-in-two-directions-between-walker-art-center-and-the-minneapolis-sculpture-garden', '/collections/artworks/blue-heart-2', '/collections/artworks/no-title-where-was-i', '/collections/artworks/no-title-he-allowed-her', '/collections/artworks/ohne-titel-untitled-2', '/collections/artworks/19-834-days', '/collections/artworks/forgiving', '/collections/artworks/study-for-prophecy-of-the-ancients', '/collections/artworks/drawing-for-without-words', '/collections/artworks/untitled-334', '/collections/artworks/study-for-garden-seating-reading-thinking-2', '/collections/artworks/study-for-garden-seating-reading-thinking-1', '/collections/artworks/the-castleton', '/collections/artworks/untitled-joke', '/collections/artworks/vanilla-nightmares-number-10', '/collections/artworks/vanilla-nightmares-number-9', '/collections/artworks/vanilla-nightmares-number-3', '/collections/artworks/schema-32', '/collections/artworks/double-hear-me', '/collections/artworks/untitled-study-for-the-sculpture-spoonbridge-and-cherry-1', '/collections/artworks/untitled-study-for-the-sculpture-spoonbridge-and-cherry', '/collections/artworks/notebook-page-study-for-the-sculpture-spoonbridge-and-cherry', '/collections/artworks/his-face', '/collections/artworks/untitled-drawing-for-enduring-charms', '/collections/artworks/samurai-jogger', '/collections/artworks/untitled-19', '/collections/artworks/serre-ii', '/collections/artworks/serre-i', '/collections/artworks/axonometric-drawing-and-floor-plan-of-the-reflecting-space-from-the-exhibition-tokyo-form-and-spirit']

def get_individual_urls():
    response = requests.get(index_url)
    soup = bs4.BeautifulSoup(response.text)
    return [a.attrs.get('href') for a in soup.select('div.clearfix a[href^=/collections/artworks]')]

# Date Randomizer use in format mm/dd/year hr:min _m
def strTimeProp(start, end, format, prop):
    stime = time.mktime(time.strptime(start, format))
    etime = time.mktime(time.strptime(end, format))
    ptime = stime + prop * (etime - stime)
    return time.strftime(format, time.localtime(ptime))

def randomDate(start, end, prop):
    return strTimeProp(start, end, '%m/%d/%Y', prop)
    #return strTimeProp(start, end, '%m/%d/%Y %I:%M %p', prop) // use this one for hour,min



artwork = (get_individual_urls())


# can use this to test it on one thing at a time instead of the whole website
"""
#print artwork[15] + '\n'
page = requests.get(root_url + artwork[15])
tree = html.fromstring(page.text)
response = requests.get(root_url+artwork[15])
soup = bs4.BeautifulSoup(response.text)

print "This will play with soup:"

title = soup.find('div', class_='detail_title').find('dt', text='Title').find_next_sibling('dd').text.strip()
artist = soup.find('div', class_='detail_artist').find('dt', text='Artist').find_next_sibling('dd').text.strip()
date = soup.find('div', class_='detail_date').find('dt', text='Date').find_next_sibling('dd').text.strip()
type = soup.find('div', class_='dl_item_container clearfix').find('dt', text='Type').find_next_sibling('dd').text.strip()
accessionNumber = soup.find('dt', text='Accession Number').find_next_sibling('dd').text.strip()
physicalDescription = soup.find('dt', text='Physical Description').find_next_sibling('dd').text.strip()
materials = soup.find('dt', text='Materials').find_next_sibling('dd').text.strip()
print title + "\t" + artist + "\t" + date + "\t" + type + "\t" + accessionNumber + "\t" + physicalDescription + "\t" + materials + "\n"
"""



print 'This will print out the information I need in a tabulated form:'


#info. if you had artwork in here instead it would tell you how many URLs artwork picked up
print len(data)
print data


# you can use artwork if the museum web page loads more than like 30-40 pics at a time
# just user
# for a in range(0,len(artwork)
#

# you could maybe insert a random number generator to add the "price" of the artwork.

for a in range(0,len(data)):
    page = requests.get(root_url + data[a])
    response = requests.get(root_url+data[a])
    soup = bs4.BeautifulSoup(response.text)

    # I use this to check the entire HTML file to make sure that it has the words I require
    check = soup.prettify()
    words = ['detail_title', 'Artist', 'Date', 'Type', 'Accession Number', 'Physical Description', 'Materials']

    if all(x in check for x in words):
        title = soup.find('div', class_='detail_title').find('dt', text='Title').find_next_sibling('dd').text.strip()
        artist = soup.find('div', class_='detail_artist').find('dt', text='Artist').find_next_sibling('dd').text.strip()
        date = soup.find('div', class_='detail_date').find('dt', text='Date').find_next_sibling('dd').text.strip()
        type = soup.find('div', class_='dl_item_container clearfix').find('dt', text='Type').find_next_sibling('dd').text.strip()
        accessionNumber = soup.find('dt', text='Accession Number').find_next_sibling('dd').text.strip()
        physicalDescription = soup.find('dt', text='Physical Description').find_next_sibling('dd').text.strip()
        materials = soup.find('dt', text='Materials').find_next_sibling('dd').text.strip()
        insuranceValue = random.randrange(1,1000000)
        dateAcquired = randomDate("7/1/1990", "09/20/2014", random.random())

        print title + "\t" + artist + "\t" + date + "\t" + type + "\t" + accessionNumber + "\t" + physicalDescription + "\t" + materials + "\t" + str(insuranceValue) + "\t" + dateAcquired + "\n"



