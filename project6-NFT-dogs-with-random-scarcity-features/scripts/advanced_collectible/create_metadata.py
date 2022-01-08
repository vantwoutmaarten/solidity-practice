from brownie import AdvancedCollectible, network
from scripts.helpful_scripts import get_breed
from metadata.sample_metadata import metadata_template
from pathlib import Path
import requests
import json
import os

breed_to_image_uri = {
    "PUG": "https://ipfs.io/ipfs/QmSfJCQ1cG7vdg4xBUWpA4nbbJFrtW1DUrLEUF1B4SqP3g?filename=happy-pug.png",
    "SHIBA_INU": "https://ipfs.io/ipfs/QmWtyenX1ZG1KshuC2EvaqLy7gx8X26trYk43vsgWL6fKd?filename=shiba-inu.png",
    "ST_BERNARD": "https://ipfs.io/ipfs/QmdMBp3kNKWoLPvZgCeLXXaqPWS7zsKpoP64dBHtzhAzx8?filename=st-bernard.png",
}


def main():
    advanced_collectible = AdvancedCollectible[-1]
    number_of_advanced_collectibles = advanced_collectible.tokenCounter()
    print(f"I have created {number_of_advanced_collectibles} collectibles")

    for token_id in range(number_of_advanced_collectibles):
        breed = get_breed(advanced_collectible.tokenIdToBreed(token_id))
        metadata_file_name = (
            f"./metadata/{network.show_active()}/{token_id}-{breed}.json"
        )
        print(metadata_file_name)

        collectible_metadata = metadata_template
        if Path(metadata_file_name).exists():
            print(f"{metadata_file_name} already exists! Delete it to overwrite")
        else:
            print(f"Creating Metadata file {metadata_file_name}")
            collectible_metadata["name"] = breed
            collectible_metadata["description"] = f"An Adorable {breed} dog!"

            image_file_name = "./img/" + breed.lower().replace("_", "-") + ".png"

            if os.getenv("UPLOAD_IPFS") == "true":
                image_uri = upload_to_ipfs(image_file_name)
            image_uri = image_uri if image_uri else breed_to_image_uri[breed]

            collectible_metadata["image"] = image_uri

            with open(metadata_file_name, "w") as file:
                json.dump(collectible_metadata, file)

            if os.getenv("UPLOAD_IPFS") == "true":
                upload_to_ipfs(metadata_file_name)


def upload_to_ipfs(filepath):
    print(filepath)
    with Path(filepath).open("rb") as fp:
        image_binary = fp.read()
        # upload stuff...
        ipfs_url = "http://127.0.0.1:5001"
        endpoint = "/api/v0/add"
        response = requests.post(ipfs_url + endpoint, files={"file": image_binary})
        ipfs_hash = response.json()["Hash"]
        filename = filepath.split("/")[-1:][0]
        image_uri = f"https://ipfs.io/ipfs/{ipfs_hash}?filename={filename}"
        print(image_uri)
        return image_uri
