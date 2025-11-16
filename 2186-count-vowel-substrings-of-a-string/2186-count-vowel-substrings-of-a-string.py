class Solution(object):
    def countVowelSubstrings(self, word):
        """
        :type word: str
        :rtype: int
        """
        vowels = ['a','e','i','o','u']
        counter = 0
        for i in range(len(word)):
            if word[i] not in vowels:
                continue 
            
            seen_vowels = set()

            for j in range(i,len(word)):
                if word[j] not in vowels:
                    break
                seen_vowels.add(word[j])
                if len(seen_vowels)==5:
                        counter+=1
        return counter





        