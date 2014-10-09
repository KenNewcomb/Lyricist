Lyricist
======

Lyricist prints the lyrics of the currently playing song to the shell. The program grabs the track information from the operating system and scrapes various websites for lyrics.

News
----
**09.24.14** - Rhythmbox is currently supported.

**09.15.14** - Development has resumed. I am in the process of converting Lyricist to Python 3.

**05.26.14** - SongLyrics.com is now supported.

**05.20.14** - A functional version of lyricist now exists.

Supported sources:
-----------------
1. AZLyrics.com
2. SongLyrics.com


Supported Music Players:
----------------------
1. <a href="http://en.wikipedia.org/wiki/Banshee_%28media_player%29" target="_blank">Banshee</a>
2. <a href="https://en.wikipedia.org/wiki/Rhythmbox" target="_blank">Rhythmbox</a>


To be implemented:
-----------------
1. Support for other common media players
2. Support for other sources of lyrics
3. Improvements to the way Lyricist searches for lyrics. If a title includes superfluous words such as "feat." lyricist may not find any lyrics. 

Known bugs:
-----------
- SongLyrics.com often gives a blank "page" of lyrics. This is in contrast with their "No Lyrics Found" page, which the program correctly handles. The program outputs a series of spaces. This bug will be further investigated.
