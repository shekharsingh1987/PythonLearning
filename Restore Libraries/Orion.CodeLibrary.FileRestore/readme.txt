-----------------------------------------------------------------------------------------------------
-------------- File Restore -------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------
This library you can use when you are having a scenario 
where you have to restore file/files from a source location 
to destination.

How to use:
-----------
1. Initialize the object
	//File restore
    FileRestoreManager fileManager = new FileRestoreManager();

2. Initialize an event
	fileManager.OnFileRestore += FileManager_OnFileRestore;

3. Define FileManager_OnFileRestore method 
	 private static void FileManager_OnFileRestore(object sender, RestoreStatus eventArg)
        {
			//Do something.
            Console.WriteLine(eventArg.status.ToString());
            Console.WriteLine(eventArg.errorInfo);
            Console.ReadKey();
        }


Special Case:
When you wnat filter the file to be copied, then there a propert defined. you can write pattern there.
	fileManager.FileTypeSearchPattern = $"*.exe";
 