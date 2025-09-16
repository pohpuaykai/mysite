TEST_DATUM = {
    ('hin', '0'): {'expected': '(= y (int (* (^ "e" x) (D x v_{0})) v_{0}))', 'input': '(= y (+ (^ "e" x) v_{0}))'},#(^ "e" $0)
    ('vor', '0'): {   'expected': '(= y (+ (^ "e" x) v_{0}))',
                      'input': '(= y (int (* (^ "e" x) (D x x)) x))'},#(int (* (^ "e" $0) (D $0 $1)) $1)

                      
    ('hin', '1'): {'expected': '(= y (int (* (^ x x) (+ (* (D x v_{0}) (log "e" x)) (* (D x v_{0}) (/ x x)))) v_{0}))', 'input': '(= y (+ (^ x x) v_{0}))'},#(^ $0 $1)
    ('vor', '1'): {   'expected': '(= y (+ (^ x x) v_{0}))',
                      'input': '(= y (int (* (^ x x) (+ (* (D x x) (log "e" x)) (* (D x x) (/ x x)))) x))'}#(int (* (^ $0 $1) (+ (* (D $1 $2) (log "e" $0)) (* (D $0 $2) (/ $1 $0)))) $2)

}