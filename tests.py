import Tri_bulle

## test 
def tests_tri_bulle():
    assert Tri_bulle.tri_bulle('') == ''
    assert Tri_bulle.tri_bulle('aaa') == 'aaa'
    assert Tri_bulle.tri_bulle('abc') == 'abc'
    assert Tri_bulle.tri_bulle('cba') == 'abc'
    assert Tri_bulle.tri_bulle('zbgtj') == 'bgjtz'
    
    