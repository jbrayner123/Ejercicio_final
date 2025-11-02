# TODO: BFS and Dijkstra endpoints
from fastapi import APIRouter
router = APIRouter(prefix="/graph", tags=["algorithms"])

@router.get("/bfs")
def run_bfs(start_id:int): raise NotImplementedError
@router.get("/shortest-path")
def run_shortest_path(src_id:int, dst_id:int): raise NotImplementedError
