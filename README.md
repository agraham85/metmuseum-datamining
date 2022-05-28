# COMP4447_Project
Project for Data Tools 1 COMP4447

Team members: Mike Schmidlin, Andrew, Peter Strimbu


Mission:
This team examined the "MetObjects" data set consisting of data from all the objects within the Metropolitan Museum of Art. The data was cleaned as much as possible and then summary data visuals were created to examine the data. 


Data set:
The dat set had 477,805 rows and 54 columns consisting of mostly text data but also numberical, boolean, and categorical data. The data contains properties related to artwork such as created dates, artist information, what materials the art is made out of, etc...


Logistics:
The data columns were divided up so each team member attempted to clean 1/3 of the data columns. In this way we attempted to clean the whole data set. This took place over two weeks with weekly meetings. At this point each team member took columns they found interesting and generated visuals. All code updates and cleaning was pushed to a remote gitgub repo.  


Cleaning difficulties:
There were many things in this dataset that made it difficult to clean. There was the usual issues of missing data and inconsistent formatting. Series.str methods were a good method for dealing with these inconsistencies. In addition there were extra challenges in this dataset such as multiple data entries per cell. For example if a piece of art had multiple artists associated with it they would be in a single cell delimited by a "|". 


Final Product:
Each person in the project worked from two different ipynb files. In addition, all cleaning techniques were combined in the "cleaning.py" file which outputs four different pickle files for storing the cleaned data (artist_df.pkl, city_df.pkl, clean_artist_df.pkl, clean_df.pkl, country_df.pkl). The artist, country, and object files reflect the need for seperated data based on the "|" for cells with more then one data point. Finally, the cleaning_utils.py contains some functions utilized for splitting the rows of the data frame based on a delimiter. 


cleaning_peter.ipynb - contains cleaning and visualizations code made by Peter

a_cleaning.ipynb - contains cleaning code made by Andrew
a_visuals.ipynb - contains visualization code made by Andrew

mike_cleaning_ipynb - contains cleaning code made by Mike
mike_visuals.ipynb - contains visualization code made by Mike

cleaning.py - contains all cleaning code combined into one executable py file
cleaning_utils.py - contains split_rows function for data cells with multiple data points




