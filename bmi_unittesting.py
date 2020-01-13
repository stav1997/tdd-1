import bmi
import unittest

class BmiTest(unittest.TestCase):

    def test_bmi(self):

        hight1 = "kjf"
        hight2 = -20
        hight3 = 1.5

        weight1 = "sdf"
        weight2 = -80
        weight3 = 90

        expected_result1 = -1
        expected_result2 = -1
        expected_result3 = -1
        expected_result4 = -1
        expected_result5 = -1
        expected_result6 = -1
        expected_result7 = -1
        expected_result8 = -1
        expected_result9 = weight3/hight3**2

        actual_result1 = bmi.BMI.bmi(hight1, weight1)
        actual_result2 = bmi.BMI.bmi(hight1, weight2)
        actual_result3 = bmi.BMI.bmi(hight1, weight3)
        actual_result4 = bmi.BMI.bmi(hight2, weight1)
        actual_result5 = bmi.BMI.bmi(hight2, weight2)
        actual_result6 = bmi.BMI.bmi(hight2, weight3)
        actual_result7 = bmi.BMI.bmi(hight3, weight1)
        actual_result8 = bmi.BMI.bmi(hight3, weight2)
        actual_result9 = bmi.BMI.bmi(hight3, weight3)

        self.assertEqual(expected_result1, actual_result1)
        self.assertEqual(expected_result2, actual_result2)
        self.assertEqual(expected_result3, actual_result3)
        self.assertEqual(expected_result4, actual_result4)
        self.assertEqual(expected_result5, actual_result5)
        self.assertEqual(expected_result6, actual_result6)
        self.assertEqual(expected_result7, actual_result7)
        self.assertEqual(expected_result8, actual_result8)
        self.assertEqual(expected_result9, actual_result9)

    def test_result(self):

        re1 = "sdef"

        re2 = -23

        re3 = 0
        re4 = 18.5
        re5 = 13

        re6 = 18.8
        re7 = 24.9
        re8 = 20

        re9 = 25
        re10 = 29.9
        re11 = 26

        re12 = 30
        re13 = 34.9
        re14 = 32

        re15 = 35
        re16 = 39.9
        re17 = 36

        re18 = 40
        re19 = 48

        expected_result1 = -1
        expected_result2 = -1
        expected_result3 = "under weight"
        expected_result4 = "normal weight"
        expected_result5 = "under weight"
        expected_result6 = "normal weight"
        expected_result7 = "normal weight"
        expected_result8 = "normal weight"
        expected_result9 = "over weight"
        expected_result10 = "over weight"
        expected_result11 = "over weight"
        expected_result12 = "obesity first degree"
        expected_result13 = "obesity first degree"
        expected_result14 = "obesity first degree"
        expected_result15 = "obesity second degree"
        expected_result16 = "obesity second degree"
        expected_result17 = "obesity second degree"
        expected_result18 = "obesity third degree"
        expected_result19 = "obesity third degree"


        actual_result1 = bmi.result(re1)
        actual_result2 = bmi.result(re2)
        actual_result3 = bmi.result(re3)
        actual_result4 = bmi.result(re4)
        actual_result5 = bmi.result(re5)
        actual_result6 = bmi.result(re6)
        actual_result7 = bmi.result(re7)
        actual_result8 = bmi.result(re8)
        actual_result9 = bmi.result(re9)
        actual_result10 = bmi.result(re10)
        actual_result11 = bmi.result(re11)
        actual_result12 = bmi.result(re12)
        actual_result13 = bmi.result(re13)
        actual_result14 = bmi.result(re14)
        actual_result15 = bmi.result(re15)
        actual_result16 = bmi.result(re16)
        actual_result17 = bmi.result(re17)
        actual_result18 = bmi.result(re18)
        actual_result19 = bmi.result(re19)

        self.assertEqual(expected_result1, actual_result1)
        self.assertEqual(expected_result2, actual_result2)
        self.assertEqual(expected_result3, actual_result3)
        self.assertEqual(expected_result4, actual_result4)
        self.assertEqual(expected_result5, actual_result5)
        self.assertEqual(expected_result6, actual_result6)
        self.assertEqual(expected_result7, actual_result7)
        self.assertEqual(expected_result8, actual_result8)
        self.assertEqual(expected_result9, actual_result9)
        self.assertEqual(expected_result10, actual_result10)
        self.assertEqual(expected_result11, actual_result11)
        self.assertEqual(expected_result12, actual_result12)
        self.assertEqual(expected_result13, actual_result13)
        self.assertEqual(expected_result14, actual_result14)
        self.assertEqual(expected_result15, actual_result15)
        self.assertEqual(expected_result16, actual_result16)
        self.assertEqual(expected_result17, actual_result17)
        self.assertEqual(expected_result18, actual_result18)
        self.assertEqual(expected_result19, actual_result19)

        if __name__ == '__main__':
            unittest.main()