import requests

# List of image URLs (replace with your URLs)
urls = [
    "https://cdn.builder.io/api/v1/image/assets/a563236501f24f7e9a93d4bc4ad334bf/5af6eb9686dfc8808ad13a03635ac322f933a3011d47339e2487bd056ee7b4dd?apiKey=a563236501f24f7e9a93d4bc4ad334bf&"
    "https://cdn.builder.io/api/v1/image/assets/a563236501f24f7e9a93d4bc4ad334bf/e7d116053a75c31d3894399bc0399f4737d78562f5cd4d8d35454f33bcfcf061?apiKey=a563236501f24f7e9a93d4bc4ad334bf&"
    "https://cdn.builder.io/api/v1/image/assets/a563236501f24f7e9a93d4bc4ad334bf/a91044a8321787d8646b1fc4951cb7249148c397768696eb048763b0d5720838?apiKey=a563236501f24f7e9a93d4bc4ad334bf&"
    "https://cdn.builder.io/api/v1/image/assets/a563236501f24f7e9a93d4bc4ad334bf/59e19b8f7f867fbcee81ff593bae99b300ca4b13bf2d2e8173a7d3594310c5f6?apiKey=a563236501f24f7e9a93d4bc4ad334bf&"
    "https://cdn.builder.io/api/v1/image/assets/a563236501f24f7e9a93d4bc4ad334bf/18282fdf33855363f159c3a8a51938df29eab37cf8901a391316ea11cb385c14?apiKey=a563236501f24f7e9a93d4bc4ad334bf&"
    "https://cdn.builder.io/api/v1/image/assets/a563236501f24f7e9a93d4bc4ad334bf/5303c9869af594c53334350de3881e952c16245f85eb2a2f25ff1f86d0e12f90?apiKey=a563236501f24f7e9a93d4bc4ad334bf&"
    "https://cdn.builder.io/api/v1/image/assets/a563236501f24f7e9a93d4bc4ad334bf/1aeabc45f1122f35a1d9918954ba9158dca951ea8288828c8f28accd014ffae3?apiKey=a563236501f24f7e9a93d4bc4ad334bf&"
    "https://cdn.builder.io/api/v1/image/assets/a563236501f24f7e9a93d4bc4ad334bf/ff2a71aa264e647303137856c7e569ad3f30130967c53d0efca24268b6b52805?apiKey=a563236501f24f7e9a93d4bc4ad334bf&"
    "https://cdn.builder.io/api/v1/image/assets/a563236501f24f7e9a93d4bc4ad334bf/addb707cbba08ca3a7f9c80091bd028aac2aa134821801d38daafc212aaad3df?apiKey=a563236501f24f7e9a93d4bc4ad334bf&"
    "https://cdn.builder.io/api/v1/image/assets/a563236501f24f7e9a93d4bc4ad334bf/06e14b67ad96d338348f5043de02fcd9193888ea32c0c0812ae03200031749b1?apiKey=a563236501f24f7e9a93d4bc4ad334bf&"
    "https://cdn.builder.io/api/v1/image/assets/a563236501f24f7e9a93d4bc4ad334bf/8b58f2002566502ec38370c464958927071b2a8a13e0f0d3814847a95865b526?apiKey=a563236501f24f7e9a93d4bc4ad334bf&"
    "https://cdn.builder.io/api/v1/image/assets/a563236501f24f7e9a93d4bc4ad334bf/99f8951466ffd9810b9c9ebbe888d717ef9e47e389622fb1606ef6b31f8ee131?apiKey=a563236501f24f7e9a93d4bc4ad334bf&"
    "https://cdn.builder.io/api/v1/image/assets/a563236501f24f7e9a93d4bc4ad334bf/99f8951466ffd9810b9c9ebbe888d717ef9e47e389622fb1606ef6b31f8ee131?apiKey=a563236501f24f7e9a93d4bc4ad334bf&"
    "https://cdn.builder.io/api/v1/image/assets/a563236501f24f7e9a93d4bc4ad334bf/99f8951466ffd9810b9c9ebbe888d717ef9e47e389622fb1606ef6b31f8ee131?apiKey=a563236501f24f7e9a93d4bc4ad334bf&"
    "https://cdn.builder.io/api/v1/image/assets/a563236501f24f7e9a93d4bc4ad334bf/99f8951466ffd9810b9c9ebbe888d717ef9e47e389622fb1606ef6b31f8ee131?apiKey=a563236501f24f7e9a93d4bc4ad334bf&"
    "https://cdn.builder.io/api/v1/image/assets/a563236501f24f7e9a93d4bc4ad334bf/c943adb094e7a3bd441c58cd3d5ad3406ce306340e968489b581cf82aa191d4e?apiKey=a563236501f24f7e9a93d4bc4ad334bf&"
    "https://cdn.builder.io/api/v1/image/assets/a563236501f24f7e9a93d4bc4ad334bf/12f43f8da99830ab7334e34a965f3595f377c51486e2ab2f91730b00e31d82e1?apiKey=a563236501f24f7e9a93d4bc4ad334bf&"
    "https://cdn.builder.io/api/v1/image/assets/a563236501f24f7e9a93d4bc4ad334bf/c18a8dd1535bd1b997888a9b6978f18a156a881a4ebaeec3b82ea9cf2738f812?apiKey=a563236501f24f7e9a93d4bc4ad334bf&"
    "https://cdn.builder.io/api/v1/image/assets/a563236501f24f7e9a93d4bc4ad334bf/17ece96a7f30ccf1ce6eee918467c50a70e349a121492d2d583edd79538d1e67?apiKey=a563236501f24f7e9a93d4bc4ad334bf&"
    "https://cdn.builder.io/api/v1/image/assets/a563236501f24f7e9a93d4bc4ad334bf/21a636b16151d2bb690f2f588baa272500b50aff6f05bea1fc38aa55af034499?apiKey=a563236501f24f7e9a93d4bc4ad334bf&"
    "https://cdn.builder.io/api/v1/image/assets/a563236501f24f7e9a93d4bc4ad334bf/910f77442a5b0593023b56b405dbf35040c38d51464924b4229afb8ef4104704?apiKey=a563236501f24f7e9a93d4bc4ad334bf&"
    "https://cdn.builder.io/api/v1/image/assets/a563236501f24f7e9a93d4bc4ad334bf/910f77442a5b0593023b56b405dbf35040c38d51464924b4229afb8ef4104704?apiKey=a563236501f24f7e9a93d4bc4ad334bf&"
    "https://cdn.builder.io/api/v1/image/assets/a563236501f24f7e9a93d4bc4ad334bf/8f39db999983f0118f253c626bfc68eedd03d4b8ff483637ba4ac73483a8d693?apiKey=a563236501f24f7e9a93d4bc4ad334bf&"
    
    # Add all other URLs here
]

for idx, url in enumerate(urls):
    try:
        response = requests.get(url)
        with open(f"image_{idx}.jpg", "wb") as f:
            f.write(response.content)
        print(f"Downloaded image_{idx}.jpg")
    except Exception as e:
        print(f"Failed to download {url}: {str(e)}")