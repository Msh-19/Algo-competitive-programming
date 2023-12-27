class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.token = dict()
        self.time = timeToLive

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.token[tokenId] = currentTime

    def renew(self, tokenId: str, currentTime: int) -> None:
        limit = currentTime - self.time
        if tokenId in self.token and self.token[tokenId]>limit:
            self.token[tokenId] = currentTime

    def countUnexpiredTokens(self, currentTime: int) -> int:
        limit = currentTime - self.time
        c = 0
        for i in self.token:
            if self.token[i]>limit:
                c+=1
        return c


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)