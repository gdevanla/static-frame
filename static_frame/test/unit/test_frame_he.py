

import unittest

import frame_fixtures as ff

# from static_frame import Frame
from static_frame import FrameHE
from static_frame.test.test_case import TestCase


class TestUnit(TestCase):

    def test_frame_he_slotted_a(self) -> None:

        f1 = FrameHE.from_element(1, index=(1,2), columns=(3,4,5))

        with self.assertRaises(AttributeError):
            f1.g = 30 #type: ignore #pylint: disable=E0237
        with self.assertRaises(AttributeError):
            f1.__dict__ #pylint: disable=W0104


    def test_frame_he_hash_a(self) -> None:

        f1 = ff.parse('s(5,3)|i(I,str)|c(I,int)|v(int,str,bool)').to_frame_he()
        f2 = ff.parse('s(5,3)|i(I,str)|c(I,int)|v(int,str,bool)').to_frame_he()
        f3 = ff.parse('s(5,3)|i(I,str)|c(I,int)|v(int,bool,bool)').to_frame_he()
        f4 = ff.parse('s(5,3)|i(I,str)|c(I,str)|v(int,str,bool)').to_frame_he()

        self.assertEqual(hash(f1), hash(f2))
        # same indices, different types
        self.assertNotEqual(hash(f1), hash(f3))
        self.assertNotEqual(hash(f1), hash(f4))

        q = {f1, f2, f3, f4}
        self.assertEqual(len(q), 3)
        self.assertTrue(f1 in q)
        self.assertTrue(f2 in q)

        d = {f1: 'foo', f3: 'bar'}
        self.assertTrue(f2 in d)
        self.assertTrue(f3 in d)
        self.assertEqual(d[f3], 'bar')





if __name__ == '__main__':
    unittest.main()
