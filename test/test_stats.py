"""
`stats` module unit tests.

"""

import unittest

import numpy as np
import scipy

import fc.stats

class TestMean(unittest.TestCase):
    """
    Test proper behavior of fc.stats.mean.

    """
    def setUp(self):
        # 10x2 array
        self.a = np.array([[0, 8, 6, 1, 1, 6, 5, 9, 2, 2],
                           [9, 9, 2, 0, 2, 0, 8, 8, 4, 7]]).T
        # FCSFile
        self.d = fc.io.FCSData('test/Data001.fcs')

    def test_array(self):
        """
        Test size, type, and values when using a 2D numpy array.

        """
        s_fc = fc.stats.mean(self.a)
        s_lib = np.mean(self.a, axis=0)
        self.assertIsInstance(s_fc, type(s_lib))
        self.assertEqual(s_fc.shape, (2,))
        np.testing.assert_array_equal(s_fc, s_lib)

    def test_fcs_data(self):
        """
        Test size, type, and values when using an FCSData object.

        """
        s_fc = fc.stats.mean(self.d)
        s_lib = np.mean(self.d.view(np.ndarray), axis=0)
        self.assertIsInstance(s_fc, type(s_lib))
        self.assertEqual(s_fc.shape, (6,))
        np.testing.assert_array_equal(s_fc, s_lib)

    def test_fcs_data_slice_1d(self):
        """
        Test size, type, and values when using a 1D sliced FCSData object.

        """
        s_fc = fc.stats.mean(self.d[:, 'FL1-H'])
        s_lib = np.mean(self.d[:, 'FL1-H'].view(np.ndarray))
        self.assertIsInstance(s_fc, type(s_lib))
        self.assertEqual(s_fc.shape, ())
        self.assertEqual(s_fc, s_lib)

    def test_fcs_data_argument_one_channel(self):
        """
        Test size, type, and values when specifying one channel via the
        `channels` argument.

        """
        s_fc = fc.stats.mean(self.d, channels='FL1-H')
        s_lib = np.mean(self.d[:, 'FL1-H'].view(np.ndarray))
        self.assertIsInstance(s_fc, type(s_lib))
        self.assertEqual(s_fc.shape, ())
        self.assertEqual(s_fc, s_lib)

    def test_fcs_data_argument_many_channels(self):
        """
        Test size, type, and values when specifying many channels via the
        `channels` argument.

        """
        s_fc = fc.stats.mean(self.d, channels=['FL1-H', 'FL2-H', 'FL3-H'])
        s_lib = np.mean(self.d[:, [2, 3, 4]].view(np.ndarray), axis=0)
        self.assertIsInstance(s_fc, type(s_lib))
        self.assertEqual(s_fc.shape, (3,))
        np.testing.assert_array_equal(s_fc, s_lib)

