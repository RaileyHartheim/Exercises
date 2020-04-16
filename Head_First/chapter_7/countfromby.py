class CountFromBy:
    def __init__(self, v: int=0, i: int=1) -> None:
        v = self.val
        i = self.incr
    
    def __repr__(self) -> str:
        return str(self.val)
    
    def increase(self) -> None:
        self.val += self.incr
