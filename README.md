# 🚀 Awesome Ad Serving Platforms

<div align="center">
  <img src="assets/banner.svg" alt="Awesome Ad Serving Platforms Banner" />
</div>

<div align="center">
  <a href="https://github.com/ishandutta2007/Awesome-Awesome-Awesome"><img src="https://img.shields.io/badge/Awesome-%E2%9C%94-blueviolet?style=flat-square&logo=github" alt="Awesome"/></a>
  <a href="https://discord.gg/jc4xtF58Ve"><img src="https://img.shields.io/badge/Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white" alt="Discord" /></a>
  <a href="https://github.com/ishandutta2007"><img alt="GitHub followers" src="https://img.shields.io/github/followers/ishandutta2007?label=Follow" /></a>
</div>

*A comprehensive, curated list of the best open-source and SaaS ad serving platforms, header bidding tools, and ad tech solutions to maximize publisher revenue.*

## 🔗 Similar Projects to Ad Serving Platforms

**Ad Serving Platforms** (Ad Servers) manage the delivery, targeting, tracking, and reporting of digital advertisements across websites, apps, and other digital properties. They handle campaign management, inventory allocation, real-time decisioning, and analytics for publishers, advertisers, and ad networks. Leading platforms include Google Ad Manager, Kevel, Revive Adserver, AdButler, Broadstreet, Epom, AdGlare, Equativ, OpenX, and Smart AdServer.

Below is a **curated list** of notable platforms and their open-source equivalents. The open-source ad serving space is led by Revive Adserver, with newer modern alternatives emerging.

## 🏢 SaaS / Hosted Platforms

