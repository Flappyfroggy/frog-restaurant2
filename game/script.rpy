define f = Character('Froggo', color="#88E788")
define k = Character('Karen', color="#FA766E")
define m = Character('Mia', color="#DAB1DA")

label start:
    scene black
    show frog at left
    show mia at right
    with fade
    m "I hope no one realises this establishment isn't approved by the health inspector..."
    f "don't worry, everyone in town loves it here anyways!"
    f "no one would care about the health codes!"
    m "I hope you're right..."
    f "i can always just pretend it is approved!"
    f "hey look, the new person should be here any minute now!"
    m "i'll go greet them!"
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
    hide softserve
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
    hide fruit
    jump order_done

label order_done:
    m "I'll get you the manager right away."
    hide miauniform
    k "HURRY WOMAN!"
    show miauniform at right
menu: 

    "i'm sorry, what did you say?":
        jump polite
    "Shut up.":
        jump rude

label polite:
    m "I'm sorry, what did you say?"
    k "I SAID YOU NEED TO HURRY! AND WHERE IS THE MANAGER I ASKED FOR!"
    m "I'm sorry about the wait."
    k "THIS PLACE IS SO DISRESPECTFUL!"
    m "Let me get you the manager."
    hide miauniform
    show frog at right
    f "hewo!"
    k "AND WHO ARE YOU!"
    f "I'm the manager and chef here."
    k "YOU CAN'T BE! THATS SO UNSAFE!"
    f "You walked into Frog's restaurant."
    k "AND FROG'S RESTAURANT IS A HEALTHCODE VIOLATION!"
    f "This restaurant has already been visited and approved by the local health inspector :D"
    f "Feel free to dine elsewhere if you want!"
    k "NO. THIS IS UNACCEPTABLE. JUST GET ME SOME SAFE FOOD."
    f "okie dokie! all our food is safe here!"
    hide frog
    show miauniform at right
    m "i'll get you a matcha soft serve."
    show softserve at center
    k "wait this tastes..."
menu: 

    "actually pretty good!":
        jump good
    "TERRIBLE.":
        jump terrible
label good:
    k "This does taste pretty nice.."
    k "i'm sorry i was rude earlier..."
    hide miauniform
    show frog at right
    f "don't worry about it!"
    "Good Ending"
    return
label terrible:
    k "This is.. TERRIBLE."
    k "PAINFUL to consume."
    k "It is causing me EMOTIONAL DAMAGE looking at this softserve."
    k "I'm calling a health inspector."
    "The health inspector visits your restaurant."
    "The Frog is regarded as unsafe."
    "You have been asked to close down."
    "Bad Ending."
    return

 

label rude: 
    m "Shut up."
    m "Could you close your mouth?"
    m "or perhaps rest your vocal chords?"
    k "HOW DARE YOU SPEAK TO ME THAT WAY! I DEMAND TO SPEAK TO YOUR MANAGER!"
    show frog
    f "hi!"
    m "This karen is a artless onion eyed gudgeon."
    m "or even a loggerheaded earth vexing dewberry."
    k "that's so OFFENSIVE! HOW DARE YOU!"
    k "SHUT DOWN THIS RESTAURANT NOW! OR I'LL SUE!"
menu: 

    "No!":
        jump no
    "Okay.":
        jump yes

label no:
    m "No! never!"
    f "yep no thanks!" 
    k "FINE! I'LL JUST SUE YOU THEN!"
    f "That is utterly perplexing, but suit yourself."
    k "YOU GAVE ME EMOTIONAL TRAUMA! AND THE FOOD WAS DISGUSTING!"
    k "I'M CALLING A LAWYER!"
    m "Good luck finding one that will take your case."
    k "THIS ISN'T OVER! BYE! I'LL BE SEEING YOU SOON IN COURT!"
    "The next day you receive a letter in the mail."
    "You have been sued by Karen for emotional trauma. You are to appear in court next week."
    menu:

        "Go to court.":
            jump court
        "Ignore the letter.":
            jump ignore
label court:
    scene black
    "You appear in court."
    "After a long trial, the judge rules in your favour."
    "You win the case!"
    scene restaurant outside
    with fade
    show karen at center
    show mia at left
    show frog at right
    k "I'm sorry that i sued you... would you mind if i ordered again? i really liked the food here.."
    m "Of course! we're glad you enjoyed it."
    k "i'm so sorry...."
    f "yipppeeeeeeeeeee another customer!"
    "Good Ending."
    return
label ignore:
    scene black
    "You ignore the letter."
    "A week later, you receive another letter in the mail."
    "You have been fined $5000 for health code violations."
    "You are to shut down your restaurant immediately."
    scene restaurant inside
    with fade
    show miauniform at right 
    show karen at left
    k "I told you this place was a health code violation! I can't believe you ignored the letter!"
    m "I'm sorry... i didn't think it would come to this..."
    f "oh no..."
    menu: 

        "fight the fine.":
            jump fight
        "shut down the restaurant.":
            jump yes
label fight:
    f "we'll fight it!"
    k "You can't win against the government! Just shut it down!"
    m "we have to try!"
    "You fight the fine in court."
    "After a long trial, the judge rules for you."
    "You won the case!"
    scene restaurant outside
    with fade
    show karen at center
    show mia at left
    show frog at right
    k "You won the case? I'm sorry for doubting you.."
    k "The food is actually pretty good here..."
    k "Would you mind if i ordered again?"
    m "Of course! we're glad you enjoyed it."
    f "yipppeeeeeeeee lets have A PARTY!"
    "Good Ending."
    return
label yes:
    f "ok."
    k "are you going to shut down this restaurant??"
    f "yes..."
    m "NOOOOO!"
    "Bad Ending."
    
    return



    


