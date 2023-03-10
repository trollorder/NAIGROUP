from pathlib import Path

from peekingduck.pipeline.nodes.dabble import fps , tracking ,statistics,bbox_count
from peekingduck.pipeline.nodes.draw import bbox, legend,zones
from peekingduck.pipeline.nodes.input import visual
from peekingduck.pipeline.nodes.model import yolo , efficientdet
from peekingduck.pipeline.nodes.output import media_writer, screen,csv_writer
from peekingduck.runner import Runner
from src.custom_nodes.dabble import debug
from src.custom_nodes.output import stationcountsqlite

def main():
    debug_node = debug.Node(pkd_base_dir=Path.cwd() / "src" / "custom_nodes")
    visual_node = visual.Node(source=str(Path.cwd() / "Video Testing/Queue 1.mp4"))
    effdetect_node = efficientdet.Node(detect=["person"])
    tracking_node = tracking.Node(type = "iou")
    bbox_count_node = bbox_count.Node()
    stationcountsqlite_node = stationcountsqlite.Node()
    screen_node=screen.Node()

    runner = Runner(
        nodes=[visual_node,
            effdetect_node,
            tracking_node,
            bbox_count_node,
            screen_node,            
            stationcountsqlite_node]
        
    )
    runner.run()
    

main()