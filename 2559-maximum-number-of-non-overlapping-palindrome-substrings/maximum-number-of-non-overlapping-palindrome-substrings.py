class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        """
        Find the maximum number of non-overlapping palindromic substrings of length at least k.
      
        Args:
            s: Input string
            k: Minimum length of palindromic substrings
          
        Returns:
            Maximum number of non-overlapping palindromic substrings
        """
        from functools import cache
      
        @cache
        def find_max_palindromes(start_index: int) -> int:
            """
            Dynamic programming function to find maximum palindromes starting from index.
          
            Args:
                start_index: Current starting position in the string
              
            Returns:
                Maximum number of palindromes from this position
            """
            # Base case: reached end of string
            if start_index >= string_length:
                return 0
          
            # Option 1: Skip current position and check from next index
            max_count = find_max_palindromes(start_index + 1)
          
            # Option 2: Try to include palindromes starting at current position
            # Check all possible ending positions that form palindromes of length >= k
            for end_index in range(start_index + k - 1, string_length):
                if is_palindrome[start_index][end_index]:
                    # Include this palindrome and continue from position after it
                    max_count = max(max_count, 1 + find_max_palindromes(end_index + 1))
          
            return max_count
      
        string_length = len(s)
      
        # Build 2D DP table to check if substring s[i:j+1] is a palindrome
        # is_palindrome[i][j] = True if s[i:j+1] is a palindrome
        is_palindrome = [[True] * string_length for _ in range(string_length)]
      
        # Fill the palindrome table bottom-up
        # Start from the end of string and work backwards
        for start in range(string_length - 1, -1, -1):
            for end in range(start + 1, string_length):
                # A substring is palindrome if:
                # 1. First and last characters match
                # 2. Inner substring is also a palindrome (or length <= 2)
                is_palindrome[start][end] = (s[start] == s[end] and 
                                            is_palindrome[start + 1][end - 1])
      
        # Find the maximum number of palindromes
        result = find_max_palindromes(0)
      
        # Clear the cache to free memory
        find_max_palindromes.cache_clear()
      
        return result
