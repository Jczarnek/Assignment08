#------------------------------------------#
# Title: CD_Inventory.py
# Desc: Assignnment 08 - Working with classes
# Change Log: (John Czarnek, 2021-Aug-28, copy and pasted parts of my Assignment07 code
#		        John Czarnek, 2021-Aug-28, created CD class)
#               John Czarnek, 2021-Aug-29, created FileIO class and 
#                   added static methods save_inventory and load_inventory
#               John Czarnek, 2021-Aug-29, modified input_CD method of class 
#                   to function with CD objects
#		        John Czarnek, 2021-Aug-29, removed delete functionality
# DBiesinger, 2030-Jan-01, created file
# DBiesinger, 2030-Jan-01, added pseudocode to complete assignment 08
#------------------------------------------#
import pickle
# -- DATA -- #
strFileName = 'cdInventory.dat'
lstOfCDObjects = []
class CD:
    """Stores data about a CD:

    properties:
        cd_id: (int) with CD ID
        cd_title: (string) with the title of the CD
        cd_artist: (string) with the artist of the CD
    methods:

    """

    #   Constructor  @
    def __init__(self,cd_id,cd_title,cd_artist):
        self.__cd_id = cd_id
        self.__cd_title = cd_title
        self.__cd_artist = cd_artist
        
    #  Properties  #
    
    @property
    def cd_id(self):
        return self.__cd_id
    
    @property
    def cd_title(self):
        return self.__cd_title
    
    @property
    def cd_artist(self):
        return self.__cd_artist
    
        
    #  Methods  #
    def __str__(self):
        return str(self.__cd_id) + '\t ' + self.__cd_title + ' ' + '(by: ' + self.__cd_artist + ')'
    


# -- PROCESSING -- #
class FileIO:
    """Processes data to and from file:

    properties:

    methods:
        save_inventory(file_name, lst_Inventory): -> None
        load_inventory(file_name): -> (a list of CD objects)

    """

    @staticmethod
    def save_inventory(file_name, lst_Inventory):
        """Function to write table to digital file
        
        Args : file name to write to, and the 2D list of CD objects
        
        Returns : writes to file
        """
        objFile = open(file_name, 'wb')
        pickle.dump(lst_Inventory, objFile)
        objFile.close()
        
    @staticmethod
    def load_inventory(file_name):
        """Function to manage data ingestion from file to a list of CD objects

        Reads the data from binary file identified by file_name into a 2D table

        Args:
            file_name (string): name of file used to read the data from
            

        Returns:
            table (list of dictionaries)
        """
        objFile = open(file_name,'rb')
        table = pickle.load(objFile)
        objFile.close()
        return table    
     

# -- PRESENTATION (Input/Output) -- #
class IO:
    """Displays menu, gets user input, displays current inventory, and gets CD information

    properties:

    methods:
        print_menu(): -> None
        menu_choice(): -> 
        show_inventory(table):->(a list of CD objects)
        input_CD():

    """
    @staticmethod
    def print_menu():
        """Displays a menu of choices to the user

        Args:
            None.

        Returns:
            None.
        """

        print('Menu\n\n[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
        print('[s] Save Inventory to file\n[x] exit\n')

    @staticmethod
    def menu_choice():
        """Gets user input for menu selection

        Args:
            None.

        Returns:
            choice (string): a lower case sting of the users input out of the choices l, a, i, d, s or x

        """
        choice = ' '
        while choice not in ['l', 'a', 'i', 's', 'x']:
            choice = input('Which operation would you like to perform? [l, a, i, s or x]: ').lower().strip()
        print()  # Add extra space for layout
        return choice

    @staticmethod
    def show_inventory(table):
        """Displays current inventory table

        Args:
            table (list of CD objects): 2D data structure that holds the data during runtime.

        Returns:
            None.

        """
        print('======= The Current Inventory: =======')
        print('ID\tCD Title (by: Artist)\n')
        for row in table:
            print(row)
        print('======================================')
    

    @staticmethod 
    def input_CD():
        """Gets data input from user about CD to be added
        
        Args : None
        
        Returns : a list of data about the CD
        """
        while True:
            try:
                strID = int(input('Enter ID: ').strip())
                break
            except ValueError:
               print("Please enter an integer")
        strTitle = input('What is the CD\'s title? ').strip()
        strArtist = input('What is the Artist\'s name? ').strip()
        new_CD_data = CD(strID,strTitle,strArtist)
        return(new_CD_data)
        

# -- Main Body of Script -- #
# 1. When program starts, read in the currently saved Inventory; if not file, then writes blank file
try:
    lstOfCDObjects = FileIO.load_inventory(strFileName)
except FileNotFoundError:
    FileIO.save_inventory(strFileName, lstOfCDObjects)

# 2. start main loop
while True:
    # 2.1 Display Menu to user and get choice
    IO.print_menu()
    strChoice = IO.menu_choice()

    # 3. Process menu selection
    # 3.1 process exit first
    if strChoice == 'x':
        break
    # 3.2 process load inventory
    if strChoice == 'l':
        print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
        strYesNo = input('type \'yes\' to continue and reload from file. otherwise reload will be canceled')
        if strYesNo.lower() == 'yes':
            print('reloading...')
            lstOfCDObjects = FileIO.load_inventory(strFileName)
        else:
            input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
        continue  # start loop back at top.
    # 3.3 process add a CD
    elif strChoice == 'a':
        # 3.3.1 Ask user for new ID, CD Title and Artist
        new_data=IO.input_CD()
        # 3.3.2 Add item to the table
        lstOfCDObjects.append(new_data)
        continue  # start loop back at top.
    # 3.4 process display current inventory
    elif strChoice == 'i':
        IO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
    # 3.6 process save inventory to file
    elif strChoice == 's':
        # 3.6.1 Display current inventory and ask user for confirmation to save
        IO.show_inventory(lstOfCDObjects)
        strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
        # 3.6.2 Process choice
        if strYesNo == 'y':
            # 3.6.2.1 save data
            FileIO.save_inventory(strFileName,lstOfCDObjects)
        else:
            input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
        continue  # start loop back at top.
    # 3.7 catch-all should not be possible, as user choice gets vetted in IO, but to be save:
    else:
        print('General Error')




