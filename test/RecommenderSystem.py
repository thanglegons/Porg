import unittest
from recommend.recommender import RecommenderSystem


class Test(unittest.TestCase):

    def test_top_k_recommend(self):
        correct_tests = [0, 2, 5, 10, 20, 50]
        for test in correct_tests:
            params = {'id': '9780451524935', 'top': str(test)}
            response = RecommenderSystem(params).process()
            try:
                self.assertEqual(len(response['book_ids']), test)
                print("Correct test with " + str(test))
            except Exception:
                self.assertEqual(0, 1)
        wrong_tests = [-1, -2, -100]
        for test in wrong_tests:
            params = {'id': '9780451524935', 'top': str(test)}
            response = RecommenderSystem(params).process()
            try:
                self.assertEqual(response['message'], 'failed')
                print("Correct test with " + str(test))
            except Exception:
                self.assertEqual(0, 1)


if __name__ == '__main__':
    unittest.main()
