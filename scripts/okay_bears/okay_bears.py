class MerchTraits:
    cloth_traits = [
        "Denim Jacket",
        "Leather Jacket",
        "Legacy Windbreaker",
        "Loose Overalls",
        "Okay Tee",
        "Okay Hoodie",
        "Urban Hoodie",
        "Vintage Windbreaker",
        "Sleeveless Tee",
    ]

    hat_traits = [
        "Backwards Flat Cap",
        "Black Bucket Hat",
        "Ear Tag",
        "Flat Cap",
        "Okay Beanie",
        "Pom Pom Beanie",
        "Skate Cap",
    ]

    mouth_traits = [
        "Yoyo",
    ]

    eyewear_traits = [
        "Wayfarer Sunglasses"
    ]

    all = cloth_traits + hat_traits + mouth_traits + eyewear_traits


class Bears:
    def __init__(self, json_data: list):
        self.bears = self.load_bears(json_data)

    def load_bears(self, json_data) -> list:
        bears = []
        for page in json_data:
            for bear in page:
                bears.append(Bear(
                    bear['name'],
                    bear['tokenAddress'],
                    bear['imageUrl'],
                    bear['traits']
                ))
        return bears

    def __iter__(self):
        return iter(self.bears)

    def __len__(self):
        return len(self.bears)

    def __getitem__(self, index):
        return self.bears[index]

    def __repr__(self):
        return f"Bears(bears={self.bears})"


class Bear:
    def __init__(
                self, name: str,
                token_address: str,
                image_url: str,
                traits: list
            ):
        self.name = name
        self.token_address = token_address
        self.image_url = image_url
        self.traits = traits
        self.merch_traits = self.merch_traits()
        self.num_merch_traits = len(self.merch_traits)
        self.double_merch = self.double_merch()

    def __repr__(self):
        return f"Bear(name={self.name}, tokenAddress={self.token_address}, imageUrl={self.image_url}, traits={self.traits})"

    def __str__(self):
        return f"Bear(name={self.name}, tokenAddress={self.token_address}, imageUrl={self.image_url}, traits={self.traits})"

    def merch_traits(self) -> list:
        traits = []
        for trait in self.traits:
            if trait['trait_type'] == 'Clothes' and trait['value'] in MerchTraits.cloth_traits:
                traits.append(trait)
            elif trait['trait_type'] == 'Hat' and trait['value'] in MerchTraits.hat_traits:
                traits.append(trait)
            elif trait['trait_type'] == 'Mouth' and trait['value'] in MerchTraits.mouth_traits:
                traits.append(trait)
            elif trait['trait_type'] == 'Eyewear' and trait['value'] in MerchTraits.eyewear_traits:
                traits.append(trait)
        return traits

    def double_merch(self) -> bool:
        if self.num_merch_traits > 1:
            return True
        else:
            return False
