# Pod Types

## Ideas

### IXP

- no route filtering
- no shaping
- 1 LAN, partial mesh of direct peerings or RS

### Transit SP / T1

- you care about which ASs are passing
- filtering of prefixes
- anycast

### Access provider

- business - shaping, bgp, prefix delegation
- residentials - pppoe, v6 address alocation, mtus
- cgnat
- dns64/nat64
- content filtering
- captive portals (wifi?)

### Content provider

- ddos protection
- dns
- geolocation services
- distributed caches
