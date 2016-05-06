import os
import networkx as nx
from nxpd import draw

from .conftest import ARTIFACTS_DIR


TEST_GRAPH_OUTPUT = os.path.join(
    ARTIFACTS_DIR,
    'simple_graph.png'
)


def test_read_generate_graph(g):
    if os.path.isfile(TEST_GRAPH_OUTPUT):
        os.remove(TEST_GRAPH_OUTPUT)

    nx_graph = g.render_graph(
        filter_subgraph=True
    )
    draw(nx_graph, TEST_GRAPH_OUTPUT, show=False)

    # some data is drawn
    assert os.path.isfile(TEST_GRAPH_OUTPUT)
    filesize = os.stat(TEST_GRAPH_OUTPUT).st_size
    assert filesize > 1000

    assert len(nx_graph.nodes()) > 5
    assert nx.number_connected_components(nx_graph.to_undirected()) == 1


def test_simplification(g):
    output_png = os.path.join(ARTIFACTS_DIR, 'tree.png')

    if os.path.isfile(output_png):
        os.remove(output_png)

    g.simplify(min_edges=0)
    nx_tree = g.render_graph(
        filter_subgraph=True
    )
    draw(nx_tree, output_png, show=False)
