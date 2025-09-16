TEST_DATUM={
    ('vor', '0'): {   'expected': '(= a (- 0 (- 0 a)))',
                      'input': '(= a a)'},
    ('hin', '0'): {   'expected': '(= a a)',
                      'input': '(= a (- 0 (- 0 a)))'},

    ('vor', '1'): {   'expected': '(= c (- (- 0 a) (- 0 b)))',
                      'input': '(= c (- b a))'},
    ('hin', '1'): {   'expected': '(= c (- b a))',
                      'input': '(= c (- (- 0 a) (- 0 b)))'},


                      }