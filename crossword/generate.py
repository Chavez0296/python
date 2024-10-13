from queue import Queue
import sys

from crossword import *
from crossword import Crossword, Variable


class CrosswordCreator():

    def __init__(self, crossword):
        """
        Create new CSP crossword generate.
        """
        self.crossword = crossword
        self.domains = {
            var: self.crossword.words.copy()
            for var in self.crossword.variables
        }

    def letter_grid(self, assignment):
        """
        Return 2D array representing a given assignment.
        """
        letters = [
            [None for _ in range(self.crossword.width)]
            for _ in range(self.crossword.height)
        ]
        for variable, word in assignment.items():
            direction = variable.direction
            for k in range(len(word)):
                i = variable.i + (k if direction == Variable.DOWN else 0)
                j = variable.j + (k if direction == Variable.ACROSS else 0)
                letters[i][j] = word[k]
        return letters

    def print(self, assignment):
        """
        Print crossword assignment to the terminal.
        """
        letters = self.letter_grid(assignment)
        for i in range(self.crossword.height):
            for j in range(self.crossword.width):
                if self.crossword.structure[i][j]:
                    print(letters[i][j] or " ", end="")
                else:
                    print("█", end="")
            print()

    def save(self, assignment, filename):
        """
        Save crossword assignment to an image file.
        """
        from PIL import Image, ImageDraw, ImageFont
        cell_size = 100
        cell_border = 2
        interior_size = cell_size - 2 * cell_border
        letters = self.letter_grid(assignment)

        # Create a blank canvas
        img = Image.new(
            "RGBA",
            (self.crossword.width * cell_size,
             self.crossword.height * cell_size),
            "black"
        )
        font = ImageFont.truetype("assets/fonts/OpenSans-Regular.ttf", 80)
        draw = ImageDraw.Draw(img)

        for i in range(self.crossword.height):
            for j in range(self.crossword.width):

                rect = [
                    (j * cell_size + cell_border,
                     i * cell_size + cell_border),
                    ((j + 1) * cell_size - cell_border,
                     (i + 1) * cell_size - cell_border)
                ]
                if self.crossword.structure[i][j]:
                    draw.rectangle(rect, fill="white")
                    if letters[i][j]:
                        _, _, w, h = draw.textbbox((0, 0), letters[i][j], font=font)
                        draw.text(
                            (rect[0][0] + ((interior_size - w) / 2),
                             rect[0][1] + ((interior_size - h) / 2) - 10),
                            letters[i][j], fill="black", font=font
                        )

        img.save(filename)

    def solve(self):
        """
        Enforce node and arc consistency, and then solve the CSP.
        """
        self.enforce_node_consistency()
        self.ac3()
        return self.backtrack(dict())

    def enforce_node_consistency(self):
        """
        Update `self.domains` such that each variable is node-consistent.
        (Remove any values that are inconsistent with a variable's unary
         constraints; in this case, the length of the word.)
        """
        for var in self.crossword.variables:
            unfit = []
            
            for word in self.domains[var]:
                if len(word) != var.length:
                    unfit.append(word)
            
            for word in unfit:
                self.domains[var].remove(word)
        

    def revise(self, x, y):
        """
        Make variable `x` arc consistent with variable `y`.
        To do so, remove values from `self.domains[x]` for which there is no
        possible corresponding value for `y` in `self.domains[y]`.

        Return True if a revision was made to the domain of `x`; return
        False if no revision was made.
        """
        overlap = self.crossword.overlaps[x, y]

        if overlap is None:
            return False
        
        i, j = overlap
        revised = False
        unfit = []

        for word_lat in self.domains[x]:
            found = False
            for word_hori in  self.domains[y]:
                if word_lat[i] == word_hori[j]:
                    found = True
                    break
            
            if not found:
                unfit.append(word_lat)
        
        for word_lat in unfit:
            self.domains[x].remove(word_lat)
            revised = True
        
        return revised
        raise NotImplementedError

    def ac3(self, arcs=None):
        """
        Update `self.domains` such that each variable is arc consistent.
        If `arcs` is None, begin with initial list of all arcs in the problem.
        Otherwise, use `arcs` as the initial list of arcs to make consistent.

        Return True if arc consistency is enforced and no domains are empty;
        return False if one or more domains end up empty.
        """
        queue = Queue()

        if arcs is None:
            for x in self.crossword.variables:
                for y in self.crossword.neighbors(x):
                    queue.put((x, y))
        else:
            for arc in arcs:
                queue.put(arc)
        
        while not queue.empty():
            x, y = queue.get()

            if self.revise(x, y):
                if len(self.domains[x]) == 0:
                    return False
            
            for neighnor in self.crossword.neighbors(x):
                if neighnor != y:
                    queue.put((neighnor, x))

        return True
    
        raise NotImplementedError

    def assignment_complete(self, assignment):
        """
        Return True if `assignment` is complete (i.e., assigns a value to each
        crossword variable); return False otherwise.
        """
        for var in self.crossword.variables:
            if var not in assignment or assignment[var] is None:
                return False
        
        return True
        raise NotImplementedError

    def consistent(self, assignment):
        """
        Return True if `assignment` is consistent (i.e., words fit in crossword
        puzzle without conflicting characters); return False otherwise.
        """
        for var in assignment:
            word = assignment[var]
            #print(f"Checking variable: {var}, assigned word: {word}")

            # Check if the length of the word matches the variable's length
            if len(word) != var.length:
                #print(f"Length mismatch: {len(word)} != {var.length}")
                return False
            
            for neighbor in self.crossword.neighbors(var):
                if neighbor in assignment:
                    neighborWord = assignment[neighbor]
                    overlap = self.crossword.overlaps[var, neighbor]

                    if overlap is not None:
                        i, j = overlap
                        #print(f"Checking overlap: {var} with {neighbor} at positions {i}, {j}")
                        # Check for character conflict at the overlapping positions
                        if word[i] != neighborWord[j]:
                            #print(f"Conflict: {word[i]} != {neighborWord[j]}")
                            return False
        return True
        raise NotImplementedError

    def order_domain_values(self, var, assignment):
        """
        Return a list of values in the domain of `var`, in order by
        the number of values they rule out for neighboring variables.
        The first value in the list, for example, should be the one
        that rules out the fewest values among the neighbors of `var`.
        """
        def count_rules_out(value):
        # Count how many values this assignment rules out in neighboring variables
            count = 0
            for neighbor in self.crossword.neighbors(var):
                if neighbor not in assignment:  # Only consider unassigned neighbors
                    # Assume neighbor has its own domain of possible values
                    count += len(self.domains[neighbor])
            return count

        # Sort domain values by the count of ruled-out options in neighbors
        return sorted(self.domains[var], key=count_rules_out)
        raise NotImplementedError

    def select_unassigned_variable(self, assignment):
        """
        Return an unassigned variable not already part of `assignment`.
        Choose the variable with the minimum number of remaining values
        in its domain. If there is a tie, choose the variable with the highest
        degree. If there is a tie, any of the tied variables are acceptable
        return values.
        """
        unassigned = [
        var for var in self.crossword.variables if var not in assignment
        ]

        # Create a list of tuples for sorting: (domain length, -degree, variable)
        variable_info = []
        for var in unassigned:
            degree = len(self.crossword.neighbors(var))  # Count of neighbors
            domain_length = len(self.domains[var])  # Domain size
            variable_info.append((domain_length, -degree, var))

        # Sort the tuples first by the length of their domain, then by degree
        variable_info.sort(key=lambda x: (x[0], x[1]))  # Sort based on the first and second elements

        # Extract the variable with the best priority
        return variable_info[0][2] if variable_info else None
        raise NotImplementedError

    def backtrack(self, assignment):
        """
        Using Backtracking Search, take as input a partial assignment for the
        crossword and return a complete assignment if possible to do so.

        `assignment` is a mapping from variables (keys) to words (values).

        If no assignment is possible, return None.
        """
        if self.assignment_complete(assignment):
            #print("Completed assignment:", assignment)
            return assignment

        var = self.select_unassigned_variable(assignment)
        #print(f"Selecting variable: {var}")

        for value in self.order_domain_values(var, assignment):
            #print(f"Trying value '{value}' for variable {var}")
            assignment[var] = value

            if self.consistent(assignment):
                #print(f"Value '{value}' is consistent with current assignment.")
                result = self.backtrack(assignment)
                if result is not None:
                    return result
                #print(f"Backtracking from value '{value}' for variable {var}")

            del assignment[var]
            #print(f"Removed assignment for variable {var}, trying next value.")

        return None
        raise NotImplementedError


def main():

    # Check usage
    if len(sys.argv) not in [3, 4]:
        sys.exit("Usage: python generate.py structure words [output]")

    # Parse command-line arguments
    structure = sys.argv[1]
    words = sys.argv[2]
    output = sys.argv[3] if len(sys.argv) == 4 else None

    # Generate crossword
    crossword = Crossword(structure, words)
    creator = CrosswordCreator(crossword)
    assignment = creator.solve()

    # Print result
    if assignment is None:
        print("No solution.")
    else:
        creator.print(assignment)
        if output:
            creator.save(assignment, output)


if __name__ == "__main__":
    main()
