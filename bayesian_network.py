class BayesianNetwork:
    def __init__(self):
        self.nodes = []
        self.cpt = {}  
        self.dependencies = {} 

    def add_node(self, name):
        if name not in self.nodes:
            self.nodes.append(name)
    
    def set_dependency(self, child, parent):
        if child not in self.dependencies:
            self.dependencies[child] = []
        self.dependencies[child].append(parent)

    def add_probability(self, string, probability):
        self.cpt[string] = probability
        complementary = "~" + string 
        comp = 1-probability 
        self.cpt[complementary] = 1 - probability

    def find_probability(self, prob):
        if prob in self.cpt:
            return self.cpt[prob]
        else: 
            return "Could not find probability."

    def total_probability(self, event, given):
        total = 0
        for g in given:
            key = f"{event}|{given}"
            if key in self.cpt and given in self.cpt:
                total += self.probabilities[key]*self.probabilities[given]
            else:
                return f"Error: Not enough information to calculate."
        return total

    def bayes_formula(self, event, given):
        reverse_key = f"{given}|{event}"
        if (
            reverse_key in self.cpt
            and event in self.cpt
            and given in self.cpt
        ):
            numerator = self.cpt[reverse_key] * self.cpt[event]
            denominator = self.cpt[given]
            if denominator == 0:
                return "Error: Division by zero."
            return numerator / denominator
        return "Error: Missing probabilities."

    def joint_probability(self, event, given):
        key = f"{event}|{given}"
        if key in self.cpt and given in self.cpt:
            return self.cpt[key] * self.cpt[given]
        return "Error: Missing probabilities."
    
    def display_network(self): 
        print("\nNodes:")
        print(self.nodes)
        print("\nConditional Probability Table:")
        for conditions, prob in self.cpt.items():
            print(f"P({conditions}) = {prob}")
        print("\nDependencies:")
        for child, parents in self.dependencies.items():
            print(f"{child} depends on {parents}")
 
def bayes_network():
    bn = BayesianNetwork()
    print("Build a Bayesian Network!")
    while True:
        print("\nOptions:")
        print("1: Add a Node")
        print("2: Set a Dependency")
        print("3: Define a Probability")
        print("4: Find a Probability")
        print("5: Display")
        print("6: Quit")
        choice = input()

        if choice == "1":
            name = input("Enter node name: ")
            bn.add_node(name)
            print(f"{name} added.")

        elif choice == "2":
            child = input("Enter child name: ")
            if child not in bn.nodes:
                print("Node does not exist. Add the node first.")
                continue
            parent = input("Enter parent name: ")
            if parent not in bn.nodes:
                print("Node does not exist. Add the node first.")
                continue
            bn.set_dependency(child, parent)
            print(f"{parent} is the parent of node {child}.")

        elif choice == "3":
            prob = input("Enter a probability value (eg. P(query|given) = 0.1): ")
            if prob.startswith("P("):
                try:
                    part, val = prob.split("=")
                    part = part.strip()[2:-1]
                    probability = float(val.strip())
                    bn.add_probability(part, probability)
                    print("Probability added.")
                except Exception as e:
                    print(f"Error: {e}") 

        elif choice == "4":
            search = input("Type in the probability that you are looking for: (eg. P(O1|G)) ")
            if search.startswith("P("):
                try:
                    prob = search.strip()[2:-1]
                    print(bn.find_probability(prob))
                except Exception as e:
                    print(f"Error: {e}") 

        elif choice == "5": 
            bn.display_network()

        elif choice == "6":
            print("Quitting Bayesian Network Builder.")
            break

        else:
            print("Invalid. Try again.")

if __name__ == "__main__":
    bayes_network()