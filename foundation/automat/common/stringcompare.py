class StringCompare:
    """TODO please put LongestCommonSubsequence, LongestCommonSubstring here too :D"""

    @classmethod
    def damerauLevenshtein(cls, a, b):
        """Courtesy of https://en.wikipedia.org/wiki/Damerau%E2%80%93Levenshtein_distance

        """
        d = [[0 for _ in range(len(b)+1)] for _ in range(len(a)+1)]# a is the first index, b is the second index
        # import pdb;pdb.set_trace()

        for i in range(0, len(a)+1):
            d[i][0] = i
        for j in range(0, len(b)+1):
            d[0][j] = j

        for i in range(1, len(a)+1):
            for j in range(1, len(b)+1):
                if a[i-1] == b[j-1]:
                    cost = 0
                else:
                    cost = 1
                d[i][j] = min(
                    d[i-1][j]+1, #deletion
                    d[i][j-1]+1, #insertion
                    d[i-1][j-1]+cost #substitution
                )
                if i >1 and j >1 and a[i-1]==b[j-2] and a[i-2]==b[j-1]:
                    d[i][j] = min(d[i][j], d[i-2][j-2]+1)#transposition
        #
        import pprint; pp = pprint.PrettyPrinter(indent=4);
        pp.pprint(d)
        #
        return d[len(a)][len(b)]