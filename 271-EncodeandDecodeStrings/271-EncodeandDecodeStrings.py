# Last updated: 18/06/2025, 19:57:30
class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        enc_str = ""
        for s in strs:
            enc_str += str(len(s))+"#"+s
        return enc_str


    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        res = []
        i = 0

        while i < len(s):
            j = i
            # Move j to find '#' character
            while s[j]!= '#':
                j += 1
            length = int(s[i:j])

            i = j + 1
            j = i + length

            res.append(s[i:j])
            
            i = j
        
        return res


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))