class RateLimiter:
    def __init__(self, limit_n):
        self.limit_n = limit_n
        self.req = {}


    def allow_request(self, user_id):
        if user_id not in self.req:
            self.req[user_id] = self.limit_n - 1
            return True
        elif self.req[user_id] > 0:
            self.req[user_id] -= 1
            return True
        else:
            return False


RL = RateLimiter(5)
print(RL.allow_request("atiya"))
print(RL.allow_request("atiya"))
print(RL.allow_request("atiya"))
print(RL.allow_request("atiya"))
print(RL.allow_request("atiya"))
print(RL.allow_request("atiya"))





