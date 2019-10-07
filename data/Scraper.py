from selenium import webdriver
from BeautifulSoup import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


# options = webdriver.ChromeOptions()
# options.add_argument("--incognito")
# capabilities = options.to_capabilities()
# driver = webdriver.Chrome(ChromeDriverManager().install(),desired_capabilities=capabilities)
driver = webdriver.Chrome(ChromeDriverManager().install())
baseUrl = "https://www.infoplease.com/arts-entertainment/movies-and-videos/top-100-movie-quotes"
driver.get(baseUrl)


content = driver.page_source
soup = BeautifulSoup(content)
print soup


o = []
for li in soup.findAll('li',attrs={'dir':"ltr"}):
    o.append(li.find('p').text)

print o

data = []
year = []
title = []


#o= [u"\u201cFrankly, my dear, I don't give a damn.\u201dGone With the Wind, 1939", u"\u201cI'm going to make him an offer he can't refuse.\u201dThe Godfather, 1972&nbsp;Fun fact: This line makes it into eachGodfatherfilm in some way or another.", u"\u201cYou don't understand! I coulda had class. I coulda been a contender. I could've been somebody, instead of a bum, which is what I am.\u201dOn the Waterfront, 1954", u"\u201cToto, I've got a feeling we're not in Kansas anymore.\u201dThe Wizard of Oz, 1939Fun fact: As one of the most famous movie quotes&nbsp;in film&nbsp;history, this line has been parodied by many&nbsp;different movies and television shows. &nbsp;", u"\u201cHere's looking at you, kid.\u201dCasablanca, 1942", u'\u201cGo ahead, make my day.\u201dSudden Impact, 1983', u"\u201cAll right, Mr. DeMille, I'm ready for my close-up.\u201dSunset Blvd., 1950", u'\u201cMay the Force be with you.\u201dStar Wars, 1977', u"\u201cFasten your seatbelts. It's going to be a bumpy night.\u201dAll About Eve, 1950", u'\u201cYou talking to me?\u201dTaxi Driver, 1976Fun fact: Robert DeNiro improvised this line. The script only said&nbsp;"Travis speaks to himself in the mirror" so DeNiro took some liberties and was ultimately successful.', u"\u201cWhat we've got here is failure to communicate.\u201dCool Hand Luke, 1967", u'\u201cI love the smell of napalm in the morning.\u201dApocalypse Now, 1979', u'\u201cLove means never having to say you\'re sorry.\u201dLove Story, 1970Fun fact: Two years later Ryan O\'Neal will hear this line again in the filmWhat\'s Up Doc&nbsp;when Barbara Streisand says it to his character&nbsp;and respond, "That\'s the dumbest thing I\'ve ever heard."', u'\u201cThe stuff that dreams are made of.\u201dThe Maltese Falcon, 1941', u'\u201cE.T. phone home.\u201dE.T. The Extra-Terrestrial, 1982', u'\u201cThey call me Mister Tibbs!\u201dIn the Heat of the Night, 1967', u'\u201cRosebud.\u201dCitizen Kane, 1941', u'\u201cMade it, Ma! Top of the world!\u201dWhite Heat, 1949', u"\u201cI'm as mad as hell, and I'm not going to take this anymore!\u201dNetwork, 1976", u'\u201cLouis, I think this is the beginning of a beautiful friendship.\u201dCasablanca, 1942', u'\u201cA census taker once tried to test me. I ate his liver with some fava beans and a nice Chianti.\u201dThe Silence of the Lambs, 1991', u'\u201cBond. James Bond.\u201dDr. No, 1962', u"\u201cThere's no place like home.\u201dThe Wizard of Oz, 1939", u"\u201cI am big! It's the pictures that got small.\u201dSunset Blvd., 1950", u'\u201cShow me the money!\u201dJerry Maguire, 1996', u"\u201cWhy don't you come up sometime and see me?\u201dShe Done Him Wrong, 1933", u"\u201cI'm walking here! I'm walking here!\u201dMidnight Cowboy, 1969", u"\u201cPlay it, Sam. Play 'As Time Goes By.'\u201dCasablanca, 1942", u"\u201cYou can't handle the truth!\u201dA Few Good Men, 1992", u'\u201cI want to be alone.\u201dGrand Hotel, 1932', u'\u201cAfter all, tomorrow is another day!\u201dGone With the Wind, 1939', u'\u201cRound up the usual suspects.\u201dCasablanca, 1942', u"\u201cI'll have what she's having.\u201dWhen Harry Met Sally, 1989", u"\u201cYou know how to whistle, don't you, Steve? You just put your lips together and blow.\u201dTo Have and Have Not, 1944", u"\u201cYou're gonna need a bigger boat.\u201dJaws, 1975", u"\u201cBadges? We ain't got no badges! We don't need no badges! I don't have to show you any stinking badges!\u201dThe Treasure of the Sierra Madre, 1948", u"\u201cI'll be back.\u201dThe Terminator, 1984", u'\u201cToday, I consider myself the luckiest man on the face of the earth.\u201dThe Pride of the Yankees, 1942', u'\u201cIf you build it, he will come.\u201dField of Dreams, 1989', u"\u201cMama always said life was like a box of chocolates. You never know what you're gonna get.\u201dForrest Gump, 1994", u'\u201cWe rob banks.\u201dBonnie and Clyde, 1967', u'\u201cPlastics.\u201dThe Graduate, 1967', u"\u201cWe'll always have Paris.\u201dCasablanca, 1942", u"\u201cI see dead people.\u201dThe Sixth Sense, 1999Fun fact: When Haley Joel Osmet says this line the camera goes to Bruce Willis's face. This is a cinematic clue that Bruce Willis's character is dead.", u'\u201cStella! Hey, Stella!\u201d A Streetcar Named Desire, 1951', u"\u201cOh, Jerry, don't let's ask for the moon. We have the stars.\u201dNow, Voyager, 1942", u'\u201cShane. Shane. Come back!\u201dShane, 1953', u"\u201cWell, nobody's perfect.\u201dSome Like It Hot, 1959", u'\u201cIt\'s alive! It\'s alive!\u201dFrankenstein, 1931Fun fact:&nbsp;The original line was "It\'s alive! It\'s alive! In the name of God! Now I know what it\'s like to be God!"\u200b\u200b\u200b&nbsp;Censors cut Dr. Frankenstein\'s full line because it was considered sacrilege.', u'\u201cHouston, we have a problem.\u201dApollo 13, 1995', u"\u201cYou've got to ask yourself one question: 'Do I feel lucky?' Well, do ya, punk?\u201dDirty Harry, 1971", u'\u201cYou had me at \u2018hello.\u2019\u201dJerry Maguire, 1996', u"\u201cOne morning I shot an elephant in my pajamas. How he got in my pajamas, I don't know.\u201dAnimal Crackers, 1930", u"\u201cThere's no crying in baseball!\u201dA League of Their Own, 1992", u'\u201cLa-dee-da, la-dee-da.\u201dAnnie Hall, 1977', u"\u201cA boy's best friend is his mother.\u201dPsycho, 1960", u'\u201cGreed, for lack of a better word, is good.\u201dWall Street, 1987', u'\u201cKeep your friends close, but your enemies closer.\u201dThe Godfather II, 1974', u"\u201cAs God is my witness, I'll never be hungry again.\u201dGone With the Wind, 1939", u"\u201cWell, here's another nice mess you've gotten me into!\u201dSons of the Desert, 1933", u'\u201cSay \u201chello\u201d to my little friend!\u201dScarface, 1983', u'\u201cWhat a dump.\u201dBeyond the Forest, 1949', u"\u201cMrs. Robinson, you're trying to seduce me. Aren't you?\u201dThe Graduate, 1967", u'\u201cGentlemen, you can\'t fight in here! This is the War Room!"Dr. Strangelove, 1964', u'\u201cElementary, my dear Watson.\u201dThe Adventures of Sherlock Holmes, 1929Fun fact:&nbsp;Sherlock Holmes never says this iconic quote in any of the books the character is based off of.', u'\u201cGet your stinking paws off me, you damned dirty ape.\u201dPlanet of the Apes, 1968', u'\u201cOf all the gin joints in all the towns in all the world, she walks into mine.\u201dCasablanca, 1942', u"\u201cHere's Johnny!\u201dThe Shining, 1980", u"\u201cThey're here!\u201dPoltergeist, 1982", u'\u201cIs it safe?\u201dMarathon Man, 1976', u"\u201cWait a minute, wait a minute. You ain't heard nothin' yet!\u201dThe Jazz Singer, 1927", u'\u201cNo wire hangers, ever!\u201dMommie Dearest, 1981', u'\u201cMother of mercy, is this the end of Rico?\u201dLittle Caesar, 1930', u"\u201cForget it, Jake, it's Chinatown.\u201dChinatown, 1974", u'\u201cI have always depended on the kindness of strangers.\u201dA Streetcar Named Desire, 1951', u'\u201cHasta la vista, baby.\u201dTerminator 2: Judgment Day, 1991\u200b\u200b\u200b\u200b\u200b', u'\u201cSoylent Green is people!\u201dSoylent Green, 1973', u'\u201cOpen the pod bay doors, HAL.\u201d2001: A Space Odyssey, 1968', u"Striker: Surely you can't be serious.", u'\u201cYo, Adrian!\u201dRocky, 1976', u'\u201cHello, gorgeous.\u201dFunny Girl, 1968', u"\u201cToga! Toga!\u201dNational Lampoon's Animal House, 1978", u'\u201cListen to them. Children of the night. What music they make.\u201dDracula, 1931', u"\u201cOh, no, it wasn't the airplanes. It was Beauty killed the Beast.\u201dKing Kong, 1933", u'\u201cMy precious.\u201dThe Lord of the Rings: Two Towers, 2002', u'\u201cAttica! Attica!\u201dDog Day Afternoon, 1975', u"\u201cSawyer, you're going out a youngster, but you've got to come back a star!\u201d42nd Street, 1933", u"\u201cListen to me, mister. You're my knight in shining armor. Don't you forget it. You're going to get back on that horse, and I'm going to be right behind you, holding on tight, and away we're gonna go, go, go!\u201dOn Golden Pond, 1981", u"\u201cTell 'em to go out there with all they got and win just one for the Gipper.\u201dKnute Rockne All American, 1940", u'\u201cA martini. Shaken, not stirred.\u201dGoldfinger, 1964', u"\u201cWho's on first.\u201dThe Naughty Nineties, 1945", u"\u201cCinderella story. Outta nowhere. A former greenskeeper, now, about to become the Masters champion. It looks like a mirac...It's in the hole! It's in the hole! It's in the hole!\u201dCaddyshack, 1980", u'\u201cLife is a banquet, and most poor suckers are starving to death!\u201dAuntie Mame, 1958', u'\u201cI feel the need - the need for speed!\u201dTop Gun, 1986', u'\u201cCarpe diem. Seize the day, boys. Make your lives extraordinary.\u201dDead Poets Society, 1989', u'\u201cSnap out of it!\u201dMoonstruck, 1987', u'\u201cMy mother thanks you. My father thanks you. My sister thanks you. And I thank you.\u201dYankee Doodle Dandy, 1942', u'\u201cNobody puts Baby in a corner.\u201dDirty Dancing, 1987', u"\u201cI'll get you, my pretty, and your little dog, too!\u201dThe Wizard of Oz, 1939", u"\u201cI'm king of the world!\u201dTitanic, 1997"]
for oi in o:
    oi = oi.encode('ascii','ignore')
    if 'Fun fact' in oi:
        oi = oi.split('Fun')[0]
    year.append(oi.split(",")[-1])
    oi = oi.split(",")[:-1]
    print oi
    if len(oi)!=0:
        if "." in oi[-1]:
            title.append(oi[-1].split(".")[1])
            oi[-1]=oi[-1].split(".")[0]
        elif "!" in oi[-1]:
            title.append(oi[-1].split("!")[1])
            oi[-1]=oi[-1].split("!")[0]
        
        d = " ".join(oi)
        data.append(d)
    else:
        title.append(" ")
        data.append(" ")


print len(data)
print len(title)
print len(year)

from collections import OrderedDict

final = []
i = 0
while i < 94: 
    d = OrderedDict() 
    d["quote"]=data[i]
    d["character"]=""
    d["title"]=title[i]
    d["actor"]=""
    d["year"]=year[i]
    final.append(d)
    i = i+1


print final
# final = {"":final}
import json
f = open("movie.json",'w')
print json.dumps(final,f,indent=4)
        



