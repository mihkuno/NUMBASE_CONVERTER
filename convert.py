def hex_to_bin(hex):
    pass
def hex_to_oct(hex):
    pass
def hex_to_dec(hex):
    pass

# Decimal to Binary
def dec_to_bin(dec):
    result = ''
    while dec != 0:
        rem = dec % 2
        dec //= 2
        result = str(rem) + result
    return result

# Decimal to Hexadecimal
def dec_to_hex(dec):
    pass

# Decimal to Octal
def dec_to_oct(dec):
    pass

# Binary to Hexadecimal
def bin_to_hex(bin): # (priority)
    # 8 4 2 1 | 8 4 2 1  
    # 0 0 1 1   1 1 1 0 -> 3E

    # check if divisible by 4
    while len(bin) % 4 != 0: 
        # add missing right zeroes 
        bin = '0'+bin # to the right

    # reverse the bits then,
    # split in 4 equal parts
    hexSplit = [ bin[start:start+4][::-1]
                 for start in reversed(range(0, len(bin), 4)) ] 

    # convert base 4 chunks into decimal
    for idx, chunk in enumerate(hexSplit):
        exponent = 1
        chunkTotal = 0
        for bit in chunk:
            bit = int(bit)
            if bit == 1:
                 chunkTotal += exponent
            exponent *= 2
        hexSplit[idx] = chunkTotal
    hexSplit = hexSplit[::-1]

    hexResult = []
    leadingZero = True
    for idx, chunk in enumerate(hexSplit):
       
        # remove leading zero
        if chunk <= 0 and leadingZero: 
            continue
        else: leadingZero = False
        
        # convert chunks <10 to characters
        if chunk >= 10: 
            # 65 is A in ascii table
            hexResult.append(chr(hexSplit[idx] % 10 + 65))
        else:
            # append number instead 
            hexResult.append(hexSplit[idx])
    
    print(hexSplit, hexResult)
    return '0x'+"".join([str(e) for e in hexResult])


# Binary to Decimal
def bin_to_dec(bin):
    # 128  64  32  16   8   4   2   1
    # 0    0    0   0   0   0   0   0
    result = 0
    initial = 1
    for item in reversed(bin):
        item = int(item)
        if item == 1:
            result += initial
        initial *= 2
    return result


# Binary to Octal
def bin_to_oct(bin):
    # 4 2 1 | 4 2 1 | 4 2 1
    # 0 0 0   1 1 1   1 1 0 -> 76

    # check if divisible by 3
    while len(bin) % 3 != 0: 
        # add missing right zeroes 
        bin = '0'+bin # to the right

    # reverse the bits then,
    # split in 3 equal parts
    octSplit = [ bin[start:start+3][::-1]
                 for start in reversed(range(0, len(bin), 3)) ] 

    # convert base 3 chunks into decimal
    for idx, chunk in enumerate(octSplit):
        exponent = 1
        chunkTotal = 0
        for bit in chunk:
            bit = int(bit)
            if bit == 1:
                 chunkTotal += exponent
            exponent *= 2
        octSplit[idx] = chunkTotal
    octSplit = octSplit[::-1]

    octResult = []
    leadingZero = True
    for idx, chunk in enumerate(octSplit):
       
        # remove leading zero
        if chunk <= 0 and leadingZero: 
            continue
        else: leadingZero = False
       
        # append number instead 
        octResult.append(octSplit[idx])

    print(octSplit, octResult)
    return "".join([str(e) for e in octResult])


def oct_to_dec(oct):
    pass
def oct_to_bin(oct):
    pass
def oct_to_hex(oct):
    pass