# pocketinternet

A Pocket Internet for teaching how the Internet really works.

**Background:** providing a fully automated lab environment for running iNOG workshops or testing features at scale.

**Idea:** an infinitely scalable topology (on demand add/remove with automated provisioning) that mimics the Internet, with each participant being an ISP (small mesh of BGP routers that inject prefixes with policy).

The whole network would be a web of interconnected pods, each pod being built based on a blueprint inspired from various Service Provider types (transit, IXP, broadband, content). The pods themselves should be as lightweight as possible, so that many of them can be run at the same time on IaaS at low cost.

**Goal:** teach BGP and automation in an environment that emulates a simplified version of the Internet. Stretch goals: developing more advanced policies, monitoring, mapping or testing new BGP extensions.
