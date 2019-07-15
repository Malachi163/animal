size(720,720)
background(0,255,255)

noStroke()
fill(0,255,0)
rect(0,360,720,720) # The grass

fill(94,74,72) # brown
rect(300,450,125,80) #Body of the dog

ellipse(440,445,50,50) # head of the dog

fill(243,255,71) #Dirty Yellow
ellipse(0,0,200,200) # The sun

ellipse(440,400,10,50) #ear

fill(94,74,72)
translate(390,530)
rotate(-PI/3)
translate(-300,-500)
rect(300,500,50,100) #front leg

translate(200,410)
rotate(-PI/3)
translate(-300,-500)
rect(300,500,50,100) #hind leg
