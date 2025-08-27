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
    m "follow me!"
    scene restaurant outside
    with fade
    show mia at left
    show karen at right
    m "Here we are! My favourite restaurant!"
    m "It looks so great, doesn't it?"
    k "I don't know, it looks a bit shabby."
    m "... I actually work here, so let me just get my uniform on and i'll meet you inside."
    scene restaurant inside
    with dissolve
    show mia at right 
    show karen at center
    m "What may i get you?"
    k "Well, just give me the usual, you know what I like."
    m "You're new to town... im sorry, i don't know what you like."
    k "What? thats just bad service! You should have heard of me by now, i'm like famous!"
    m "I apologize for the inconvenience, but I really don't know what you like."
    k "I have 2 followers on Facebook! You should know me! I have a YouTube channel with 3 subscribers! I'm giving this place a bad review!"
    
menu:

    "Fine, just give me a matcha soft serve.":
        jump m
    "Just get me an assortment of fruits.":
        jump f    
label m:
    m "notes down order in a notebook*"
    k "HEY STOP WASTING PAPER! I'm VEGAN! IT'S HURTING MY EYES!"
    m "ignores karen* Let me go get that for you."
    hide mia
    k "HURRY UP! I DON'T HAVE ALL DAY!"
    show mia at right
    show softserve at center
    k "Ew, why is it green? THAT COLOUR IS GOING TO POISON ME!"
    m "sorry about that. Matcha is made from tea leaves with a green pigment coming from chlorophyll."
    k "I DON'T CARE! GET ME THE MANAGER!"
        jump order_done        
label f:
    m "Sure, one fruit assortment coming right up!"
    k "BE QUICK OR I'LL LEAVE A BAD REVIEW!"
    m "Of course, I'll be right back with that."
    hide mia
    k "WHERE IS MY ORDER! WHY DID YOU LEAVE ME HERE ALONE?!"
    show mia at right
    "Hi, here is your order."
    show fruit_assortment at center
    k "What is this? IS THIS A JOKE? I WANTED THE FRUIT CUT! AND AVOCADOS ARE NOT FRUITS!"
    m "I apologize, I thought you wanted the fruit assortment as it is."
    k "JUST GET ME THE MANAGER! I CAN'T BELIEVE THIS PLACE!"
        jump order_done

label order_done:
    m "I'll get you the manager right away."
    
    


