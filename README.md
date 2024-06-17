# Abstrct:
The project developed in python. It is an console application uses that requires 2 parameters: City, [Country code]
The project check if there is internet connection otherwise it notify the user. if there is so it goes to the weather site "https://openweathermap.org/forecast5#name5" and perform a query using two api calls.


# Note: There is a refactoring which enters logic , classes , Code strategy -  Done - you may look on the link:WeatherOOP here in my repo .
        Add refactoring plan\design. read belwo or at read me at the new REPO:
        # The refactoring is at public repo here - youy may see for correct writing , the use of events , cache and layer of B logic
        https://github.com/GuyYar1/WeatherOOP - Done ready to use. Please refer to this as the delivery project.

        old site: https://weather-forecast-17-gy.streamlit.app/
        
        
# Steps:

# Run it using streamlit:
    1. Open the phaycharm or python terminal 

Note: locally without "streamlit" is fully implemented according to requirements.
       streamlit have few capabilities such as: results list, TZ stamp.

# Run it using streamlit:
    1. Open the pycharm powershell 
    2. type: streamlit run app.py
    3. GUI is running locally and connection to restfull api retried data.
    note: if you want to see the entire support with date TZ you should run the console app. yet not supported at streamlit.

    <img width="618" alt="image" src="https://github.com/GuyYar1/PythonDelivRepo/assets/132554415/1ed3ff3f-7018-4bef-b1cd-141fe4e454e9">

# Run it locally using pycharm or python 311 interpreter :
    1.Run the project , the main is sign as the main run configuration.
    2.Answer the two question, click enter (case sensative key1&Key2 uniqness) .
    3.Results retrived in the output pane.
        3.1. if there is no internet, use mem or persistance cache.
        3.2. If more than 2 hours have passed since the last query from the cache, perform a new restfull api query.
    4.check that the country you selected is the current one, otherwise click 1 to continue.
    5. The service is console currently and provide option to do multiple queries.
    
# General:    
The project has one class that uses its own attributes and methods. it uses a common Import file to all of its files. that way we can do one import on each file.
    Files:
            1.common_imports.py - gather all the import module or packs into one file and later on use one import all from this collection.
            2.TimeUtils.py - time utilities that handles the time zone and similar.
            3.requirements.txt - output of the moduls and pack that installed on developer pc. (should consider in future to clean dependencies to knwo which are used)
            4.gitignore - ignore not relevant files that related to dev IDE or others irrlevant.
            5.IpNetUtils.py - allow to check network, replace an ip in case of blocking from web api service.
            6. WeatherForecast.py - include the functionality of the program using inheritance.
 
    
    # class WeatherForecast(CacheBase) 
        # Superclass (Base Class): CacheBase
            This is the class from which WeatherForecast inherits. It contains the methods and attributes related to caching that will be shared among different subclasses.
            
        # Subclass (Derived Class): WeatherForecast
            This is the class that inherits from CacheBase. It extends the functionality of CacheBase by adding weather-specific methods and attributes.   
            Files: 
                1.Cach.py - cache class with all the regular method CRUD.
                2.cache_file.pkl - module that save cach to file. file is saved on the project folder
        
# key Gen Data Privacy 
The api Key is saved as encoded 64bit UFT-8 {Base64 is used to encode binary data into a text format . When there is a Text need to strings are typically represented using UTF-8 encoding. This ensures that all characters, including special characters}
    Files: 
        1.EncodingUtils.py - File that holds the utilities of encoding and encoding. read fromfile combinewithdecode, extract api  using regex.

# Prerequisite:
# 1.
   In the beginning there is a need to install packages using pip install: 
      python -m pip install requests
     install geopy
     pip install geopy timezonefinder # PIp on terminal
     pip install geopy timezonefinder pytz
     pip install python-dotenv # halt due to conflicts
     pip install file

     e.g: look on requirements.txt.

# 2.   look also on the commit file name Common_Import save time import on each file.
        later on when we use the pythone with those package or module s we need to import them:
        so i created one file that shows the pack and moduls that were in my pc when my project was run\built. look on the file:requirements.txt.


# Refactoring Plan - Design:

The current project is flat with no logic.
Low separation to classes.currently there are utils and one class.

Refactor will include:

A.Server side (weather server):
    API Server took its data from the DB transfer it to the client request it: ( our app)
    prepare the data and send us it DTO structure.

B.our app - Backend
    should be:
        1 our app is basically print the data results on the screen using stream lit.        
        2 "Weather service Printer"  using injection , is being injected with "weather manager" .
        3 "weather manager" role is to give command to specific parser of the specific URL API request.
        4 In case GUI  "requested to bring the data and save it" the process began.
        "requested to bring the data and save it" process - Parser get the URL from the "weather manager" and the parser, request the data on a generic data model. each parser has derived class that fit to one specific                 query. 
        5 The parser parse the generic data model to specific model object and save it.
        6 This action is asyncronus when the parser finish, it raises an event that the data is ready.        
        7 When the "weather manager" got an event from specific parser that the data was saved in the model. it added it to the queue.
          And by its own timeline it refers to the queue one by one.
        
        8 For the meantime, we have only one GUI that invoke one trigger at a time, but we should consider to check in unit test that it could handle a burst of queries.
           Our app is basically all the time get data from the server, no such case that we update or post requests from our side to server.

C.our app- FrontEnd

    The connection between the backend to the "Weather service Printer" which is the high hierarchy class. it based on a singleton, so the updates should be connected via binding per GUI ID.
    In case of multiple request or multiple GUI support we should use the GUI ID. - for the mean time GUI ID will be 1 and only.
    
