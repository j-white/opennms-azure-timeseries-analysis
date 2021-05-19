import os, re, unicodedata
from pathlib import Path
from avro.datafile import DataFileReader
from avro.io import DatumReader
from azure.storage.blob import ContainerClient
from collectionset_pb2 import CollectionSet


def slugify(value, allow_unicode=False):
    """
    Taken from https://github.com/django/django/blob/master/django/utils/text.py
    Convert to ASCII if 'allow_unicode' is False. Convert spaces or repeated
    dashes to single dashes. Remove characters that aren't alphanumerics,
    underscores, or hyphens. Convert to lowercase. Also strip leading and
    trailing whitespace, dashes, and underscores.
    """
    value = str(value)
    if allow_unicode:
        value = unicodedata.normalize('NFKC', value)
    else:
        value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore').decode('ascii')
    value = re.sub(r'[^\w\s-]', '', value.lower())
    return re.sub(r'[-\s]+', '-', value).strip('-_')


def download_blobs(local_path):
    sas_url = 'INSERT_URL_HERE'
    client = ContainerClient.from_container_url(sas_url)
    blob_list = client.list_blobs()

    # Create a local directory to hold blob data
    Path(local_path).mkdir(parents=True, exist_ok=True)

    # Download all the blobs
    for blob in blob_list:
        download_file_path = os.path.join(local_path, slugify(blob.name))
        print("Downloading blob to \n\t" + download_file_path)
        with open(download_file_path, "wb") as download_file:
            download_file.write(client.download_blob(blob).readall())


def handle_collection_set(cset):
    for resource in cset.resource:
        # Build a string representing the associated "resource"
        resource_id = None
        resource_type = resource.WhichOneof('resource')
        if resource_type == 'node':
            resource_id = "node:" + resource.node.node_label
        elif resource_type == 'interface':
            resource_id = "node:" + resource.interface.node.node_label + ":interface:" + str(resource.interface.if_index)
        elif resource_type == 'generic':
            resource_id = "node:" + resource.generic.node.node_label +\
                          ":generic:" + resource.generic.type + "/" + resource.generic.instance
        elif resource_type == 'response':
            resource_id = "response:" + resource.response.location + "/" + resource.response.instance

        # Output the numeric values in tabular format
        for attribute in resource.numeric:
            # timestamp, resource_id, metric name, metric value
            print("%d,%s,%s,%.2f" % (cset.timestamp, resource_id, attribute.name, attribute.value))


def handle_file(path):
    print("Reading file from: " + path)
    reader = DataFileReader(open(path, "rb"), DatumReader())
    for record in reader:
        cset = CollectionSet()
        cset.ParseFromString(record['Body'])
        handle_collection_set(cset)


if __name__ == '__main__':
    local_path = "./data"
    download_blobs(local_path)

    for (_, _, filenames) in os.walk(local_path):
        for filename in filenames:
            handle_file(os.path.join(local_path, filename))