class TestGeometricMean(unittest.TestCase):
    """
    Test proper behavior of fc.stats.gmean.

    """
    def setUp(self):
        # 10x2 array
        self.a = np.array([[0, 8, 6, 1, 1, 6, 5, 9, 2, 2],
                           [9, 9, 2, 0, 2, 0, 8, 8, 4, 7]]).T
        # FCSFile
        self.d = fc.io.FCSData('test/Data001.fcs')

    def test_array(self):
        """
        Test size, type, and values when using a 2D numpy array.

        """
        s_fc = fc.stats.gmean(self.a)
        s_lib = scipy.stats.gmean(self.a, axis=0)
        self.assertIsInstance(s_fc, type(s_lib))
        self.assertEqual(s_fc.shape, (2,))
        np.testing.assert_array_equal(s_fc, s_lib)

    def test_fcs_data(self):
        """
        Test size, type, and values when using an FCSData object.

        """
        s_fc = fc.stats.gmean(self.d)
        s_lib = scipy.stats.gmean(self.d.view(np.ndarray), axis=0)
        self.assertIsInstance(s_fc, type(s_lib))
        self.assertEqual(s_fc.shape, (6,))
        np.testing.assert_array_equal(s_fc, s_lib)

    def test_fcs_data_slice_1d(self):
        """
        Test size, type, and values when using a 1D sliced FCSData object.

        """
        s_fc = fc.stats.gmean(self.d[:, 'FL1-H'])
        s_lib = scipy.stats.gmean(self.d[:, 'FL1-H'].view(np.ndarray))
        self.assertIsInstance(s_fc, type(s_lib))
        self.assertEqual(s_fc.shape, ())
        self.assertEqual(s_fc, s_lib)

    def test_fcs_data_argument_one_channel(self):
        """
        Test size, type, and values when specifying one channel via the
        `channels` argument.

        """
        s_fc = fc.stats.gmean(self.d, channels='FL1-H')
        s_lib = scipy.stats.gmean(self.d[:, 'FL1-H'].view(np.ndarray))
        self.assertIsInstance(s_fc, type(s_lib))
        self.assertEqual(s_fc.shape, ())
        self.assertEqual(s_fc, s_lib)

    def test_fcs_data_argument_many_channels(self):
        """
        Test size, type, and values when specifying many channels via the
        `channels` argument.

        """
        s_fc = fc.stats.gmean(self.d, channels=['FL1-H', 'FL2-H', 'FL3-H'])
        s_lib = scipy.stats.gmean(self.d[:, [2, 3, 4]].view(np.ndarray), axis=0)
        self.assertIsInstance(s_fc, type(s_lib))
        self.assertEqual(s_fc.shape, (3,))
        np.testing.assert_array_equal(s_fc, s_lib)

class TestMedian(unittest.TestCase):
    """
    Test proper behavior of fc.stats.median.

    """
    def setUp(self):
        # 10x2 array
        self.a = np.array([[0, 8, 6, 1, 1, 6, 5, 9, 2, 2],
                           [9, 9, 2, 0, 2, 0, 8, 8, 4, 7]]).T
        # FCSFile
        self.d = fc.io.FCSData('test/Data001.fcs')

    def test_array(self):
        """
        Test size, type, and values when using a 2D numpy array.

        """
        s_fc = fc.stats.median(self.a)
        s_lib = np.median(self.a, axis=0)
        self.assertIsInstance(s_fc, type(s_lib))
        self.assertEqual(s_fc.shape, (2,))
        np.testing.assert_array_equal(s_fc, s_lib)

    def test_fcs_data(self):
        """
        Test size, type, and values when using an FCSData object.

        """
        s_fc = fc.stats.median(self.d)
        s_lib = np.median(self.d.view(np.ndarray), axis=0)
        self.assertIsInstance(s_fc, type(s_lib))
        self.assertEqual(s_fc.shape, (6,))
        np.testing.assert_array_equal(s_fc, s_lib)

    def test_fcs_data_slice_1d(self):
        """
        Test size, type, and values when using a 1D sliced FCSData object.

        """
        s_fc = fc.stats.median(self.d[:, 'FL1-H'])
        s_lib = np.median(self.d[:, 'FL1-H'].view(np.ndarray))
        self.assertIsInstance(s_fc, type(s_lib))
        self.assertEqual(s_fc.shape, ())
        self.assertEqual(s_fc, s_lib)

    def test_fcs_data_argument_one_channel(self):
        """
        Test size, type, and values when specifying one channel via the
        `channels` argument.

        """
        s_fc = fc.stats.median(self.d, channels='FL1-H')
        s_lib = np.median(self.d[:, 'FL1-H'].view(np.ndarray))
        self.assertIsInstance(s_fc, type(s_lib))
        self.assertEqual(s_fc.shape, ())
        self.assertEqual(s_fc, s_lib)

    def test_fcs_data_argument_many_channels(self):
        """
        Test size, type, and values when specifying many channels via the
        `channels` argument.

        """
        s_fc = fc.stats.median(self.d, channels=['FL1-H', 'FL2-H', 'FL3-H'])
        s_lib = np.median(self.d[:, [2, 3, 4]].view(np.ndarray), axis=0)
        self.assertIsInstance(s_fc, type(s_lib))
        self.assertEqual(s_fc.shape, (3,))
        np.testing.assert_array_equal(s_fc, s_lib)

