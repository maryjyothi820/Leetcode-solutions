1138:Alpabet_board_path.py
class Solution:
    def alphabetBoardPath(self, target):
        pos = {}

        for i in range(26):
            ch = chr(ord('a') + i)
            pos[ch] = (i // 5, i % 5)

        r = c = 0
        ans = []

        for ch in target:
            nr, nc = pos[ch]

            # Move Up
            while r > nr:
                ans.append('U')
                r -= 1

            # Move Left
            while c > nc:
                ans.append('L')
                c -= 1

            # Move Down
            while r < nr:
                ans.append('D')
                r += 1

            # Move Right
            while c < nc:
                ans.append('R')
                c += 1

            ans.append('!')

        return ''.join(ans)
