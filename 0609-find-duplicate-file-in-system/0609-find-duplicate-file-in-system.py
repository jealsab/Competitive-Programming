class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        '''
            ["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)","root 4.txt(efgh)"]
        '''
        dict = collections.defaultdict(list)
        for path in paths:
            store = path.split()
            directory, files = store[0], store[1:]
            for file in files:
                name, content = file.rstrip(')').split('(')
                dict[content].append(directory + '/'+name)
        result = []
        for key, value in dict.items():
            if len(value) > 1:
                result.append(value)
        return result
