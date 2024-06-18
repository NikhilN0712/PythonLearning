class move_characters:
    def move_fwd(self):
        print("move forward 1 step")

    def move_bwd(self):
        print("move backward 1 step")

class jump_characters:
    def jump_1level(self):
        print("jump charecter 1 level")

    def jump_2level(self):
        print("jump charecter 2 level")

class pokemon(move_characters, jump_characters):
    def move_bwd(self):
        print("pokemon moveing")

p = pokemon()
p.move_bwd()
p.jump_1level()

class micky(move_characters, jump_characters):
    pass

m = micky()
m.move_fwd()
m.jump_1level()