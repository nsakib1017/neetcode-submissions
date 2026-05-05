class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        list_of_operends = []
        for i in tokens:
            if i == "+":
                opp_a = list_of_operends.pop()
                opp_b = list_of_operends.pop()
                list_of_operends.append(int(opp_a) + int(opp_b))
            elif i == "-":
                opp_a = list_of_operends.pop()
                opp_b = list_of_operends.pop()
                list_of_operends.append(int(opp_b) - int(opp_a))
            elif i == "*":
                opp_a = list_of_operends.pop()
                opp_b = list_of_operends.pop()
                list_of_operends.append(int(opp_a) * int(opp_b))
            elif i == "/":
                opp_a = list_of_operends.pop()
                opp_b = list_of_operends.pop()
                list_of_operends.append(int(int(opp_b) / int(opp_a)))
            else:
               list_of_operends.append(int(i))
        return list_of_operends.pop()