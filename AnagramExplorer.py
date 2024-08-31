class AnagramExplorer:
    def __init__(self, all_words: list[str]):
       self.__corpus = all_words
       self.anagram_lookup = self.build_lookup_dict() # Only calculated once, when the explorer object is created

    @property
    def corpus(self):
      return self.__corpus

    def is_valid_anagram_pair(self, pair:tuple[str], letters:list[str]) -> bool:
       '''Checks whether a pair of words:
            -are both included in the allowable word list (self.corpus)    
            -are both at least 3 letters long (and the same)
            -form a valid anagram pair
            -consist entirely of letters chosen at the beginning of the game

            Args:
                pair (tuple): Two strings representing the guessed pair
                letters (list): A list of letters from which the anagrams should be created

            Returns:
                bool: Returns True if the word pair fulfills all validation requirements, otherwise returns False
       '''
       word1,word2 = pair
       word1_official = word1.lower()
       word2_official = word2.lower()
      
       
      
       if word1_official not in map(str.lower,self.__corpus) or word2_official not in map(str.lower, self.__corpus):
          return False
       if len(word1_official)<3 or len(word2_official)<3 or len(word1_official) != len(word2_official):
          return False
       if sorted(word1_official) != sorted(word2_official): 
          return False
       if word1_official == word2_official:
          return False
       letter_count = {letter: letters.count(letter) for letter in letters}
       for letter in word1_official:
          if word1_official.count(letter) > letter_count.get(letter,0):
             return False
       return True 
    

        ### END SOLUTION 
        
    def build_lookup_dict(self) -> dict:
        '''Creates a fast dictionary look-up (via either prime hash or sorted tuple) of all anagrams in a word corpus.
       
            Args:
                corpus (list): A list of words which should be considered

            Returns:
                dict: Returns a dictionary with  keys that return sorted lists of all anagrams of the key (per the corpus)
        '''
        anagram_dict = {}
        for word in self.__corpus:
           key = tuple(sorted(word))
           if key not in anagram_dict:
              anagram_dict[key] = []
           anagram_dict[key].append(word)
        for key in anagram_dict:
           anagram_dict[key].sort()
        return anagram_dict
           
        


        ### END SOLUTION 

    def get_all_anagrams(self, letters: list[str]) -> set:
        '''Creates a set of all unique words that could have been used to form an anagram pair.
           Words which can't create any anagram pairs should not be included in the set.

            Ex)
            corpus: ["abed", "mouse", "bead", "baled", "abled", "rat", "blade"]
            all_anagrams: {"abed",  "abled", "baled", "bead", "blade"}

            Args:
              letters (list): A list of letters from which the anagrams should be created

            Returns:
              set: all unique words in corpus which form at least 1 anagram pair
        '''
        permission_words = set()
        letter_set = {letter: letters.count(letter) for letter in letters}

        for key, words in self.anagram_lookup.items():
               if len(key) > 2 and all(key.count(letter) <= letter_set.get(letter,0) for letter in key):
                  if len(words) >1:
                     for word in words:
                        if len(word) >=3: 
                           permission_words.add(word)
        return permission_words
        ### END SOLUTION 

    def get_most_anagrams(self, letters:list[str]) -> str:
        '''Returns any word from one of the largest lists of anagrams that 
           can be formed using the given letters.
           
            Args:
              letters (list): A list of letters from which the anagrams should be created

            Returns:
              str: a single word from the largest anagram families
        '''
        max_anagrams = 0
        output_word = ""
        letter_set = {letter: letters.count(letter) for letter in letters}
        
        for key, words in self.anagram_lookup.items():
            if all(key.count(letter) <= letter_set.get(letter,0) for letter in key):
                if len(words) > max_anagrams:
                    max_anagrams = len(words)
                    output_word = words[0]
        
        return output_word


        ### END SOLUTION 

if __name__ == "__main__":
  words1 = [
     "abed","abet","abets","abut","acme","acre","acres","actors","actress","airmen","alert","alerted","ales","aligned","allergy","alter","altered","amen","anew","angel","angle","antler","apt",
     "bade","baste","bead","beast","beat","beats","beta","betas","came","care","cares","casters","castor","costar","dealing","gallery","glean","largely","later","leading","learnt","leas","mace","mane",
     "marine","mean","name","pat","race","races","recasts","regally","related","remain","rental","sale","scare","seal","tabu","tap","treadle","tuba","wane","wean"
  ]
  words2 = ["rat", "mouse", "tar", "art", "chicken", "stop", "pots", "tops" ]

  letters = ["l", "o", "t", "s", "r", "i", "a"]

  my_explorer = AnagramExplorer(words2)

  print(my_explorer.is_valid_anagram_pair(("rat", "tar"), letters))
  print(my_explorer.is_valid_anagram_pair(("stop", "pots"), letters))
  print(my_explorer.get_most_anagrams(letters))
  print(my_explorer.get_all_anagrams(letters))