class TestMode(unittest.TestCase):
    """
    Test proper behavior of fc.stats.median.

    """
    def setUp(self):
        # 10x2 array
        self.a = np.array([[0, 8, 6, 1, 1, 6, 5, 9, 2, 2],
                           [9, 9, 2, 0, 2, 0, 8, 8, 4, 7]]).T
        # FCSFile
        self.d = fc.io.FCSData('test/Data001.fcs')

    def test_array(self):
        """
        Test size, type, and values when using a 2D numpy array.

        """
        s_fc = fc.stats.mode(self.a)
        s_lib = scipy.stats.mode(self.a, axis=0)[0][0]
        self.assertIsInstance(s_fc, type(s_lib))
        self.assertEqual(s_fc.shape, (2,))
        np.testing.assert_array_equal(s_fc, s_lib)

    def test_fcs_data(self):
        """
        Test size, type, and values when using an FCSData object.

        """
        s_fc = fc.stats.mode(self.d)
        s_lib = scipy.stats.mode(self.d.view(np.ndarray), axis=0)[0][0]
        self.assertIsInstance(s_fc, type(s_lib))
        self.assertEqual(s_fc.shape, (6,))
        np.testing.assert_array_equal(s_fc, s_lib)

    def test_fcs_data_slice_1d(self):
        """
        Test size, type, and values when using a 1D sliced FCSData object.

        """
        s_fc = fc.stats.mode(self.d[:, 'FL1-H'])
        s_lib = scipy.stats.mode(self.d[:, 'FL1-H'].view(np.ndarray))[0][0]
        self.assertIsInstance(s_fc, type(s_lib))
        self.assertEqual(s_fc.shape, ())
        self.assertEqual(s_fc, s_lib)

    def test_fcs_data_argument_one_channel(self):
        """
        Test size, type, and values when specifying one channel via the
        `channels` argument.

        """
        s_fc = fc.stats.mode(self.d, channels='FL1-H')
        s_lib = scipy.stats.mode(self.d[:, 'FL1-H'].view(np.ndarray))[0][0]
        self.assertIsInstance(s_fc, type(s_lib))
        self.assertEqual(s_fc.shape, ())
        self.assertEqual(s_fc, s_lib)

    def test_fcs_data_argument_many_channels(self):
        """
        Test size, type, and values when specifying many channels via the
        `channels` argument.

        """
        s_fc = fc.stats.mode(self.d, channels=['FL1-H', 'FL2-H', 'FL3-H'])
        s_lib = scipy.stats.mode(self.d[:, [2, 3, 4]].view(np.ndarray),
                                 axis=0)[0][0]
        self.assertIsInstance(s_fc, type(s_lib))
        self.assertEqual(s_fc.shape, (3,))
        np.testing.assert_array_equal(s_fc, s_lib)

