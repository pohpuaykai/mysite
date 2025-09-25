TEST_DATUM={
    ('vor', '0'): {   'expected': '(= a (- 0 (- 0 a)))',
                      'input': '(= a a)'},
    ('hin', '0'): {   'expected': '(= a a)',
                      'input': '(= a (- 0 (- 0 a)))'},

    ('vor', '1'): {   'expected': '(= c (- (- 0 a) (- 0 b)))',
                      'input': '(= c (- b a))'},
    ('hin', '1'): {   'expected': '(= c (- b a))',
                      'input': '(= c (- (- 0 a) (- 0 b)))'},


    ('vor', '2'): {   'expected': '(= a (- 0 (+ (- 0 b) c)))',
                      'input': '(= a (- b c))'},
    ('hin', '2'): {   'expected': '(= a (- b c))',
                      'input': '(= a (- 0 (+ (- 0 b) c)))'},



    ('vor', '3'): {   'expected': '(= a (- 0 (- (- 0 b) c)))',
                      'input': '(= a (+ b c))'},
    ('hin', '3'): {   'expected': '(= a (+ b c))',
                      'input': '(= a (- 0 (- (- 0 b) c)))'},

                      }