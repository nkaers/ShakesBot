# ShakesBot
A Bot for the Game Shakes & Fidget. It can be used to find items which are not registered in your scrapbook yet.<br>
You need to have the **Real Holy Grail**. <br>
This Bot can only be used on Windows.<br><br>

## How to Use
You need to go to the **Hall of Fame** and select a random enemy. Then start the ShakesBot.exe and wait. You do not need the source code which is the ShakesBot.py file. You are not allowed to change the window and I would not recommend to move the mouse too much, since the Bot works on Image Detection and the Pointer can interfere with the Bot. In the console output you can see that the Bot is working. Once it found an enemy with an unknown Item the Bot will stop and stay an that enemy. The console will show you how many players were searched in the progress.

## How does it work
The Bot makes two screenshots of your Game Window with a delay of 1 second in between. Since the **Real Holy Grail** will highlight unknown Items by changing their size, the Image Detection can spot the difference of the two screenshots.<br>
It compares the two images and checks if on one of them an item is bigger than on the other and stops if this is the case. If the two images are completely the same, all items are known to the player and this enemy can be ignored. In this case the Bot will move up to the next person and will continue on doing this until an enemy is found.<br><br>
The taken screenshots will immediately be cut to just show the regions which the Bot has to use. After the Bot compares the two images the images will be deleted and cannot be found anywhere again. Therefore no personal data will be extracted by this Bot and its only purpose is to find unknown items.<br><br>
The source code can also be found in this repository for further details.
