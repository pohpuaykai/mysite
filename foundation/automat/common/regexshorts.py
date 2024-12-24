import re

class Regexshorts:

    @classmethod
    def getMatchesOrNone(cls, pattern, searchText):
        """
        Just a simple wrapper to simplify the syntax of re.search
        Only first the FIRST OCCURENCE of each capturing group!

        :param pattern: regex
        :type pattern: str
        :param searchText: text to search in for `pattern`
        :type pattern: str
        :return: tuple containing all the matches, or empty tuple
        :rtype: tuple
        """
        matches = re.search(pattern, searchText)
        if matches: #if matches not None
            return matches.groups()
        return ()

    @classmethod
    def findAllMatches(cls, pattern, searchText):
        """
        Just a simple wrapper to simplify the syntex of re.finditer
        Finds all the occurences of each capturing group
        Ex :- if we are looking for x in 'xyxyxy', 3 matches will be returned.

        :param pattern: regex
        :type pattern: str
        :param searchText: text to search in for `pattern`
        :type pattern: str
        :return: list containing every re.Match that fits the pattern
        :rtype: list[re.Match]
        """
        return list(re.finditer(pattern, searchText))


    @classmethod
    def lazyPrefixFinder(cls, prefix, st):
        """
        returns position of prefix in st, only when __next__ is called (LAZY)

        :param prefix:
        :type prefix: str
        :param st:
        :type st: str
        """
        chopped = 0
        startingPos = 0
        while startingPos < len(st):
            try:
                startingPos = st.index(prefix)
                st = st[startingPos+len(prefix):]
                yield chopped+startingPos
                chopped += startingPos+len(prefix)
            except:
                return

    @classmethod
    def replaceAtPos(cls, st, startPos, endPos, replacement):
        """
        replace the st from startPos(inclusive) to endPos(exclusive) with replacement
        Essentiellement, c'est syntactic-sucre pour
        st[startPos:endPos] = replacement

        :param st:
        :type st: str
        :param startPos:
        :type startPos: int
        :param endPos:
        :type endPos: int
        :param replacement:
        :type replacement: str
        """
        firstPiece = st[:startPos]
        thirdPiece = st[endPos:]
        return firstPiece + replacement + thirdPiece