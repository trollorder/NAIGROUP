from pathlib import Path

from peekingduck.pipeline.nodes.dabble import fps , tracking ,statistics,bbox_count
from peekingduck.pipeline.nodes.draw import bbox, legend
from peekingduck.pipeline.nodes.input import visual
from peekingduck.pipeline.nodes.model import yolo , efficientdet
from peekingduck.pipeline.nodes.output import media_writer, screen,csv_writer
from peekingduck.runner import Runner
from src.custom_nodes.dabble import debug
from src.custom_nodes.output import sqlite

def main():
    debug_node = debug.Node(pkd_base_dir=Path.cwd() / "src" / "custom_nodes")
    visual_node = visual.Node(source=str(Path.cwd() / "Video Testing/Video 2.mp4"))
    effdetect_node = efficientdet.Node(detect=["person"])
    statistics_node = statistics.Node(maximum='obj_attrs["ids"]')
    tracking_node = tracking.Node(type = "iou")
    bbox_count_node = bbox_count.Node()
    csv_writer_node = csv_writer.Node(file_path=str(Path.cwd() / "output" / "new.csv"),stats_to_track= ['obj_attrs','cum_max','count'])
    sqlite_node = sqlite.Node()
    screen_node=screen.Node()
    runner = Runner(
        nodes=[visual_node,
            effdetect_node,
            tracking_node,
            bbox_count_node,
            screen_node,
            csv_writer_node,
            sqlite_node]
        
    )
    runner.run()
    

main()