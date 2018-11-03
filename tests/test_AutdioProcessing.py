from unittest import TestCase

import AudioProcessing as ap

class test_AudioProcessing(TestCase):
    def test_calculateAbsoluteAveragePositive(self):
        soundArray = [2,2,2]
        self.assertEqual(2, ap.AudioProcessing.calculateAbsotuteAverage(ap, soundArray=soundArray))


    def test_calculateAbsoluteAverageMixed(self):
        soundArray = [2, -2, 2]
        self.assertEqual(2, ap.AudioProcessing.calculateAbsotuteAverage(ap, soundArray=soundArray))


    def test_calculateAbsoluteAverageNegative(self):
        soundArray = [-2, -2, -2]
        self.assertEqual(2, ap.AudioProcessing.calculateAbsotuteAverage(ap, soundArray=soundArray))
