from csp import Constraint, CSP
from typing import Dict, List, Optional

class Solution(Constraint[str, str]):
    def __init__(self, place1: str, place2: str) -> None:
        super().__init__([place1, place2])
        self.place1: str = place1
        self.place2: str = place2
  
    def satisfied(self, assignment: Dict[str, str]) -> bool:
        # If either place is not in the assignment then it is not
        # yet possible for their colors to be conflicting
        if self.place1 not in assignment or self.place2 not in assignment:
            return True
        # check the color assigned to place1 is not the same as the
        # color assigned to place2
        return assignment[self.place1] != assignment[self.place2]
if __name__ == '__main__':
    variables: List[str] = ['Class 1', 'Class 2', 'Class 3', 'Class 4', 'Class 5']
    domains: Dict[str, List[str]] = {}
    domains['Class 1'] = {'Professor C'}
    domains['Class 2'] = {'Professor B', 'Professor C'}
    domains['Class 3'] = {'Professor A','Professor B', 'Professor C'}
    domains['Class 4'] = {'Professor A','Professor B', 'Professor C'}
    domains['Class 5'] = {'Professor B', 'Professor C'}
    csp: CSP[str, str] = CSP(variables, domains)
    csp.add_constraint(Solution('Class 1', 'Class 2'))
    csp.add_constraint(Solution('Class 2', 'Class 3'))
    csp.add_constraint(Solution('Class 3', 'Class 4'))
    csp.add_constraint(Solution('Class 4', 'Class 5'))
    csp.add_constraint(Solution('Class 4', 'Class 2'))
    csp.add_constraint(Solution('Class 5', 'Class 3'))
solution: Optional[Dict[str, str]] = csp.backtracking_search()
if solution is None:
    print('No solution found!')
else:
  
    print(solution)