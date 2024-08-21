def decodeMessage(key: str, message: str) -> str:
        hm = {' ':' '}
        result = ''
        alpha_set = 'abcdefghijklmnopqrstuvwxyz'
        i = 0
        for chr in key:
            if chr not in hm:
                hm[chr] = alpha_set[i]
                i += 1
        for chr in message:
            result += hm[chr]
        return result
