
def escapeshellarg_sim(arg):
    """Simulates PHP's escapeshellarg() function."""
    arg = arg.replace("'", "''")
    return "'" + arg + "'"

# Test cases
test_cases = [
    "test",
    "'test'",
    "`ls -l`",
    "\ncat /etc/passwd",
    "abc^def",
    "'; ls -l '",
    '"',
    '$',
    ';',
    '&',
    '|',
    '\n',
    "abc^def",
    "test;ls",
    "test#comment",
    "'test;ls#'"
]

for test_case in test_cases:
    escaped_arg = escapeshellarg_sim(test_case)
    print(f"Input: {test_case}, Escaped: {escaped_arg}")