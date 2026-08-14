binary = input("Enter a 4-bit binary number: ")

# Check if input is exactly 4 bits, doesn't start with 0, and only contains 0 or 1
if len(binary) == 4 and binary[0] != "0" and all(bit in "01" for bit in binary):
    m = len(binary)
    r = 0
    
    # Calculate the number of redundant bits needed
    while (2**r) < (m + r + 1):
        r += 1
        
    n = m + r
    hamming = [0] * (n + 1)
    j = 0
    
    # Place data bits into non-parity positions
    for i in range(1, n + 1):
        if i & (i - 1) == 0:
            continue
        hamming[i] = binary[j]
        j += 1
        
    # Calculate parity bits using even parity
    for i in range(r):
        p = 2**i
        parity = 0
        for j in range(1, n + 1):
            if j & p:
                parity ^= int(hamming[j])
        hamming[p] = str(parity)
        
    print("Hamming Code:", "".join(hamming[1:]))
else:
    print("Not valid")
