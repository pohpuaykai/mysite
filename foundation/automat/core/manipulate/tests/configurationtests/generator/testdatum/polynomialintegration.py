TEST_DATUM = {
    ('hin', '0'): {'expected': '(= y (int "1" x))', 'input': '(= y (+ x v_{0}))'},#$0
    ('vor', '0'): {'expected': '(= y (+ x v_{0}))', 'input': '(= y (int "1" x))'},#(int "1" $0)


    ('hin', '1'): {'expected': '(= y (int (* a (* n (^ x (- n "1")))) x))', 'input': '(= y (+ (* a (^ x n)) v_{0}))'},#(* $0 (^ $1 $2))
    ('vor', '1'): {   'expected': '(= y (+ (* a (^ x n)) v_{0}))',
                      'input': '(= y (int (* a (* n (^ x (- n "1")))) x))'}#(int (* $0 (* $2 (^ $1 (- $2 "1")))) $1)

}