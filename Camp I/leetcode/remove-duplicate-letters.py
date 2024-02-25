class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        mstack = []
        bouncer = set()
        occured = {}

        for i in range(len(s)):
            occured[s[i]] = i

        for i in range(len(s)):
            if s[i] not in bouncer:
                while mstack and mstack[-1] > s[i] and occured[mstack[-1]] > i:
                    bouncer.remove(mstack.pop())

                mstack.append(s[i])
                bouncer.add(s[i])

        return "".join(mstack)