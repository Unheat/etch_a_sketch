'''
A simple test program for pot2px.

These tests have some tolerance (+/- 1 px) to allow
for different implementation decisions.
Note that these tests are not exhaustive.
You can add more if you think of them!

Author: Matt Law
CS109
'''

from etchasketch import pot2px
import math

def test_pot2px():
    '''
    Runs through a number of test cases for pot2px
    Throws an assertion error if any of them fail.
    Otherwise, prints "All tests passed!"

    Inputs: None
    Outputs: None   
    '''
    # Edge cases
    assert math.isclose(pot2px(0, -400, 400), -400, abs_tol=1), "Test case 0 (-400, 400) failed"
    assert math.isclose(pot2px(65535, -400, 400), 400, abs_tol=1), "Test case(-400, 400) 65535 failed"
    
    # Midpoint test: rounding to closest pot value
    assert math.isclose(pot2px(32768, -400, 400), 0, abs_tol=1), "Test case (-400, 400) 32768 failed"
    
    # Test with smaller range
    assert math.isclose(pot2px(0, -200, 200), -200, abs_tol=1), "Test case 0 (-200, 200) failed"
    assert math.isclose(pot2px(65535, -200, 200), 200, abs_tol=1), "Test case 65535 (-200, 200) failed"
    assert math.isclose(pot2px(32768, -200, 200), 0, abs_tol=1), "Test case 32768 (-200, 200) failed"
    
    # Test with non-symmetric range
    assert math.isclose(pot2px(0, 100, 500), 100, abs_tol=1), "Test case 0 (100, 500) failed"
    assert math.isclose(pot2px(65535, 100, 500), 500, abs_tol=1), "Test case 65535 (100, 500) failed"
    assert math.isclose(pot2px(32768, 100, 500), 300, abs_tol=1), "Test case 32768 (100, 500) failed"
    
    # Arbitrary values
    assert math.isclose(pot2px(16384, -400, 400), -200, abs_tol=1), "Test case 16384 failed"
    assert math.isclose(pot2px(49152, -800, 800), 400, abs_tol=1), "Test case 49152 failed"

    print("All tests passed!")


if __name__=='__main__':
    test_pot2px()

