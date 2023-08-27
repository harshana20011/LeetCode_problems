class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = ['a', 'e', 'i', 'o', 'u']
        vowels_upp = []
        for i, vowel in enumerate(vowels):
                vowels_upp.append( vowels[i].upper())        
        total_vowel = vowels+vowels_upp
        word = list(s)
        start = 0
        end = len(s)-1 
        while start < end:
                if word[start] in total_vowel and word[end] in total_vowel:
                        word[start], word[end] = word[end], word[start]
                        start+=1
                        end-=1
                elif word[start] not in total_vowel:
                        start += 1
                elif word[end] not in total_vowel:
                        end -= 1 
                        
        return ''.join(word)