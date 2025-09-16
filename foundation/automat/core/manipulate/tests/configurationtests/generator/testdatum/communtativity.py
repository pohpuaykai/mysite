TEST_DATUM={   
    ('hin', '0'): {'expected': '(= a (+ c b))', 'input': '(= a (+ b c))'},
    ('vor', '0'): {'expected': '(= a (+ c b))', 'input': '(= a (+ b c))'},
    ('hin', '1'): {'expected': '(= a (* c b))', 'input': '(= a (* b c))'},
    ('vor', '1'): {'expected': '(= a (* c b))', 'input': '(= a (* b c))'},
    ('hin', '2'): {'expected': '(= b a)', 'input': '(= a b)'},
    ('vor', '2'): {'expected': '(= b a)', 'input': '(= a b)'}}