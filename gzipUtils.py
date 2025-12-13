# pip install gzip

import gzip
import shutil

def compress_file(input_file, output_file):
    with open(input_file, 'rb') as f_in:
        with gzip.open(output_file, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)

def decompress_file(input_file, output_file):
    with gzip.open(input_file, 'rb') as f_in:
        with open(output_file, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out) 

# Example usage:
# Compress a file
print("Compressing 'user_data.txt' to 'user_data.txt.gz'")
compress_file('user_data.txt', 'user_data.txt.gz')  

# Decompress a file
print("Decompressing 'user_data.txt.gz' to 'decompressed_user_data.txt'")
decompress_file('user_data.txt.gz', 'decompressed_user_data.txt')   
