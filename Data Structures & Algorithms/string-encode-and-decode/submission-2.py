class Solution:
    # First ?1000? chars are the header of every message. They hold the information after which characters there should be a space
    def encode(self, strs: List[str]) -> str:

        spaces = []

        for word in strs:
            spaces.append(len(word))

        # spaces.pop()
        
        spaces = ";".join(str(x) for x in spaces)
        spaces = list(spaces)
        
        header = ["x"] * 1000        

        for i, char in enumerate(spaces):
            header[i] = char
        
        message = "".join(header)

        for word in strs:
            message = message + word

        return message



    def decode(self, s: str) -> List[str]:

        header = s[:1000]
        header = header.replace("x", "")
        message = s[1000:]
        strs = []

        if header == "":
            return []

        spaces = header.split(";")

        start = 0

        for length in spaces:
            length = int(length)

            word = message[start:start+length]
            strs.append(word)

            start = start + length

        return strs



