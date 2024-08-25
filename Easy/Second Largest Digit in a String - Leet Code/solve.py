def secondHighest(s: str) -> int:
      num1 = -1
      num2 = -1

      for i in range(len(s)):
          if s[i].isdigit():
              
              if int(s[i]) > num1:
                  num2 = int(num1)
                  num1 = int(s[i])
              
              if int(s[i]) < num1 and int(s[i]) > num2:
                  num2 = int(s[i])
      
      return num2 if num2 != -1 else -1