| Platform | Description | Pricing | Free Tier Limit | Company Size (Valuation/Revenue) |
|---|---|---|---|---|
| **[Google Ad Manager](https://admanager.google.com/)** | The dominant enterprise ad server (formerly DoubleClick for Publishers / DFP) for large publishers, with advanced targeting, yield management, and programmatic integration. | Custom / CPM based after free tier | 90M-200M non-video impressions/month depending on region, 800K video impressions | >$1 Trillion |
| **[Equativ](https://equativ.com/)** | (formerly Smart AdServer) — Established ad serving and monetization platform. | Custom enterprise pricing | None | ~$100M+ |
| **[OpenX](https://www.openx.com/)** | Programmatic-focused platform (ad exchange / SSP heritage; original ad server evolved into Revive). | Custom enterprise pricing | None | ~$100M+ |
| **Smart AdServer** | Legacy/enterprise ad serving solution (now under Equativ in many markets). | Custom enterprise pricing | None | ~$100M+ |
| **[Kevel](https://www.kevel.com/)** | API-first ad serving platform designed for custom ad experiences, retail media, and developers building their own ad products. | Custom, based on features and API volume | None | ~$20M+ |
| **[Epom](https://epom.com/)** | Full-featured ad server supporting multiple formats, targeting, and optimization. | Starts at $250/month | None (14-day free trial) | ~$5M+ |
| **[AdButler](https://www.adbutler.com/)** | Flexible, configurable ad server popular with mid-market publishers and networks. | Starts at ~$179/month | None | ~$2M+ |
| **[Broadstreet](https://broadstreetads.com/)** | Ad server focused on direct-sold inventory, local publishers, and client-friendly ad creation/reporting. | Starts at $299/month | None | ~$2M+ |
| **[AdGlare](https://www.adglare.com/)** | Lightweight, modern ad server with real-time tracking and multi-format support. | Paid subscription | None (14-day free trial up to 10M requests) | ~$1M+ |

## 🔓 Open-Source Software 💻

### Full Open-Source Ad Servers
- **[Revive Adserver](https://github.com/revive-adserver/revive-adserver)** [![GitHub stars](https://img.shields.io/github/stars/revive-adserver/revive-adserver?style=social&color=white)](https://github.com/revive-adserver/revive-adserver/stargazers) — The world’s most popular free, open-source ad serving system (evolved from OpenX Source). Supports banner/HTML5/video ads, campaign management, targeting rules, detailed statistics, and multi-publisher/advertiser setups. Fully self-hosted under GPL. Also offers an optional Hosted edition.
- **[OpenAdServer](https://github.com/seanZhang414/openadserver)** [![GitHub stars](https://img.shields.io/github/stars/seanZhang414/openadserver?style=social&color=white)](https://github.com/seanZhang414/openadserver/stargazers) — Modern open-source ad serving platform built with Python, FastAPI, and PyTorch. Features ML-powered CTR prediction (DeepFM), real-time eCPM bidding, multiple ad formats, smart targeting, and Docker-based deployment. Positioned as a self-hosted alternative to Google Ad Manager with full data ownership.
- **[GreenRobot Ad Server](https://github.com/greenrobotllc/adserver)** [![GitHub stars](https://img.shields.io/github/stars/greenrobotllc/adserver?style=social&color=white)](https://github.com/greenrobotllc/adserver/stargazers) — An API-enabled yield optimization system written in PHP (Laravel). Designed to intelligently rotate ads between various networks.
- **[Adshares AdServer](https://github.com/adshares/adserver)** [![GitHub stars](https://img.shields.io/github/stars/adshares/adserver?style=social&color=white)](https://github.com/adshares/adserver/stargazers) — An open-source solution built on the Adshares blockchain ecosystem, combining DSP and SSP functionalities.
- **[Volt Adserver](https://github.com/krish512/volt)** [![GitHub stars](https://img.shields.io/github/stars/krish512/volt?style=social&color=white)](https://github.com/krish512/volt/stargazers) — A project currently under development, built with GoLang, focusing on performance and modern APIs.

### Related Open-Source Ad Tech Tools
- **[Prebid.js](https://github.com/prebid/Prebid.js)** [![GitHub stars](https://img.shields.io/github/stars/prebid/Prebid.js?style=social&color=white)](https://github.com/prebid/Prebid.js/stargazers) + **[Prebid Server](https://github.com/prebid/prebid-server)** [![GitHub stars](https://img.shields.io/github/stars/prebid/prebid-server?style=social&color=white)](https://github.com/prebid/prebid-server/stargazers) — Leading open-source header bidding framework and server-side auction solution. Widely used by publishers to run real-time auctions with multiple demand partners before (or alongside) an ad server.
- Community and research projects for DSP/RTB components, simple banner rotators, and specialized ad delivery engines (e.g., older OIO Publisher-style scripts or experimental AI-native ad engines).

### Supporting Building Blocks
- Open-source analytics and tracking tools that can be paired with ad servers for advanced reporting.
- Custom ad decisioning engines built on modern web frameworks when full ad-server features are not required.

### Typical Open-Source Approach
1. **Core ad server** — Revive Adserver (mature & battle-tested) or OpenAdServer (modern ML-focused)
2. **Header bidding / yield** — Prebid.js + Prebid Server
3. **Hosting & scaling** — Self-managed infrastructure (Docker/Kubernetes) or Revive’s hosted option
4. **Reporting & optimization** — Built-in stats + custom dashboards or integration with open analytics tools

These solutions give publishers and networks complete ownership of ad data, zero revenue share on self-hosted deployments, and full customization of targeting and delivery logic.

---

**How to contribute**  
Fork this repository, add a new project (with link + short description + category), and open a pull request.  
Prefer actively maintained open-source projects related to ad serving, ad servers, header bidding, or publisher monetization tools.

**License**  
This list is public domain / CC0. Feel free to copy into your own awesome list or README.

Star the projects you find useful — open ad tech helps publishers keep control of their inventory and revenue! 📢

##  Star History
<div align="center">
<a href="https://www.star-history.com/?repos=ishandutta2007%2FAwesome-Ad-Serving-Platform&type=date&legend=bottom-right">
<picture>
<source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=ishandutta2007/Awesome-Ad-Serving-Platform&type=date&theme=dark&legend=bottom-right" />
<source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=ishandutta2007/Awesome-Ad-Serving-Platform&type=date&legend=bottom-right" />
<img alt="Star History Chart" src="https://api.star-history.com/chart?repos=ishandutta2007/Awesome-Ad-Serving-Platform&type=date&legend=bottom-right" />
</picture>
</a>
</div>
# Awesome-Ad-Serving-Platform

