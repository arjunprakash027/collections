from moralis import evm_api
from base64_file import BASE64

api_key = ""

body = [
    {
        "path": "content/arjun_resume_v2.pdf",
        "content" : BASE64
    }
]

result = evm_api.ipfs.upload_folder(
    api_key = api_key,
    body = body,
)

print(result)
