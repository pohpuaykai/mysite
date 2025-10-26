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


    ('hin', '4'): {   'expected': '(= (* a b) a)',
                      'input': '(= b 1)'},
    ('vor', '4'): {   'expected': '(= b 1)',
                      'input': '(= (* a b) a)'},


    ('hin', '5'): {   'expected': '(= (* (* a b) c) a)',
                      'input': '(= (* b c) 1)'},
    ('vor', '5'): {   'expected': '(= (* b c) 1)',
                      'input': '(= (* (* a b) c) a)'},


    ('hin', '6'): {   'expected': '(= a (/ (* b a) c))',
                      'input': '(= 1 (/ b c))'},
    ('vor', '6'): {   'expected': '(= 1 (/ b c))',
                      'input': '(= a (/ (* b a) c))'},



}