class TestStd(unittest.TestCase):
    """
    Test proper behavior of fc.stats.std.

    """
    def setUp(self):
        # 10x2 array
        self.a = np.array([[0, 8, 6, 1, 1, 6, 5, 9, 2, 2],
                           [9, 9, 2, 0, 2, 0, 8, 8, 4, 7]]).T
        # FCSFile
        self.d = fc.io.FCSData('test/Data001.fcs')

    def test_array(self):
        """
        Test size, type, and values when using a 2D numpy array.

        """
        s_fc = fc.stats.std(self.a)
        s_lib = np.std(self.a, axis=0)
        self.assertIsInstance(s_fc, type(s_lib))
        self.assertEqual(s_fc.shape, (2,))
        np.testing.assert_array_equal(s_fc, s_lib)

    def test_fcs_data(self):
        """
        Test size, type, and values when using an FCSData object.

        """
        s_fc = fc.stats.std(self.d)
        s_lib = np.std(self.d.view(np.ndarray), axis=0)
        self.assertIsInstance(s_fc, type(s_lib))
        self.assertEqual(s_fc.shape, (6,))
        np.testing.assert_array_equal(s_fc, s_lib)

    def test_fcs_data_slice_1d(self):
        """
        Test size, type, and values when using a 1D sliced FCSData object.

        """
        s_fc = fc.stats.std(self.d[:, 'FL1-H'])
        s_lib = np.std(self.d[:, 'FL1-H'].view(np.ndarray))
        self.assertIsInstance(s_fc, type(s_lib))
        self.assertEqual(s_fc.shape, ())
        self.assertEqual(s_fc, s_lib)

    def test_fcs_data_argument_one_channel(self):
        """
        Test size, type, and values when specifying one channel via the
        `channels` argument.

        """
        s_fc = fc.stats.std(self.d, channels='FL1-H')
        s_lib = np.std(self.d[:, 'FL1-H'].view(np.ndarray))
        self.assertIsInstance(s_fc, type(s_lib))
        self.assertEqual(s_fc.shape, ())
        self.assertEqual(s_fc, s_lib)

    def test_fcs_data_argument_many_channels(self):
        """
        Test size, type, and values when specifying many channels via the
        `channels` argument.

        """
        s_fc = fc.stats.std(self.d, channels=['FL1-H', 'FL2-H', 'FL3-H'])
        s_lib = np.std(self.d[:, [2, 3, 4]].view(np.ndarray), axis=0)
        self.assertIsInstance(s_fc, type(s_lib))
        self.assertEqual(s_fc.shape, (3,))
        np.testing.assert_array_equal(s_fc, s_lib)

class TestCv(unittest.TestCase):
    """
    Test proper behavior of fc.stats.cv.

    """
    def setUp(self):
        # 10x2 array
        self.a = np.array([[0, 8, 6, 1, 1, 6, 5, 9, 2, 2],
                           [9, 9, 2, 0, 2, 0, 8, 8, 4, 7]]).T
        # FCSFile
        self.d = fc.io.FCSData('test/Data001.fcs')

    def test_array(self):
        """
        Test size, type, and values when using a 2D numpy array.

        """
        s_fc = fc.stats.cv(self.a)
        s_lib = np.std(self.a, axis=0) \
                    / np.mean(self.a, axis=0)
        self.assertIsInstance(s_fc, type(s_lib))
        self.assertEqual(s_fc.shape, (2,))
        np.testing.assert_array_equal(s_fc, s_lib)

    def test_fcs_data(self):
        """
        Test size, type, and values when using an FCSData object.

        """
        s_fc = fc.stats.cv(self.d)
        s_lib = np.std(self.d.view(np.ndarray), axis=0) \
                    / np.mean(self.d.view(np.ndarray), axis=0)
        self.assertIsInstance(s_fc, type(s_lib))
        self.assertEqual(s_fc.shape, (6,))
        np.testing.assert_array_equal(s_fc, s_lib)

    def test_fcs_data_slice_1d(self):
        """
        Test size, type, and values when using a 1D sliced FCSData object.

        """
        s_fc = fc.stats.cv(self.d[:, 'FL1-H'])
        s_lib = np.std(self.d[:, 'FL1-H'].view(np.ndarray)) \
                    / np.mean(self.d[:, 'FL1-H'].view(np.ndarray))
        self.assertIsInstance(s_fc, type(s_lib))
        self.assertEqual(s_fc.shape, ())
        self.assertEqual(s_fc, s_lib)

    def test_fcs_data_argument_one_channel(self):
        """
        Test size, type, and values when specifying one channel via the
        `channels` argument.

        """
        s_fc = fc.stats.cv(self.d, channels='FL1-H')
        s_lib = np.std(self.d[:, 'FL1-H'].view(np.ndarray)) \
                    / np.mean(self.d[:, 'FL1-H'].view(np.ndarray))
        self.assertIsInstance(s_fc, type(s_lib))
        self.assertEqual(s_fc.shape, ())
        self.assertEqual(s_fc, s_lib)

    def test_fcs_data_argument_many_channels(self):
        """
        Test size, type, and values when specifying many channels via the
        `channels` argument.

        """
        s_fc = fc.stats.cv(self.d, channels=['FL1-H', 'FL2-H', 'FL3-H'])
        s_lib = np.std(self.d[:, [2, 3, 4]].view(np.ndarray), axis=0) \
                    / np.mean(self.d[:, [2, 3, 4]].view(np.ndarray), axis=0)
        self.assertIsInstance(s_fc, type(s_lib))
        self.assertEqual(s_fc.shape, (3,))
        np.testing.assert_array_equal(s_fc, s_lib)

