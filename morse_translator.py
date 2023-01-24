import time

class MorseTranslator:

    def __init__(self, time_unit, on, off):
        self.time_unit = time_unit
        self.on = on
        self.off = off
        self.encoding_table = {
                "a" : self.a,
                "b" : self.b,
                "c" : self.c,
                "d" : self.d,
                "e" : self.e,
                "f" : self.f,
                "g" : self.g,
                "h" : self.h,
                "i" : self.i,
                "j" : self.j,
                "k" : self.k,
                "l" : self.l,
                "m" : self.m,
                "n" : self.n,
                "o" : self.o,
                "p" : self.p,
                "q" : self.q,
                "r" : self.r,
                "s" : self.s,
                "t" : self.t,
                "u" : self.u,
                "p" : self.p,
                "w" : self.w,
                "x" : self.x,
                "y" : self.y,
                "z" : self.z,
                "1" : self.one,
                "2" : self.two,
                "3" : self.three,
                "4" : self.four,
                "5" : self.five,
                "6" : self.six,
                "7" : self.seven,
                "8" : self.eight,
                "9" : self.nine,
                "0" : self.zero
            }

    def is_valid_input(self, message):
        for character in message:
            if not character in self.encoding_table:
                return False
        return len(message) > 0           
        

    def encode_letter(self, character):
        if character in self.encoding_table:
            self.encoding_table[character]()
        else:
            raise ValueError("cannot encode " + character)

    def encode_word(self, word):
        beggining = True
        for character in word:
            if beggining:
                beggining = False
            else:
                self.space_l()
            self.encode_letter(character)

    def encode_message(self, phrase):
        beggining = True
        for word in phrase.lower().split():
            if beggining:
                beggining = False
            else:
                self.space_w()
            self.encode_word(word)

    def encode_signal(self , signal):
        if not self.is_valid_input(signal):
            raise ValueError("Cannot Send: Invalid Message")    
        self.start()
        self.space_w()
        self.encode_message(signal.strip())
        self.space_w()
        self.end()
        

    def tap(self):
        time.sleep(1 * self.time_unit)

    def dot(self, end_letter=False):
        self.on()
        time.sleep(1 * self.time_unit)
        self.off()
        if not end_letter:
            self.tap()

    def dash(self, end_letter=False):
        self.on()
        time.sleep(3 * self.time_unit)
        self.off()
        if not end_letter:
            self.tap()

    def space_l(self):
        time.sleep(3 * self.time_unit)

    def space_w(self):
        time.sleep(7 * self.time_unit)


    def start(self):
        self.dash()
        self.dot()
        self.dash()
        self.dot()
        self.dash(True)
        
    def end(self):
        self.dot()
        self.dot()
        self.dot()
        self.dash()
        self.dot()
        self.dash(True)
        

    def a(self):
        self.dot()
        self.dash(True)

    def b(self):
        self.dash()
        self.dot()
        self.dot()
        self.dot(True)

    def c(self):
        self.dash()
        self.dot()
        self.dash()
        self.dot(True)

    def d(self):
        self.dash()
        self.dot()
        self.dot(True)

    def e(self):
        self.dot(True)

    def f(self):
        self.dot()
        self.dot()
        self.dash()
        self.dot(True)

    def g(self):
        self.dash()
        self.dash()
        self.dot(True)

    def h(self):
        self.dot()
        self.dot()
        self.dot()
        self.dot(True)

    def i(self):
        self.dot()
        self.dot(True)

    def j(self):
        self.dot()
        self.dash()
        self.dash()
        self.dash(True)

    def k(self):
        self.dash()
        self.dot()
        self.dash(True)

    def l(self):
        self.dot()
        self.dash()
        self.dash()
        self.dash(True)

    def m(self):
        self.dash()
        self.dash(True)

    def n(self):
        self.dash()
        self.dot(True)

    def o(self):
        self.dash()
        self.dash()
        self.dash(True)

    def p(self):
        self.dot()
        self.dash()
        self.dash()
        self.dot(True)

    def q(self):
        self.dash()
        self.dash()
        self.dot()
        self.dash(True)

    def r(self):
        self.dot()
        self.dash()
        self.dot(True)

    def s(self):
        self.dot()
        self.dot()
        self.dot(True)

    def t(self):
        self.dot(True)

    def u(self):
        self.dot()
        self.dot()
        self.dash(True)

    def v(self):
        self.dot()
        self.dot()
        self.dot()
        self.dash(True)

    def w(self):
        self.dot()
        self.dash()
        self.dash(True)

    def x(self):
        self.dash()
        self.dot()
        self.dot()
        self.dash(True)

    def y(self):
        self.dash()
        self.dot()
        self.dash()
        self.dash(True)

    def z(self):
        self.dash()
        self.dash()
        self.dot()
        self.dot(True)

    def one(self):
        self.dot()
        self.dash()
        self.dash()
        self.dash()
        self.dash(True)

    def two(self):
        self.dot()
        self.dot()
        self.dash()
        self.dash()
        self.dash(True)

    def three(self):
        self.dot()
        self.dot()
        self.dot()
        self.dash()
        self.dash(True)

    def four(self):
        self.dot()
        self.dot()
        self.dot()
        self.dot()
        self.dash(True)

    def five(self):
        self.dot()
        self.dot()
        self.dot()
        self.dot()
        self.dot(True)

    def six(self):
        self.dash()
        self.dot()
        self.dot()
        self.dot()
        self.dot(True)

    def seven(self):
        self.dash()
        self.dash()
        self.dot()
        self.dot()
        self.dot(True)

    def eight(self):
        self.dash()
        self.dash()
        self.dash()
        self.dot()
        self.dot(True)

    def nine(self):
        self.dash()
        self.dash()
        self.dash()
        self.dash()
        self.dot(True)

    def zero(self):
        self.dash()
        self.dash()
        self.dash()
        self.dash()
        self.dash(True)

