TEST_DATUM={
    ('hin', '0'): {   'expected': '(= a (nroot (- "0" b) c))',
                      'input': '(= a (nroot b (/ "1" c)))'},
    ('vor', '0'): {   'expected': '(= a (nroot b (/ "1" c)))',
                      'input': '(= a (nroot (- "0" b) c))'}}