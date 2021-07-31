

from session12 import Polygon
from functools import lru_cache
import math




class IteratorPolygon:

    def __init__(self, m, R):
        if m < 3:
            raise ValueError('m must be greater than 3')
        self._m = m
        self._R = R
        self._i = 3
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self._i > self._m:
            raise StopIteration
        else:
            result = Polygon(self._i, self._R)
            self._i += 1
            return result



class Polygons:
    def __init__(self, m, R):
        if m < 3:
            raise ValueError('m must be greater than 3')
        self._m = m
        self._R = R
        #self._polygons = [Polygon(i, R) for i in range(3, m+1)]
        self._max_efficiency_polygon = None
        
    def __len__(self):
        return self._m - 2

    
    def __repr__(self):
        return f'Polygons(m={self._m}, R={self._R})'
    
    def __iter__(self):
        return IteratorPolygon(self._m, self._R)
    
   
    @property
    def max_efficiency_polygon(self):
        if self._max_efficiency_polygon is None:
            sorted_polygons = sorted(IteratorPolygon(self._m, self._R), 
                                     key=lambda p: p.area/p.perimeter,
                                    reverse=True)
            self._max_efficiency_polygon = sorted_polygons[0]
        return self._max_efficiency_polygon

    