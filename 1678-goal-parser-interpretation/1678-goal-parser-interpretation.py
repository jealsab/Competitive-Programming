class Solution(object):
    def interpret(self, command):
        """
        :type command: str
        :rtype: str
        """
        output=[]
        for i in range(len(command)):
            if command[i]=='G':
                output.append("G")
            elif command[i]=='(':
                if command[i+1]==')':
                    output.append("o")
                else:
                    output.append("al")
        return "".join(output)