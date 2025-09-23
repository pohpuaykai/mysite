TEST_DATUM={
    ('hin', '0'): {   'expected': '(= (* a b) (* a c))',
                      'input': '(= b c)'},
    ('vor', '0'): {   'expected': '(= b c)',
                      'input': '(= (* a b) (* a c))'},

    ('hin', '1'): {   'expected': '(= (/ a b) (/ c b))',
                      'input': '(= a c)'},
    ('vor', '1'): {   'expected': '(= a c)',
                      'input': '(= (/ a b) (/ c b))'},

    ('hin', '2'): {   'expected': '(= (+ a b) (+ a c))',
                      'input': '(= b c)'},
    ('vor', '2'): {   'expected': '(= b c)',
                      'input': '(= (+ a b) (+ a c))'},

    ('hin', '3'): {   'expected': '(= (- b a) (- c a))',
                      'input': '(= b c)'},
    ('vor', '3'): {   'expected': '(= b c)',
                      'input': '(= (- b a) (- c a))'},


}