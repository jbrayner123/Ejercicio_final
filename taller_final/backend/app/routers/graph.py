# TODO: CRUD nodes/edges (protected). Use get_current_user dependency.
from fastapi import APIRouter
router = APIRouter(prefix="/graph", tags=["graph"])

@router.post("/nodes") def create_node(): raise NotImplementedError
@router.get("/nodes") def list_nodes(): raise NotImplementedError
@router.delete("/nodes/{node_id}") def delete_node(node_id:int): raise NotImplementedError
@router.post("/edges") def create_edge(): raise NotImplementedError
@router.get("/edges") def list_edges(): raise NotImplementedError
@router.delete("/edges/{edge_id}") def delete_edge(edge_id:int): raise NotImplementedError
