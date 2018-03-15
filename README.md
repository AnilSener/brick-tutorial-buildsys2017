# Brick Tutorial at BuildSys 2017

## Contents
- `Brick Composition.ipynb`: Learning what Brick instance looks internally with constructing it from the scratch. This would not be a repetitive work that you need to do for everytime, but useful for understanding Brick's concepts. You can learn SPARQL basic also.
- `Brick Conversion (Tutorial).ipynb`: Tutorial of how to convert some raw metdata in BMS to Brick. It uses simple regular expression rules and relationship mapping to automate the process
- `Brick Conversion (Full).ipynb`: Converting the all sample raw metadata defined in `metadata/brick_sample_building_raw.csv`. It is not intended for the tutorial, but it is more complete than Brick conversoin (Tutorial) and one may look into it if interested.
- `Brick Queries and Data Analysis.ipynb`: How to use SPARQL to query Brick for complex question and how to use integrate with usable data analysis (fault diagnosis) that can be used across any buildings in Brick.


### Data Description
- `metadata/brick_sample_building_raw.csv`: sample raw metadata from a BMS.
- `metadata/sample_building.ttl`: Brickified sample building. Intantiated from the above file with the Brick Conversion (Full).ipynb
- `data/`: timeseries data corresponding to UUIDs described in the ``metadata/brick_sample_building_raw.csv``


## Resources
- [Brick Official Website](http://brickschema.org/)
- [Brick Github Repository](https://github.com/BuildSysUniformMetadata/Brick.git)
- [BuildSys 2017](http://buildsys.acm.org/2017/)
- [Brick Tutorial at BuildSys 2017](https://brickschema.org/buildsys2017/)
