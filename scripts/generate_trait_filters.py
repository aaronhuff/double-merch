import json
from okay_bears.okay_bears import MerchTraits

double_merch = json.load(open("data/double_merch.json"))
traits = MerchTraits.all

traits_filters = {
    "traits": []
}

for trait in traits:
    trait_dict = {
            "name": trait,
            "images": [],
        }
    for bear in double_merch:
        for merch_trait in bear["merch_traits"]:
            if merch_trait["value"] == trait:
                trait_dict["images"].append(f"images/thumbail/{bear['name']}.png")
    trait_dict["count"] = len(trait_dict["images"])
    traits_filters["traits"].append(trait_dict)

all_bears = {
        "name": "All",
        "images": [],
}
for bear in double_merch:
    all_bears["images"].append(f"images/thumbail/{bear['name']}.png")
all_bears["count"] = len(all_bears["images"])
traits_filters["traits"].append(all_bears)

with open("data/traits_filters.json", "w") as f:
    f.write(json.dumps(traits_filters, indent=4))
