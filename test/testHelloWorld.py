from nose.tools import eq_
import helloWorld as uut


def test_helloWorld():
    eq_(uut.helloworld(), 0)