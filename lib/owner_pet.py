class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        """Return a list of pets owned by this owner."""
        result = []
        for pet in Pet.all:
            if pet.owner == self:
                result.append(pet)
        return result

    def add_pet(self, pet):
        """Add a pet to this owner."""
        if not isinstance(pet, Pet):
            raise Exception("pet must be a Pet instance")
        pet.owner = self

    def get_sorted_pets(self):
        """
        Return this owner's pets sorted by their names.
        """
        def get_pet_name(pet):
            return pet.name
        
        return sorted(self.pets(), key=get_pet_name)


class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        self.name = name

        # Validate pet_type
        if pet_type not in Pet.PET_TYPES:
            raise Exception(f"Invalid pet type: {pet_type}")
        self.pet_type = pet_type

        # Validate owner
        if owner is not None and not isinstance(owner, Owner):
            raise Exception("Owner must be an Owner instance or None")
        self.owner = owner

        # Track this instance
        Pet.all.append(self)

Owner.name="Akumu"
Pet.pet_type="dog"

owner1=Owner("Akumu")
owner2 = Owner("Mumbi")

pet2 = Pet("Bella", "cat", owner1)
pet4 = Pet("Milo", "rodent")