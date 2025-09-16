TEST_DATUM = {
    ('hin', '0'): {'expected': '(= y (D (^ "e" x) x))', 'input': '(= y (* (^ "e" x) (D x x)))'},#(* (^ "e" $0) (D $0 $1))
    ('vor', '0'): {'expected': '(= y (* (^ "e" x) (D x x)))', 'input': '(= y (D (^ "e" x) x))'},#(D (^ "e" $0) $1)

    
    ('hin', '1'): {   'expected': '(= y (D (^ x x) x))',
                      'input': '(= y (* (^ x x) (+ (* (D x x) (log "e" x)) (* (D x x) (/ x x)))))'},#(* (^ $0 $1) (+ (* (D $1 $2) (log "e" $0)) (* (D $0 $2) (/ $1 $0))))
    ('vor', '1'): {'expected': '(= y (* (^ x x) (+ (* (D x x) (log "e" x)) (* (D x x) (/ x x)))))', 'input': '(= y (D (^ x x) x))'}#(D (^ $0 $1) $2)

  }