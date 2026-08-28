class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        from collections import Counter

        n = len(s)
        cnt = Counter(s)

        # A palindrome can have at most one character with odd frequency
        odd = [c for c in cnt if cnt[c] % 2]
        if len(odd) > 1:
            return ""

        # Build the multiset for the first half
        half_cnt = [0] * 26
        for i in range(26):
            half_cnt[i] = cnt[chr(ord('a') + i)] // 2

        m = n // 2

        def make_palindrome(half):
            if n % 2:
                return half + odd[0] + half[::-1]
            return half + half[::-1]

        # Smallest possible palindrome
        half = ''.join(
            chr(ord('a') + i) * half_cnt[i]
            for i in range(26)
        )

        p = make_palindrome(half)

        if p > target:
            return p

        # We need the smallest half-string > target[:m]
        t = target[:m]

        counts = half_cnt[:]
        prefix = []
        possible_greater = []

        # Match target as long as possible.
        # At each position remember the smallest character that
        # could be made greater than target[i].
        for i in range(m):
            x = ord(t[i]) - ord('a')

            # Save a possible larger character at this position
            greater = -1
            for c in range(x + 1, 26):
                if counts[c] > 0:
                    greater = c
                    break

            if greater != -1:
                possible_greater.append((i, prefix[:], greater, counts[:]))

            # Continue matching target if possible
            if 0 <= x < 26 and counts[x] > 0:
                prefix.append(t[i])
                counts[x] -= 1
            else:
                break
        else:
            # target[:m] itself is possible.
            # If its palindrome is greater than target, use it.
            candidate = make_palindrome(t)
            if candidate > target:
                return candidate

        # Find the rightmost position where we can make the half larger.
        if possible_greater:
            i, pref, greater, old_counts = possible_greater[-1]

            old_counts[greater] -= 1

            result = ''.join(pref)
            result += chr(ord('a') + greater)

            # Fill remaining characters in smallest order
            for c in range(26):
                result += chr(ord('a') + c) * old_counts[c]

            candidate = make_palindrome(result)

            if candidate > target:
                return candidate

        return ""