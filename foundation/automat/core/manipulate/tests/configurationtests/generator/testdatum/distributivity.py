TEST_DATUM={
    ('hin', '0'): {   'expected': '(= a (+ (* b c) (* b d)))',
                      'input': '(= a (* b (+ c d)))'},
    ('vor', '0'): {   'expected': '(= a (* b (+ c d)))',
                      'input': '(= a (+ (* b c) (* b d)))'},
    ('hin', '1'): {   'expected': '(= a (- (* b c) (* b d)))',
                      'input': '(= a (* b (- c d)))'},
    ('vor', '1'): {   'expected': '(= a (* b (- c d)))',
                      'input': '(= a (- (* b c) (* b d)))'},

    ('hin', '2'): {
      'expected':'(= a (+ (/ b c) (/ b d)))',
      'input':'(= a (* b (+ (/ 1 c) (/ 1 d))))'
    },
    ('vor', '2'): {
      'expected':'(= a (* b (+ (/ 1 c) (/ 1 d))))',
      'input':'(= a (+ (/ b c) (/ b d)))'
    },

    ('hin', '3'): {
      'expected':'(= a (- (/ b c) (/ b d)))',
      'input':'(= a (* b (- (/ 1 c) (/ 1 d))))'
    },
    ('vor', '3'): {
      'expected':'(= a (* b (- (/ 1 c) (/ 1 d))))',
      'input':'(= a (- (/ b c) (/ b d)))'
    },

    ('hin', '4'): {
      'expected':'(= a (+ (/ b c) (* b d)))',
      'input':'(= a (* b (+ (/ 1 c) d)))'
    },
    ('vor', '4'): {
      'expected':'(= a (* b (+ (/ 1 c) d)))',
      'input':'(= a (+ (/ b c) (* b d)))'
    },

    ('hin', '5'): {
      'expected':'(= a (- (/ b c) (* b d)))',
      'input':'(= a (* b (- (/ 1 c) d)))'
    },
    ('vor', '5'): {
      'expected':'(= a (* b (- (/ 1 c) d)))',
      'input':'(= a (- (/ b c) (* b d)))'
    },


    ('hin', '6'): {
      'expected':'(= a (+ (* b c) (/ b d)))',
      'input':'(= a (* b (+ c (/ 1 d))))'
    },
    ('vor', '6'): {
      'expected':'(= a (* b (+ c (/ 1 d))))',
      'input':'(= a (+ (* b c) (/ b d)))'
    },

    ('hin', '7'): {
      'expected':'(= a (- (* b c) (/ b d)))',
      'input':'(= a (* b (- c (/ 1 d))))'
    },
    ('vor', '7'): {
      'expected':'(= a (* b (- c (/ 1 d))))',
      'input':'(= a (- (* b c) (/ b d)))'
    },



    ('hin', '8'): {   'expected': '(= a (+ (/ b d) (/ c d)))',
                      'input': '(= a (/ (+ b c) d))'},
    ('vor', '8'): {   'expected': '(= a (/ (+ b d) c))',
                      'input': '(= a (+ (/ b c) (/ d c)))'},
    ('hin', '9'): {   'expected': '(= a (- (/ b d) (/ c d)))',
                      'input': '(= a (/ (- b c) d))'},
    ('vor', '9'): {   'expected': '(= a (/ (- b d) c))',
                      'input': '(= a (- (/ b c) (/ d c)))'},

    ('hin', '10'): {   'expected': '(= a (+ (* b d) (* c d)))',
                      'input': '(= a (* (+ b c) d))'},
    ('vor', '10'): {   'expected': '(= a (* (+ b d) c))',
                      'input': '(= a (+ (* b c) (* d c)))'},
    ('hin', '11'): {   'expected': '(= a (- (* b d) (* c d)))',
                      'input': '(= a (* (- b c) d))'},
    ('vor', '11'): {   'expected': '(= a (* (- b d) c))',
                      'input': '(= a (- (* b c) (* d c)))'},



    ('hin', '12'): {   'expected': '(- (* a b) (* c a))',
                      'input': '(* (- b c) a)'},
    ('vor', '12'): {   'expected': '(* (- b c) a)',
                      'input': '(- (* a b) (* c a))'},
    ('hin', '13'): {   'expected': '(- (* b a) (* a c))',
                      'input': '(* (- b c) a)'},
    ('vor', '13'): {   'expected': '(* (- b c) a)',
                      'input': '(- (* b a) (* a c))'}


                      }