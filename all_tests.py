#-*-coding:utf-8-*-
__author__ = 'Administrator'
import unittest

import baidu
import youdao

testunit = unittest.TestSuite()

testunit.addTest(unittest.makeSuite(baidu.Baidu))
testunit.addTest(unittest.makeSuite(youdao.Youdao))

runner = unittest.TextTestRunner()
runner.run(testunit)