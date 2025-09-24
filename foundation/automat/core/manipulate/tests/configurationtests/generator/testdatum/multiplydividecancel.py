TEST_DATUM={
    ('hin', '0'): {   'expected': '(= (* (/ a v_{0}) v_{0}) (* (/ a v_{1}) v_{1}))',
                      'input': '(= a a)'},
    ('vor', '0'): {'expected': '(= a b)', 'input': '(= a (* (/ b c) c))'},

    ('hin', '1'): {   'expected': '(= (/ (* a v_{0}) v_{0}) (/ (* a v_{1}) v_{1}))',
                      'input': '(= a a)'},
    ('vor', '1'): {'expected': '(= a b)', 'input': '(= a (/ (* b c) c))'},

    ('hin', '2'): {
      'expected':'(= a (/ b c))',
      'input':'(= a (* b (/ 1 c)))'
    },

    ('vor', '2'): {
      'expected':'(= a (* b (/ 1 c)))',
      'input':'(= a (/ b c))'

    }
    }