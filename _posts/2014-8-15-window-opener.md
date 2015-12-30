---
title: The Window Opener 2000
layout: post
published: true
description: "My first arduino project."
---
To open my windows, I have to stop whatever I'm doing, rotate my chair 90 degrees, place push my feet against my freezing hardwood floor, walk about 6 feet to my window rod where I have a 30% chance of stubbing my toe on my guitar amp, rotate the blinds for about 5 seconds, walk back to my chair (20% chance of stubbing toe on drawers), sit down, rotate my chair back 90 degrees, and finally rest my hands back on my keyboard and mouse.  This is the 20th century.  I can message someone living across the globe instantaneously; I can sit in a hunk of metal and move it up to 120 miles per hour just by slightly angling my right foot, and yet for some reason, I'm still getting up to open my windows like some uncivilized troglodyte.  

Today has marked the end of such peasantry.  Utilizing an arduino, servo, and switch, I have won yet another battle against physical exertion. 


Expertly crafted schematic:  


![](/images/blinds1.jpg)  


On the Arduino:  


![](/images/blinds2.jpg)  


In action:  


<video width="889" height="500" controls>
  <source src="/images/blinds.webm" type="video/mp4">
  <source src="/images/blinds.mp4" type="video/mp4">
Your browser does not support the video tag.
</video>


Code:
<a href="https://gist.github.com/heems/ab70192e81f322f4414d">On Github</a>  

I used <a href="https://www.foxytronics.com/products/68-springrc-sm-s4303r-continuous-rotation-servo">this</a> servo from FoxyTronics.  The 5 volts provided by the arduino was enough for the servo to rotate my slightly sticky window rod.  

 

