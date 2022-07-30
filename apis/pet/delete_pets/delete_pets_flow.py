import cloudinary.uploader
from models.pet import Pet
from utils.utils import json_message


class DeletePetsFlow:

    def __call__(self):

        pets = Pet.objects()

        public_ids = []
        public_ids = list(map(
            lambda pet: pet.to_json()['img_public_id'],
            pets))

        for public_id in public_ids:
            cloudinary.uploader.destroy(public_id)

        Pet.objects.delete()
        return json_message("Mascotas borradas")
