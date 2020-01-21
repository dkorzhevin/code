def calculate_storage(filesize):
    block_size = 4096
    # Use floor division to calculate how many blocks are fully occupied
    full_blocks = filesize // block_size
    # Use the modulo operator to check whether there's any remainder
    partial_block = filesize % block_size
    # Depending on whether there's a remainder or not, return the right number.
    if filesize < 4096:
        return block_size
    elif partial_block > 0:
        return full_blocks * block_size + block_size    
    return full_blocks * block_size

print(calculate_storage(1))    # Should be 4096
print(calculate_storage(4096)) # Should be 4096
print(calculate_storage(4097)) # Should be 8192