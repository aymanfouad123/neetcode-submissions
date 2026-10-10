class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for ele in strs:
            result += str(len(ele)) + "#" + ele
        return result

    def decode(self, s: str) -> List[str]:
        i = 0
        decoded = []

        while i<len(s):
            # capturing the offset
            j = i
            while s[j] != "#":
                j+=1
            
            offset = int(s[i:j])
            
            i = j + 1
            j = offset + i

            decoded.append(s[i:j])
            i = j

        return decoded
            
