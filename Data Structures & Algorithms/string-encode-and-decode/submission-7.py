class Solution:
    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0: return "\r"

        return "\n".join(strs)

    def decode(self, s: str) -> List[str]:
        if s == "\r": return []
        return s.split("\n")
