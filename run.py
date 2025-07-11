from DoExtractContent import *
from DoGenerateTOC import *
from DoVisitArticles import *
from constants import *

tasks = [
    #DoVisitArticles(FILE_CACHE_VISIT),
    DoExtractContent(FILE_CACHE_CONTENT, FILE_CACHE_VISIT),
    DoGenerateTOC(FILE_CACHE_CONTENT, FILE_CACHE_TOC),
]

for task in tasks:
    taskName = task.__class__.__name__
    print(f"Executing '{taskName}'")
    task.execute()
