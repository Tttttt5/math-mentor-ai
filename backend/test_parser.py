from agents.parser_agent import parse_problem


if __name__ == "__main__":

    question = "find derivative x square plus 3x"

    result = parse_problem(question)

    print("\nParsed Result:\n")
    print(result)