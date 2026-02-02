def simple_chatbot(user_query):
    user_query = user_query.lower()

    if user_query == "what is the total revenue?":
        return (
            "Based on the latest data:\n"
            "Microsoft: $227.6B\n"
            "Apple: $383.3B\n"
            "Tesla: $96.7B"
        )

    elif user_query == "how has net income changed over the last year?":
        return (
            "Net income trend:\n"
            "Microsoft: Increased\n"
            "Apple: Slightly decreased\n"
            "Tesla: Fluctuated due to pricing and costs"
        )

    elif user_query == "which company has the highest revenue?":
        return "Apple has the highest total revenue among the three companies."

    elif user_query == "is operating cash flow increasing?":
        return (
            "Yes.\n"
            "Microsoft and Apple show stable operating cash flow growth.\n"
            "Tesla shows variation year to year."
        )

    elif user_query == "help":
        return (
            "I can answer these questions:\n"
            "- What is the total revenue?\n"
            "- How has net income changed over the last year?\n"
            "- Which company has the highest revenue?\n"
            "- Is operating cash flow increasing?"
        )

    else:
        return "Sorry, I can only answer predefined financial questions."


# Chat loop
print("Financial Chatbot (type 'help' to see questions, 'exit' to quit)\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Chatbot: Thank you! Goodbye.")
        break

    response = simple_chatbot(user_input)
    print("Chatbot:", response)
