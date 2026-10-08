class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        """
        Remove the outermost parentheses of every primitive valid parentheses string.
        A primitive string is a valid parentheses string that cannot be split into 
        two non-empty valid parentheses strings.
      
        Args:
            s: A valid parentheses string
          
        Returns:
            The string with outermost parentheses removed from each primitive part
        """
        result = []
        depth = 0  # Track the depth/level of nested parentheses
      
        for char in s:
            if char == '(':
                # Increment depth when encountering opening parenthesis
                depth += 1
                # Only add to result if it's not an outermost opening parenthesis
                # (depth > 1 means we're inside at least one pair already)
                if depth > 1:
                    result.append(char)
            else:  # char == ')'
                # Decrement depth when encountering closing parenthesis
                depth -= 1
                # Only add to result if it's not an outermost closing parenthesis
                # (depth > 0 means we're still inside at least one pair)
                if depth > 0:
                    result.append(char)
      
        return ''.join(result)
