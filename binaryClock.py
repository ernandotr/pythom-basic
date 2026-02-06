import datetime

now = datetime.datetime.now()

h, m, s = now.hour, now.minute, now.second
def to_binary(n):
    return bin(n)[2:].zfill(6).replace('0', '⬛').replace('1', '🟩')

print("Binary Clock:")
print("Hours:   ", to_binary(h))
print("Minutes: ", to_binary(m))
print("Seconds: ", to_binary(s)) 
