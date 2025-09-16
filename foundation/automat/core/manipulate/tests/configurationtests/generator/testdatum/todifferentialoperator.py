TEST_DATUM={
    ('hin', '0'): {   'expected': '(= (* (/ d (* d x)) (* u v)) (+ (* u (/ (* d v) (* d x))) (* v (/ (* d u) (* d x)))))',
                      'input': '(= (D (* u v) x) (+ (* u (/ (* d v) (* d x))) (* v (/ (* d u) (* d x)))))'},
    ('vor', '0'): {   'expected': '(= (D (* u v) x) (+ (* u (/ (* d v) (* d x))) (* v (/ (* d u) (* d x)))))',
                      'input': '(= (* (/ d (* d x)) (* u v)) (+ (* u (/ (* d v) (* d x))) (* v (/ (* d u) (* d x)))))'},


    ('hin', '1'): {   'expected': '(= (* (/ d (* d x)) (* u v)) (+ (* u (/ (* d v) (* d x))) (* v (/ (* d u) (* d x)))))',
                      'input': '(= (* (/ d (* d x)) (* u v)) (+ (* u (D v x)) (* v (D u x))))'},
    ('vor', '1'): {   'expected': '(= (* (/ d (* d x)) (* u v)) (+ (* u (D v x)) (* v (D u x))))',
                      'input': '(= (* (/ d (* d x)) (* u v)) (+ (* u (/ (* d v) (* d x))) (* v (/ (* d u) (* d x)))))'},


    ('hin', '2'): {   'expected': '(= (* (/ partial (* partial x)) (* u v)) (+ (* u (/ (* partial v) (* partial x))) (* v (/ (* partial u) (* partial x)))))',
                      'input': '(= (D (* u v) x) (+ (* u (/ (* partial v) (* partial x))) (* v (/ (* partial u) (* partial x)))))'},
    ('vor', '2'): {   'expected': '(= (D (* u v) x) (+ (* u (/ (* partial v) (* partial x))) (* v (/ (* partial u) (* partial x)))))',
                      'input': '(= (* (/ partial (* partial x)) (* u v)) (+ (* u (/ (* partial v) (* partial x))) (* v (/ (* partial u) (* partial x)))))'},


    ('hin', '3'): {   'expected': '(= (* (/ partial (* partial x)) (* u v)) (+ (* u (/ (* partial v) (* partial x))) (* v (/ (* partial u) (* partial x)))))',
                      'input': '(= (* (/ partial (* partial x)) (* u v)) (+ (* u (D v x)) (* v (D u x))))'},
    ('vor', '3'): {   'expected': '(= (* (/ partial (* partial x)) (* u v)) (+ (* u (D v x)) (* v (D u x))))',
                      'input': '(= (* (/ partial (* partial x)) (* u v)) (+ (* u (/ (* partial v) (* partial x))) (* v (/ (* partial u) (* partial x)))))'}

                      }