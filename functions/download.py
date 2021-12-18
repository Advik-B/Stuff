from functions.getlink import create_link
from functions.naming import name
from functions.custom_progressbar import QCustomProgressBar
from tqdm import tqdm
import cloudscraper
import os
import sys
import threading


class NoDataError(Exception):
    pass

NO_DATA = 'no-recorded-data.html'

downloader = cloudscraper.create_scraper()

def download(date: int, month: int, year: int, output_folder: str=None):
    global downloader
    global NO_DATA
    download_link = create_link(date, month, year, console_output=True)
    file_name = name(download_link)
    stream = downloader.get(download_link, stream=True)
    # Generate the save location if output_folder is not specified
    if not output_folder:
        output_folder = os.path.join(os.getcwd(), 'downloads')
    not_resolved = True
    i = 0
    # Resolve conflicts
    while not_resolved:
        if os.path.isdir(output_folder):
           not_resolved = False
           continue
       
        # Create the output folder if it doesn't exist
        elif not os.path.isdir(output_folder):
            os.makedirs(output_folder)
            not_resolved = False
            continue
        
        if os.path.isfile(output_folder):
            output_folder += str(i)
            continue
    
        i += 1
    # Downloading the file
    with open(os.path.join(output_folder, file_name), 'wb') as file:
        for chunk in tqdm(stream.iter_content(chunk_size=1024), total=int(stream.headers['content-length'], 0)/1024, unit='KB'):
            if chunk:
                file.write(chunk)
                file.flush()
        
        file.close()
        stream.close()
    
    # Check if the file is downloaded is in the right format
    
    with open(os.path.join(os.getcwd(), 'errors', NO_DATA), 'rb') as f:
        no_data = f.read()
    with open(os.path.join(output_folder, file_name), 'rb') as f:
        data = f.read()

    if data == no_data:
        os.remove(os.path.join(output_folder, file_name))
        raise NoDataError('No data recorded for the specified date.').with_traceback(sys.exc_info()[2])
        
    else:
        print(f'Downloaded file to {output_folder} ({stream.headers["content-length"]} bytes)\n\nFull Path: {os.path.join(output_folder, file_name)}')
        return os.path.join(output_folder, file_name)

def download_GUI(date: int,
                 month: int,
                 year: int,
                 output_folder: str=None,
                 progress_bar: QCustomProgressBar=None):

    def download(date: int,
                 month: int,
                 year: int,
                 output_folder: str=None,
                 progress_bar: QCustomProgressBar=None):
        
        global downloader
        global NO_DATA
        download_link = create_link(date, month, year, console_output=True)
        file_name = name(download_link)
        stream = downloader.get(download_link, stream=True)
        # Generate the save location if output_folder is not specified
        if not output_folder:
            output_folder = os.path.join(os.getcwd(), 'downloads')
        not_resolved = True
        i = 0
        # Resolve conflicts
        while not_resolved:
            if os.path.isdir(output_folder):
                not_resolved = False
                continue
        
            # Create the output folder if it doesn't exist
            elif not os.path.isdir(output_folder):
                os.makedirs(output_folder)
                not_resolved = False
                continue
            
            if os.path.isfile(output_folder):
                output_folder += str(i)
                continue
        
            i += 1
        # Downloading the file
        
        # Prepare the progress bar
        progress_bar.setMaximum(int(stream.headers['content-length']))
        progress_bar.setValue(0)
        progress_bar.setTextVisible(False)
        print(progress_bar.maximum())
        with open(os.path.join(output_folder, file_name), 'wb') as file:
            for chunk in tqdm(stream.iter_content(chunk_size=1024), total=int(stream.headers['content-length'], 0)/1024, unit='KB'):
                if chunk:
                    file.write(chunk)
                    progress_bar.step(1024)
                    file.flush()
            
            file.close()
            stream.close()
            print(progress_bar.value())
        
        # Check if the file is downloaded is in the right format
        
        with open(os.path.join(os.getcwd(), 'errors', NO_DATA), 'rb') as f:
            no_data = f.read()
        with open(os.path.join(output_folder, file_name), 'rb') as f:
            data = f.read()

        if data == no_data:
            os.remove(os.path.join(output_folder, file_name))
            raise NoDataError('No data recorded for the specified date.').with_traceback(sys.exc_info()[2])
            
        else:
            print(f'Downloaded file to {output_folder} ({stream.headers["content-length"]} bytes)\n\nFull Path: {os.path.join(output_folder, file_name)}')
            return os.path.join(output_folder, file_name)
    
    t = threading.Thread(target=download, args=(date, month, year, output_folder, progress_bar))
    t.start()