from gqlalchemy.vendors.memgraph import Memgraph
import yaml
from gqlalchemy.loaders import ParquetS3FileSystemImporter

memgraph = Memgraph("127.0.0.1", 7687)

memgraph.drop_database()

import csv

header = ["ind_id", "name", "surname", "add_id"]
data = [
    [1, "Tomislav", "Petrov", 1],
    [2, "Ivan", "Horvat", 3],
    [3, "Marko", "Horvat", 3],
    [4, "John", "Doe", 2],
    [5, "John", "Though", 4],
]

with open("individual.csv", "w", encoding="UTF8", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(data)

header = ["add_id", "street", "street_num", "city"]
data = [
    [1, "Ilica", 2, "Zagreb"],
    [2, "Death Valley", 0, "Knowhere"],
    [3, "Horvacanska", 3, "Horvati"],
    [4, "Broadway", 12, "New York"],
]

with open("address.csv", "w", encoding="UTF8", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(data)

with open("./gqlalchemy/config.yml", "r") as cfg:
    data_conf = yaml.safe_load(cfg)

print(data_conf)

from gqlalchemy.loaders import CSVLocalFileSystemImporter

importer = CSVLocalFileSystemImporter(
    data_configuration=data_conf,
    path="./",
)

importer.translate(drop_database_on_start=True)
