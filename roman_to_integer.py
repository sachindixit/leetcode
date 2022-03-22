class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        s = 'MCMXCIV'
        """

        total = 0
        roman_list = [{'I':1}, {'V':5}, {'X':10}, {'L':50}, {'C':100}, {'D':500}, {'M':1000},]
        roman_list_index = ['I','V','X','L','C','D','M']
        prev_char = None
        prev_num = 0
        str_list = list(s)

        for char in str_list:
            idx = roman_list_index.index(char)
            val = roman_list[idx][char]
            if ((prev_char == 'I' and char in ('V','X')) or
                (prev_char == 'X' and char in ('L','C')) or
                (prev_char == 'C' and char in ('D','M'))):
                total = (total - prev_num) + (val - prev_num)
            else:
                total = total + val
            prev_char = char
            prev_num = val
            print("running total % d" % total)
        print ("final total %d " % total)
        return total

