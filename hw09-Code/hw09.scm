;;; Homework 09: Scheme List, Tail Recursion and Macro

;;; Required Problems

(define (make-change total biggest)
  (define (count-change total biggest lst)
    (cond
      ((= biggest 0) '())
      ((= total 0) (cons lst nil))
      ((= total 1) (cons (append lst '(1)) nil))
      ((< total 0) '())
      ((= biggest total) (append (cons (append lst (cons biggest nil)) nil) (count-change total (- biggest 1) lst)))
      (else (let ((with-biggest (count-change (- total biggest) biggest (append lst (cons biggest nil))))
                  (without-biggest (count-change total (- biggest 1) lst)))
                 (append with-biggest without-biggest)
            )
      )
    )
  )
  (count-change total biggest '())
)


(define (find n lst)
  (define (find-up n lst index)
    (cond
      ((= (car lst) n) index)
      ((null? (cdr lst)) #f)
      (else (find-up n (cdr lst) (+ index 1)))
    )
  )
  (find-up n lst 0)
)


(define (find-nest n sym)
  (define (if-in n sym)
    (if (pair? (car sym)) (define x (if-in n (car sym))) (if (= (car sym) n) (define x #t) (define x #f)))
    (if x
      x
      (if (null? (cdr sym))
        #f
        (if-in n (cdr sym))
      )
    )
  )
  (define (find-up n sym str)
    (cond
      ((pair? (car sym)) (if (if-in n (car sym))
                                  (find-up n (car sym) `(car ,str))
                                  (find-up n (cdr sym) `(cdr ,str))
                                )
      )
      ((= (car sym) n) `(car ,str))
      (else (find-up n (cdr sym) `(cdr ,str)))
    )
  )
  (define x (eval sym))
  (find-up n x sym)
)


(define-macro (def func args body)
  `(define ,func (lambda ,args ,body))
)


(define (combine lst1 vals indices i)
    (if (null? indices)
      lst1
      (if (= i (car indices))
        (append (cons (car vals) nil) (combine lst1 (cdr vals) (cdr indices) (+ i 1)))
        (append (cons (car lst1) nil) (combine (cdr lst1) vals indices (+ i 1)))
      )
    )
  )
(define (split args indices i)
    (if (null? indices)
      args
      (if (= i (car indices))
        (split (cdr args) (cdr indices) (+ i 1))
        (append (cons (car args) nil) (split (cdr args) indices (+ i 1)))
      )
    )
  )
(define-macro (k-curry fn args vals indices)
  (define lst1 (split args indices 0))
  `(lambda ,lst1 ,(cons fn (combine lst1 vals indices 0)))
)


(define-macro (let* bindings expr)
  (if (null? bindings)
    `(let ,bindings ,expr)
    `(let (,(car bindings)) (let* ,(cdr bindings) ,expr))
  )
)

;;; Just For Fun Problems

; Tree ADT
(define (tree label branches) (cons label branches))
(define (label t) (car t))
(define (branches t) (cdr t))
(define (is-leaf t) (null? (branches t)))

; A tree for test
(define t1 (tree 1
  (list
    (tree 2
      (list
        (tree 3 nil)
        (tree 7 (list
          (tree 7 nil)))))
    (tree 3 nil)
    (tree 6
      (list
        (tree 7 nil))))))

(define (find-in-tree t goal)
  'YOUR-CODE-HERE
)

; Helper Functions for you
(define (cadr lst) (car (cdr lst)))
(define (cddr lst) (cdr (cdr lst)))
(define (caddr lst) (car (cdr (cdr lst))))
(define (cdddr lst) (cdr (cdr (cdr lst))))

(define-macro (infix expr)
  ''YOUR-CODE-HERE
)
