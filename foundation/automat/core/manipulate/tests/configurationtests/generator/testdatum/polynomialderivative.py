TEST_DATUM = {
    ('hin', '0'): {'expected': '(= y (D v_{0} v_{0}))', 'input': '(= y "1")'},#"1"
    ('vor', '0'): {'expected': '(= y "1")', 'input': '(= y (D x x))'},#(D $0 $0)


    ('hin', '1'): {   'expected': '(= y (D (* a (^ x n)) x))',
                      'input': '(= y (* a (* n (^ x (- n "1")))))'},#(* $0 (* $2 (^ $1 (- $2 "1"))))
    ('vor', '1'): {'expected': '(= y (* a (* n (^ x (- n "1")))))', 'input': '(= y (D (* a (^ x n)) x))'}#(D (* $0 (^ $1 $2)) $1)

}