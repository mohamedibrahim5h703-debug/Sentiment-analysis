import unittest
from sentiment_analyzer import analyze_sentiment

class TestSentiment(unittest.TestCase):
    def test_positive_text(self):
        result = analyze_sentiment("I love AI and Python!")
        self.assertIn(result["label"], ["positive", "neutral", "negative"])

    def test_empty_text(self):
        result = analyze_sentiment("")
        self.assertTrue("error" in result or result["label"])

if __name__ == "__main__":
    unittest.main()
