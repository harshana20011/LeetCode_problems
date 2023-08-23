class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        try:
            if not (word1.isalpha() and word2.isalpha()):
                raise ValueError("Both word1 and word2 should contain only alphabetic characters")
            
            length_word1 = len(word1)
            length_word2 = len(word2)
            
            if length_word1 < 1 or length_word2 > 100:
                raise ValueError("word1 should have at least one letter and word2 should have at most 100 letters")
            
            word_merge = []
            list_letters_word_1 = list(word1)
            list_letters_word_2 = list(word2)
            repertoire_words = {1: list_letters_word_1, 2: list_letters_word_2}

            if length_word1 == length_word2:
                i = 1
                u = 0
                for _ in word1:
                    if i in repertoire_words:
                        word_merge.extend(repertoire_words[i][u])
                        i += 1
                        word_merge.extend(repertoire_words[i][u])
                        i -= 1
                        u += 1
                
                return ''.join(word_merge)
            
            elif length_word1 > length_word2:
                i = 1
                u = 0
                for _ in word2:
                    if i in repertoire_words:
                        word_merge.extend(repertoire_words[i][u])
                        i += 1
                        word_merge.extend(repertoire_words[i][u])
                        i -= 1
                        u += 1
                
                for u in range(length_word1-length_word2):
                    word_merge.extend(repertoire_words[1][u+length_word2])
                return ''.join(word_merge)
            else: 
                i = 1
                u = 0
                for _ in word1:
                    if i in repertoire_words:
                        word_merge.extend(repertoire_words[i][u])
                        i += 1
                        word_merge.extend(repertoire_words[i][u])
                        i -= 1
                        u += 1
                
                for u in range(length_word2-length_word1):
                    word_merge.extend(repertoire_words[2][u+length_word1])
                return ''.join(word_merge)

        except ValueError as e:
            print(e)