TEST_DATUM={
    ('hin', '0'): {'expected': '(= (+ "0" a) (+ "0" a))', 'input': '(= a a)'},
    ('vor', '0'): {'expected': '(= a b)', 'input': '(= a (+ "0" b))'},


    ('hin', '1'): {'expected': '(= (+ a "0") (+ a "0"))', 'input': '(= a a)'},
    ('vor', '1'): {'expected': '(= a b)', 'input': '(= a (+ b "0"))'},

    ('hin', '2'): {'expected': '(= (- a "0") (- a "0"))', 'input': '(= a a)'},
    ('vor', '2'): {'expected': '(= a b)', 'input': '(= a (- b "0"))'}}