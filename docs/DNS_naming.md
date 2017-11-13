# Pocket Internet DNS

### Principles: 

* .lab is the TLD for the entire lab setup
* .demo.lab is the global domain for cross-POD testing
* .Pxxyyy.lab is the specific domain for every POD
* There will be pre-configured DNS names for every router interface and server instance. 
* There will be three names per interface, one for dual-stack, one for IPv4 only and one for IPv6 only

### This will give us the following definitions: 

* __Backbone router interfaces__  
  Rn.Pxxyyy.BB.lab  [A+AAAA]  
  Rnv4.Pxxyyy.BB.lab [A only]  
  Rnv6.Pxxyyy.BB.lab [AAAA only]

* __Internal router interfaces__  
  Rn.Pxxyyy.lab  [A+AAAA]  
  Rnv4.Pxxyyy.lab [A only]  
  Rnv6.Pxxyyy.lab [AAAA only]
  
* __Server interfaces__  
  Ss.Pxxyyy.lab [A+AAAA]  
  Ssv4.Pxxyyy.lab [A only]  
  Ssv6.Pxxyyy.lab [AAAA only]
  
* __Global CNAMES__  
  i.e. www.demo.lab  = Ss.Pxxyyy.lab

### Reminder on variables: 

* xx is the first part of the POD number (PODx.y). It can be between 16 - 31
* yyy is the second part of the POD number (PODx.y). It can be between 1-255
* n is the router instance within a POD, with local significance only. Can be 1-89
* s is the server instance within a POD, with local significance only. Can be 1-154
