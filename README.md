#### What is we Game?
* WeGame is a web app that help gamers and game developers in many aspects:
Gamers can get game recommendations predicted by AI according to their gaming history from different gaming platforms and try new indie games that are available on WeGame.co. Users get bonus points based on their activity, while playing games and leaving reviews; Each bonus points equals some amount of money; Thus the more active a user is on the platform, the more money they can earn. Prizes for outstanding users will be available and supported by our foundation.
* Testing and getting feedback for games is essential, especilly while they still are in development. Unfortunatly, this is can be a big problem for indie developers who might not have the resources to hire hundreds or thousands of players to test their games before their release. On our platforrm, developers can get feedback and reviews from a community of gamers during production. The developers who register their games our platform will get the opportunity to grow a fan base before release and test their "still-in-development" games for a very small fee. This money will then go back to the gamers on the platform. After developers reach a milestone (according to money that they earned and users count) they will pay us some money, most part of this money will be spent on prizes for gamers.

### How is this projects structured:
In the short amount of time we had for the hackathon, we only got to build some
components and part of the project. All of our teammates enjoy working on this project and
wish to continue it in the future.
* One of the developed sections is the website's front-end. We managed to complete
the design of most of the pages that website is going to need.
* Another part is the recommendation engine, which is in the  WeGameRecs file. It isn't
still fully developed, but its functional (although primitive). For now, you can access it via command line. If you have a steam account and want to use that, run SteamUser.py and follow the instructions. Then go and run GameRecs. If you dont have a steam account, no problem, there already is a sample file in the dataClean folder. These scripts use
the user data fetched from steam, and the API from igdb.com to get information
about the content and to use in the recommendation system. The engine then finds matches
from games on our platform. Since we still dont have any real developers on the website, 
we created sample files for it, just so we could test if it works. The AI will become more complicated as our project grows. We will support connection with more platforms, and use
trophy data for games to predict how much a user likes a partiular game. When our database
of indie developers grows on our platform, we can introduce collacrative filtering to the recommendation engine as well.
* We also started development for registeration pages. Some of the scripts use sql express and sql managament studia, and some write to files. These are only for prototyping. Once we launch the website, we will have more sophisticated security measures for registeration.

