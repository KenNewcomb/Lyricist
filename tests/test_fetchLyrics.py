import unittest
from modules import fetchLyrics

class fetchLyricsTest(unittest.TestCase):

	def test_AZLyrics_Gets_Correct_Lyrics(self):
		lyrics = fetchLyrics.AZLyrics(["washed out","amor fati"])
		print lyrics
		self.assertIn("inside",lyrics)

unittest.main()
