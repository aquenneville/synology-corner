#!/usr/bin/python

import os
import sys
import re
import shutil


def main():

    is_dry_run = False
    destination_folder = '/volumes1/photo/database/'

    if len(sys.argv[1]) == 1 and sys.argv[1] == "-h":
        print("Usage: " + sys.argv[0] + " to organize the photos or movies (files with extension: )" +
                                        "by year and month in a separate folder ")
        print(sys.argv[0] + " can be run in dry mode with: --dry_run")
        exit(0)

    elif len(sys.argv[1]) == 1 and sys.argv[1] == "--dry_run":
        is_dry_run = True

    for dir_path, dir_names, file_names in os.walk("./"):
        for filename in file_names:
            if filename.endswith('.png', '.jpg', '.jpeg', 'mp4'):
                print('> Managing the digital photo: ' + os.path.join(dir_path, filename))
                match_date_obj = re.match(r'\d{8}', filename, re.M | re.I)

                if match_date_obj:
                    year = match_date_obj.group()[1:4]
                    month = match_date_obj.group()[5:6]

                    if not os.path.exists(os.path.join(destination_folder, year, month, filename)):
                        os.makedirs(os.path.join(destination_folder, year, month))
                        print('> Creating the sub folder: ' + os.path.join(destination_folder, year, month, filename))

                    if not is_dry_run:
                        p = os.fork()
                        if p == 0:
                            shutil.copy2(os.path.join(dir_path, filename),
                                     os.path.join(destination_folder, year, month, filename))
                            print('> Copied the file to: ' + os.path.join(destination_folder, year, month, filename))
                            print('> Remove file: ' + os.path.join(destination_folder, year, month, filename))
                            break
                else:
                    print('> Could not find date YYYYMMDD in filename: ' + os.path.join(dir_path, filename))
            else:
                print('> Jump over file: ' + os.path.join(dir_path, filename) + ' it is not a photo or movie. ' +
                      'Expecting extensions to be: jpg, jpeg, png, mp4')


if __name__ == "__main__":
    main(sys.argv)
