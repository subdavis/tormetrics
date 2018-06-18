import ipaddress
import requests
import json

def getAmazonRanges():
    f = open("ip-ranges.json", "r")
    ranges_json = json.loads(f.read())
    ranges = [ ipaddress.ip_network(netstring['ip_prefix']) for netstring in ranges_json['prefixes']]
    return sorted(ranges)

def getTorIPList():
    with open("torlist", "r") as f:
        lines = f.read().splitlines()
        addresses = []
        for line in lines:
            if (len(line) < 16):
                addresses.append(ipaddress.ip_network(line))
        return sorted(addresses)

def findInRanges(ipList, ranges):
    matches = []
    irange = 0
    ilist = 0

    while irange < len(ranges) and ilist < len(ipList):
        ip = ipList[ilist]
        range = ranges[irange]
        
        if range.overlaps(ip):
            ilist += 1
            matches.append(ip)
        else:
            result = ip.compare_networks(range)
            if result < 0:
                ilist += 1
            else:
                irange += 1
    return matches

if __name__ == "__main__":
    print("Finding TOR nodes in the AWS network...  IPv4 only!")
    ranges = getAmazonRanges()
    print("Loaded {} network ranges from AWS.".format(len(ranges)))
    addresses = getTorIPList()
    print("Loaded {} addresses from TOR service.".format(len(addresses)))
    matches = findInRanges(addresses, ranges)
    print("Found {} matches out of {} total addresses.".format(len(matches), len(addresses)))
    [print(m.network_address) for m in matches]