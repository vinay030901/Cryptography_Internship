# Comparison of Chacha20-Poly1305 and AES

- This is a research project which I did under IEEE from June 2021 - July 2021.
- The motivation of the research project is to find whether the current industry standard AES is best for 5G or it should be replaced with any other cipher.
- I tried to find various algorithms which could give better results than AES.
- While searching for algorithm, I found Chacha20-Poly1305 cipher.
- ChaCha20-Poly1305 is an authenticated encryption with additional data (AEAD) algorithm, that combines the ChaCha20 stream cipher with the Poly1305 message authentication code. Its usage in IETF protocols is standardized in RFC 8439. It has fast software performance, and without hardware acceleration, is usually faster than AES-GCM.
- To prove this fact I wrote programs for both AES-GCM and Chacha20-poly1305 and ran them in mobiles which do not provide us with hardware acceleration.
- The result was that Chacha20-poly1305 was two times faster than AES-GCM in most of the cases.
- The contents and code of chacha20-poly1305 is in WORKING folder and of AES-GCM IN AESWORKING folder. 

![cryptoss](https://user-images.githubusercontent.com/68092657/213728135-3289bda0-28d7-4602-a758-2f5f466ac0e5.png)
