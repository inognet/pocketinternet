# Pocket Internet

A Pocket Internet for teaching how the Internet really works.

## Mission statement & Background

**Background:** providing a fully automated lab environment for running training workshops or testing features at scale. The idea was originally formulated by [Cristian Sirbu](https://trueneutral.eu) for the [NetEngCode Hackathon](https://github.com/cmsirbu/netengcodehack/blob/master/20170422-dublin-hack.md) in Dublin (Apr 2017) and subsequently kickstarted by an awesome team at the [RIPE NCC IPv6 Hackathon](docs/preso/20171105_Pocket_Internet.pdf) in Copenhagen (Nov 2017).

**Idea:** an infinitely scalable topology that interconnects small pods (ISPs) into a procedurally generated network (the Internet). Each pod design would be based on a blueprint inspired from real life SPs (e.g. transit, IXP, broadband, content) and be as lightweight as possible, while still allowing for enough policy/complexity to be built in, so that many of them can be run at the same time on IaaS at low cost.

**Goal:** teach Internet technologies and concepts (BGP, DNS, HTTP, CDN, IPv4/v6, DHCPv4/v6, NAT64, routing policy) and automation in an environment that emulates a simplified version of the actual Internet. Stretch goals: developing more advanced policies, monitoring, mapping or testing new BGP extensions.

## Design and Documentation

Documentation for the project can be found under the [docs](docs/) folder.

## Demo

A pre-packaged VM with the demo topology showcased at the RIPE hackathon is in the works.

## Setup

### Prerequisites

Before cloning this repo, you should ensure you have docker installed. Please note that due to the amount of private address space we use within Docker for our [addressing scheme](docs/IP_address_plan.md) we recommend using a clean machine that you are not already using Docker with for this, as our first step reconfigures the Docker daemon to not conflict with our allocated addressing.

To help getting started with this, we are planning to write a Vagrantfile to bring up a basic Docker host.

### Running PocketInternet

First, install using `python setup.py install`.

Once done, a one-off Docker configuration should be applied. Do this using `sudo pocketinternet configure-docker`.

Once that has been done your one-time setup has been completed. Next, deploy your lab using `pocketinternet setup`.

This uses `lab.yml` by default, however a different yml file can be specified using the `-c filename.yml` command line flag.

## Contributing

We appreciate your input! We'd like to make contributing to this project as easy and transparent as possible, be it:

- Reporting a bug
- Discussing the current state of the code
- Submitting a fix
- Proposing new features
- Becoming a maintainer

We use GitHub to host code, to track issues and feature requests, as well as accept pull requests. The process is explained here - [Github Flow](https://guides.github.com/introduction/flow/index.html) - and we're happy to help you get on your way to contributing to the project!

Please read more about the [contribution guidelines and project code of conduct here](https://github.com/inognet/pocketinternet/blob/master/CONTRIBUTING.md).

## Acknowledgements

Maintained by [Cristian Sirbu](https://github.com/cmsirbu) and [contributors](https://github.com/inognet/pocketinternet/graphs/contributors).

The project was kickstarted through 2 hackathons by the following awesome people:

- Henrik Kramshøj
- Harry Reeder
- Evangelos Balaskas
- Andy Mindnich
- Samer Lahoud
- Dónal O Duibhir
