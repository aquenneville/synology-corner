#!/usr/bin/python

import os
import sys
import re
import shutil
import time

def main(argv):

    ext = [".jpg", ".png", ".jpeg", ".mp4"]
    is_dry_run = False
    destination_folder = '/volume1/photo/database/'
    start = time.time()
    
    if len(argv) == 2: 
    
        if len(argv) == 2 and argv[1] == "-h":
            print("Usage: " + argv[0] + " to organize the photos or movies (files with extension: )" +
                                        "by year and month in a separate folder ")
            print(argv[0] + " can be run in dry mode with: --dry_run")
            exit(0)

        elif len(argv) == 2 and argv[1] == "--dry_run":
            is_dry_run = True

    print(is_dry_run)
    file_cnt = 0
    for dir_path, dir_names, file_names in os.walk("/volume1/photo/mobile/alain/"):
        for filename in file_names:
            # print(filename)
            if filename.endswith(tuple(ext)):
                print('> Managing the digital photo: ' + os.path.join(dir_path, filename))
                #match_date_obj = re.match(r"20\d{6}", filename, re.M | re.I)
                match_date_obj = re.search(r"20\d{6}", filename)
                
                if match_date_obj:
                    year = match_date_obj.group()[:4]
                    #print("year"+os.path.join(destination_folder, year))
                    #if not os.path.exists(os.path.join(destination_folder, year)):
                    #    print("creating"+os.path.join(destination_folder, year))
                    #    os.makedirs(os.path.join(destination_folder, year))
                    month = match_date_obj.group()[4:6]
                    #print(month)
                    if not os.path.exists(os.path.join(destination_folder, year, month)):
                        print(os.path.join(destination_folder, year, month))
                        os.makedirs(os.path.join(destination_folder, year, month))
                        print('> Creating the sub folder: ' + os.path.join(destination_folder, year, month))
                    if not os.path.isfile(os.path.join(destination_folder, year, month, filename)):
                        if not is_dry_run:
                            p = os.fork()
                            if p == 0:
                                print(str(os.getpid()) + "> Copying the file " + os.path.join(dir_path, filename))
                                shutil.copy2(os.path.join(dir_path, filename),
                                     os.path.join(destination_folder, year, month, filename))
                                #file_cnt = file_cnt + 1
                                break
                            #print('> Copied the file to: ' + os.path.join(destination_folder, year, month, filename))
                            file_cnt = file_cnt + 1
                            #print('> Remove file: ' + os.path.join(destination_folder, year, month, filename))
                           #     break
                    else:
                        print('> File had already been copied')       
                else:
                    print('> Could not find date YYYYMMDD in filename: ' + os.path.join(dir_path, filename))
            else:
                print('> Jump over file: ' + os.path.join(dir_path, filename) + ' it is not a photo or movie. ' +
                      'Expecting extensions to be: jpg, jpeg, png, mp4')


    print("Number of files copied: " + str(file_cnt))
    end = time.time()
    print(end - start)    

if __name__ == "__main__":
    main(sys.argv)
