# Pocket Internet Addressing

## Infrastructure addressing

### Backbone network
 * __IPv4__ 172.16.0.0 /12 
 * __IPv6__ fd00:bb:: /64

### POD addressing, x, y & n
* __POD x.y__ is the number of the POD, where  
  __x__ can be between 16-31 and  
  __y__ between 1-255  
  __n__ is the router instance in this POD (need to be at least one, can be multiple for resilience / multi-homing)  
  __s__ is the server instance within a POD

* POD networks  
  __IPv4__ 10.x.y.0 /24  
  __IPv6__ fd00:x:y:: /48   [in a simple POD, with just a single network behind the BB router, we'll only use the first /64:   fd00:x:y:: /64]

* POD interfaces to the backbone (external address of the backbone router connecting the POD)  
  __IPv4__  172.x.y.n  
  __IPv6__  fd00:bb::x.y.n  
 
* POD interfaces to the internal network  
  __IPv4__  10.x.y.[n+10]  
  __IPv6__  fd00:bb::x.y.[n+10]

* Server interfaces within the POD, where [s] is the server instance within this POD  
  __IPv4__  10.x.y.[s+100]  
  __IPv6__  fd00:bb::x.y.[s+100]

## Example: 
### POD 16.1  - simple example with one single POD bridge internally and a single BB router (instance 1)
* This gives us:  x= 16, y=1, n=1  
  internal IPv4 range is 10.16.1.0/24  
  internal IPv6 range is fd00:16:1:: /64

* addresses for backbone router  
  internal: 10.16.1.11 /24  & fd00:16.1::11 /64  
  external: 172.16.1.1 /12 & fd00:bb::16:1:1 /64

* address for server instance one
  10.16.1.101 /24 & fd00:16:1::101 /64


## Sample IP addressing diagram for three simple PODs

![IP addressing example](docs/img/Sample_IP_addressing.png)


## Addressing explained
1. There are infratructure addresses for the central backbone, as well as individual and unique addressing per POD

2. The purpose of the backbone is to facilitate general connectivity between those containers with an interface to the backbone (consider the backbone like a flat IXP). 
It opens the possibility for every backbone member to talk directly to another backbone member to  start forming routing adjacencies. 

3. The addressing per POD facilitates communication just within this POD, for all members of it. Outbound connectivity from this POD is expected to traverse the router instance(s) connecting it to the backbone. 

4. IP addressing is build such that it reflects the POD number, for easy readability in both IPv4 and IPv6 addresses

5. IPv6 addressing is based on ULA, since this environment is considered private and not be routed on the Internet. 

6. The POD numbers are two digits called POD x.y, where x can be a number between 16-31 and y a number between 1-255.  
   [Sidenote: the x numbering scheme was driven by the use of the 172.16.0.0/12 IPv4 backbone range.   
              the y number starts with 1, because otherwise the 0 would be ommited in some IPv6 :: representation]

7. The internal interface addresses can not start with .1, since this is pre-occupied by the docker host interface within the network  
   Therefore, router interfaces will be [n+10], i.e. .11, .12, ... until .99 [which gives a max of 89 router intances within a single POD]  
   Server interfaces will be [s+100], .101, .102, ... until .254 [which gives a max of 154 server instances within a single POD]

8. Every IPv6 subnet with interfaces in it will be a /64

9. In more complex PODs with more than one network internally, the IPv4 /24 and the IPv6 /48 can be sub-devided into smaller subnets (not defined yet)


## AS numbers
* For readability purposes, ASNs have been selected from the private 32bit ASN notation, 
  this will allow to embedd the POD-x.y notation directly into the ASN
* The y value is always padded to three digits
* An assumption has been made that one POD is only a single AS  

* ASN will look like this: __42000xxyyy__
* Resulting in the following range: __4200016001 to 4200031255__
