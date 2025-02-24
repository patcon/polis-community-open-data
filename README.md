# Polis: Crowdsourced Open Data

This is a collection of crowd-sourced open data from Polis conversations discovered over the years.

The purpose of this repo is to more easily share data from a wide variety of sources and processes (of difference sizes) with independant researchers. I am specfically hopeful it will help researchers to development and test democracy-supporting algorithms.

This repo currently only contains data from conversations that have been closed to new votes. This is in the interest of keeping open Polis conversations overly discoverable and susceptible to introduction of junk data.

For a description of all conversations, see [`conversations.csv`](conversations.csv).

## Roadmap

- [x] Update CSV from Google Sheet daily
- [x] Update datasets from Polis API weekly
- [ ] Check lastvote and skip if nothing newer
- [ ] Summarize conversation topics in README
- [ ] Figure out better way to write export content as CSV instead of JSON
- [ ] Document usage with `polis-community/red-dwarf`
- [ ] Figure out a way to strip conversation IDs to publish conversations still open
- [ ] Fail more gracefully when data fetches fail. (Still try to commit results)
