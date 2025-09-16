TEST_DATUM={
    ('hin', '0'): {   'expected': '(= a (+ (/ b c) (/ d e)))',
                      'input': '(= a (/ (+ (* b e) (* c d)) (* c e)))'},
    ('vor', '0'): {   'expected': '(= a (/ (+ (* b e) (* c d)) (* c e)))',
                      'input': '(= a (+ (/ b c) (/ d e)))'}}