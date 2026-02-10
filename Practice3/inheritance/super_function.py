class P:
    def __init__(self,n): self.n=n
class S(P):
    def __init__(self,n,g): super().__init__(n); self.g=g
s=S('Alex',90); print(s.n,s.g)