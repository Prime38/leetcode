def countPalindromeSubstrings(s: str) -> str:

    ans=0

    for i in range(len(s)):
        # odd length
        l, r = i, i
        while l >= 0 and r < len(s) and s[l] == s[r]:
            ans+=1
            l -= 1
            r += 1

        # even length
        l, r = i, i + 1
        while l >= 0 and r < len(s) and s[l] == s[r]:
            ans += 1
            l -= 1
            r += 1
    return ans


if __name__ == '__main__':
    print(countPalindromeSubstrings( "aaab"))
