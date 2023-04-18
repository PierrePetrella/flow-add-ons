# Flow add ons

![GitHub release (latest by date)](https://img.shields.io/github/v/release/dataiku/dss-plugin-flow-add-ons) ![Build status](https://img.shields.io/badge/build-passing-brightgreen) ![Support level](https://img.shields.io/badge/support-Unsupported-orange)

This Dataiku plugin is composed of X components:
- Transpose dataset : recipe
- Drop empty columns : recipe
- Add recordID : recipe
- Add record ID : prepare step

Documentation : link

## Transpose Dataset:
Input:
- 1 dataset
Output : 
- 1 dataset
Parameters :
- Column to use as column names after transpose

Usage:
- Transpose a dataset without any limitation (leveraging pandas)


## Drop empty columns:
Input:
- 1 dataset
Output : 
- 1 dataset
Parameters :
- None

Usage:
- Drop all columns with ALL empty columns


## Add recordID:
Input:
- 1 dataset
Output : 
- 1 dataset
Parameters :
- RecordID name
- RecordID start

Usage:
- As a Prepare Recipe Step
- As a visual Recipe

## License

This plugin is distributed under the [Apache License version 2.0](LICENSE).