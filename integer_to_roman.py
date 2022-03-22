class Solution(object):


    def intToRoman(self, s):
        """
        :type s: str
        :rtype: int
        """


        def get_roman_char(n):
            if n >= 1000:
                return 'M', 1000
            elif n >= 900:
                return 'CM', 900
            elif n >= 500:
                return 'D', 500
            elif n >= 400:
                return 'CD', 400
            elif n >= 100:
                return 'C', 100
            elif n >= 90:
                return 'XC', 90
            elif n >= 50:
                return 'L', 50
            elif n >= 40:
                return 'XL', 40
            elif n >= 10:
                return 'X', 10
            elif n >= 9:
                return 'IX', 9
            elif n >= 5:
                return 'V', 5
            elif n >= 4:
                return 'IV', 4
            elif n >= 1:
                return 'I', 1
            
        roman_str = ''
        while (s > 0):
            r, s_less = get_roman_char(s)
            roman_str = roman_str + r
            s = s - s_less
        return roman_str
