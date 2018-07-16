import unittest
from number_door import NumberDoor
import constants as c


class TestNumberDoor(unittest.TestCase):

    def test_add_ball(self):
        door = NumberDoor(1, '../images/Doors/Door-1.png')
        result = door.add_ball(1)
        self.assertTrue(result)

        result = door.add_ball(2)
        self.assertTrue(result)

        result = door.add_ball(3)
        self.assertTrue(result)

        result = door.add_ball(4)
        self.assertTrue(result)

        result = door.add_ball(5)
        self.assertTrue(result)

        result = door.add_ball(6)
        self.assertFalse(result)

        self.assertTrue(door.get_slots() == [1, 2, 3, 4, 5])

    def test_remove_ball(self):
        door = NumberDoor(1, '../images/Doors/Door-1.png')
        door.set_slots([1, 2, 3, 6, 7])
        result = door.remove_ball(1)
        self.assertTrue(result)

        result = door.remove_ball(6)
        self.assertTrue(result)

        self.assertTrue(door.get_slots() == [c.DEFAULT_SLOT_VALUE, 2, 3, c.DEFAULT_SLOT_VALUE, 7])

        door.set_slots([c.DEFAULT_SLOT_VALUE, c.DEFAULT_SLOT_VALUE, c.DEFAULT_SLOT_VALUE,
                        c.DEFAULT_SLOT_VALUE, c.DEFAULT_SLOT_VALUE])
        result = door.remove_ball(9)
        self.assertFalse(result)

    def test_has_valid_solution(self):
        door = NumberDoor(4, '../images/Doors/Door-4.png')
        door.add_ball(3)
        door.add_ball(5)
        door.add_ball(6)
        door.add_ball(8)
        valid_result = door.has_valid_solution()
        self.assertTrue(valid_result)

    def test_has_valid_solution_length(self):
        door = NumberDoor(5, '../images/Doors/Door-5.png')
        door.add_ball(5)
        self.assertFalse(door.has_valid_solution())

        for x in range(c.MIN_SLOTS - 1):
            door.add_ball(9)
        self.assertTrue(door.has_valid_solution())

    def test_reset(self):
        door = NumberDoor(5, '../images/Doors/Door-5.png')
        door.add_ball(3)
        door.add_ball(5)
        door.add_ball(6)
        door.add_ball(8)
        door.reset()

        self.assertTrue(door.get_slots() == [c.DEFAULT_SLOT_VALUE, c.DEFAULT_SLOT_VALUE, c.DEFAULT_SLOT_VALUE,
                                             c.DEFAULT_SLOT_VALUE, c.DEFAULT_SLOT_VALUE])


if __name__ == '__main__':
    unittest.main()
