# The rgb function is incomplete. Complete it so that passing in RGB decimal values will result in a hexadecimal
# representation being returned. Valid decimal values for RGB are 0 - 255.
# Any values that fall out of that range must be rounded to the closest valid value.
# # Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.

def rgb(r, g, b):
    return '{:02X}{:02X}{:02X}'.format(values_check(r), values_check(g), values_check(b))

def values_check(x):
    return 0 if x < 0 else 255 if x > 255 else x

#Examples:
print(rgb(-1, 200, 256))
print(rgb(0, 0, 0))
print(rgb(255, 255, 255))