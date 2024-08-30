import random

def ipv4_generator(n):
    """Generate and return a list of n random IPV4 addresses."""
    ipv4_addresses = []
    for _ in range(n):
        # Generates 4 random bytes in denary and adds it to the address.
        address = [str(random.randint(0,255)) for _ in range(4)]
        # Separates bytes in address with full stops.
        ipv4_addresses.append(".".join(address))
    return ipv4_addresses

def zero_compression(address):
    """Perform zero compression on an IPV6 address and return result."""
    # Finding the longest sequence of 0000 groups.
    longest_start, longest_length = -1, 0
    current_start, current_length = -1, 0
    for i in range(len(address)):
        if address[i] == "0000":
            current_length += 1
            if current_start == -1:
                current_start = i
            if current_length > longest_length:
                longest_start, longest_length = current_start, current_length
        else:
            current_start, current_length = -1, 0
    # Replace longest sequence of 0000 with ::
    if longest_length > 0:
        for j in range(longest_start+1,longest_start+longest_length):
            address[j] = "placeholder"
        if longest_length == 8:
            address[longest_start] = "::"
        elif longest_start == 0 or longest_start + longest_length == len(address):
            address[longest_start] = ":"
        else:
            address[longest_start] = ""
        # Removes place holders.
        address = [group for group in address if group != "placeholder"]
    return address

def ipv6_generator(n):
    """Generate and return a list of n random IPV6 addresses."""
    ipv6_addresses = []
    for _ in range(n):
        # Generates 8 groups of 4 random hex digits.
        address = ["".join(random.choices("0123456789ABCDEF",k=4)) for _ in range(8)]
        # Zero compresses address and then separates it with colons.
        ipv6_addresses.append(":".join(zero_compression(address)))
    return ipv6_addresses

# Takes user input for address type and the number of addresses to be generated
address_type = input("Would you like to generate IPV4 addresses or IPV6 addresses?: ")
# Validates address type.
while address_type.lower() not in ["ipv4","v4","ipv6","v6"]:
    print("Please enter either IPV4 or IPV6")
    address_type = input("Would you like to generate IPV4 addresses or IPV6 addresses?: ")

no_of_addresses = int(input("Enter number of addresses to generate: "))

if address_type.lower() in ["ipv4","v4"]:
    print(ipv4_generator(no_of_addresses))
else:
    print(ipv6_generator(no_of_addresses))