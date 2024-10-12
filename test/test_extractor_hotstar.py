import unittest
from yt_dlp import YoutubeDL
from yt_dlp.extractor.hotstar import HotstarIE

class TestHotstarExtractor(unittest.TestCase):
    def setUp(self):
        self.ydl_opts = {
            'cookiefile': 'testdata/cookies.txt',
            'verbose': True,
        }
        self.ydl = YoutubeDL(self.ydl_opts)

    def test_hotstar_v2_api(self):
        """Test Hotstar extractor with the new v2 API endpoint"""
        url = 'https://www.hotstar.com/in/shows/yeh-rishta-kya-kehlata-hai/586/abhira-ruhi-learn-the-truth/1000903272/watch'
        info = self.ydl.extract_info(url, download=False)
        self.assertIsNotNone(info)
        self.assertEqual(info.get('id'), '1000903272')
        self.assertIsNotNone(info.get('title'))
        # Additional assertions based on the expected structure of the response

    def test_hotstar_extractor_with_invalid_url(self):
        """Test Hotstar extractor with an invalid URL"""
        url = 'https://www.hotstar.com/in/invalid-url'
        with self.assertRaises(Exception):
            self.ydl.extract_info(url, download=False)

    def test_hotstar_extractor_with_no_cookies(self):
        """Test Hotstar extractor without cookies"""
        ydl_opts_no_cookies = {
            'verbose': True,
        }
        ydl_no_cookies = YoutubeDL(ydl_opts_no_cookies)
        url = 'https://www.hotstar.com/in/shows/yeh-rishta-kya-kehlata-hai/586/abhira-ruhi-learn-the-truth/1000903272/watch'
        with self.assertRaises(Exception):
            ydl_no_cookies.extract_info(url, download=False)

    def tearDown(self):
        self.ydl = None

if __name__ == '__main__':
    unittest.main()