class TestIqr(unittest.TestCase):
    """
    Test proper behavior of fc.stats.iqr.

    """
    def setUp(self):
        # 10x2 array
        self.a = np.array([[0, 8, 6, 1, 1, 6, 5, 9, 2, 2],
                           [9, 9, 2, 0, 2, 0, 8, 8, 4, 7]]).T
        # FCSFile
        self.d = fc.io.FCSData('test/Data001.fcs')

    def test_array(self):
        """
        Test size, type, and values when using a 2D numpy array.

        """
        s_fc = fc.stats.iqr(self.a)
        s_lib = np.percentile(self.a, 75, axis=0) \
                    - np.percentile(self.a, 25, axis=0)
        self.assertIsInstance(s_fc, type(s_lib))
        self.assertEqual(s_fc.shape, (2,))
        np.testing.assert_array_equal(s_fc, s_lib)

    def test_fcs_data(self):
        """
        Test size, type, and values when using an FCSData object.

        """
        s_fc = fc.stats.iqr(self.d)
        s_lib = np.percentile(self.d.view(np.ndarray), 75, axis=0) \
                    - np.percentile(self.d.view(np.ndarray), 25, axis=0)
        self.assertIsInstance(s_fc, type(s_lib))
        self.assertEqual(s_fc.shape, (6,))
        np.testing.assert_array_equal(s_fc, s_lib)

    def test_fcs_data_slice_1d(self):
        """
        Test size, type, and values when using a 1D sliced FCSData object.

        """
        s_fc = fc.stats.iqr(self.d[:, 'FL1-H'])
        s_lib = np.percentile(self.d[:, 'FL1-H'].view(np.ndarray), 75) \
                    - np.percentile(self.d[:, 'FL1-H'].view(np.ndarray), 25)
        self.assertIsInstance(s_fc, type(s_lib))
        self.assertEqual(s_fc.shape, ())
        self.assertEqual(s_fc, s_lib)

    def test_fcs_data_argument_one_channel(self):
        """
        Test size, type, and values when specifying one channel via the
        `channels` argument.

        """
        s_fc = fc.stats.iqr(self.d, channels='FL1-H')
        s_lib = np.percentile(self.d[:, 'FL1-H'].view(np.ndarray), 75) \
                    - np.percentile(self.d[:, 'FL1-H'].view(np.ndarray), 25)
        self.assertIsInstance(s_fc, type(s_lib))
        self.assertEqual(s_fc.shape, ())
        self.assertEqual(s_fc, s_lib)

    def test_fcs_data_argument_many_channels(self):
        """
        Test size, type, and values when specifying many channels via the
        `channels` argument.

        """
        s_fc = fc.stats.iqr(self.d, channels=['FL1-H', 'FL2-H', 'FL3-H'])
        s_lib = np.percentile(self.d[:, [2, 3, 4]].view(np.ndarray),
                              75, axis=0) \
                    - np.percentile(self.d[:, [2, 3, 4]].view(np.ndarray),
                                    25, axis=0)
        self.assertIsInstance(s_fc, type(s_lib))
        self.assertEqual(s_fc.shape, (3,))
        np.testing.assert_array_equal(s_fc, s_lib)

