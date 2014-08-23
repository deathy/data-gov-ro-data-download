data-gov-ro-data-download
=========================

data.gov.ro data set download

Downloads all data sets from the http://data.gov.ro/ CKAN instance using the CKAN API.

Both CKAN-hosted and external resources are downloaded based on their URL. In case of invalid URLs or problems 
accessing URLs a message is logged like "Error retrieving URL: url". Downloads everything to `downloads/` creating
sub-folders for each individual data set.

Also downloads API JSON responses for listing of data sets and for each data set description (saved as `package_desc.json` 
in individual data set folder)  

