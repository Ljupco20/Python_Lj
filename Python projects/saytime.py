




import sys
import time

__version__ = '1.3.0'

class numwords():
    '''
       return numbers as words
       eg., 42 becomes 'forty-two'
    '''
    _word = {
        'ones': (
            'oh', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'
        ), 'tens': (
            '', 'ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety'
        ), 'teens': (
            'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen'
        ), 'quarters':(
            'o\'clock', 'quarter', 'half'
        ), 'range': {
            'hundred': 'hundred'
        }, 'misc': {
            'minus': 'minus'
        }
    }
    _oor = 'OOR'    # Out Of Range
    
    def __init__(self, n):
        self._number = n;
    
    def numwords(self, num = None):
        'Return the numbers as words'
        
        
    
    
    