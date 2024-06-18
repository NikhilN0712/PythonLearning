class move_characters:
    def move_fwd(self):
        print("move forward 1 step")

    def move_bwd(self):
        print("move backward 1 step")

class jump_characters(move_characters):
    def jump_1level(self):
        print("jump charecter 1 level")

    def jump_2level(self):
        print("jump charecter 2 level")

class pokemon(jump_characters):
    def move_bwd(self):
        print("pokemon moveing")

p = pokemon()
p.move_bwd()
p.jump_1level()
p.move_fwd()