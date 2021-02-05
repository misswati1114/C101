

import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)


        f = open(file_from, 'rb')
        dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.AqoBw_5wH6czdOS1qTV65SDn_6kHklZQ4wJLBpzpUsGvmnXL3laAHEpDkiLsWPXex_Ptff1DMmqEXDniK8ZJ5M-yDQtL3K8lQ5Su3Y4KQ8ntdChNy90eHPy9wyrtLqlBbKFOkIUj8B8'
    transferData = TransferData(access_token)

    file_from = 'test.txt'
    file_to = '/FileTransferApp14/test.txt'  # This is the full path to upload the file to, including name that you wish the file to be called once uploaded.

    # API v2
    transferData.upload_file(file_from, file_to)
    print("file has been moved !!!")

if __name__ == '__main__':
    main()
