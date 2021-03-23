class Difference:
    def __init__(self, a):
        self.__elements = a
    
	# Add your code here
    def __init__(self, _elements = []):
        self._elements = _elements
        
    def computeDifference(self):
        extremes = [self._elements[0],self._elements[0]]
        for i in self._elements[1::]:
            extremes[0],extremes[1] = min(extremes[0], i), max(extremes[1], i)
        self.maximumDifference = extremes[1] - extremes[0]
# End of Difference class