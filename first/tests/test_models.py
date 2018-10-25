from first.models import fooditem
from mixer.backend.django import mixer

class Testmodels:

    def food_item_in_mess_menu(self):
        itemName = mixer.blend('first.item_name')
        assert itemName.__str__
