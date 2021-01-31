# Fan Engage-o-meter

While the world of in-person events may be on pause, the amount of online broadcasting and viewership is at an all-time high. Music events are no exception. With the energy and interactivity of live concerts gone, and the availability of music through streaming so readily available, producers need to develop new ways to engage their audiences at music events.

Now a little bit about us. We're both huge fans of music, but even more than that, we're huge fans of the artists we adore. Whether it's Linkin Park or Blink-182, you'll easily find us jamming to our favourite song. Music isn't just about the listening, it's also about the connection you have with the band. And what better way to connect to the band than knowing all about them?

We created a program that engages music lovers through interactive trivia games, and here's a little more as to how we did it:

## What our app does

We know that live music events online often lack the personality and energy of live concerts. This program aims to help producers evolve and try to bring some of that energy back!

Our app allows the audience to create an account, and join the event that they're attending. At the time of the event, the app will allow the user to play along with the quiz that would be displayed on the big screen (or a small screen, at home).

On the producer side of things, we help them by auto-generating questions that are engaging and relevant to the event. We get information about the artist themselves, their top tracks, and some of their lyrics to really test which fans are the most hardcore.

## How we built it

Our app is built in Android Studio using Java, and is built upon an open-source project called Topeka. Originally, we developed the app from scratch, using Firebase for the user authentication as well as to host our database, containing information on the various users, producers, events and quizzes. Due to time constraints however, we moved to using Topeka instead.

For grabbing information on the artist and generating questions, we used a couple things. First, we used the Spotify web API through Spotipy, a Python wrapper library, which allowed us to search for artists, get their top tracks, and get some metadata on the artist themselves and their songs. We then used BeautifulSoup for our webscrapper, which gets lyrics off of Genius for each song.

## Challenges

We had trouble building up our program from scratch due to how many different aspects of the project we considered at the beginning. In our original version, we created the base app, with authentication, tabs, different views between users and producers, and the user's information displayed. However, we determined we wouldn't be able to complete some crucial aspects of the program in the time given, so we opted to use Topeka as our base.

In addition, we had trouble with using Firebase functions, which would've allowed us to call JavaScript code over Firebase directly from our android app. We attempted to write our question-generating code in JavaScript, using the same Spotify API. However, this ended up being unsuccessful, and so we decided to use Python instead.

Overall, we had some innovative ideas and created some of the necessary components of it, in our Android app and our backend Python code, but we weren't fully able to combine it all into the app we were aiming for.

## Next steps

We had tons of ideas for fan engagement coming into this hackathon, and here are some of the highlights:

- Have audience members be able to turn on their camera and microphone, and the program tracks the enjoyment of the user, whether that's how much they're smiling, moving to the music, or singing along - this information could be aggregated and put up onto the big screen, or used as analytics for the producer!
- Similarly, have a karaoke feature where lyrics and a backing track are broadcasted to the audience, and they sing-along - we can use microphones to track their singing, and see how well they're doing
- Enhance our generated lyrics questions by making them more tricky, like adding rhyming words, similar-sounding words, or other parts of the song with the same tune

Also, we'd like to fully build our app from the ground up, and connect all the working parts together. 