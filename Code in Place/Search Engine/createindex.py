from Searchengine import format_clean_string


def create_index(filenames, index, file_titles):  #MILESTONE 2
    """
    This function is passed:
        filenames:      a list of file names (strings)
        index:          a dictionary mapping from terms to file names (i.e., inverted index)
                        (term -> list of file names that contain that term)
        file_titles:    a dictionary mapping from a file names to the title of the article
                        in a given file
                        (file name -> title of article in that file)
    The function will update the index passed in to include the terms in the files
    in the list filenames.  Also, the file_titles dictionary will be updated to
    include files in the list of filenames.
    >>> index = {}
    >>> file_titles = {}
    >>> create_index(['test1.txt'], index, file_titles)
    >>> index
    {'file': ['test1.txt'], '1': ['test1.txt'], 'title': ['test1.txt'], 'apple': ['test1.txt'], 'ball': ['test1.txt'], 'carrot': ['test1.txt']}
    >>> file_titles
    {'test1.txt': 'File 1 Title'}
    >>> index = {}
    >>> file_titles = {}
    >>> create_index(['test2.txt'], index, file_titles)
    >>> index
    {'file': ['test2.txt'], '2': ['test2.txt'], 'title': ['test2.txt'], 'ball': ['test2.txt'], 'carrot': ['test2.txt'], 'dog': ['test2.txt']}
    >>> file_titles
    {'test2.txt': 'File 2 Title'}
    >>> index = {}
    >>> file_titles = {}
    >>> create_index(['test1.txt', 'test2.txt'], index, file_titles)
    >>> index
    {'file': ['test1.txt', 'test2.txt'], '1': ['test1.txt'], 'title': ['test1.txt', 'test2.txt'], 'apple': ['test1.txt'], 'ball': ['test1.txt', 'test2.txt'], 'carrot': ['test1.txt', 'test2.txt'], '2': ['test2.txt'], 'dog': ['test2.txt']}
    >>> index = {}
    >>> file_titles = {}
    >>> create_index(['test1.txt', 'test2.txt', 'test2.txt'], index, file_titles)
    >>> index
    {'file': ['test1.txt', 'test2.txt'], '1': ['test1.txt'], 'title': ['test1.txt', 'test2.txt'], 'apple': ['test1.txt'], 'ball': ['test1.txt', 'test2.txt'], 'carrot': ['test1.txt', 'test2.txt'], '2': ['test2.txt'], 'dog': ['test2.txt']}
    >>> file_titles
    {'test1.txt': 'File 1 Title', 'test2.txt': 'File 2 Title'}
    >>> index = {'file': ['test1.txt'], '1': ['test1.txt'], 'title': ['test1.txt'], 'apple': ['test1.txt'], 'ball': ['test1.txt'], 'carrot': ['test1.txt']}
    >>> file_titles = {'test1.txt': 'File 1 Title'}
    >>> create_index([], index, file_titles)
    >>> index
    {'file': ['test1.txt'], '1': ['test1.txt'], 'title': ['test1.txt'], 'apple': ['test1.txt'], 'ball': ['test1.txt'], 'carrot': ['test1.txt']}
    >>> file_titles
    {'test1.txt': 'File 1 Title'}
    """
    #print ("Filenames:", filenames)
    length = len(filenames)
    print(length, "Filenames detected in the directory")
    #get filenames and open and read
    #loop through each file and open and read the contents of the file.
    #Process the contents and store in to the index
    # Build the index

    for i in range(length):  #Loop through the number of files in the directory
        name_of_file = filenames[i]
        file_titles_names = filenames[i]
        filename_list = []  # initialize and create the empty list
        # Build the index

        with open(name_of_file) as f:
            #clean_filename = strip_directory_name(name_of_file)
            clean_filename = name_of_file
            filename_list = [clean_filename]
            #print("PROCESSING FILE: ", count+1)
            for line in f:
                new_line = format_clean_string(line)
                new_line = new_line.lower()
                new_line_list = new_line.split()  #convert the line into list.
                new_line_list_length = len(new_line_list)  # get the length of the new created list of the line

                for each_element in range (new_line_list_length):
                    filename_list = [clean_filename]
                    key = index.get(new_line_list[each_element])
                    value = index.get(new_line_list[each_element])
                    #print ("KEY = ",new_line_list[each_element]," CURRENT VALUE: ", value)
                    if key != None:
                        #print ("key", new_line_list[each_element] , "already exist: Appending filename!" , value )
                        getlist = index.get(new_line_list[each_element])
                        getlist.append(clean_filename)
                        #print("GETLIST AFTER APPEND:", getlist, "GETLIST LENGTH:", len(getlist) )
                        #put the appended list back in the key value
                        key = new_line_list[each_element]
                        #print("Inserting:",getlist , "into: ", key)
                        index[key] = getlist

                        # use that length and process each element in the list
                        #each element in the new_line_list becomes a key. The file name becomes the value
                        #index[new_line_list[each_element]]=filename_list  #each put the key and key value into  the index:
                    else:
                        #print("Adding:", filename_list, "to index key: ", new_line_list[each_element])
                        index[new_line_list[each_element]] = filename_list

                    # clear out the list.
                    getlist = []
                    filename_list = []

        #Build the Dictionary for File_Titles
        with open(file_titles_names) as dictionary_f:
            first_line = dictionary_f.readline()
            #file_titles_names = strip_directory_name(file_titles_names)
            first_line = format_clean_string(first_line)
            file_titles[file_titles_names] = first_line.rstrip()

    #print("INDEX BUILD COMPLETE", index)
    #print("FILE_TITLE BUILD COMPLETE", file_titles)