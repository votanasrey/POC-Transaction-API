from graph_algorithms import query_modules
from vendors.memgraph import Memgraph
from query_builders.memgraph_query_builder import QueryBuilder

class Test:
    # BRUNO isprobati moze li se vratiti tuple ili nesto pa koristiti ko 2 argumenta funkcije
    def __init__(self) -> None:
        self.s = "mahalo"

    def __str__(self) -> str:
        pass

mg = Memgraph()
# procs = mg.get_procedures()

# bc = mg.get_procedures(starts_with="between")[0]

# bc.set_argument_values(directed=True)

# res = QueryBuilder(mg).call(bc, bc.get_arguments_for_call()).yield_().return_().execute()

# print(res)
# for r in res:
#     print(r)

import os
os.system("pytest tests/query_builders/test_memgraph_query_builder.py")

export = mg.get_procedures(starts_with="export")[0]
export.set_argument_values(path="/home/bruno")
# QueryBuilder(mg).call(export, export.get_arguments_for_call()).execute();

subgraph = "MATCH path=(n:sads)-[:relate]->(m:Heasadad)"

labels = "Chop"
relationship_types = ["THIS", "THAT"]

print(QueryBuilder(mg).call(export, export.get_arguments_for_call(), subgraph_query=subgraph)._construct_query())
