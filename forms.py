from django.forms import ModelForm
from .models import Listing


class ListingForm(ModelForm):
    class Meta:
        model=Listing
        fields= [
            "title",
            "price",
            "num_of_bedrooms",
            "num_of_birthrooms",
            "square_footage",
            "address",
            "image",
        ]