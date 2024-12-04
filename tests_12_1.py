import logging
import unittest
from tests_12_4 import Runner


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        try:
            test1 = Runner('name1', - 7)
            for i in range(10):
                test1.walk()
            self.assertEqual(test1.distance, 50)
            logging.info('"test_walk" выполнен успешно')
        except Exception as err:
            logging.warning("Неверная скорость для Runner")

    def test_run(self):
        try:
            test2 = Runner(2)
            for i in range(10):
                test2.run()
            self.assertEqual(test2.distance, 100)
            logging.info('"test_walk" выполнен успешно')
        except TypeError as err:
            logging.warning("Неверный тип данных для объекта Runner")

    def test_challenge(self):
        test3, test4 = Runner('name3'), Runner('name4')
        for i in range(10):
            test3.run()
            test4.walk()
        self.assertNotEqual(test3.distance, test4.distance)


logging.basicConfig(level='INFO', filemode='w', filename='runner_tests.log', encoding='UTF-8',
                    format='%(asctime)s | %(levelname)s | %(message)s')
