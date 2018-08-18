import unittest
import time
import _pp


class Test_pp(unittest.TestCase):
    def setUp(self):
        pass

    def test_threaded_decorator(self):
        result = []

        @_pp.threaded(False)
        def append_x(arr):
            time.sleep(1)
            arr.append("x")
            return True

        # start the threaded function call
        a = append_x(result)
        result.append("y")
        # y should be appended first then x since main thread
        # is not waiting for x to finish
        self.assertEqual(result[0], "y")
        time.sleep(1)
        # x should now be appended
        self.assertEqual(len(result), 2)
        self.assertEqual(result[1], "x")
        # await_output should return function return
        self.assertTrue(a.await_output())

    def test_run_in_thread(self):
        # should do the same thing as the threaded decorator
        result = []

        def append_x(arr):
            time.sleep(1)
            arr.append("x")
            return True

        # start the threaded function call
        a = _pp.run_threaded(append_x, result)
        result.append("y")
        # y should be appended first then x since main thread
        # is not waiting for x to finish
        self.assertEqual(result[0], "y")
        time.sleep(1)
        # x should now be appended
        self.assertEqual(len(result), 2)
        self.assertEqual(result[1], "x")
        # await_output should return function return
        self.assertTrue(a.await_output())

    def test_run_chunked(self):
        results = []

        def append_nums(nums, arr):
            arr.extend(nums)

        manager = _pp.run_chunked(append_nums, range(10),
                                  threads=8, args=[results])
        self.assertEqual(len(results), 10)
        self.assertEqual(results, list(range(10)))


if __name__ == '__main__':
    unittest.main()
