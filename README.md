# dataKFT

## Architecture

![image](https://github.com/galbrecht22/dataKFT/blob/main/dataKFT_architecture.png)

## Objects
### `controller` module
<b>Controller</b> - the central object for the coordination of data processing.
Executes extract, load and transform steps in sequence, delegating data manipulation logic to the respective Controller objects.

### `model` module
<b>TenderSchema</b> - dataclass for `Tender` objects to validate schema retrieved from `tenders` endpoint of `https://tenders.guru/api/hu/` API.  
<b>TenderDetailsSchema</b> - dataclass for `TenderDetails` objects to validate schema retrieved from `tenders/:tender_id/source_data` endpoint of `https://tenders.guru/api/hu/` API.  
<b>ShipSchema</b> - dataclass for `Ship` objects to validate schema retrieved from `ships` endpoint of `https://data-engineer-interview-api.up.railway.app/` API.

### `api` module
<b>TenderListAPIController</b> - controller object to execute requests for `tenders` endpoint of `https://tenders.guru/api/hu/` API and retrieve `Tender` objects.  
<b>TenderDetailsAPIController</b> - controller object to execute requests for `tenders/<tender_id>/source_data` endpoint of `https://tenders.guru/api/hu/` API and retrieve `TenderDetails` objects.  
<b>ShipListAPIController</b> - controller object to execute requests for `ships` endpoint of `https://data-engineer-interview-api.up.railway.app/` API and retrieve `Ship` objects.

### `database` module
<b>MongoDBController</b> - controller object to manipulate data retrieved from APIs and persist them in raw format to MongoDB. MongoDB has been chosen as database platform to load raw data from API sources.  
There are two main functions implemented - `build()`, `store()` and `load()`.  
* Purpose of `build()` is to initialize the data objects used during data processing.  
* Purpose of `store()` is to save a list of `dict` objects into a collection as documents.  
* Purpose of `load()` is to retrieve all documents from a collection.  
<b>MySQLController</b> - controller object to execute predefined ddl and dml scripts on MySQL database tables. MySQL has been chosen as backend platform to serve the required visualization.  
There are three main functions implemented - `build()`, `bulk_insert()` and `populate()`.  
* Purpose of `build()` is to initialize the data objects used during data processing.  
* Purpose of `bulk_insert()` is to insert a list of records stored in memory into data objects. Used in `load` phase.  
* Purpose of `populate()` is to execute predefined `INSERT` statements. Used in `transform` phase.