class TestRcv(unittest.TestCase):
    """
    Test proper behavior of fc.stats.rcv.

    """
    def setUp(self):
        # 10x2 array
        self.a = np.array([[0, 8, 6, 1, 1, 6, 5, 9, 2, 2],
                           [9, 9, 2, 0, 2, 0, 8, 8, 4, 7]]).T
        # FCSFile
        self.d = fc.io.FCSData('test/Data001.fcs')

    def test_array(self):
        """
        Test size, type, and values when using a 2D numpy array.

        """
        s_fc = fc.stats.rcv(self.a)
        s_lib = (np.percentile(self.a, 75, axis=0) \
                    - np.percentile(self.a, 25, axis=0)) \
                    / np.median(self.a, axis=0)
        self.assertIsInstance(s_fc, type(s_lib))
        self.assertEqual(s_fc.shape, (2,))
        np.testing.assert_array_equal(s_fc, s_lib)

    def test_fcs_data(self):
        """
        Test size, type, and values when using an FCSData object.

        """
        s_fc = fc.stats.rcv(self.d)
        s_lib = (np.percentile(self.d.view(np.ndarray), 75, axis=0) \
                    - np.percentile(self.d.view(np.ndarray), 25, axis=0)) \
                    / np.median(self.d.view(np.ndarray), axis=0)
        self.assertIsInstance(s_fc, type(s_lib))
        self.assertEqual(s_fc.shape, (6,))
        np.testing.assert_array_equal(s_fc, s_lib)

    def test_fcs_data_slice_1d(self):
        """
        Test size, type, and values when using a 1D sliced FCSData object.

        """
        s_fc = fc.stats.rcv(self.d[:, 'FL1-H'])
        s_lib = (np.percentile(self.d[:, 'FL1-H'].view(np.ndarray), 75) \
                    - np.percentile(self.d[:, 'FL1-H'].view(np.ndarray), 25)) \
                    / np.median(self.d[:, 'FL1-H'].view(np.ndarray), axis=0)
        self.assertIsInstance(s_fc, type(s_lib))
        self.assertEqual(s_fc.shape, ())
        self.assertEqual(s_fc, s_lib)

    def test_fcs_data_argument_one_channel(self):
        """
        Test size, type, and values when specifying one channel via the
        `channels` argument.

        """
        s_fc = fc.stats.rcv(self.d, channels='FL1-H')
        s_lib = (np.percentile(self.d[:, 'FL1-H'].view(np.ndarray), 75) \
                    - np.percentile(self.d[:, 'FL1-H'].view(np.ndarray), 25)) \
                    / np.median(self.d[:, 'FL1-H'].view(np.ndarray), axis=0)
        self.assertIsInstance(s_fc, type(s_lib))
        self.assertEqual(s_fc.shape, ())
        self.assertEqual(s_fc, s_lib)

    def test_fcs_data_argument_many_channels(self):
        """
        Test size, type, and values when specifying many channels via the
        `channels` argument.

        """
        s_fc = fc.stats.rcv(self.d, channels=['FL1-H', 'FL2-H', 'FL3-H'])
        s_lib = (np.percentile(self.d[:, [2, 3, 4]].view(np.ndarray),
                              75, axis=0) \
                    - np.percentile(self.d[:, [2, 3, 4]].view(np.ndarray),
                                    25, axis=0)) \
                    / np.median(self.d[:, [2, 3, 4]].view(np.ndarray), axis=0)
        self.assertIsInstance(s_fc, type(s_lib))
        self.assertEqual(s_fc.shape, (3,))
        np.testing.assert_array_equal(s_fc, s_lib)

if __name__ == '__main__':
    unittest.main()
