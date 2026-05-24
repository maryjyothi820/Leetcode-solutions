299.Bulls_and_cows
class Solution:
    def getHint(self, secret, guess):
        bulls = 0
        secret_count = {}
        guess_count = {}

        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1
            else:
                secret_count[secret[i]] = secret_count.get(secret[i], 0) + 1
                guess_count[guess[i]] = guess_count.get(guess[i], 0) + 1

        cows = 0

        for digit in secret_count:
            if digit in guess_count:
                cows += min(secret_count[digit], guess_count[digit])

        return str(bulls) + "A" + str(cows) + "B"