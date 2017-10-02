'''
test each methods in the class of cplane 
check the expect setting/output equal the result
'''

#from cplane import ListComplexPlane as LCP

from cplane import ListComplexPlane as LCP
from cplane import doubleplane 


def test_init():
    CP = LCP(1,4,3,2,5,3)
    assert CP.plane == [[(1+2j), (2.5+2j), (4+2j)], [(1+3.5j), (2.5+3.5j), (4+3.5j)], [(1+5j), (2.5+5j), (4+5j)]]
    
def test_refresh():
    CP = LCP(1,4,3,2,5,3)
    CP.apply(doubleplane)
    CP.apply(powerplane)
    CP.refresh()
    assert CP.plane == [[(1+2j), (2.5+2j), (4+2j)], [(1+3.5j), (2.5+3.5j), (4+3.5j)], [(1+5j), (2.5+5j), (4+5j)]]
    
def test_apply():
    CP = LCP(1,4,3,2,5,3)
    CP.apply(doubleplane)
    assert CP.plane == [[(2+4j), (5+4j), (8+4j)], [(2+7j), (5+7j), (8+7j)], [(2+10j), (5+10j), (8+10j)]]
    CP.apply(plane)
    
def test_zoom():
    CP = LCP(1,4,3,2,5,3)
    CP.apply(doubleplane)
    CP.apply(powerplane)
    CP.zoom(1,4,3,2,5,3)
    assert CP.plane ==[[(-12+16j), (9+40j), (48+64j)], [(-45+28j), (-24+70j), (15+112j)], [(-96+40j), (-75+100j), (-36+160j)]]
                       
def doubleplane(plane):
     for i in range(len(plane)):
        for j in range(len(plane[i])):
            plane[i][j] *=2
     return plane

def powerplane(plane):
     for i in range(len(plane)):
        for j in range(len(plane[i])):
            plane[i][j] =plane[i][j] * plane[i][j] 
     return plane
                       