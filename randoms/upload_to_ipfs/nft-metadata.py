from moralis import evm_api
import json
import base64

api_key = ""

content = {
        "name": "Arjun resume v2",
        "description": "This is the secound version of my resume uploaded in blockchain.",
        "image": "https://ipfs.moralis.io:2053/ipfs/QmfLkfxbH6M92V2iSd9mFmMyv6hzq8WjyiZEb4nLcTZ4FM/content/arjun_resume_v2.pdf",
        "attributes": [
          {
            "trait_type": "Skills",
            "value": "Python , AI , ML , Blockchain , Data Science , Data Analytics , Data Visualization , Data Engineering , Data Mining , Data Warehousing , Data",
          },
          {
            "trait_type": "Type",
            "value": "Resume on blockchain"
          },
        ],
}

body = [
    {
        "path": "metadata.json",
        "content": base64.b64encode(bytes(json.dumps(content), 'ascii')).decode('ascii')
    }
]


result = evm_api.ipfs.upload_folder(
    api_key=api_key,
    body=body,
)

print(result)