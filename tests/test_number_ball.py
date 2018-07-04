import unittest
from number_ball import NumberBall


class TestNumberBall(unittest.TestCase):

    def setUp(self):
        self.ball = NumberBall(0, '../images/Balls/Ball-1.png')

    def test_calculate_x(self):
        first_result = self.ball.calculate_x(30, 15, 0)
        mid_result = self.ball.calculate_x(30, 15, 5)
        last_result = self.ball.calculate_x(30, 15, 8)
        self.assertEqual(first_result, 45)
        self.assertEqual(mid_result, 495)
        self.assertEqual(last_result, 765)

    def test_calculate_y(self):
        result = self.ball.calculate_y(30, 15)
        self.assertEqual(result, 45)


if __name__ == '__main__':
    unittest.main()
