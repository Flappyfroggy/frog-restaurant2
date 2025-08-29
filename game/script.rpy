define f = Character('Froggo', color="#88E788")
define k = Character('Karen', color="#FA766E")
define m = Character('Mia', color="#DAB1DA")

label start:
 
    scene meadow
    with dissolve
    show mia at left 
    show karen at center
    m "welcome to town! I bet you're starving. Let's go to my favourite restaurant!"
    m "It's just around the corner. I hope you like it!"
    k "hurry up, let's go. Don't keep me waiting."
    scene restaurant outside
    with fade
    show mia at left
    show karen at right
    m "Here we are! My favourite restaurant!"
    m "It looks so great, doesn't it?"
    k "I don't know, it looks a bit shabby. I could build it myself better than this."
    m "... I'm actually the co-owner, so let me just get my uniform on and i'll meet you inside."
    scene restaurant inside
    with dissolve
    show miauniform at right 
    show karen at left
    m "What may i get you?"
    k "Well, just give me the usual, you know what I like."
    m "You're new to town... im sorry, i don't know what you want to order."
    k "What? thats just bad service! You should have heard of me by now, i'm like famous!"
    m " I'm sorry?"
    k "I have 2 followers on Facebook! You should know me! I'm giving this place a bad review!"
    m "Is there anything you would still like to order?"
menu:

    "Fine, just give me a matcha soft serve.":
        jump m
    "Just get me an assortment of fruits.":
        jump f    
label m:
    k "Fine, just give me a matcha soft serve."
    m "notes down order in a notebook*"
    k "HEY STOP WASTING PAPER! I'm VEGAN! IT'S HURTING MY EYES!"
    m "ignores karen* Let me go get that for you."
    hide miauniform
    k "HURRY UP! I DON'T HAVE ALL DAY!"
    show miauniform at right
    show softserve at center
    k "Ew, why is it green? THAT COLOUR IS GOING TO POISON ME!"
    m "sorry about that. Matcha is made from tea leaves with a green pigment coming from chlorophyll."
    k "I DON'T CARE! GET ME THE MANAGER!"
    jump order_done        
label f:
    k "Just get me an assortment of fruits."
    m "Sure, one fruit assortment coming right up!"
    k "BE QUICK OR I'LL LEAVE A BAD REVIEW!"
    m "Of course, I'll be right back with that."
    hide miauniform
    k "WHERE IS MY ORDER! WHY DID YOU LEAVE ME HERE ALONE?!"
    show miauniform at right
    "Hi, here is your order."
    show fruit at center
    k "What is this? IS THIS A JOKE? I WANTED THE FRUIT CUT! AND AVOCADOS ARE NOT FRUITS!"
    m "I apologize, I thought you wanted the fruit assortment as it is."
    k "JUST GET ME THE MANAGER! I CAN'T BELIEVE THIS PLACE!"
    jump order_done

label order_done:
    m "I'll get you the manager right away."
    hide miauniform
    k "HURRY WOMAN!"
    show at right miauniform
menu: 

    "i'm sorry, what did you say?":
        jump polite
    "Shut up.":
        jump rude

label polite:
    m "I'm sorry, what did you say?"
    k "I SAID YOU NEED TO HURRY! AND WHERE IS THE MANAGER I ASKED FOR!"
    m "I'm sorry about the wait."
    K "THIS PLACE IS SO DISRESPECTFUL!"
    m "Let me get you the manager."
    hide miauniform
    show frog
    f "Hi, what seems to be the problem?"
    k "AND WHO ARE YOU!"
    f "I'm the manager and chef here."
    k "YOU CAN'T BE! THATS SO UNSAFE!"
    f "You walked into Frog's restaurant."
    k "AND FROG'S RESTAURANT IS A HEALTHCODE VIOLATION!"
    f "This restaurant has already been visited and approved by the local health inspector."
    f "Feel free to dine elsewhere if you want!"
    k "NO. THIS IS UNACCEPTABLE. JUST GET ME SOME SAFE FOOD."
    jump food # FINISH THIS PART 

label rude: 
    m "Shut up."
    m "Could you close your mouth?"
    m "or perhaps rest your vocal chords?"
    m "(insult)"
    m "(more insults)"
    k "that's so OFFENSIVE! HOW DARE YOU!"
    k "SHUT DOWN THIS RESTAURANT NOW! OR I'LL SUE!"
menu: 

    "No!":
        jump no
    "Okay.":
        jump yes

label no:
    m "No! never!" # FINISH THIS PART
label yes:
    m "Okay.. please don't sue!"
    k "are you going to shut down this restaurant??"
    m "yes..."
    "Bad Ending"
    
    return



    


