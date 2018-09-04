from nose.tools import with_setup, raises, eq_
import helloWorld as uut

def test_helloWorld():
    eq_(uut.helloworld(), 0)
    