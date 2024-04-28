import kaggle

kaggle.api.authenticate()

while True:
    
    item = input("Please enter the dataset you need to search: ")
    print()
    
    ##Searching for dataset
    datasets = kaggle.api.dataset_list(search=item)
    print(datasets)

    print()
    name = input("Enter the dataset name you have chosen: ")
    print()

    ##Listing out the files in the dataset
    print("The files in your dataset are: " , kaggle.api.dataset_list_files(name).files)


    ##To download the dataset
    kaggle.api.dataset_download_files(name , path='.' , unzip=True)


    ##To download the metadata
    kaggle.api.dataset_metadata(name , path='.')
    
    print()

    while True:
    
        choice = input("Want to get another Dataset?: ")

        if choice.lower() == 'no':
            break

        elif choice.lower() != 'yes':
            print("Invalid choice!! >:(")
            continue
        
        else:
            break

    if choice.lower() == 'no':
        break
