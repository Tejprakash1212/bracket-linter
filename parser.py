def check_brackets(text):

    stack = []

    opening = ['(', '[', '{']
    closing = [')', ']', '}']

    matches = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    errors = []

    for i, ch in enumerate(text):

        # Opening bracket
        if ch in opening:

            stack.append((ch, i))

        # Closing bracket
        elif ch in closing:

            if not stack:

                errors.append(
                    f"Extra closing bracket '{ch}' at position {i}"
                )

            else:

                top, pos = stack[-1]

                if top == matches[ch]:

                    stack.pop()

                else:

                    errors.append(
                        f"Mismatched '{ch}' at position {i}"
                    )

    # Remaining unclosed brackets
    while stack:

        ch, pos = stack.pop()

        errors.append(
            f"Unclosed bracket '{ch}' at position {pos}"
        )

    return errors