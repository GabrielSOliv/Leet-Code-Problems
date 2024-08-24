def encode(strs: list[str]) -> str:
  strOut = ''
  for i in strs:
      strOut += i + '$'
  
  return strOut


def decode(s: str) -> list[str]:
  strList =[]
  currentStr = ''
  for i in range(len(s)):
      if s[i] != '$':
          currentStr += s[i]
      else:
          strList.append(currentStr)
          currentStr = ''
  
  return strList
