class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded=""
        char_=  "é"
        for s in strs:
            encoded=encoded+s+char_
        return encoded
    def decode(self, s: str) -> List[str]:
        char_=  "é"
        output = [""]
        if s:
            output = s.split(char_)
        return output[:len(output)-1]