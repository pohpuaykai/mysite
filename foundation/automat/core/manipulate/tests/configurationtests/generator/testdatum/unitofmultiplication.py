TEST_DATUM = {
    ('hin', '0'): {'expected': '(= (* y "1") (* x "1"))', 'input': '(= y x)'},#$0
    ('vor', '0'): {'expected': '(= y x)', 'input': '(= y (* x "1"))'},#(* $0 "1")


    ('hin', '1'): {'expected': '(= (/ y "1") (/ x "1"))', 'input': '(= y x)'},#$0
    ('vor', '1'): {'expected': '(= y x)', 'input': '(= y (/ x "1"))'}#(/ $0 "1")

    }