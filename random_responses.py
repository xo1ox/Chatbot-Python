import random

def random_string():
    random_list = [
        "Please write something more descriptive!"
        "I don't understand what you mean. Could you phrase your question differently?"
        "Oh, you wrote something I don't understand yet."
        "I'm terribly sorry, I didn't understand that."
        "I can't answer that yet. Please ask a different question."
    ]

    list_count = len(random_list)
    random_item = random.randrange(list_count)

    return random_list[random_item]